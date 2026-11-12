/* CraicBet Spotlight Search — macOS Spotlight-style overlay.
   Opens on click of any [data-spotlight] element or Cmd/Ctrl+K.
   Loads search-index.json on first open, searches client-side. */
(function () {
  'use strict';

  var index = null;
  var indexLoading = false;
  var overlay = null;
  var input = null;
  var resultsList = null;
  var selectedIdx = -1;
  var currentResults = [];
  var debounceTimer = null;

  /* ── GRAI register (loaded separately in grai-data.js) ── */
  function normBrand(s) { return s.toLowerCase().replace(/[^a-z0-9]/g, ''); }

  /* ── Helpers ── */
  function esc(s) {
    return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
  }
  function normalise(s) {
    return String(s).toLowerCase().replace(/[^a-z0-9\s]/g,' ').replace(/\s+/g,' ').trim();
  }
  function tokenise(s) {
    return normalise(s).split(' ').filter(function(w){return w.length>1;});
  }

  function scoreEntry(entry, tokens) {
    var titleN = normalise(entry.title||'');
    var h1N = normalise(entry.h1||'');
    var descN = normalise(entry.description||'');
    var textN = normalise(entry.text||'');
    var urlN = normalise(entry.url||'');
    var score = 0;
    for (var i=0; i<tokens.length; i++) {
      var t = tokens[i];
      if (titleN.indexOf(t)!==-1) score+=10;
      if (h1N.indexOf(t)!==-1) score+=8;
      if (descN.indexOf(t)!==-1) score+=5;
      if (textN.indexOf(t)!==-1) score+=2;
      if (urlN.indexOf(t)!==-1) score+=3;
      if (t.length>=4) {
        var p = t.slice(0,Math.max(4,Math.floor(t.length*0.7)));
        if (titleN.indexOf(t)===-1 && titleN.indexOf(p)!==-1) score+=4;
        if (h1N.indexOf(t)===-1 && h1N.indexOf(p)!==-1) score+=3;
        if (descN.indexOf(t)===-1 && descN.indexOf(p)!==-1) score+=2;
      }
    }
    return score;
  }

  /* ── Build DOM ── */
  function buildOverlay() {
    if (overlay) return;

    overlay = document.createElement('div');
    overlay.id = 'spotlightOverlay';
    overlay.innerHTML =
      '<div id="spotlightBackdrop"></div>' +
      '<div id="spotlightBox">' +
        '<div id="spotlightInputWrap">' +
          '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#8abba0" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink:0"><circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5"/></svg>' +
          '<input type="text" id="spotlightInput" placeholder="Search CraicBet…" autocomplete="off" spellcheck="false">' +
          '<kbd id="spotlightKbd">ESC</kbd>' +
        '</div>' +
        '<div id="spotlightResults"></div>' +
        '<div id="spotlightFooter">' +
          '<span><kbd>&uarr;</kbd><kbd>&darr;</kbd> navigate</span>' +
          '<span><kbd>&#9166;</kbd> open</span>' +
          '<span><kbd>esc</kbd> close</span>' +
        '</div>' +
      '</div>';

    var style = document.createElement('style');
    style.textContent =
      '#spotlightOverlay{position:fixed;top:0;left:0;width:100%;height:100%;z-index:99999;display:none;align-items:flex-start;justify-content:center;padding-top:min(20vh,160px)}' +
      '#spotlightOverlay.open{display:flex}' +
      '#spotlightBackdrop{position:fixed;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,.55);backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px)}' +
      '#spotlightBox{position:relative;width:min(640px,92vw);background:#152b1e;border:1px solid rgba(255,255,255,.12);border-radius:16px;box-shadow:0 25px 60px rgba(0,0,0,.5);overflow:hidden;display:flex;flex-direction:column;max-height:min(520px,70vh)}' +
      '#spotlightInputWrap{display:flex;align-items:center;gap:12px;padding:16px 20px;border-bottom:1px solid rgba(255,255,255,.08)}' +
      '#spotlightInput{flex:1;background:transparent;border:none;outline:none;color:#fff;font-size:18px;font-family:inherit}' +
      '#spotlightInput::placeholder{color:#6a9a7a}' +
      '#spotlightKbd{background:rgba(255,255,255,.1);color:#6a9a7a;font-size:11px;padding:2px 8px;border-radius:4px;font-family:inherit}' +
      '#spotlightResults{overflow-y:auto;flex:1}' +
      '#spotlightResults::-webkit-scrollbar{width:6px}' +
      '#spotlightResults::-webkit-scrollbar-thumb{background:rgba(255,255,255,.15);border-radius:3px}' +
      '.sp-item{display:flex;align-items:center;gap:12px;padding:12px 20px;cursor:pointer;text-decoration:none;color:#fff;transition:background .1s}' +
      '.sp-item:hover,.sp-item.active{background:rgba(242,101,34,.15)}' +
      '.sp-item.active{background:rgba(242,101,34,.25)}' +
      '.sp-icon{width:36px;height:36px;border-radius:8px;background:rgba(255,255,255,.06);display:flex;align-items:center;justify-content:center;flex-shrink:0;font-size:16px}' +
      '.sp-text{flex:1;min-width:0}' +
      '.sp-title{font-size:15px;font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}' +
      '.sp-title mark{background:transparent;color:#F26522;font-weight:700}' +
      '.sp-url{font-size:12px;color:#6a9a7a;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}' +
      '.sp-empty{padding:32px 20px;text-align:center;color:#6a9a7a;font-size:14px}' +
      '.sp-loading{padding:24px 20px;text-align:center;color:#6a9a7a;font-size:14px}' +
      '#spotlightFooter{display:flex;gap:16px;padding:10px 20px;border-top:1px solid rgba(255,255,255,.08);font-size:12px;color:#6a9a7a}' +
      '#spotlightFooter kbd{background:rgba(255,255,255,.1);padding:1px 6px;border-radius:3px;font-family:inherit;font-size:11px}' +
      '@media(max-width:600px){#spotlightBox{border-radius:12px;max-height:80vh}#spotlightFooter{display:none}#spotlightOverlay{padding-top:60px}}';

    document.head.appendChild(style);
    document.body.appendChild(overlay);

    input = document.getElementById('spotlightInput');
    resultsList = document.getElementById('spotlightResults');

    // Events
    document.getElementById('spotlightBackdrop').addEventListener('click', closeSpotlight);
    input.addEventListener('input', function() {
      clearTimeout(debounceTimer);
      debounceTimer = setTimeout(function(){ doSearch(input.value); }, 150);
    });
    input.addEventListener('keydown', function(e) {
      if (e.key === 'Escape') { closeSpotlight(); e.preventDefault(); }
      else if (e.key === 'ArrowDown') { e.preventDefault(); moveSelection(1); }
      else if (e.key === 'ArrowUp') { e.preventDefault(); moveSelection(-1); }
      else if (e.key === 'Enter') { e.preventDefault(); openSelected(); }
    });
  }

  /* ── Search ── */
  function loadIndex(cb) {
    if (index) { cb(); return; }
    if (indexLoading) { return; }
    indexLoading = true;
    resultsList.innerHTML = '<div class="sp-loading">Loading search index…</div>';
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/pages/search-index.json', true);
    xhr.onload = function() {
      if (xhr.status === 200) {
        try { index = JSON.parse(xhr.responseText); } catch(e) {}
      }
      indexLoading = false;
      cb();
    };
    xhr.onerror = function() {
      indexLoading = false;
      resultsList.innerHTML = '<div class="sp-empty">Could not load search index.</div>';
    };
    xhr.send();
  }

  function getIcon(url) {
    if (/grai/i.test(url)) return '🛡️';
    if (/betting|bet|horse|gaa|football|acca/i.test(url)) return '🏇';
    if (/casino|slot|bonus|wagering|deposit/i.test(url)) return '🎰';
    if (/news/i.test(url)) return '📰';
    if (/\/ga\//i.test(url)) return '🇮🇪';
    if (/\/pl\//i.test(url)) return '🇵🇱';
    return '📄';
  }

  function highlightTitle(title, tokens) {
    var h = esc(title);
    tokens.forEach(function(t) {
      if (t.length < 2) return;
      var rx = new RegExp('(' + t.replace(/[.*+?^${}()|[\]\\]/g,'\\$&') + ')','gi');
      h = h.replace(rx, '<mark>$1</mark>');
    });
    return h;
  }

  function doSearch(query) {
    var q = query.trim();
    selectedIdx = -1;
    currentResults = [];

    if (!q) {
      showPopular();
      return;
    }

    if (!index) {
      loadIndex(function(){ doSearch(q); });
      return;
    }

    var tokens = tokenise(q);
    if (!tokens.length) { showPopular(); return; }

    var scored = [];
    for (var i=0; i<index.length; i++) {
      var s = scoreEntry(index[i], tokens);
      if (s > 0) scored.push({ entry: index[i], score: s });
    }
    scored.sort(function(a,b){ return b.score - a.score; });
    currentResults = scored.slice(0, 8).map(function(x){ return x.entry; });

    if (!currentResults.length) {
      resultsList.innerHTML = '<div class="sp-empty">No results for "' + esc(q) + '"</div>';
      return;
    }

    var html = '';
    currentResults.forEach(function(entry, idx) {
      var title = entry.title || entry.h1 || entry.url;
      var url = entry.url || '';
      html += '<a class="sp-item" href="' + esc(url) + '" data-idx="' + idx + '">' +
        '<div class="sp-icon">' + getIcon(url) + '</div>' +
        '<div class="sp-text">' +
          '<div class="sp-title">' + highlightTitle(title, tokens) + '</div>' +
          '<div class="sp-url">craicbet.com' + esc(url) + '</div>' +
        '</div>' +
      '</a>';
    });
    resultsList.innerHTML = html;
  }

  function showPopular() {
    var popular = [
      { title: 'GRAI Licence Explained', url: '/pages/grai-licence-explained' },
      { title: 'Betting Sites Ireland', url: '/pages/betting-sites-ireland' },
      { title: 'Best Casinos Ireland', url: '/pages/best-casinos-ireland' },
      { title: 'Free Bets Ireland', url: '/pages/free-bets-ireland' },
      { title: 'Casino Bonuses', url: '/pages/casino-bonuses-ireland' },
      { title: 'GRAI Licensed Bookmakers', url: '/pages/grai-licensed-bookmakers-ireland' },
    ];
    currentResults = popular;
    var html = '<div style="padding:10px 20px 4px;font-size:11px;font-weight:600;color:#6a9a7a;text-transform:uppercase;letter-spacing:1px">Popular pages</div>';
    popular.forEach(function(p, idx) {
      html += '<a class="sp-item" href="' + esc(p.url) + '" data-idx="' + idx + '">' +
        '<div class="sp-icon">' + getIcon(p.url) + '</div>' +
        '<div class="sp-text"><div class="sp-title">' + esc(p.title) + '</div>' +
        '<div class="sp-url">craicbet.com' + esc(p.url) + '</div></div></a>';
    });
    resultsList.innerHTML = html;
  }

  function moveSelection(dir) {
    if (!currentResults.length) return;
    selectedIdx += dir;
    if (selectedIdx < 0) selectedIdx = currentResults.length - 1;
    if (selectedIdx >= currentResults.length) selectedIdx = 0;
    var items = resultsList.querySelectorAll('.sp-item');
    for (var i=0; i<items.length; i++) {
      items[i].classList.toggle('active', i === selectedIdx);
    }
    if (items[selectedIdx]) items[selectedIdx].scrollIntoView({ block: 'nearest' });
  }

  function openSelected() {
    if (selectedIdx >= 0 && selectedIdx < currentResults.length) {
      window.location.href = currentResults[selectedIdx].url;
    } else if (currentResults.length > 0) {
      window.location.href = currentResults[0].url;
    }
  }

  /* ── Open / Close ── */
  function openSpotlight() {
    buildOverlay();
    overlay.classList.add('open');
    input.value = '';
    selectedIdx = -1;
    showPopular();
    // Small delay so the transition renders before focus
    setTimeout(function(){ input.focus(); }, 50);
    document.body.style.overflow = 'hidden';
  }

  function closeSpotlight() {
    if (!overlay) return;
    overlay.classList.remove('open');
    document.body.style.overflow = '';
  }

  /* ── Global keyboard shortcut: Cmd/Ctrl + K ── */
  document.addEventListener('keydown', function(e) {
    if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
      e.preventDefault();
      if (overlay && overlay.classList.contains('open')) {
        closeSpotlight();
      } else {
        openSpotlight();
      }
    }
  });

  /* ── Intercept search link clicks ── */
  document.addEventListener('click', function(e) {
    var a = e.target.closest('a[href*="/pages/search"]');
    if (a) {
      e.preventDefault();
      openSpotlight();
    }
  });

  /* ── Expose globally for megamenu ── */
  window.openSpotlight = openSpotlight;
})();
