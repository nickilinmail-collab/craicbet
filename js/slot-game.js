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

/* badge */
.cb-slot-fab .cb-badge{
  background:#fff;color:#F26522;font-size:11px;font-weight:800;
  padding:2px 7px;border-radius:20px;text-transform:uppercase;
  animation:cb-badge-bounce 1.5s ease-in-out infinite;
}
@keyframes cb-badge-bounce{
  0%,100%{transform:scale(1);}
  50%{transform:scale(1.15);}
}

/* overlay */
.cb-slot-overlay{
  position:fixed;inset:0;z-index:9999;
  background:rgba(0,0,0,.7);
  display:flex;align-items:center;justify-content:center;
  opacity:0;pointer-events:none;
  transition:opacity .3s;
}
.cb-slot-overlay.open{opacity:1;pointer-events:all;}

/* modal */
.cb-slot-modal{
  background:linear-gradient(160deg,#0A2E14 0%,#0F3D1C 100%);
  border-radius:20px;padding:28px 24px;
  width:min(380px,92vw);text-align:center;
  color:#fff;font-family:'Inter',sans-serif;
  box-shadow:0 20px 60px rgba(0,0,0,.5);
  transform:scale(.85);transition:transform .3s;
  position:relative;
}
.cb-slot-overlay.open .cb-slot-modal{transform:scale(1);}

.cb-slot-close{
  position:absolute;top:12px;right:16px;background:none;border:none;
  color:rgba(255,255,255,.6);font-size:22px;cursor:pointer;
  transition:color .2s;
}
.cb-slot-close:hover{color:#fff;}

.cb-slot-title{
  font-size:22px;font-weight:800;margin:0 0 4px;
  background:linear-gradient(90deg,#F26522,#fbbf24);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;
}
.cb-slot-subtitle{font-size:13px;color:rgba(255,255,255,.5);margin-bottom:18px;}

/* reels */
.cb-reels{
  display:flex;gap:10px;justify-content:center;margin-bottom:20px;
}
.cb-reel{
  width:80px;height:90px;
  background:rgba(255,255,255,.08);
  border:2px solid rgba(255,255,255,.12);
  border-radius:14px;
  display:flex;align-items:center;justify-content:center;
  font-size:48px;line-height:1;
  overflow:hidden;position:relative;
  transition:border-color .3s;
}
.cb-reel.win{border-color:#F26522;box-shadow:0 0 20px rgba(242,101,34,.4);}

.cb-reel-inner{
  display:flex;flex-direction:column;align-items:center;
  transition:transform .1s;
}

/* spin button */
.cb-spin-btn{
  background:linear-gradient(135deg,#F26522,#e8511a);
  color:#fff;border:none;border-radius:50px;
  padding:14px 48px;font-size:18px;font-weight:800;
  cursor:pointer;font-family:'Inter',sans-serif;
  transition:all .2s;letter-spacing:1px;
  box-shadow:0 4px 15px rgba(242,101,34,.4);
}
.cb-spin-btn:hover:not(:disabled){transform:scale(1.05);box-shadow:0 6px 25px rgba(242,101,34,.5);}
.cb-spin-btn:disabled{opacity:.5;cursor:default;}

/* result message */
.cb-result{
  min-height:28px;margin:14px 0 6px;
  font-size:15px;font-weight:600;
  transition:opacity .3s;
}

/* CTA */
.cb-cta{
  display:inline-block;
  background:linear-gradient(135deg,#F26522,#e8511a);
  color:#fff;text-decoration:none;border-radius:50px;
  padding:13px 36px;font-size:16px;font-weight:700;
  font-family:'Inter',sans-serif;
  box-shadow:0 4px 15px rgba(242,101,34,.4);
  transition:all .2s;
  animation:cb-cta-glow 1.8s ease-in-out infinite;
  margin-top:8px;
}
.cb-cta:hover{transform:scale(1.05);box-shadow:0 6px 25px rgba(242,101,34,.5);}
@keyframes cb-cta-glow{
  0%,100%{box-shadow:0 4px 15px rgba(242,101,34,.4);}
  50%{box-shadow:0 4px 30px rgba(242,101,34,.6),0 0 50px rgba(242,101,34,.2);}
}

.cb-cta-wrap{display:none;margin-top:10px;}
.cb-cta-wrap.show{display:block;}

/* try-again link */
.cb-again{
  display:inline-block;margin-top:12px;
  color:rgba(255,255,255,.5);font-size:13px;cursor:pointer;
  text-decoration:underline;background:none;border:none;
  font-family:'Inter',sans-serif;
}
.cb-again:hover{color:#fff;}

/* confetti canvas */
.cb-confetti{
  position:absolute;inset:0;pointer-events:none;border-radius:20px;overflow:hidden;
}

/* mobile */
@media(max-width:480px){
  .cb-slot-fab{bottom:16px;right:12px;padding:11px 18px;font-size:14px;}
  .cb-reel{width:68px;height:78px;font-size:40px;}
  .cb-slot-modal{padding:22px 16px;}
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
    <div class="cb-slot-modal">
      <canvas class="cb-confetti" id="cbConfetti"></canvas>
      <button class="cb-slot-close">${t.close}</button>
      <div class="cb-slot-title">${t.title}</div>
      <div class="cb-slot-subtitle">CraicBet.com</div>
      <div class="cb-reels" id="cbReels"></div>
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

  // create reels
  const reelEls = [];
  for (let i = 0; i < REEL_COUNT; i++) {
    const reel = document.createElement('div');
    reel.className = 'cb-reel';
    const inner = document.createElement('div');
    inner.className = 'cb-reel-inner';
    inner.textContent = SYMBOLS[Math.floor(Math.random() * SYMBOLS.length)];
    reel.appendChild(inner);
    reelsEl.appendChild(reel);
    reelEls.push({ el: reel, inner: inner });
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
    spinBtn.disabled = true;
    resultEl.textContent = '';
    ctaWrap.classList.remove('show');
    reelEls.forEach(r => r.el.classList.remove('win'));
    stopConfetti();

    const final = getResult();

    // animate each reel
    const delays = [0, 300, 600];
    const promises = reelEls.map((reel, i) => animateReel(reel, final[i], SPIN_MS + delays[i]));
    await Promise.all(promises);

    // check result
    const isWin = final[0] === final[1] && final[1] === final[2];
    if (isWin) {
      reelEls.forEach(r => r.el.classList.add('win'));
      resultEl.textContent = t.win;
      sfx.win();
      startConfetti();
    } else {
      resultEl.textContent = t.almost;
      sfx.almost();
    }

    ctaWrap.classList.add('show');
    spinning = false;
    spinBtn.disabled = false;
  }

  function animateReel(reel, finalSymbol, duration) {
    return new Promise(resolve => {
      const start = performance.now();
      const interval = 80;
      let last = start;

      function tick(now) {
        if (now - last >= interval) {
          reel.inner.textContent = SYMBOLS[Math.floor(Math.random() * SYMBOLS.length)];
          sfx.tick();
          last = now;
        }
        if (now - start < duration) {
          requestAnimationFrame(tick);
        } else {
          reel.inner.textContent = finalSymbol;
          sfx.reelStop(0);
          resolve();
        }
      }
      requestAnimationFrame(tick);
    });
  }

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
