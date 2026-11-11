/* CraicBet share bar: added to the end of every article page (loaded from megamenu.js). */
(function () {
  if (document.getElementById('cb-share')) return;
  var host = document.querySelector('.article-content') || document.querySelector('article');
  if (!host) return; // home page, hubs without an article and the web app have no share bar
  var lang = (document.documentElement.lang || 'en').slice(0, 2).toLowerCase();
  var T = {
    en: { h: 'Found this useful? Share it', copy: 'Copy link', done: 'Copied', more: 'Share' },
    ga: { h: 'An raibh sé seo úsáideach? Roinn é', copy: 'Cóipeáil an nasc', done: 'Cóipeáilte', more: 'Roinn' },
    pl: { h: 'Przydatne? Udostępnij', copy: 'Kopiuj link', done: 'Skopiowano', more: 'Udostępnij' }
  }[lang] || null;
  if (!T) T = { h: 'Found this useful? Share it', copy: 'Copy link', done: 'Copied', more: 'Share' };
  var canon = document.querySelector('link[rel="canonical"]');
  var url = (canon && canon.href) || location.href.split('#')[0];
  var title = (document.querySelector('h1') || {}).textContent || document.title;
  title = title.replace(/\s+/g, ' ').trim();
  var e = encodeURIComponent;
  var links = [
    ['X', 'https://twitter.com/intent/tweet?text=' + e(title) + '&url=' + e(url)],
    ['WhatsApp', 'https://wa.me/?text=' + e(title + ' ' + url)],
    ['Facebook', 'https://www.facebook.com/sharer/sharer.php?u=' + e(url)]
  ];
  var box = document.createElement('div');
  box.id = 'cb-share';
  box.setAttribute('style', 'margin:28px 0;padding:16px 18px;background:#0A2E14;border-radius:12px;color:#fff;display:flex;flex-wrap:wrap;align-items:center;gap:10px');
  var lab = document.createElement('strong');
  lab.textContent = T.h;
  lab.setAttribute('style', 'margin-right:6px;font-size:15px');
  box.appendChild(lab);
  var btnStyle = 'display:inline-block;padding:9px 16px;border-radius:8px;background:#fff;color:#0A2E14;font-weight:700;font-size:14px;text-decoration:none;border:0;cursor:pointer;font-family:inherit;line-height:1.2';
  function track(name) { if (window.gtag) { window.gtag('event', 'share_click', { method: name, page: location.pathname }); } }
  if (navigator.share) {
    var nb = document.createElement('button');
    nb.type = 'button'; nb.textContent = T.more;
    nb.setAttribute('style', btnStyle + ';background:#F26522;color:#fff');
    nb.addEventListener('click', function () { track('native'); navigator.share({ title: title, url: url }).catch(function () {}); });
    box.appendChild(nb);
  }
  links.forEach(function (l) {
    var a = document.createElement('a');
    a.href = l[1]; a.target = '_blank'; a.rel = 'noopener'; a.textContent = l[0];
    a.setAttribute('style', btnStyle);
    a.addEventListener('click', function () { track(l[0]); });
    box.appendChild(a);
  });
  var cp = document.createElement('button');
  cp.type = 'button'; cp.textContent = T.copy;
  cp.setAttribute('style', btnStyle + ';background:transparent;color:#fff;border:1px solid #fff');
  cp.addEventListener('click', function () {
    track('copy');
    var ok = function () { cp.textContent = T.done; setTimeout(function () { cp.textContent = T.copy; }, 2000); };
    if (navigator.clipboard && navigator.clipboard.writeText) { navigator.clipboard.writeText(url).then(ok).catch(function () {}); }
    else { var t = document.createElement('textarea'); t.value = url; document.body.appendChild(t); t.select(); try { document.execCommand('copy'); ok(); } catch (x) {} document.body.removeChild(t); }
  });
  box.appendChild(cp);
  host.appendChild(box);
})();
