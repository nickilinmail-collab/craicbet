/* Clean URL: strip .html from the address bar */
(function(){
  try{
    if(/\.html$/.test(location.pathname)){
      var p = location.pathname.replace(/index\.html$/,'').replace(/\.html$/,'');
      history.replaceState(null, '', p + location.search + location.hash);
    }
  }catch(e){}
})();
