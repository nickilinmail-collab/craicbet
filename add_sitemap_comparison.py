#!/usr/bin/env python3
"""Append 50 comparison page URLs to sitemap.xml"""

SLUGS = [
    "irish-bookmaker-vs-grai-licensed-alternative",
    "racing-specialist-bookmaker-alternative-ireland",
    "market-leader-sportsbook-alternative-ireland",
    "betting-exchange-alternative-ireland-comparison",
    "in-play-betting-site-comparison-ireland",
    "horse-racing-betting-site-comparison-ireland",
    "football-betting-site-comparison-ireland",
    "mobile-betting-app-comparison-ireland",
    "best-odds-guaranteed-site-comparison-ireland",
    "fastest-payout-bookmaker-comparison",
    "lowest-margin-bookmaker-ireland-comparison",
    "best-acca-boost-betting-site-ireland",
    "cash-out-feature-comparison-ireland",
    "live-streaming-betting-ireland-comparison",
    "most-markets-betting-site-ireland",
    "customer-service-betting-site-comparison",
    "deposit-options-comparison-ireland",
    "new-customer-offer-comparison-ireland",
    "price-boost-comparison-ireland",
    "betting-site-reload-comparison-ireland",
    "marathonbet-vs-betsson-ireland",
    "dafabet-vs-18bet-ireland",
    "coolbet-vs-campobet-ireland",
    "interwetten-vs-betmaster-ireland",
    "leon-bet-vs-marathonbet-ireland",
    "sportbet-vs-18bet-comparison",
    "expekt-vs-betsson-ireland",
    "bet-at-home-vs-marathonbet-ireland",
    "dafabet-vs-marathonbet-ireland",
    "coolbet-vs-marathonbet-ireland",
    "fonbet-vs-betboom-ireland",
    "betmaster-vs-sportsbet-io-ireland",
    "jackbit-vs-metaspins-ireland",
    "bc-game-vs-mystake-ireland",
    "fezbet-vs-spinbet-ireland",
    "matched-betting-vs-value-betting-ireland",
    "fixed-odds-vs-exchange-betting-ireland",
    "single-bet-vs-accumulator-ireland",
    "in-play-vs-pre-match-betting-ireland",
    "ante-post-vs-day-of-race-betting",
    "free-bets-vs-deposit-match-ireland",
    "debit-card-vs-revolut-betting",
    "ecopayz-vs-neteller-betting-ireland",
    "responsible-gambling-tools-comparison-ireland",
    "grai-vs-mga-licence-for-players",
    "betting-app-vs-mobile-site-ireland",
    "exchange-lay-betting-vs-bookmaker",
    "bet-builder-vs-acca-ireland",
    "tote-vs-fixed-odds-horse-racing-ireland",
    "spread-betting-vs-binary-betting-ireland",
]

entries = ""
for slug in SLUGS:
    entries += f"""  <url>
    <loc>https://craicbet.com/pages/{slug}</loc>
    <lastmod>2026-11-05</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>\n"""

sitemap_path = "/home/claude/craicbet/sitemap.xml"
with open(sitemap_path, "r", encoding="utf-8") as f:
    content = f.read()

# Insert before closing </urlset>
new_content = content.replace("</urlset>", entries + "</urlset>")
with open(sitemap_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print(f"Added {len(SLUGS)} URLs to sitemap.xml")
