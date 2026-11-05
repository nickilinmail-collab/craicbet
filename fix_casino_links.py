#!/usr/bin/env python3
import re, os

PAGES = "/home/claude/craicbet/pages"

HUB_BOX_BEST = """<div style="background:#fef3f0;border:1px solid #c0392b;border-radius:8px;padding:16px 20px;margin:20px 0">
  <strong>🎰 Casino Guides</strong>
  <ul style="margin:8px 0 0;padding-left:18px;columns:2;column-gap:24px">
    <li><a href="why-no-grai-casino-licence-ireland">GRAI casino licence: the facts</a></li>
    <li><a href="best-casino-bonuses-ireland">Best casino bonuses</a></li>
    <li><a href="live-casino-ireland">Live casino guide</a></li>
    <li><a href="fast-payout-casino-ireland">Fast payout casinos</a></li>
    <li><a href="slots-highest-rtp-ireland">Highest RTP slots</a></li>
    <li><a href="new-casino-sites-ireland-2026">New casino sites 2026</a></li>
    <li><a href="casino-paypal-ireland">Casino PayPal Ireland</a></li>
    <li><a href="casino-wagering-requirement-explained">Wagering requirements explained</a></li>
    <li><a href="casino-withdrawal-times-ireland">Withdrawal times</a></li>
    <li><a href="gambling-self-exclusion-ireland">Self-exclusion Ireland</a></li>
  </ul>
</div>
"""

HUB_BOX_WHY = """<div style="background:#fef3f0;border:1px solid #c0392b;border-radius:8px;padding:16px 20px;margin:20px 0">
  <strong>🎰 Casino Guides for Irish Players</strong>
  <ul style="margin:8px 0 0;padding-left:18px;columns:2;column-gap:24px">
    <li><a href="best-casinos-ireland">Best casinos for Irish players</a></li>
    <li><a href="best-casino-bonuses-ireland">Best casino bonuses</a></li>
    <li><a href="live-casino-ireland">Live casino guide</a></li>
    <li><a href="fast-payout-casino-ireland">Fast payout casinos</a></li>
    <li><a href="slots-highest-rtp-ireland">Highest RTP slots</a></li>
    <li><a href="new-casino-sites-ireland-2026">New casino sites 2026</a></li>
    <li><a href="casino-paypal-ireland">PayPal casinos Ireland</a></li>
    <li><a href="gambling-self-exclusion-ireland">Self-exclusion register</a></li>
  </ul>
</div>
"""

BACKLINK = """<p style="background:#fef3f0;border-left:3px solid #c0392b;padding:10px 14px;margin:20px 0;border-radius:0 6px 6px 0;font-size:0.95em">
  ⚠️ <strong>Important:</strong> <a href="why-no-grai-casino-licence-ireland">GRAI has not issued any casino licences — find out what this means for Irish players →</a>
</p>
"""

def insert_before_first_h2(content, box):
    # Find first <h2 occurrence
    m = re.search(r'<h2[\s>]', content)
    if not m:
        return content, False
    pos = m.start()
    return content[:pos] + box + content[pos:], True

# STEP 1 — best-casinos-ireland.html
path1 = os.path.join(PAGES, "best-casinos-ireland.html")
with open(path1) as f:
    c = f.read()
if "Casino Guides" not in c:
    c, ok = insert_before_first_h2(c, HUB_BOX_BEST)
    if ok:
        with open(path1, "w") as f:
            f.write(c)
        print("STEP 1: inserted hub box into best-casinos-ireland.html")
    else:
        print("STEP 1: no <h2> found in best-casinos-ireland.html")
else:
    print("STEP 1: hub box already present in best-casinos-ireland.html")

# STEP 2 — why-no-grai-casino-licence-ireland.html
path2 = os.path.join(PAGES, "why-no-grai-casino-licence-ireland.html")
with open(path2) as f:
    c = f.read()
if "Casino Guides for Irish Players" not in c:
    c, ok = insert_before_first_h2(c, HUB_BOX_WHY)
    if ok:
        with open(path2, "w") as f:
            f.write(c)
        print("STEP 2: inserted hub box into why-no-grai-casino-licence-ireland.html")
    else:
        print("STEP 2: no <h2> found")
else:
    print("STEP 2: hub box already present")

# STEP 3 — backlink on spoke pages
SPOKES = [
    "best-casino-apple-pay-ireland.html","best-casino-baccarat-ireland.html",
    "best-casino-blackjack-ireland.html","best-casino-bonuses-ireland.html",
    "best-casino-crash-games-ireland.html","best-casino-crypto-ireland.html",
    "best-casino-fast-payout-ireland.html","best-casino-free-spins-ireland.html",
    "best-casino-google-pay-ireland.html","best-casino-high-rtp-ireland.html",
    "best-casino-jackpots-ireland.html","best-casino-live-blackjack-ireland.html",
    "best-casino-live-dealer-ireland.html","best-casino-live-roulette-ireland.html",
    "best-casino-low-wagering-ireland.html","best-casino-megaways-ireland.html",
    "best-casino-mobile-ireland.html","best-casino-new-ireland-2026.html",
    "best-casino-no-deposit-ireland.html","best-casino-poker-ireland.html",
    "best-casino-revolut-ireland.html","best-casino-roulette-ireland.html",
    "best-casino-slots-ireland.html","best-casino-vip-programme-ireland.html",
    "best-casino-welcome-bonus-ireland.html","best-casino-without-account-ireland.html",
    "casino-account-verification-ireland.html","casino-bonus-abuse-ireland.html",
    "casino-bonuses-ireland.html","casino-deposit-limit-ireland.html",
    "casino-glossary.html","casino-grai-ireland.html","casino-holdem-ireland.html",
    "casino-legal-ireland-2026.html","casino-loyalty-program-ireland.html",
    "casino-loyalty-programmes-ireland.html","casino-odds-vs-sports-betting-odds.html",
    "casino-payment-methods.html","casino-payout-percentage-ireland.html",
    "casino-paypal-ireland.html","casino-rtp-guide-ireland.html",
    "casino-self-exclusion-ireland.html","casino-tournaments-ireland.html",
    "casino-wagering-requirement-explained.html","casino-welcome-bonus-ireland.html",
    "casino-withdrawal-times-ireland.html","casino-without-grai-licence-ireland.html",
    "fast-payout-casino-ireland.html","fast-payout-casinos.html",
    "live-casino-ireland.html","live-casino-vs-rng-games.html",
    "new-casino-sites-ireland-2026.html","new-casinos-ireland.html",
    "slots-highest-rtp-ireland.html","slots-vs-table-games.html",
    "slots-with-bonus-buys-ireland.html",
]

updated = 0
skipped_present = 0
skipped_missing = 0

for fname in SPOKES:
    fpath = os.path.join(PAGES, fname)
    if not os.path.exists(fpath):
        print(f"  MISSING: {fname}")
        skipped_missing += 1
        continue
    with open(fpath) as f:
        c = f.read()
    if "why-no-grai-casino-licence-ireland" in c:
        skipped_present += 1
        continue
    # Find last </p> before </footer>
    footer_pos = c.find("</footer>")
    if footer_pos == -1:
        print(f"  NO FOOTER: {fname}")
        continue
    # Find last </p> before footer
    segment = c[:footer_pos]
    last_p_end = segment.rfind("</p>")
    if last_p_end == -1:
        print(f"  NO </p>: {fname}")
        continue
    insert_at = last_p_end + 4  # after </p>
    c = c[:insert_at] + "\n" + BACKLINK + c[insert_at:]
    with open(fpath, "w") as f:
        f.write(c)
    updated += 1

print(f"\nSTEP 3: {updated} files updated, {skipped_present} already had backlink, {skipped_missing} files missing")
