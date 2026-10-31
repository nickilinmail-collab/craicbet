/*  CraicBet Mini Slot Machine — conversion widget
    Self-contained: injects its own CSS, floating button, and modal.
    Just add <script src="/js/slot-game.js"></script> before </body>.
    Tracking link placeholder: https://plusfind.info/go/2e7c17f7eb1e426bd9fae5242aaa9b3e365b64d1eb0a0b0b/                    */

(function () {
  /* ===== Slot machine sound engine (Web Audio, no files) ===== */
  const sfx = (function(){
    let ctx = null;
    function ac(){
      if(!ctx){ try{ ctx = new (window.AudioContext||window.webkitAudioContext)(); }catch(e){ return null; } }
      if(ctx && ctx.state === 'suspended') ctx.resume().catch(function(){});
      return ctx;
    }
    function blip(freq, t0, dur, vol, type){
      const c = ac(); if(!c) return;
      const o = c.createOscillator(), g = c.createGain();
      o.type = type || 'square';
      o.frequency.setValueAtTime(freq, t0);
      g.gain.setValueAtTime(0.0001, t0);
      g.gain.exponentialRampToValueAtTime(vol, t0 + 0.005);
      g.gain.exponentialRampToValueAtTime(0.0001, t0 + dur);
      o.connect(g); g.connect(c.destination);
      o.start(t0); o.stop(t0 + dur + 0.02);
    }
    return {
      unlock: function(){ ac(); },
      lever: function(){
        const c = ac(); if(!c) return; const t = c.currentTime;
        const o = c.createOscillator(), g = c.createGain();
        o.type = 'sawtooth';
        o.frequency.setValueAtTime(700, t);
        o.frequency.exponentialRampToValueAtTime(180, t + 0.18);
        g.gain.setValueAtTime(0.08, t);
        g.gain.exponentialRampToValueAtTime(0.0001, t + 0.2);
        o.connect(g); g.connect(c.destination); o.start(t); o.stop(t + 0.22);
      },
      tick: function(){
        const c = ac(); if(!c) return;
        blip(1800 + Math.random()*500, c.currentTime, 0.03, 0.045, 'square');
      },
      reelStop: function(n){
        const c = ac(); if(!c) return; const t = c.currentTime;
        blip(220 - n*30, t, 0.09, 0.22, 'sine');
        blip(2500, t, 0.02, 0.06, 'square');
      },
      win: function(){
        const c = ac(); if(!c) return; const t = c.currentTime;
        [523, 659, 784, 1047, 1319, 1568].forEach(function(f, i){ blip(f, t + i*0.09, 0.25, 0.14, 'triangle'); });
        for(let i = 0; i < 12; i++){
          blip(2000 + Math.random()*2500, t + 0.5 + i*0.07 + Math.random()*0.03, 0.08, 0.05, 'sine');
        }
        [523, 784, 1047].forEach(function(f){ blip(f, t + 0.95, 0.5, 0.1, 'triangle'); });
      },
      almost: function(){
        const c = ac(); if(!c) return; const t = c.currentTime;
        blip(392, t, 0.16, 0.1, 'triangle');
        blip(311, t + 0.17, 0.26, 0.1, 'triangle');
      }
    };
  })();


  'use strict';

  /* ── symbols & paytable ── */
  const SYMBOLS = ['🍒','🍋','🍊','🍇','💎','7️⃣','⭐','🍀'];
  const REEL_COUNT = 3;
  const SPIN_MS = 2000;

  /* ── i18n ── */
  const lang = document.documentElement.lang || 'en';
  const T = {
    en: {
      fab: '🎰 Try Your Luck!',
      title: 'Lucky Spin',
      spin: 'SPIN',
      cta: '🎁 Claim the Bonus →',
      win: '🎉 YOU WIN! Claim your bonus now!',
      almost: '😮 So close! Try again or claim a bonus!',
      tryAgain: 'Spin Again',
      free: 'FREE',
      close: '✕'
    },
    pl: {
      fab: '🎰 Spróbuj Szczęścia!',
      title: 'Szczęśliwy Spin',
      spin: 'KRĘĆ',
      cta: '🎁 Odbierz Bonus →',
      win: '🎉 WYGRYWASZ! Odbierz bonus teraz!',
      almost: '😮 Tak blisko! Spróbuj ponownie lub odbierz bonus!',
      tryAgain: 'Kręć Ponownie',
      free: 'ZA DARMO',
      close: '✕'
    },
    ga: {
      fab: '🎰 Bain Triail As!',
      title: 'Casadh Ámharach',
      spin: 'CAS',
      cta: '🎁 Éiligh an Bónas →',
      win: '🎉 BHUAIGH TÚ! Éiligh do bhónas anois!',
      almost: '😮 Chomh gar! Bain triail eile as nó éiligh bónas!',
      tryAgain: 'Cas Arís',
      free: 'SAOR IN AISCE',
      close: '✕'
    }
  };
  const t = T[lang] || T.en;

  /* ── inject CSS ── */
  const css = document.createElement('style');
  css.textContent = `
/* floating button */
.cb-slot-fab{
  position:fixed;bottom:24px;right:24px;z-index:9998;
  background:linear-gradient(135deg,#F26522,#1B8C3D);
  color:#fff;border:none;border-radius:60px;
  padding:14px 24px;font-size:16px;font-weight:700;
  cursor:pointer;box-shadow:0 4px 20px rgba(242,101,34,.45);
  font-family:'Inter',sans-serif;
  animation:cb-fab-pulse 2s ease-in-out infinite;
  transition:transform .2s;
  display:flex;align-items:center;gap:8px;
}
.cb-slot-fab:hover{transform:scale(1.08);}
@keyframes cb-fab-pulse{
  0%,100%{box-shadow:0 4px 20px rgba(242,101,34,.45);}
  50%{box-shadow:0 4px 35px rgba(123,63,191,.7),0 0 60px rgba(242,101,34,.35);}
}
.cb-slot-fab .cb-badge{
  background:#fff;color:#F26522;font-size:11px;font-weight:800;
  padding:2px 7px;border-radius:20px;text-transform:uppercase;
  animation:cb-badge-bounce 1.5s ease-in-out infinite;
}
@keyframes cb-badge-bounce{0%,100%{transform:scale(1);}50%{transform:scale(1.15);}}

/* overlay */
.cb-slot-overlay{
  position:fixed;inset:0;z-index:9999;
  background:rgba(0,0,0,.75);
  display:flex;align-items:center;justify-content:center;
  opacity:0;pointer-events:none;transition:opacity .3s;
}
.cb-slot-overlay.open{opacity:1;pointer-events:all;}

/* modal = cabinet */
.cb-slot-modal{
  background:linear-gradient(160deg,#0A2E14 0%,#0F3D1C 100%);
  border-radius:22px;padding:24px 22px 26px;
  width:min(400px,92vw);text-align:center;
  color:#fff;font-family:'Inter',sans-serif;
  box-shadow:0 20px 60px rgba(0,0,0,.55),0 0 0 4px #7a4a12,0 0 0 7px #c8871f,0 0 45px rgba(242,101,34,.25);
  transform:scale(.85);transition:transform .3s;
  position:relative;
}
.cb-slot-overlay.open .cb-slot-modal{transform:scale(1);}
.cb-slot-modal.shake{animation:cb-shake .45s ease;}
@keyframes cb-shake{
  0%,100%{transform:scale(1) translateX(0);}
  20%{transform:scale(1) translateX(-9px) rotate(-.6deg);}
  40%{transform:scale(1) translateX(8px) rotate(.5deg);}
  60%{transform:scale(1) translateX(-6px);}
  80%{transform:scale(1) translateX(4px);}
}
.cb-slot-modal.winflash{animation:cb-winflash 1.6s ease;}
@keyframes cb-winflash{
  0%,100%{box-shadow:0 20px 60px rgba(0,0,0,.55),0 0 0 4px #7a4a12,0 0 0 7px #c8871f,0 0 45px rgba(242,101,34,.25);}
  25%,75%{box-shadow:0 20px 60px rgba(0,0,0,.55),0 0 0 4px #ffd34d,0 0 0 7px #ffb300,0 0 90px rgba(255,200,60,.8);}
  50%{box-shadow:0 20px 60px rgba(0,0,0,.55),0 0 0 4px #fff,0 0 0 7px #ffd34d,0 0 120px rgba(255,220,100,.9);}
}

/* marquee bulbs */
.cb-bulbs{display:flex;justify-content:center;gap:9px;margin:-4px 0 8px;}
.cb-bulbs i{
  width:10px;height:10px;border-radius:50%;
  background:#5c3a10;box-shadow:inset 0 0 2px rgba(0,0,0,.6);
  animation:cb-bulb 1.1s linear infinite;
}
.cb-bulbs i:nth-child(2n){animation-delay:.55s;}
@keyframes cb-bulb{
  0%,49%{background:#ffd34d;box-shadow:0 0 8px #ffd34d,0 0 16px rgba(255,211,77,.6);}
  50%,100%{background:#5c3a10;box-shadow:inset 0 0 2px rgba(0,0,0,.6);}
}
.cb-slot-overlay .cb-bulbs i{animation-play-state:running;}
.cb-slot-modal.spinning .cb-bulbs i{animation-duration:.35s;}

.cb-slot-close{
  position:absolute;top:10px;right:14px;background:none;border:none;
  color:rgba(255,255,255,.6);font-size:22px;cursor:pointer;transition:color .2s;z-index:3;
}
.cb-slot-close:hover{color:#fff;}

.cb-slot-title{
  font-size:24px;font-weight:900;margin:0 0 2px;letter-spacing:1px;
  background:linear-gradient(90deg,#ffd34d,#F26522,#ffd34d);
  background-size:200% 100%;
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;
  animation:cb-title-shine 3s linear infinite;
}
@keyframes cb-title-shine{0%{background-position:0 0;}100%{background-position:200% 0;}}
.cb-slot-subtitle{font-size:12px;color:rgba(255,255,255,.45);margin-bottom:12px;letter-spacing:2px;text-transform:uppercase;}

/* reel window */
.cb-machine{position:relative;padding:0 26px;}
.cb-reels{
  display:flex;gap:8px;justify-content:center;
  background:linear-gradient(180deg,#07230f,#0c3317);
  border:3px solid #c8871f;border-radius:16px;
  padding:12px 10px;position:relative;margin-bottom:18px;
  box-shadow:inset 0 6px 18px rgba(0,0,0,.6);
}
.cb-reel{
  width:84px;height:96px;border-radius:10px;overflow:hidden;position:relative;
  background:linear-gradient(180deg,#d9d9d9 0%,#ffffff 22%,#ffffff 78%,#c9c9c9 100%);
  box-shadow:inset 0 10px 14px rgba(0,0,0,.35),inset 0 -10px 14px rgba(0,0,0,.35);
}
.cb-reel::after{ /* glass shine */
  content:'';position:absolute;inset:0;pointer-events:none;
  background:linear-gradient(105deg,transparent 40%,rgba(255,255,255,.35) 48%,transparent 56%);
}
.cb-strip{
  position:absolute;left:0;top:0;width:100%;
  will-change:transform;
}
.cb-cell{
  height:96px;display:flex;align-items:center;justify-content:center;
  font-size:52px;line-height:1;
}
.cb-reel.spin-blur .cb-cell{filter:blur(1.5px);}
.cb-reel.land .cb-strip{animation:cb-land .32s ease-out;}
@keyframes cb-land{
  0%{margin-top:0;}35%{margin-top:14px;}70%{margin-top:-6px;}100%{margin-top:0;}
}
.cb-reel.win{box-shadow:inset 0 10px 14px rgba(0,0,0,.2),inset 0 -10px 14px rgba(0,0,0,.2),0 0 0 3px #ffd34d,0 0 22px rgba(255,211,77,.8);}

/* payline */
.cb-payline{
  position:absolute;left:4px;right:4px;top:50%;height:3px;margin-top:-1.5px;
  background:linear-gradient(90deg,transparent,#F26522 15%,#F26522 85%,transparent);
  border-radius:2px;opacity:.55;pointer-events:none;z-index:2;
}
.cb-payline::before,.cb-payline::after{
  content:'▶';position:absolute;top:50%;transform:translateY(-50%);
  font-size:13px;color:#ffd34d;text-shadow:0 0 6px rgba(255,211,77,.8);
}
.cb-payline::before{left:-3px;}
.cb-payline::after{right:-3px;content:'◀';}
.cb-payline.hit{opacity:1;animation:cb-payline-hit .5s ease 4;}
@keyframes cb-payline-hit{
  0%,100%{background:linear-gradient(90deg,transparent,#F26522 15%,#F26522 85%,transparent);}
  50%{background:linear-gradient(90deg,transparent,#ffd34d 15%,#ffd34d 85%,transparent);box-shadow:0 0 18px #ffd34d;}
}

/* lever */
.cb-lever{
  position:absolute;right:-18px;top:6px;width:20px;height:110px;cursor:pointer;z-index:2;
}
.cb-lever .cb-lever-base{
  position:absolute;right:0;top:44px;width:14px;height:34px;border-radius:5px;
  background:linear-gradient(90deg,#8a5a16,#c8871f,#8a5a16);
  box-shadow:0 2px 6px rgba(0,0,0,.5);
}
.cb-lever .cb-lever-arm{
  position:absolute;right:4px;bottom:50px;width:6px;height:62px;border-radius:3px;
  background:linear-gradient(90deg,#9aa0a6,#e8eaed,#9aa0a6);
  transform-origin:bottom center;transition:transform .18s ease-in;
}
.cb-lever .cb-lever-arm::after{
  content:'';position:absolute;top:-16px;left:50%;transform:translateX(-50%);
  width:20px;height:20px;border-radius:50%;
  background:radial-gradient(circle at 35% 30%,#ff9d5c,#F26522 55%,#a33c0a);
  box-shadow:0 2px 6px rgba(0,0,0,.5);
}
.cb-lever.pulled .cb-lever-arm{transform:rotateX(150deg);}

/* spin button */
.cb-spin-btn{
  background:linear-gradient(180deg,#ff8a48,#F26522 45%,#c84f12);
  color:#fff;border:none;border-radius:50px;
  padding:14px 52px;font-size:19px;font-weight:900;
  cursor:pointer;font-family:'Inter',sans-serif;
  transition:all .15s;letter-spacing:2px;
  box-shadow:0 5px 0 #8f3708,0 8px 18px rgba(242,101,34,.45);
}
.cb-spin-btn:hover:not(:disabled){transform:translateY(-1px);box-shadow:0 6px 0 #8f3708,0 10px 24px rgba(242,101,34,.55);}
.cb-spin-btn:active:not(:disabled){transform:translateY(4px);box-shadow:0 1px 0 #8f3708,0 4px 10px rgba(242,101,34,.4);}
.cb-spin-btn:disabled{opacity:.55;cursor:default;box-shadow:0 2px 0 #8f3708;}

/* result */
.cb-result{min-height:28px;margin:14px 0 4px;font-size:15px;font-weight:700;transition:opacity .3s;}

/* CTA */
.cb-cta{
  display:inline-block;
  background:linear-gradient(135deg,#F26522,#e8511a);
  color:#fff;text-decoration:none;border-radius:50px;
  padding:13px 36px;font-size:16px;font-weight:700;
  font-family:'Inter',sans-serif;
  box-shadow:0 4px 15px rgba(242,101,34,.4);
  transition:all .2s;animation:cb-cta-glow 1.8s ease-in-out infinite;
  margin-top:8px;
}
.cb-cta:hover{transform:scale(1.05);box-shadow:0 6px 25px rgba(242,101,34,.5);}
@keyframes cb-cta-glow{
  0%,100%{box-shadow:0 4px 15px rgba(242,101,34,.4);}
  50%{box-shadow:0 4px 30px rgba(242,101,34,.6),0 0 50px rgba(242,101,34,.2);}
}
.cb-cta-wrap{display:none;margin-top:8px;}
.cb-cta-wrap.show{display:block;}

.cb-again{
  display:inline-block;margin-top:12px;
  color:rgba(255,255,255,.5);font-size:13px;cursor:pointer;
  text-decoration:underline;background:none;border:none;font-family:'Inter',sans-serif;
}
.cb-again:hover{color:#fff;}

.cb-confetti{position:absolute;inset:0;pointer-events:none;border-radius:22px;overflow:hidden;z-index:4;}

@media(max-width:480px){
  .cb-slot-fab{bottom:16px;right:12px;padding:11px 18px;font-size:14px;}
  .cb-reel{width:70px;height:84px;}
  .cb-cell{height:84px;font-size:44px;}
  .cb-slot-modal{padding:20px 14px 22px;}
  .cb-machine{padding:0 20px;}
  .cb-lever{right:-10px;}
}
`;
  document.head.appendChild(css);

  /* ── build DOM ── */
  // floating button
  const fab = document.createElement('button');
  fab.className = 'cb-slot-fab';
  fab.innerHTML = `${t.fab} <span class="cb-badge">${t.free}</span>`;
  document.body.appendChild(fab);

  // overlay
  const overlay = document.createElement('div');
  overlay.className = 'cb-slot-overlay';
  overlay.innerHTML = `
    <div class="cb-slot-modal" id="cbModal">
      <canvas class="cb-confetti" id="cbConfetti"></canvas>
      <button class="cb-slot-close">${t.close}</button>
      <div class="cb-slot-title">${t.title}</div>
      <div class="cb-bulbs"><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i></div>
      <div class="cb-slot-subtitle">CraicBet.com</div>
      <div class="cb-machine">
        <div class="cb-reels" id="cbReels"><div class="cb-payline" id="cbPayline"></div></div>
        <div class="cb-lever" id="cbLever"><div class="cb-lever-base"></div><div class="cb-lever-arm"></div></div>
      </div>
      <button class="cb-spin-btn" id="cbSpin">${t.spin}</button>
      <div class="cb-result" id="cbResult"></div>
      <div class="cb-cta-wrap" id="cbCtaWrap">
        <a href="https://plusfind.info/go/2e7c17f7eb1e426bd9fae5242aaa9b3e365b64d1eb0a0b0b/" class="cb-cta" id="cbCta" target="_blank" rel="noopener">${t.cta}</a><br>
        <button class="cb-again" id="cbAgain">${t.tryAgain}</button>
      </div>
    </div>
  `;
  document.body.appendChild(overlay);

  const reelsEl = document.getElementById('cbReels');
  const spinBtn = document.getElementById('cbSpin');
  const resultEl = document.getElementById('cbResult');
  const ctaWrap = document.getElementById('cbCtaWrap');
  const againBtn = document.getElementById('cbAgain');
  const closeBtn = overlay.querySelector('.cb-slot-close');
  const confettiCanvas = document.getElementById('cbConfetti');
  const ctx = confettiCanvas.getContext('2d');

  const modalEl = document.getElementById('cbModal');
  const leverEl = document.getElementById('cbLever');
  const paylineEl = document.getElementById('cbPayline');

  // create reels: each is a window over a vertical strip of symbols
  const CELL_H = window.matchMedia('(max-width:480px)').matches ? 84 : 96;
  const reelEls = [];
  for (let i = 0; i < REEL_COUNT; i++) {
    const reel = document.createElement('div');
    reel.className = 'cb-reel';
    const strip = document.createElement('div');
    strip.className = 'cb-strip';
    const startSym = SYMBOLS[Math.floor(Math.random() * SYMBOLS.length)];
    strip.appendChild(makeCell(startSym));
    reel.appendChild(strip);
    reelsEl.appendChild(reel);
    reelEls.push({ el: reel, strip: strip, current: startSym });
  }

  function makeCell(sym) {
    const d = document.createElement('div');
    d.className = 'cb-cell';
    d.textContent = sym;
    return d;
  }

  /* ── game logic ── */
  let spinning = false;
  let spinCount = 0;

  function open() { overlay.classList.add('open'); }
  function close() { overlay.classList.remove('open'); }

  fab.addEventListener('click', open);
  closeBtn.addEventListener('click', close);
  overlay.addEventListener('click', function (e) {
    if (e.target === overlay) close();
  });

  function getResult() {
    spinCount++;
    const results = [];
    // Every 3rd spin give a "win" (2 matching + nudge), every 5th a full win
    if (spinCount % 5 === 0) {
      // full win
      const s = SYMBOLS[Math.floor(Math.random() * SYMBOLS.length)];
      return [s, s, s];
    }
    if (spinCount % 2 === 0) {
      // near miss — 2 matching
      const s = SYMBOLS[Math.floor(Math.random() * SYMBOLS.length)];
      let other = SYMBOLS[Math.floor(Math.random() * SYMBOLS.length)];
      while (other === s) other = SYMBOLS[Math.floor(Math.random() * SYMBOLS.length)];
      const pos = Math.floor(Math.random() * 3);
      for (let i = 0; i < 3; i++) results.push(i === pos ? other : s);
      return results;
    }
    // random
    for (let i = 0; i < 3; i++) results.push(SYMBOLS[Math.floor(Math.random() * SYMBOLS.length)]);
    return results;
  }

  async function spin() {
    if (spinning) return;
    spinning = true;
    sfx.unlock();
    sfx.lever();
    leverEl.classList.add('pulled');
    setTimeout(function(){ leverEl.classList.remove('pulled'); }, 450);
    modalEl.classList.add('spinning');
    modalEl.classList.remove('winflash');
    spinBtn.disabled = true;
    resultEl.textContent = '';
    ctaWrap.classList.remove('show');
    paylineEl.classList.remove('hit');
    reelEls.forEach(r => r.el.classList.remove('win', 'land'));
    stopConfetti();

    const final = getResult();

    // tick sounds while reels turn
    const tickTimer = setInterval(function(){ sfx.tick(); }, 90);

    const delays = [0, 350, 700];
    const promises = reelEls.map((reel, i) => animateReel(reel, final[i], SPIN_MS + delays[i], i));
    await Promise.all(promises);
    clearInterval(tickTimer);
    modalEl.classList.remove('spinning');

    const isWin = final[0] === final[1] && final[1] === final[2];
    const nearMiss = !isWin && (final[0] === final[1] || final[1] === final[2] || final[0] === final[2]);
    if (isWin) {
      reelEls.forEach(r => r.el.classList.add('win'));
      paylineEl.classList.add('hit');
      modalEl.classList.add('winflash');
      resultEl.textContent = t.win;
      sfx.win();
      startConfetti();
    } else {
      if (nearMiss) {
        modalEl.classList.add('shake');
        setTimeout(function(){ modalEl.classList.remove('shake'); }, 500);
      }
      resultEl.textContent = t.almost;
      sfx.almost();
    }

    ctaWrap.classList.add('show');
    spinning = false;
    spinBtn.disabled = false;
  }

  // Real reel: build a long vertical strip, scroll it down with easing, bounce on stop
  function animateReel(reel, finalSymbol, duration, idx) {
    return new Promise(resolve => {
      const LOOPS = 22 + idx * 6; // symbols to scroll past
      const strip = reel.strip;
      // rebuild strip: current symbol on top, randoms, final at bottom
      strip.style.transition = 'none';
      strip.style.transform = 'translateY(0)';
      strip.innerHTML = '';
      strip.appendChild(makeCell(reel.current));
      for (let i = 0; i < LOOPS - 1; i++) {
        strip.appendChild(makeCell(SYMBOLS[Math.floor(Math.random() * SYMBOLS.length)]));
      }
      strip.appendChild(makeCell(finalSymbol));
      reel.current = finalSymbol;

      // force reflow, then animate to the last cell
      void strip.offsetHeight;
      reel.el.classList.add('spin-blur');
      strip.style.transition = 'transform ' + duration + 'ms cubic-bezier(.12,.65,.28,1)';
      strip.style.transform = 'translateY(-' + (LOOPS * CELL_H) + 'px)';

      let done = false;
      function finish() {
        if (done) return;
        done = true;
        reel.el.classList.remove('spin-blur');
        reel.el.classList.add('land');
        setTimeout(function(){ reel.el.classList.remove('land'); }, 350);
        sfx.reelStop(idx);
        resolve();
      }
      strip.addEventListener('transitionend', finish, { once: true });
      setTimeout(finish, duration + 120); // safety
    });
  }

  leverEl.addEventListener('click', spin);
  spinBtn.addEventListener('click', spin);
  againBtn.addEventListener('click', function () {
    ctaWrap.classList.remove('show');
    resultEl.textContent = '';
    spin();
  });

  /* ── confetti ── */
  let confettiParts = [];
  let confettiRAF = null;

  function startConfetti() {
    confettiCanvas.width = confettiCanvas.offsetWidth;
    confettiCanvas.height = confettiCanvas.offsetHeight;
    confettiParts = [];
    for (let i = 0; i < 60; i++) {
      confettiParts.push({
        x: Math.random() * confettiCanvas.width,
        y: Math.random() * confettiCanvas.height * -1,
        w: 6 + Math.random() * 6,
        h: 4 + Math.random() * 4,
        vx: (Math.random() - 0.5) * 3,
        vy: 2 + Math.random() * 3,
        color: ['#F26522','#1B8C3D','#fbbf24','#22c55e','#ef4444','#3b82f6'][Math.floor(Math.random()*6)],
        rot: Math.random() * 360,
        rv: (Math.random() - 0.5) * 10
      });
    }
    drawConfetti();
  }

  function drawConfetti() {
    ctx.clearRect(0, 0, confettiCanvas.width, confettiCanvas.height);
    let alive = false;
    confettiParts.forEach(p => {
      p.x += p.vx;
      p.y += p.vy;
      p.rot += p.rv;
      if (p.y < confettiCanvas.height + 20) alive = true;
      ctx.save();
      ctx.translate(p.x, p.y);
      ctx.rotate(p.rot * Math.PI / 180);
      ctx.fillStyle = p.color;
      ctx.fillRect(-p.w / 2, -p.h / 2, p.w, p.h);
      ctx.restore();
    });
    if (alive) confettiRAF = requestAnimationFrame(drawConfetti);
  }

  function stopConfetti() {
    if (confettiRAF) cancelAnimationFrame(confettiRAF);
    ctx.clearRect(0, 0, confettiCanvas.width, confettiCanvas.height);
  }
})();
