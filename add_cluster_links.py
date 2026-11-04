#!/usr/bin/env python3
"""Add cluster hub blocks to all new pages that are missing them."""

import os, re

PAGES = "pages"

CLUSTERS = {
    "horse_racing": {
        "color": "#3b82f6",
        "bg": "#f0f7ff",
        "title": "🏇 Horse Racing Betting Guide",
        "pages": [
            ("Horse Racing Betting Ireland", "horse-racing-betting-ireland"),
            ("Each-Way Betting Explained", "horse-racing-each-way-betting"),
            ("Handicap Betting Guide", "horse-racing-handicap-betting"),
            ("Cheltenham Betting Guide", "cheltenham-betting-guide"),
            ("Irish National Hunt Betting", "irish-national-hunt-betting"),
            ("Horse Racing Tips Guide", "horse-racing-tips-guide"),
            ("Flat Racing vs Jumps", "flat-racing-vs-jumps-ireland"),
            ("Cheltenham 2027 Betting", "cheltenham-2027-betting"),
            ("Grand National 2027", "grand-national-2027-betting"),
            ("Leopardstown Racing", "leopardstown-racing-betting"),
            ("The Curragh Racecourse", "curragh-racecourse-betting"),
            ("Punchestown Betting", "punchestown-betting-guide"),
        ],
        "targets": [
            "horse-racing-each-way-betting",
            "horse-racing-handicap-betting",
            "cheltenham-betting-guide",
            "irish-national-hunt-betting",
            "horse-racing-tips-guide",
            "flat-racing-vs-jumps-ireland",
            "cheltenham-2027-betting",
            "leopardstown-racing-betting",
            "curragh-racecourse-betting",
            "punchestown-betting-guide",
            "fairyhouse-racing-betting",
            "grand-national-2027-betting",
            "best-odds-horse-racing-ireland",
            "betting-on-irish-horses-uk-racing",
        ],
    },
    "gaa": {
        "color": "#16a34a",
        "bg": "#f0fdf4",
        "title": "🏐 GAA Betting Hub",
        "pages": [
            ("GAA Betting Guide", "gaa-betting-guide"),
            ("GAA Betting Markets", "gaa-betting-markets"),
            ("GAA Championship Betting", "gaa-championship-betting"),
            ("GAA Handicap Betting", "gaa-handicap-betting"),
            ("Munster Championship Betting", "munster-championship-betting"),
            ("Leinster Championship Betting", "leinster-championship-betting"),
            ("GAA Live Betting", "gaa-live-betting"),
            ("GAA Betting Tips Today", "gaa-betting-tips-today"),
        ],
        "targets": [
            "gaa-betting-markets",
            "gaa-championship-betting",
            "gaa-handicap-betting",
            "munster-championship-betting",
            "leinster-championship-betting",
            "gaa-live-betting",
            "gaa-betting-tips-today",
        ],
    },
    "free_bets": {
        "color": "#a855f7",
        "bg": "#fdf4ff",
        "title": "🎁 Free Bets & Bonuses",
        "pages": [
            ("How Free Bets Work Ireland", "how-free-bets-work-ireland"),
            ("Free Bet Wagering Explained", "free-bet-wagering-explained"),
            ("Best Odds Promotions", "best-odds-betting-promotions"),
            ("Reload Bonus Betting", "reload-bonus-betting-ireland"),
            ("Casino Welcome Bonus Ireland", "casino-welcome-bonus-ireland"),
            ("Bonus Abuse Ireland", "bonus-abuse-ireland"),
            ("Free Bet Calculator", "free-bet-calculator"),
        ],
        "targets": [
            "how-free-bets-work-ireland",
            "free-bet-wagering-explained",
            "best-odds-betting-promotions",
            "reload-bonus-betting-ireland",
            "casino-welcome-bonus-ireland",
            "bonus-abuse-ireland",
        ],
    },
    "payments": {
        "color": "#2563eb",
        "bg": "#eff6ff",
        "title": "💳 Payments & Withdrawals",
        "pages": [
            ("Revolut Blocked? What to Do", "revolut-blocked-gambling-ireland"),
            ("Fastest Withdrawal Betting", "fastest-withdrawal-betting-ireland"),
            ("Debit Card Betting Ireland", "debit-card-betting-ireland"),
            ("E-Wallet Betting Ireland", "e-wallet-betting-ireland"),
            ("Deposit Limits Ireland", "deposit-limit-betting-ireland"),
            ("PayPal Betting Ireland", "paypal-betting-ireland"),
            ("Revolut Betting Ireland", "revolut-betting-ireland"),
            ("Skrill & Neteller Betting", "skrill-neteller-betting-ireland"),
            ("Apple Pay & Google Pay", "apple-pay-google-pay-betting-ireland"),
        ],
        "targets": [
            "revolut-blocked-gambling-ireland",
            "fastest-withdrawal-betting-ireland",
            "debit-card-betting-ireland",
            "e-wallet-betting-ireland",
            "deposit-limit-betting-ireland",
        ],
    },
    "calculators": {
        "color": "#ca8a04",
        "bg": "#fefce8",
        "title": "🧮 Betting Calculators & Tools",
        "pages": [
            ("All Betting Calculators", "betting-calculators-ireland"),
            ("How to Use Betting Calculators", "how-to-use-betting-calculators"),
            ("Each-Way Terms Explained", "each-way-terms-explained"),
            ("Accumulator Odds Explained", "accumulator-odds-explained"),
            ("Kelly Criterion Betting", "kelly-criterion-betting"),
            ("Acca Calculator", "acca-calculator"),
            ("Each-Way Calculator", "each-way-calculator"),
            ("Odds Converter", "odds-converter"),
            ("Free Bet Calculator", "free-bet-calculator"),
            ("Arbitrage Calculator", "arbitrage-calculator"),
            ("Dutching Calculator", "dutching-calculator"),
            ("Odds Formats Explained", "odds-formats-explained"),
        ],
        "targets": [
            "how-to-use-betting-calculators",
            "each-way-terms-explained",
            "accumulator-odds-explained",
            "kelly-criterion-betting",
        ],
    },
}


def build_block(cluster):
    links_html = "\n".join(
        f'          <li><a href="{slug}">{label}</a></li>'
        for label, slug in cluster["pages"]
    )
    return f"""
  <!-- cluster hub block -->
  <aside style="background:{cluster['bg']};border-left:4px solid {cluster['color']};border-radius:0 8px 8px 0;padding:16px 20px;margin:32px 0;font-size:0.95em">
    <strong style="color:{cluster['color']}">{cluster['title']}</strong>
    <ul style="margin:8px 0 0;padding-left:20px;columns:2;column-gap:24px">
{links_html}
    </ul>
  </aside>
  <!-- end cluster hub block -->
"""


def inject(filepath, block):
    with open(filepath, encoding="utf-8") as f:
        html = f.read()

    # Skip if already has cluster block
    if "cluster hub block" in html:
        return False, "already has block"

    # Insert before </article> or before <footer or before </main>
    for marker in ["</article>", '<footer', "</main>"]:
        if marker in html:
            html = html.replace(marker, block + marker, 1)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(html)
            return True, f"inserted before {marker}"

    return False, "no insertion point found"


updated = []
skipped = []

for cluster_key, cluster in CLUSTERS.items():
    block = build_block(cluster)
    for slug in cluster["targets"]:
        fp = os.path.join(PAGES, f"{slug}.html")
        if not os.path.exists(fp):
            skipped.append((slug, "file not found"))
            continue
        ok, reason = inject(fp, block)
        if ok:
            updated.append((slug, cluster_key, reason))
        else:
            skipped.append((slug, reason))

print(f"\n✅ Updated {len(updated)} pages:")
for slug, cluster, reason in updated:
    print(f"  [{cluster}] {slug} — {reason}")

print(f"\n⏭  Skipped {len(skipped)}:")
for slug, reason in skipped:
    print(f"  {slug} — {reason}")
