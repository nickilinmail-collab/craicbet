/* CraicBet geo-switcher: sets a 90-day cookie when user manually picks IE or UK */
(function () {
  document.addEventListener('DOMContentLoaded', function () {
    var switcher = document.querySelector('.lang-switcher');
    if (!switcher) return;
    var links = switcher.querySelectorAll('a');
    links.forEach(function (a) {
      a.addEventListener('click', function () {
        var href = a.getAttribute('href') || '';
        var geo = (href.indexOf('/uk') > -1 || href === './' && window.location.pathname.indexOf('/uk') > -1) ? 'uk' : 'ie';
        // Simple heuristic: if the link goes to ../ or pages/ it's IE, if it goes to uk/ it's UK
        if (href.indexOf('uk') > -1) geo = 'uk';
        else geo = 'ie';
        var d = new Date();
        d.setTime(d.getTime() + 90 * 24 * 60 * 60 * 1000);
        document.cookie = 'cb_geo=' + geo + ';expires=' + d.toUTCString() + ';path=/';
      });
    });
  });
})();
