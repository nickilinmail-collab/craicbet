/* CraicBet mobile mega menu — shared across all pages.
   Builds the two-column fullscreen menu (same design as the homepage) and binds it to .burger.
   Links are absolute so the script works at any depth. */
(function () {
  if (document.getElementById('megaMenu')) return; // homepage has its own markup
  var lang = (document.documentElement.getAttribute('lang') || 'en').slice(0, 2);

  var MENUS = {
    en: {
      search: ['🔍 Search', '/pages/search'],
      items: [
        ['🏛️', 'GRAI', 'GRAI Licensing', [
          ['GRAI Licence Explained', '/pages/grai-licence-explained'],
          ['GRAI-Licensed Bookmakers', '/pages/grai-licensed-bookmakers-ireland'],
          ['Licence Checker', '/pages/grai-licence-checker'],
          ['Licence Register Tracker', '/pages/grai-licence-register-tracker'],
          ['GRAI Complaints', '/pages/grai-complaints-ireland'],
          ['Is Gambling Legal?', '/pages/is-online-gambling-legal-ireland'],
          ['Unlicensed Sites Warning', '/pages/unlicensed-betting-sites-ireland']]],
        ['⚽', 'Betting', 'Sports Betting', [
          ['Best Betting Sites', '/pages/betting-sites-ireland'],
          ['Betting Apps', '/pages/betting-apps-ireland'],
          ['Free Bets Ireland', '/pages/free-bets-ireland'],
          ['Horse Racing', '/pages/horse-racing-betting-ireland'],
          ['GAA Betting', '/pages/gaa-betting-ireland'],
          ['Football Betting', '/pages/football-betting-ireland'],
          ['Acca Calculator', '/pages/accumulator-calculator-ireland']]],
        ['🎰', 'Casinos', 'Online Casinos', [
          ['Best Casinos Ireland', '/pages/best-casinos-ireland'],
          ['Fast Payout Casinos', '/pages/fast-payout-casinos'],
          ['Revolut Casinos', '/pages/revolut-casinos'],
          ['Google Pay Casinos', '/pages/google-pay-casino-ireland'],
          ['Trustly Casinos', '/pages/trustly-casino-ireland'],
          ['Bank Blocks Guide', '/pages/irish-banks-blocking-casino-deposits']]],
        ['🎁', 'Bonuses', 'Bonuses & Offers', [
          ['Casino Bonuses', '/pages/casino-bonuses-ireland'],
          ['No Deposit Bonuses', '/pages/no-deposit-bonus'],
          ['Wagering Explained', '/pages/wagering-requirements-explained'],
          ['Wagering Calculator', '/pages/wagering-calculator'],
          ['Welcome Bonuses', '/pages/casino-bonuses-ireland#welcome']]],
        ['🎲', 'Slots', 'Slots', [
          ['All Slot Reviews', '/pages/slot-reviews'],
          ['Gates of Olympus', '/pages/slots/gates-of-olympus'],
          ['Sweet Bonanza', '/pages/slots/sweet-bonanza'],
          ['Big Bass Bonanza', '/pages/slots/big-bass-bonanza'],
          ['Book of Dead', '/pages/slots/book-of-dead'],
          ['What Is RTP?', '/pages/rtp-explained']]],
        ['📖', 'Guides', 'Guides', [
          ['All Guides', '/pages/guides'],
          ['Latest News', '/pages/news/'],
          ['Responsible Gambling', '/pages/responsible-gambling'],
          ['Gambling Tax Ireland', '/pages/gambling-tax-ireland'],
          ['Each-Way Betting', '/pages/each-way-betting-guide'],
          ['Offshore Casinos', '/pages/offshore-casinos-ireland'],
          ['About CraicBet', '/pages/about']]]
      ]
    },
    ga: {
      search: ['🔍 Cuardach', '/pages/search'],
      items: [
        ['🏛️', 'GRAI', 'Ceadúnas GRAI', [['Ceadúnas GRAI in Éirinn', '/ga/ceadunas-grai-eire'], ['Geallghlacadóirí le ceadúnas GRAI', '/ga/buimeadoiri-le-ceadunas-grai']]],
        ['⚽', 'Gealltóireacht', 'Gealltóireacht', [['Geallghlacadóirí in Éirinn', '/ga/geallghlacadoiri-eireann']]],
        ['🎰', 'Caisíneonna', 'Caisíneonna', [['Na caisíneonna is fearr', '/ga/na-caisinoenna-is-fearr'], ['Caisíneo beo', '/ga/caisineo-beo'], ['Léirmheasanna', '/ga/leirmheasanna-caisineo']]],
        ['🎁', 'Bónais', 'Bónais', [['Bónais caisíneo', '/ga/bonais-caisineo']]],
        ['🎲', 'Sliotáin', 'Sliotáin', [['Sliotáin ar líne', '/ga/spinnteanna-saor-in-aisce']]],
        ['⚡', 'Íocaíochtaí', 'Íocaíochtaí Tapa', [['Íocaíochtaí tapa', '/ga/iocaiochtai-tapa']]],
        ['📖', 'Treoracha', 'Treoracha', [['Gach treoir', '/ga/treoracha'], ['English', '/']]]
      ]
    },
    pl: {
      search: ['🔍 Szukaj', '/pages/search'],
      items: [
        ['🏛️', 'GRAI', 'Licencja GRAI', [['Licencja GRAI w Irlandii', '/pl/licencja-grai-irlandia'], ['Bukmacherzy z licencją GRAI', '/pl/bukmacherzy-z-licencja-grai'], ['Licencja bukmacherska GRAI', '/pl/licencja-bukmacherska-grai-irlandia']]],
        ['⚽', 'Zakłady', 'Zakłady bukmacherskie', [['Zakłady bukmacherskie w Irlandii', '/pl/zaklady-bukmacherskie-irlandia']]],
        ['🎰', 'Kasyna', 'Kasyna online', [['Najlepsze kasyna', '/pl/najlepsze-kasyna'], ['Kasyno na żywo', '/pl/kasyno-na-zywo'], ['Recenzje kasyn', '/pl/recenzje-kasyn']]],
        ['🎁', 'Bonusy', 'Bonusy', [['Bonusy kasynowe', '/pl/bonusy-kasynowe']]],
        ['🎲', 'Sloty', 'Sloty', [['Darmowe spiny', '/pl/darmowe-spiny']]],
        ['⚡', 'Wypłaty', 'Szybkie wypłaty', [['Szybkie wypłaty', '/pl/szybkie-wyplaty']]],
        ['📖', 'Poradniki', 'Poradniki', [['Wszystkie poradniki', '/pl/poradniki'], ['English', '/']]]
      ]
    }
  };
  var M = MENUS[lang] || MENUS.en;

  // Which top item matches the current page (for initial highlight)
  var path = location.pathname;
  var activeIdx = 0;
  M.items.forEach(function (it, i) {
    if (it[3].some(function (l) { return l[1].split('#')[0] !== '/' && path.indexOf(l[1].split('#')[0]) === 0; })) activeIdx = i;
  });

  var css = '#megaMenu{position:fixed;inset:0;z-index:10000;background:rgba(0,0,0,.6);display:none}' +
    '#megaMenu .mm-inner{display:flex;width:min(680px,100vw);height:100%;margin-left:auto;background:#0d2518;box-shadow:-4px 0 40px rgba(0,0,0,.5)}' +
    '#megaMenu .mm-left{width:200px;flex-shrink:0;background:rgba(0,0,0,.3);display:flex;flex-direction:column;border-right:1px solid rgba(255,255,255,.08);padding:16px 0}' +
    '#megaMenu .mm-close{align-self:flex-end;margin:0 12px 12px;background:none;border:none;color:rgba(255,255,255,.5);font-size:1.3rem;cursor:pointer;line-height:1}' +
    '#megaMenu ul{list-style:none;margin:0;padding:0;flex:1}' +
    '#megaMenu .mm-item{display:flex;align-items:center;gap:10px;padding:13px 16px;cursor:pointer;border-left:3px solid transparent;color:rgba(255,255,255,.65);font-size:.95rem;font-weight:500}' +
    '#megaMenu .mm-item.active{border-left-color:#F26522;background:rgba(255,255,255,.07);color:#fff}' +
    '#megaMenu .mm-item .mm-arrow{margin-left:auto;opacity:.5}' +
    '#megaMenu .mm-search{display:block;margin:12px 16px 0;padding:10px;background:rgba(242,101,34,.15);border:1px solid rgba(242,101,34,.4);border-radius:8px;color:#F26522;text-align:center;font-size:.9rem;font-weight:600;text-decoration:none}' +
    '#megaMenu .mm-right{flex:1;padding:48px 24px 24px;overflow-y:auto}' +
    '#megaMenu .mm-sub{display:none}#megaMenu .mm-sub.active{display:block}' +
    '#megaMenu .mm-title{font-size:.72rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:#F26522;margin-bottom:14px}' +
    '#megaMenu .mm-sub a{display:block;padding:11px 0;color:rgba(255,255,255,.75);text-decoration:none;font-size:.97rem;font-weight:500;border-bottom:1px solid rgba(255,255,255,.07);transition:color .15s,padding-left .15s}' +
    '#megaMenu .mm-sub a:hover{color:#fff;padding-left:6px}' +
    '@media (max-width:480px){#megaMenu .mm-left{width:150px}#megaMenu .mm-item{padding:12px 10px;font-size:.88rem}#megaMenu .mm-right{padding:48px 16px 16px}}';

  var esc = function (s) { return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;'); };
  var html = '<div class="mm-inner"><div class="mm-left"><button class="mm-close" aria-label="Close menu">✕</button><ul>';
  M.items.forEach(function (it, i) {
    html += '<li class="mm-item' + (i === activeIdx ? ' active' : '') + '" data-i="' + i + '"><span>' + it[0] + '</span><span>' + esc(it[1]) + '</span><span class="mm-arrow">›</span></li>';
  });
  html += '</ul><a class="mm-search" href="' + M.search[1] + '">' + M.search[0] + '</a></div><div class="mm-right">';
  M.items.forEach(function (it, i) {
    html += '<div class="mm-sub' + (i === activeIdx ? ' active' : '') + '" data-i="' + i + '"><div class="mm-title">' + esc(it[2]) + '</div>';
    it[3].forEach(function (l) { html += '<a href="' + l[1] + '">' + esc(l[0]) + '</a>'; });
    html += '</div>';
  });
  html += '</div></div>';

  var style = document.createElement('style'); style.textContent = css; document.head.appendChild(style);
  var menu = document.createElement('div'); menu.id = 'megaMenu'; menu.setAttribute('aria-hidden', 'true'); menu.innerHTML = html;
  document.body.appendChild(menu);

  var oldBtn = document.querySelector('.burger');
  if (!oldBtn) return;
  var btn = oldBtn.cloneNode(true); // drops any old click handlers
  btn.removeAttribute('onclick');
  oldBtn.parentNode.replaceChild(btn, oldBtn);

  function open() { menu.style.display = 'block'; menu.setAttribute('aria-hidden', 'false'); btn.classList.add('is-open'); btn.setAttribute('aria-expanded', 'true'); document.body.style.overflow = 'hidden'; }
  function close() { menu.style.display = 'none'; menu.setAttribute('aria-hidden', 'true'); btn.classList.remove('is-open'); btn.setAttribute('aria-expanded', 'false'); document.body.style.overflow = ''; }
  btn.addEventListener('click', function () { menu.style.display === 'block' ? close() : open(); });
  menu.querySelector('.mm-close').addEventListener('click', close);
  menu.addEventListener('click', function (e) { if (e.target === menu) close(); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') close(); });
  menu.querySelectorAll('.mm-item').forEach(function (item) {
    item.addEventListener('click', function () {
      var i = item.getAttribute('data-i');
      menu.querySelectorAll('.mm-item').forEach(function (x) { x.classList.toggle('active', x === item); });
      menu.querySelectorAll('.mm-sub').forEach(function (s) { s.classList.toggle('active', s.getAttribute('data-i') === i); });
    });
  });
})();
