/* CraicBet menu — shared across all pages (mobile + desktop burger).
   Light accordion panel: outline icons, dark pill for the open section, sub-links on a thin rail.
   Links are absolute so the script works at any depth. */
(function () {
  var lang = (document.documentElement.getAttribute('lang') || 'en').slice(0, 2);
  var I = {
    home: '<path d="M3 11l9-7 9 7v9a1 1 0 0 1-1 1h-5v-6H9v6H4a1 1 0 0 1-1-1z"/>',
    grai: '<path d="M3 21h18M5 21V10m14 11V10M3 10l9-6 9 6M9 21v-7h6v7"/>',
    bet: '<circle cx="12" cy="12" r="9"/><path d="M12 3a9 9 0 0 1 0 18M3.5 9.5l5 1.5-1 5M20.5 9.5l-5 1.5 1 5M12 12l-3.5-1M12 12l3.5-1M12 12v4"/>',
    casino: '<rect x="3" y="3" width="18" height="18" rx="4"/><circle cx="8" cy="8" r="1.2"/><circle cx="16" cy="8" r="1.2"/><circle cx="12" cy="12" r="1.2"/><circle cx="8" cy="16" r="1.2"/><circle cx="16" cy="16" r="1.2"/>',
    gift: '<rect x="3" y="8" width="18" height="4" rx="1"/><path d="M5 12v8a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1v-8M12 8v13M12 8s-1-4-4-4-2 4 4 4m0 0s1-4 4-4 2 4-4 4"/>',
    slots: '<rect x="3" y="4" width="18" height="16" rx="3"/><path d="M8 9v6m4-6v6m4-6v6M3 12h18"/>',
    guide: '<path d="M4 4h6a3 3 0 0 1 3 3v13a2 2 0 0 0-2-2H4zM20 4h-6a3 3 0 0 0-3 3v13a2 2 0 0 1 2-2h7z"/>',
    news: '<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M7 8h10M7 12h10M7 16h6"/>',
    fast: '<path d="M13 2L4 14h7l-1 8 9-12h-7z"/>',
    folder: '<path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>',
    search: '<circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5"/>',
    spark: '<path d="M12 2l1.8 6.2L20 10l-6.2 1.8L12 18l-1.8-6.2L4 10l6.2-1.8z"/>',
    chev: '<path d="M6 9l6 6 6-6"/>'
  };
  var svg = function (k, s) { return '<svg class="mm-ic" width="' + (s || 22) + '" height="' + (s || 22) + '" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">' + I[k] + '</svg>'; };

  var MENUS = {
    en: { title: 'Menu', home: ['Home', '/'], search: ['Search the site', '/pages/search'], footer: '18+ · Gamble responsibly · 1800 753 753',
      items: [
        ['grai', 'GRAI', [
          ['GRAI Licence Explained', '/pages/grai-licence-explained'],
          ['GRAI-Licensed Bookmakers', '/pages/grai-licensed-bookmakers-ireland'],
          ['Licence Checker', '/pages/grai-licence-checker'],
          ['Licence Register Tracker', '/pages/grai-licence-register-tracker'],
          ['GRAI Complaints', '/pages/grai-complaints-ireland'],
          ['Is Gambling Legal?', '/pages/is-online-gambling-legal-ireland'],
          ['Unlicensed Sites Warning', '/pages/unlicensed-betting-sites-ireland']]],
        ['bet', 'Betting', [
          ['Best Betting Sites', '/pages/betting-sites-ireland'],
          ['Betting Apps', '/pages/betting-apps-ireland'],
          ['Free Bets Ireland', '/pages/free-bets-ireland'],
          ['Horse Racing', '/pages/horse-racing-betting-ireland'],
          ['GAA Betting', '/pages/gaa-betting-ireland'],
          ['Football Betting', '/pages/football-betting-ireland'],
          ['Acca Calculator', '/pages/accumulator-calculator-ireland']]],
        ['casino', 'Casinos', [
          ['Best Casinos Ireland', '/pages/best-casinos-ireland'],
          ['€5 Deposit Casinos', '/pages/5-euro-deposit-casino'],
          ['Minimum Deposit Casinos', '/pages/minimum-deposit-casinos-ireland'],
          ['Crypto Casinos', '/pages/crypto-casinos-ireland'],
          ['Visa & Mastercard Casinos', '/pages/visa-mastercard-casinos-ireland'],
          ['Fast Payout Casinos', '/pages/fast-payout-casinos'],
          ['Revolut Casinos', '/pages/revolut-casinos'],
          ['Google Pay Casinos', '/pages/google-pay-casino-ireland'],
          ['Trustly Casinos', '/pages/trustly-casino-ireland'],
          ['Bank Blocks Guide', '/pages/irish-banks-blocking-casino-deposits']]],
        ['gift', 'Bonuses', [
          ['Casino Bonuses', '/pages/casino-bonuses-ireland'],
          ['No Deposit Bonuses', '/pages/no-deposit-bonus'],
          ['Wagering Explained', '/pages/wagering-requirements-explained'],
          ['Wagering Calculator', '/pages/wagering-calculator']]],
        ['slots', 'Slots', [
          ['All Slot Reviews', '/pages/slot-reviews'],
          ['Gates of Olympus', '/pages/slots/gates-of-olympus'],
          ['Sweet Bonanza', '/pages/slots/sweet-bonanza'],
          ['Big Bass Bonanza', '/pages/slots/big-bass-bonanza'],
          ['Book of Dead', '/pages/slots/book-of-dead'],
          ['What Is RTP?', '/pages/rtp-explained']]],
        ['fast', 'Fast Payouts', [
          ['Fast Payout Casinos', '/pages/fast-payout-casinos'],
          ['Revolut Casinos', '/pages/revolut-casinos']]],
        ['guide', 'Guides', [
          ['All Guides', '/pages/guides'],
          ['Responsible Gambling', '/pages/responsible-gambling'],
          ['Gambling Tax Ireland', '/pages/gambling-tax-ireland'],
          ['Each-Way Betting', '/pages/each-way-betting-guide'],
          ['Offshore Casinos', '/pages/offshore-casinos-ireland'],
          ['About CraicBet', '/pages/about']]],
        ['news', 'News', [
          ['Latest news', '/pages/news/'],
          ['GRAI register tracker', '/pages/grai-licence-register-tracker']]]
      ] },
    ga: { title: 'Roghchlár', home: ['Baile', '/ga/'], search: ['Cuardach', '/pages/search'], footer: '18+ · Imir go freagrach · 1800 753 753',
      items: [
        ['grai', 'GRAI', [['Ceadúnas GRAI in Éirinn', '/ga/ceadunas-grai-eire'], ['Geallghlacadóirí le ceadúnas GRAI', '/ga/buimeadoiri-le-ceadunas-grai']]],
        ['bet', 'Gealltóireacht', [['Geallghlacadóirí in Éirinn', '/ga/geallghlacadoiri-eireann']]],
        ['casino', 'Caisíneonna', [['Na caisíneonna is fearr', '/ga/na-caisinoenna-is-fearr'], ['Caisíneo beo', '/ga/caisineo-beo'], ['Léirmheasanna', '/ga/leirmheasanna-caisineo']]],
        ['gift', 'Bónais', [['Bónais caisíneo', '/ga/bonais-caisineo']]],
        ['slots', 'Sliotáin', [['Sliotáin ar líne', '/ga/spinnteanna-saor-in-aisce']]],
        ['fast', 'Íocaíochtaí Tapa', [['Íocaíochtaí tapa', '/ga/iocaiochtai-tapa']]],
        ['guide', 'Treoracha', [['Gach treoir', '/ga/treoracha'], ['English', '/']]]
      ] },
    pl: { title: 'Menu', home: ['Główna', '/pl/'], search: ['Szukaj', '/pages/search'], footer: '18+ · Graj odpowiedzialnie · 1800 753 753',
      items: [
        ['grai', 'GRAI', [['Licencja GRAI w Irlandii', '/pl/licencja-grai-irlandia'], ['Bukmacherzy z licencją GRAI', '/pl/bukmacherzy-z-licencja-grai'], ['Licencja bukmacherska GRAI', '/pl/licencja-bukmacherska-grai-irlandia']]],
        ['bet', 'Zakłady', [['Zakłady bukmacherskie w Irlandii', '/pl/zaklady-bukmacherskie-irlandia']]],
        ['casino', 'Kasyna', [['Najlepsze kasyna', '/pl/najlepsze-kasyna'], ['Kasyno na żywo', '/pl/kasyno-na-zywo'], ['Recenzje kasyn', '/pl/recenzje-kasyn']]],
        ['gift', 'Bonusy', [['Bonusy kasynowe', '/pl/bonusy-kasynowe']]],
        ['slots', 'Sloty', [['Darmowe spiny', '/pl/darmowe-spiny']]],
        ['fast', 'Szybkie Wypłaty', [['Szybkie wypłaty', '/pl/szybkie-wyplaty']]],
        ['guide', 'Poradniki', [['Wszystkie poradniki', '/pl/poradniki'], ['English', '/']]]
      ] }
  };
  var M = MENUS[lang] || MENUS.en;

  var path = location.pathname.replace(/\.html$/, '');
  var openIdx = -1, curHref = '';
  M.items.forEach(function (it, i) {
    it[2].forEach(function (l) { var h = l[1].split('#')[0]; if (h !== '/' && path.indexOf(h) === 0 && h.length > curHref.length) { curHref = h; openIdx = i; } });
  });
  if (openIdx < 0) openIdx = 0;

  var css = '#megaMenu{position:fixed;inset:0;z-index:10000;background:rgba(0,0,0,.55);display:none;backdrop-filter:blur(2px)}' +
    '#megaMenu *{box-sizing:border-box}' +
    '#megaMenu .mm-panel{position:absolute;top:0;right:0;height:100%;width:min(400px,100vw);background:linear-gradient(180deg,#0f3a1f,#0A2E14);color:#fff;display:flex;flex-direction:column;box-shadow:-8px 0 40px rgba(0,0,0,.25);transform:translateX(100%);transition:transform .28s cubic-bezier(.4,0,.2,1);font-family:Inter,system-ui,sans-serif}' +
    '#megaMenu.open .mm-panel{transform:none}' +
    '#megaMenu .mm-head{display:flex;align-items:center;gap:12px;padding:16px 22px;font-size:1.15rem;font-weight:700;background:rgba(0,0,0,.25);color:#fff;border-bottom:1px solid rgba(255,255,255,.08)}' +
    '#megaMenu .mm-head img{height:38px;width:auto}' +
    '#megaMenu .mm-head .mm-ic{width:26px;height:26px;color:#111}' +
    '#megaMenu .mm-close{margin-left:auto;width:36px;height:36px;border-radius:50%;border:1px solid rgba(255,255,255,.15);background:rgba(255,255,255,.1);color:#fff;font-size:1.1rem;cursor:pointer;display:flex;align-items:center;justify-content:center}' +
    '#megaMenu .mm-rule{height:8px}' +
    '#megaMenu .mm-list{flex:1;overflow-y:auto;padding:4px 14px 14px;-webkit-overflow-scrolling:touch}' +
    '#megaMenu .mm-row{display:flex;align-items:center;gap:14px;padding:13px 16px;border-radius:999px;color:rgba(255,255,255,.88);text-decoration:none;font-size:1.02rem;font-weight:500;cursor:pointer;user-select:none;transition:background .15s}' +
    '#megaMenu .mm-row:hover{background:rgba(255,255,255,.08)}' +
    '#megaMenu .mm-row .mm-ic{color:#9fd3b3;flex-shrink:0}' +
    '#megaMenu .mm-row .mm-n{margin-left:auto;min-width:26px;height:24px;border-radius:7px;background:#F26522;color:#fff;font-size:.78rem;font-weight:700;display:flex;align-items:center;justify-content:center;padding:0 7px}' +
    '#megaMenu .mm-row .mm-ch{width:18px;height:18px;color:rgba(255,255,255,.5);transition:transform .2s;margin-left:6px}' +
    '#megaMenu .mm-sec.open>.mm-row .mm-ch{transform:rotate(180deg);color:#0A2E14}' +
    '#megaMenu .mm-sec{margin:2px 0}' +
    '#megaMenu .mm-sec.open>.mm-row{background:#fff;color:#0A2E14}' +
    '#megaMenu .mm-sec.open>.mm-row .mm-ic{color:#0A2E14}' +
    '#megaMenu .mm-sec.open>.mm-row .mm-n{background:#F26522;color:#fff}' +
    '#megaMenu .mm-sub{display:none;position:relative;margin:6px 0 8px 32px;padding-left:16px}' +
    '#megaMenu .mm-sub:before{content:"";position:absolute;left:0;top:8px;bottom:8px;width:1.5px;background:rgba(255,255,255,.22)}' +
    '#megaMenu .mm-sec.open>.mm-sub{display:block}' +
    '#megaMenu .mm-sub a{display:flex;align-items:center;gap:12px;padding:11px 14px;border-radius:999px;color:rgba(255,255,255,.8);text-decoration:none;font-size:.98rem;font-weight:500;transition:background .15s}' +
    '#megaMenu .mm-sub a .mm-ic{width:20px;height:20px;color:rgba(255,255,255,.55)}' +
    '#megaMenu .mm-sub a:hover{background:rgba(255,255,255,.08);color:#fff}' +
    '#megaMenu .mm-sub a.cur{background:rgba(255,255,255,.14);color:#fff;font-weight:600}' +
    '#megaMenu .mm-foot{padding:12px 22px 18px;border-top:1px solid rgba(255,255,255,.1);background:rgba(0,0,0,.2)}' +
    '#megaMenu .mm-search{display:flex;align-items:center;gap:10px;padding:12px 16px;border-radius:999px;background:#F26522;color:#fff;text-decoration:none;font-weight:600;font-size:.95rem}' +
    '#megaMenu .mm-search .mm-ic{color:#fff}' +
    '#megaMenu .mm-rg{margin-top:10px;font-size:.75rem;color:rgba(255,255,255,.6);text-align:center}' +
    '#megaMenu .mm-rg b{display:inline-block;background:#e53935;color:#fff;border-radius:999px;padding:1px 7px;font-weight:800;margin-right:6px}';

  var esc = function (s) { return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;'); };
  var h = '<div class="mm-panel" role="dialog" aria-label="' + esc(M.title) + '">' +
    '<div class="mm-head"><img src="/images/logo.svg" alt="CraicBet"><span style="opacity:.7;font-weight:500">' + esc(M.title) + '</span><button class="mm-close" aria-label="Close">✕</button></div>' +
    '<div class="mm-rule"></div><div class="mm-list">' +
    '<a class="mm-row" href="' + M.home[1] + '">' + svg('home') + '<span>' + esc(M.home[0]) + '</span></a>';
  M.items.forEach(function (it, i) {
    h += '<div class="mm-sec' + (i === openIdx ? ' open' : '') + '"><div class="mm-row" role="button" tabindex="0" aria-expanded="' + (i === openIdx) + '">' + svg(it[0]) + '<span>' + esc(it[1]) + '</span><span class="mm-n">' + it[2].length + '</span>' + svg('chev', 18).replace('mm-ic', 'mm-ic mm-ch') + '</div><div class="mm-sub">';
    it[2].forEach(function (l) { h += '<a href="' + l[1] + '"' + (l[1].split('#')[0] === curHref ? ' class="cur"' : '') + '>' + svg('folder', 20) + '<span>' + esc(l[0]) + '</span></a>'; });
    h += '</div></div>';
  });
  h += '</div><div class="mm-foot"><a class="mm-search" href="' + M.search[1] + '">' + svg('search', 20) + esc(M.search[0]) + '</a><div class="mm-rg"><b>18+</b>' + esc(M.footer) + '</div></div></div>';

  var old = document.getElementById('megaMenu'); if (old) old.parentNode.removeChild(old);
  var style = document.createElement('style'); style.textContent = css; document.head.appendChild(style);
  var menu = document.createElement('div'); menu.id = 'megaMenu'; menu.setAttribute('aria-hidden', 'true'); menu.innerHTML = h;
  document.body.appendChild(menu);

  var oldBtn = document.querySelector('.burger');
  if (!oldBtn) return;
  var btn = oldBtn.cloneNode(true); btn.removeAttribute('onclick');
  oldBtn.parentNode.replaceChild(btn, oldBtn);

  function open() { menu.style.display = 'block'; requestAnimationFrame(function () { menu.classList.add('open'); }); menu.setAttribute('aria-hidden', 'false'); btn.classList.add('is-open'); btn.setAttribute('aria-expanded', 'true'); document.body.style.overflow = 'hidden'; }
  function close() { menu.classList.remove('open'); setTimeout(function () { menu.style.display = 'none'; }, 280); menu.setAttribute('aria-hidden', 'true'); btn.classList.remove('is-open'); btn.setAttribute('aria-expanded', 'false'); document.body.style.overflow = ''; }
  btn.addEventListener('click', function () { menu.classList.contains('open') ? close() : open(); });
  menu.querySelector('.mm-close').addEventListener('click', close);
  menu.addEventListener('click', function (e) { if (e.target === menu) close(); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') close(); });
  menu.querySelectorAll('.mm-sec>.mm-row').forEach(function (row) {
    var toggle = function () {
      var sec = row.parentNode, was = sec.classList.contains('open');
      menu.querySelectorAll('.mm-sec').forEach(function (s) { s.classList.remove('open'); s.firstChild.setAttribute('aria-expanded', 'false'); });
      if (!was) { sec.classList.add('open'); row.setAttribute('aria-expanded', 'true'); }
    };
    row.addEventListener('click', toggle);
    row.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); toggle(); } });
  });
})();

/* Load the share bar on every page that uses this menu. */
(function () {
  var s = document.createElement('script');
  s.src = '/js/share.js?v=20261112b';
  s.defer = true;
  document.head.appendChild(s);
})();
