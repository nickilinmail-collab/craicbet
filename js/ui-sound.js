/* CraicBet UI click sound - subtle pop via Web Audio */
(function(){
  var ctx=null;
  function ensure(){
    if(!ctx){try{ctx=new(window.AudioContext||window.webkitAudioContext)()}catch(e){return null}}
    if(ctx&&ctx.state==='suspended'){ctx.resume().catch(function(){})}
    return ctx;
  }
  function click(){
    var c=ensure();if(!c)return;
    var t=c.currentTime;
    /* soft pop: short sine blip with fast decay */
    var o=c.createOscillator();
    var g=c.createGain();
    o.type='sine';
    o.frequency.setValueAtTime(620,t);
    o.frequency.exponentialRampToValueAtTime(380,t+0.07);
    g.gain.setValueAtTime(0.0001,t);
    g.gain.exponentialRampToValueAtTime(0.12,t+0.008);
    g.gain.exponentialRampToValueAtTime(0.0001,t+0.09);
    o.connect(g);g.connect(c.destination);
    o.start(t);o.stop(t+0.1);
  }
  document.addEventListener('pointerdown',function(e){
    var el=e.target.closest('a.btn, .btn, .nav a, .logo, .cta-btn, button, .lang-switcher a');
    if(el)click();
  },{passive:true});
})();
