/* Clean URL: strip .html from the address bar */
(function(){
  try{
    if(/\.html$/.test(location.pathname)){
      var p = location.pathname.replace(/index\.html$/,'').replace(/\.html$/,'');
      history.replaceState(null, '', p + location.search + location.hash);
    }
  }catch(e){}
})();
/* CraicBet UI sound - juicy can-crack + fizz (soda-ad style) */
(function(){
  var ctx=null,noiseBuf=null;
  function ensure(){
    if(!ctx){try{ctx=new(window.AudioContext||window.webkitAudioContext)()}catch(e){return null}}
    if(ctx.state==='suspended'){ctx.resume().catch(function(){})}
    if(!noiseBuf){
      var len=ctx.sampleRate*0.5;
      noiseBuf=ctx.createBuffer(1,len,ctx.sampleRate);
      var d=noiseBuf.getChannelData(0);
      for(var i=0;i<len;i++)d[i]=Math.random()*2-1;
    }
    return ctx;
  }
  function fizz(){
    var c=ensure();if(!c)return;
    var t=c.currentTime;

    /* 1) CRACK - sharp transient */
    var crack=c.createBufferSource();crack.buffer=noiseBuf;
    var chp=c.createBiquadFilter();chp.type='highpass';chp.frequency.value=2500;
    var cg=c.createGain();
    cg.gain.setValueAtTime(0.5,t);
    cg.gain.exponentialRampToValueAtTime(0.001,t+0.045);
    crack.connect(chp);chp.connect(cg);cg.connect(c.destination);
    crack.start(t);crack.stop(t+0.05);

    /* 2) POP - low thump body */
    var o=c.createOscillator(),og=c.createGain();
    o.type='sine';
    o.frequency.setValueAtTime(300,t);
    o.frequency.exponentialRampToValueAtTime(90,t+0.08);
    og.gain.setValueAtTime(0.35,t);
    og.gain.exponentialRampToValueAtTime(0.001,t+0.1);
    o.connect(og);og.connect(c.destination);
    o.start(t);o.stop(t+0.11);

    /* 3) FIZZ - sparkling carbonation tail */
    var fz=c.createBufferSource();fz.buffer=noiseBuf;fz.loop=true;
    var fbp=c.createBiquadFilter();fbp.type='bandpass';
    fbp.frequency.setValueAtTime(5200,t);
    fbp.frequency.exponentialRampToValueAtTime(7500,t+0.35);
    fbp.Q.value=0.9;
    var fg=c.createGain();
    fg.gain.setValueAtTime(0.0001,t+0.02);
    fg.gain.exponentialRampToValueAtTime(0.22,t+0.06);
    fg.gain.exponentialRampToValueAtTime(0.0001,t+0.42);
    fz.connect(fbp);fbp.connect(fg);fg.connect(c.destination);
    fz.start(t+0.02);fz.stop(t+0.45);
  }
  document.addEventListener('pointerdown',function(e){
    var el=e.target.closest('a.btn, .btn, .nav a, .logo, .cta-btn, button, .lang-switcher a');
    if(el)fizz();
  },{passive:true});
})();
