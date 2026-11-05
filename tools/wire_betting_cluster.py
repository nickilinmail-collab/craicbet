#!/usr/bin/env python3
"""Wire betting spoke pages back to the betting-sites-ireland superanchor."""

import os
import re

PAGES_DIR = "/home/claude/craicbet/pages"

HUB_BOX = """<div style="background:#eef6f0;border:1px solid #2d6a4f;border-radius:8px;padding:16px 20px;margin:20px 0">
  <strong>🎯 Betting Guides</strong>
  <ul style="margin:8px 0 0;padding-left:18px;columns:2;column-gap:24px">
    <li><a href="gaa-betting-ireland">GAA betting guide</a></li>
    <li><a href="horse-racing-ireland-tips-today">Horse racing tips today</a></li>
    <li><a href="cheltenham-2027-festival-guide-ireland">Cheltenham 2027 guide</a></li>
    <li><a href="six-nations-betting-ireland">Six Nations betting</a></li>
    <li><a href="premier-league-betting-ireland">Premier League betting</a></li>
    <li><a href="free-bets-ireland-no-deposit">Free bets no deposit</a></li>
    <li><a href="bet-builder-ireland">Bet builder guide</a></li>
    <li><a href="acca-betting-ireland">Acca betting explained</a></li>
    <li><a href="cash-out-betting-ireland">Cash out guide</a></li>
    <li><a href="grai-licensed-bookmakers-ireland-2026">GRAI licensed bookmakers</a></li>
  </ul>
</div>"""

BACKLINK = """<p style="background:#eef6f0;border-left:3px solid #2d6a4f;padding:10px 14px;margin:20px 0;border-radius:0 6px 6px 0;font-size:0.95em">
  🎯 <strong>See also:</strong> <a href="betting-sites-ireland">Best betting sites in Ireland — full guide →</a>
</p>"""

SPOKE_FILES = [
    "acca-betting-ireland.html","acca-calculator.html","acca-insurance-promos.html",
    "bet-builder-ireland.html","bet-builder-maths.html","bet-builder-vs-acca-ireland.html",
    "cash-out-betting-ireland.html","cash-out-calculator.html","cash-out-explained.html",
    "cash-out-feature-comparison-ireland.html","cheltenham-2027-albert-bartlett-betting.html",
    "cheltenham-2027-betting.html","cheltenham-2027-champion-day-betting.html",
    "cheltenham-2027-county-hurdle-betting.html","cheltenham-2027-festival-guide-ireland.html",
    "cheltenham-2027-gold-cup-day-betting.html","cheltenham-2027-grand-annual-betting.html",
    "cheltenham-2027-hunter-chase-betting.html","cheltenham-2027-mares-hurdle-betting.html",
    "cheltenham-2027-mares-novices-hurdle.html","cheltenham-2027-novices-hurdle-betting.html",
    "cheltenham-2027-ryanair-chase-betting.html","cheltenham-2027-stayers-hurdle-betting.html",
    "cheltenham-2027-triumph-hurdle-betting.html","cheltenham-betting-guide.html",
    "cheltenham-champion-hurdle-2027-betting.html","cheltenham-festival-2027-betting.html",
    "cheltenham-festival-betting-ireland.html","cheltenham-gold-cup-2027-betting.html",
    "cheltenham-queen-mother-champion-chase-2027.html","cheltenham-tips-guide.html",
    "cheltenham-week-betting-guide.html","free-bets-ireland-no-deposit.html",
    "free-bets-ireland.html","free-bets-vs-deposit-match-ireland.html",
    "gaa-2027-connacht-championship-betting.html","gaa-2027-football-favourites-betting.html",
    "gaa-2027-hurling-favourites-betting.html","gaa-2027-munster-hurling-championship.html",
    "gaa-betting-guide-ireland.html","gaa-betting-guide.html","gaa-betting-ireland.html",
    "gaa-betting-markets.html","gaa-betting-tips-today.html","gaa-championship-betting.html",
    "gaa-fixtures-results.html","gaa-handicap-betting.html","gaa-live-betting.html",
    "horse-racing-ante-post-guide.html","horse-racing-ante-post.html",
    "horse-racing-betting-ireland.html","horse-racing-betting-site-comparison-ireland.html",
    "horse-racing-each-way-betting.html","horse-racing-each-way-ireland.html",
    "horse-racing-form-guide.html","horse-racing-handicap-betting.html",
    "horse-racing-ireland-tips-today.html","horse-racing-nap-tips.html",
    "horse-racing-ownership-ireland.html","horse-racing-tips-guide.html",
    "premier-league-betting-ireland.html","premier-league-christmas-number-one.html",
    "premier-league-first-relegated-team.html","premier-league-golden-glove-betting.html",
    "premier-league-manager-sacking-betting.html","premier-league-relegation-2026-27.html",
    "premier-league-title-race-2026-27.html","premier-league-top-4-2026-27.html",
    "premier-league-top-scorer-2026-27-betting.html","premier-league-transfers-january-betting.html",
    "six-nations-2027-betting.html","six-nations-2027-england-ireland-betting.html",
    "six-nations-2027-grand-slam-betting.html","six-nations-2027-ireland-betting.html",
    "six-nations-2027-ireland-france-betting.html","six-nations-2027-preview-ireland.html",
    "six-nations-2027-top-scorer-betting.html","six-nations-2027-winner-betting.html",
    "six-nations-2027-wooden-spoon-betting.html","six-nations-betting-ireland.html",
    "six-nations-rugby-betting-guide.html","six-nations-week-1-betting-ireland.html",
    "spread-betting-ireland.html","spread-betting-vs-binary-betting-ireland.html",
    "spread-betting-vs-fixed-odds.html",
]

# --- STEP 1: Insert hub box before first <h2> in betting-sites-ireland.html ---
hub_path = os.path.join(PAGES_DIR, "betting-sites-ireland.html")
with open(hub_path, "r", encoding="utf-8") as f:
    hub_content = f.read()

if "Betting Guides Hub" in hub_content or "Betting Guides</strong>" in hub_content:
    print("Hub box already present in betting-sites-ireland.html — skipping.")
else:
    # Find first <h2 (case-insensitive)
    m = re.search(r'<h2[^>]*>', hub_content, re.IGNORECASE)
    if m:
        insert_pos = m.start()
        hub_content = hub_content[:insert_pos] + HUB_BOX + "\n\n    " + hub_content[insert_pos:]
        with open(hub_path, "w", encoding="utf-8") as f:
            f.write(hub_content)
        print("Hub box inserted into betting-sites-ireland.html")
    else:
        print("ERROR: No <h2> found in betting-sites-ireland.html")

# --- STEP 2: Add backlink to each spoke file ---
updated = 0
skipped_already = 0
skipped_missing = 0

for fname in SPOKE_FILES:
    fpath = os.path.join(PAGES_DIR, fname)
    if not os.path.exists(fpath):
        print(f"  MISSING: {fname}")
        skipped_missing += 1
        continue

    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    if "betting-sites-ireland" in content:
        skipped_already += 1
        continue

    # Find the last </p> before </footer> or </main> or </section>
    # Strategy: find the closing tag of the main content area, then find the last </p> before it
    end_markers = ["</footer>", "</main>", "</section>"]
    insert_pos = None

    for marker in end_markers:
        idx = content.rfind(marker)
        if idx != -1:
            # Find the last </p> before this marker
            last_p = content.rfind("</p>", 0, idx)
            if last_p != -1:
                insert_pos = last_p + len("</p>")
                break

    if insert_pos is None:
        # Fallback: insert before </body>
        idx = content.rfind("</body>")
        if idx != -1:
            insert_pos = idx
        else:
            print(f"  NO INSERT POINT: {fname}")
            continue

    new_content = content[:insert_pos] + "\n\n" + BACKLINK + "\n" + content[insert_pos:]
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(new_content)
    updated += 1

print(f"\nDone.")
print(f"  Spokes updated:        {updated}")
print(f"  Already had backlink:  {skipped_already}")
print(f"  Files not found:       {skipped_missing}")
print(f"  Total spokes in list:  {len(SPOKE_FILES)}")
