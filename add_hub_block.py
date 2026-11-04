#!/usr/bin/env python3
"""Insert the calculator hub block before </article> in all 26 calc pages."""
import os
import re

PAGES_DIR = "/home/claude/craicbet/pages"

CALC_PAGES = [
    "betting-calculators-ireland.html",
    "acca-calculator.html",
    "each-way-calculator.html",
    "lucky-15-calculator.html",
    "lucky-31-calculator.html",
    "lucky-63-calculator.html",
    "yankee-calculator.html",
    "trixie-calculator.html",
    "patent-calculator.html",
    "heinz-calculator.html",
    "super-heinz-calculator.html",
    "goliath-calculator.html",
    "canadian-calculator.html",
    "round-robin-calculator.html",
    "arbitrage-calculator.html",
    "dutching-calculator.html",
    "kelly-criterion-calculator.html",
    "free-bet-calculator.html",
    "cash-out-calculator.html",
    "rule-4-calculator.html",
    "wagering-calculator.html",
    "bookmaker-margin-calculator.html",
    "how-to-use-betting-calculators.html",
    "each-way-terms-explained.html",
    "accumulator-odds-explained.html",
    "kelly-criterion-betting.html",
]

HUB_BLOCK = '''<div style="margin:28px 0;padding:16px 20px;background:#fefce8;border-radius:8px;border-left:4px solid #ca8a04">
<strong style="display:block;margin-bottom:10px;color:#713f12">🧮 Betting Calculators Hub — All 22 Free Tools:</strong>
<div style="display:flex;flex-wrap:wrap;gap:8px">
<a href="betting-calculators-ireland" style="background:#fff;border:1px solid #fde68a;border-radius:4px;padding:5px 10px;font-size:13px;text-decoration:none;color:#92400e">All Calculators</a>
<a href="acca-calculator" style="background:#fff;border:1px solid #fde68a;border-radius:4px;padding:5px 10px;font-size:13px;text-decoration:none;color:#92400e">Acca Calculator</a>
<a href="each-way-calculator" style="background:#fff;border:1px solid #fde68a;border-radius:4px;padding:5px 10px;font-size:13px;text-decoration:none;color:#92400e">Each-Way Calculator</a>
<a href="lucky-15-calculator" style="background:#fff;border:1px solid #fde68a;border-radius:4px;padding:5px 10px;font-size:13px;text-decoration:none;color:#92400e">Lucky 15</a>
<a href="lucky-31-calculator" style="background:#fff;border:1px solid #fde68a;border-radius:4px;padding:5px 10px;font-size:13px;text-decoration:none;color:#92400e">Lucky 31</a>
<a href="lucky-63-calculator" style="background:#fff;border:1px solid #fde68a;border-radius:4px;padding:5px 10px;font-size:13px;text-decoration:none;color:#92400e">Lucky 63</a>
<a href="yankee-calculator" style="background:#fff;border:1px solid #fde68a;border-radius:4px;padding:5px 10px;font-size:13px;text-decoration:none;color:#92400e">Yankee</a>
<a href="trixie-calculator" style="background:#fff;border:1px solid #fde68a;border-radius:4px;padding:5px 10px;font-size:13px;text-decoration:none;color:#92400e">Trixie</a>
<a href="patent-calculator" style="background:#fff;border:1px solid #fde68a;border-radius:4px;padding:5px 10px;font-size:13px;text-decoration:none;color:#92400e">Patent</a>
<a href="heinz-calculator" style="background:#fff;border:1px solid #fde68a;border-radius:4px;padding:5px 10px;font-size:13px;text-decoration:none;color:#92400e">Heinz</a>
<a href="super-heinz-calculator" style="background:#fff;border:1px solid #fde68a;border-radius:4px;padding:5px 10px;font-size:13px;text-decoration:none;color:#92400e">Super Heinz</a>
<a href="goliath-calculator" style="background:#fff;border:1px solid #fde68a;border-radius:4px;padding:5px 10px;font-size:13px;text-decoration:none;color:#92400e">Goliath</a>
<a href="canadian-calculator" style="background:#fff;border:1px solid #fde68a;border-radius:4px;padding:5px 10px;font-size:13px;text-decoration:none;color:#92400e">Canadian</a>
<a href="round-robin-calculator" style="background:#fff;border:1px solid #fde68a;border-radius:4px;padding:5px 10px;font-size:13px;text-decoration:none;color:#92400e">Round Robin</a>
<a href="arbitrage-calculator" style="background:#fff;border:1px solid #fde68a;border-radius:4px;padding:5px 10px;font-size:13px;text-decoration:none;color:#92400e">Arbitrage</a>
<a href="dutching-calculator" style="background:#fff;border:1px solid #fde68a;border-radius:4px;padding:5px 10px;font-size:13px;text-decoration:none;color:#92400e">Dutching</a>
<a href="kelly-criterion-calculator" style="background:#fff;border:1px solid #fde68a;border-radius:4px;padding:5px 10px;font-size:13px;text-decoration:none;color:#92400e">Kelly Criterion</a>
<a href="free-bet-calculator" style="background:#fff;border:1px solid #fde68a;border-radius:4px;padding:5px 10px;font-size:13px;text-decoration:none;color:#92400e">Free Bet</a>
<a href="cash-out-calculator" style="background:#fff;border:1px solid #fde68a;border-radius:4px;padding:5px 10px;font-size:13px;text-decoration:none;color:#92400e">Cash Out</a>
<a href="rule-4-calculator" style="background:#fff;border:1px solid #fde68a;border-radius:4px;padding:5px 10px;font-size:13px;text-decoration:none;color:#92400e">Rule 4</a>
<a href="wagering-calculator" style="background:#fff;border:1px solid #fde68a;border-radius:4px;padding:5px 10px;font-size:13px;text-decoration:none;color:#92400e">Wagering</a>
<a href="bookmaker-margin-calculator" style="background:#fff;border:1px solid #fde68a;border-radius:4px;padding:5px 10px;font-size:13px;text-decoration:none;color:#92400e">Margin</a>
<a href="how-to-use-betting-calculators" style="background:#fff;border:1px solid #fde68a;border-radius:4px;padding:5px 10px;font-size:13px;text-decoration:none;color:#92400e">How to Use Calculators</a>
<a href="accumulator-odds-explained" style="background:#fff;border:1px solid #fde68a;border-radius:4px;padding:5px 10px;font-size:13px;text-decoration:none;color:#92400e">Acca Odds Explained</a>
<a href="each-way-terms-explained" style="background:#fff;border:1px solid #fde68a;border-radius:4px;padding:5px 10px;font-size:13px;text-decoration:none;color:#92400e">Each-Way Terms</a>
<a href="kelly-criterion-betting" style="background:#fff;border:1px solid #fde68a;border-radius:4px;padding:5px 10px;font-size:13px;text-decoration:none;color:#92400e">Kelly Criterion Guide</a>
</div>
</div>
'''

updated = []
skipped = []
missing = []

for fname in CALC_PAGES:
    path = os.path.join(PAGES_DIR, fname)
    if not os.path.exists(path):
        missing.append(fname)
        continue
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    if "Betting Calculators Hub" in content:
        skipped.append(fname)
        continue
    # Insert hub block before </article>
    new_content = content.replace("</article>", HUB_BLOCK + "\n</article>", 1)
    if new_content == content:
        print(f"WARNING: </article> not found in {fname}")
        continue
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)
    updated.append(fname)

print(f"\nUpdated ({len(updated)}): {', '.join(updated)}")
print(f"Skipped already-have-hub ({len(skipped)}): {', '.join(skipped)}")
if missing:
    print(f"MISSING FILES ({len(missing)}): {', '.join(missing)}")
