/* CraicBet geo-switcher — для внутренних страниц (не главная) */
(function () {
  function setCookie(name, value, days) {
    var d = new Date();
    d.setTime(d.getTime() + days * 24 * 60 * 60 * 1000);
    document.cookie = name + '=' + value + ';expires=' + d.toUTCString() + ';path=/';
  }

  document.addEventListener('DOMContentLoaded', function () {
    var switcher = document.querySelector('.lang-switcher');
    if (!switcher) return;

    var links = switcher.querySelectorAll('a');
    links.forEach(function (a) {
      if (a.classList.contains('active-lang')) return;

      a.addEventListener('click', function (e) {
        var onUKPage = window.location.pathname.indexOf('/uk') > -1;
        if (onUKPage) {
          // Clicking IE — set cookie, go to IE root
          e.preventDefault();
          setCookie('cb_geo', 'ie', 90);
          window.location.href = '/?geo=ie';
        } else {
          // Clicking UK — set cookie, go to UK
          e.preventDefault();
          setCookie('cb_geo', 'uk', 90);
          window.location.href = '/uk/';
        }
      });
    });
  });
})();
