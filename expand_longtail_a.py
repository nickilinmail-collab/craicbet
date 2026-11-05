#!/usr/bin/env python3
"""Long-tail cluster A: Revolut, GRAI/Legal, DNB/terms, Cheltenham, Slot RTP."""
import os

BASE = "/home/claude/craicbet/pages"
TABLE_STYLE = "width:100%;border-collapse:collapse;margin:16px 0;font-size:0.95rem"
TH = "padding:9px;border:1px solid #2d5a3d;text-align:left;color:#cde6d4"
TD = "padding:8px;border:1px solid #2d5a3d"
TR_H = "background:#1e3a28"
TR_A = "background:#0d1f14"

def th(t): return f'<th style="{TH}">{t}</th>'
def td(t): return f'<td style="{TD}">{t}</td>'
def tr_h(*c): return f'<tr style="{TR_H}">{"".join(th(x) for x in c)}</tr>'
def tr_n(*c): return f'<tr>{"".join(td(x) for x in c)}</tr>'
def tr_a(*c): return f'<tr style="{TR_A}">{"".join(td(x) for x in c)}</tr>'
def tbl(*rows): return f'<table style="{TABLE_STYLE}">{"".join(rows)}</table>'

def patch(filename, content):
    path = os.path.join(BASE, filename)
    if not os.path.exists(path):
        print(f"SKIP: {filename}")
        return
    with open(path, encoding="utf-8") as f:
        html = f.read()
    for marker in ['<div class="editorial-box"', '<div class="faq-item"', '</main>', '</article>', '</body>']:
        idx = html.find(marker)
        if idx != -1:
            html = html[:idx] + content + html[idx:]
            break
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"OK: {filename}")

# ── Revolut cluster ────────────────────────────────────────────────────────────
revolut_content = """
<h2>Revolut Gambling Block: How to Turn Off in Ireland</h2>
<p>Revolut's gambling block is a voluntary spending control you switch on and off inside the app. To disable it: open Revolut → Payments tab → Card controls → Gambling → toggle off. The toggle takes effect immediately. If you enabled it under "cool-off" mode, there may be a waiting period (typically 48 hours) before it can be deactivated — this is a deliberate friction to prevent impulsive removal during a gambling urge.</p>""" + tbl(
    tr_h("Step", "Action"),
    tr_n("1", "Open Revolut app → tap your card"),
    tr_a("2", "Tap 'Card controls' or 'Spending controls'"),
    tr_n("3", "Find 'Gambling' or 'Gambling transactions'"),
    tr_a("4", "Toggle OFF — takes effect immediately (unless in cool-off)"),
) + """

<h2>Revolut Declined at Betting Site Ireland: How to Fix</h2>
<p>If Revolut is declined at an Irish betting site, check these in order: (1) Gambling block is on — disable it in Card controls. (2) Revolut's own gambling transaction limit is reached — Revolut sets monthly limits on gambling category spending. (3) The betting site's MCC code is flagged — some operators use merchant category codes that Revolut blocks by default. (4) Revolut Premium/Metal spending limit reached. If none of these apply, contact Revolut in-app support and confirm the transaction type is permitted on your plan.</p>

<h2>Can You Use Revolut for Online Casino Ireland 2026</h2>
<p>Yes — Revolut works at GRAI-licensed online casinos in Ireland, provided the gambling block is off and no spending limits are active. Revolut is treated as a Mastercard Debit transaction by most operators. Deposits clear instantly. Withdrawals back to Revolut typically take 2–24 hours. Note: some casino operators have experienced Revolut withdrawal delays of 1–3 days due to Revolut's own processing queue — this is a Revolut-side issue, not the casino.</p>

<h2>Best Card for Online Betting Ireland with No Block</h2>
<p>Standard Visa Debit and Mastercard Debit from AIB, Bank of Ireland, and Permanent TSB generally have no default gambling block — you must opt in to block gambling. Revolut has an optional block. N26 and Monzo (available in Ireland) also allow gambling transactions by default with optional blocks. The key difference: credit cards from Irish banks almost universally block gambling, while debit cards do not.</p>
"""
patch("revolut-casinos.html", revolut_content)
patch("betting-with-revolut-ireland-2026.html", """
<h2>Revolut Gambling Block How to Turn Off Ireland</h2>
<p>To re-enable betting deposits via Revolut, open the app, go to your card, tap Spending controls, and toggle the Gambling category back on. If you set a cool-off period when activating the block, Revolut requires you to wait the full period before removal — this is intentional friction. Standard toggle-off (no cool-off) takes effect immediately.</p>

<h2>Can I Use Revolut for Online Betting Ireland 2026</h2>
<p>Yes. Revolut functions as a standard Mastercard Debit at GRAI-licensed betting sites. Deposits are instant. Withdrawals take 2–24 hours typically. Monthly gambling category limits within Revolut itself may apply — check Settings → Spending limits → Gambling if deposits start declining unexpectedly.</p>
""")

# ── Bank of Ireland block ──────────────────────────────────────────────────────
patch("bank-of-ireland-gambling-block.html", """
<h2>Bank of Ireland Gambling Block: How to Disable</h2>
<p>Bank of Ireland's gambling block (called "Gambling Freeze") is managed via the BOI Mobile Banking app. To disable: open the app → Card Controls → Gambling → toggle off. Changes apply within seconds. If you do not see this option, update the app — the feature was introduced in 2022 and may not appear on older app versions. Alternatively, call BOI at 0818 365 365 and request removal over the phone with identity verification.</p>
""" + tbl(
    tr_h("Bank", "Block name", "How to toggle", "Contact"),
    tr_n("Bank of Ireland", "Gambling Freeze", "BOI App → Card Controls", "0818 365 365"),
    tr_a("AIB", "Gambling block", "AIB app → Spending Controls", "0818 724 724"),
    tr_n("Permanent TSB", "Gambling restriction", "PTSB app → Card Management", "1800 500 000"),
    tr_a("Revolut", "Gambling toggle", "Revolut app → Card Controls", "In-app chat"),
    tr_n("N26", "Category block", "N26 app → Card Settings", "In-app chat"),
) + """
<p>All major Irish banks now offer voluntary gambling blocks. Enabling a block typically takes effect immediately; disabling may require a 24–48 hour waiting period depending on bank policy.</p>
""")

# ── GRAI legal checks ──────────────────────────────────────────────────────────
patch("grai-casino-licence-ireland-2027.html", """
<h2>Which Betting Sites Have a GRAI Licence in 2026</h2>
<p>GRAI began issuing remote betting licences on 1 July 2026 under the Gambling Regulation Act 2024. The public register of GRAI-licensed operators is available at grai.ie. As of late 2026, GRAI has issued a limited number of remote betting licences — many operators are still operating under transitional Revenue remote bookmaker permissions while their GRAI applications are processed. To check if a site is licensed: look for the GRAI licence number in the site footer (format: GRAI-XXXX-RB-YY-XXXX).</p>

<h2>GRAI Licence Number: How to Check Ireland</h2>
<p>Every GRAI remote betting licensee must display their licence number prominently on their website, typically in the footer. To verify: copy the licence number, go to grai.ie, and use the licence checker tool. Valid format example: GRAI-0191-RB-26-0001. If a site claims to be GRAI-licensed but no number is visible, or the number does not appear on the GRAI register, the site is unlicensed — do not deposit.</p>

<h2>Can I Bet on Unlicensed Sites from Ireland Legally</h2>
<p>It is not illegal for an Irish individual to place a bet on an unlicensed site. However, unlicensed sites offer zero consumer protection: no GRAI complaints process, no segregated funds requirement, no KYC guarantees, and no recourse if the site refuses to pay. The legal risk is the site's, not yours — but the financial risk is entirely yours. GRAI strongly advises using only GRAI-licensed operators.</p>
""")

# ── Odds/terms ─────────────────────────────────────────────────────────────────
patch("what-does-dnb-mean-betting.html", """
<h2>DNB vs Asian Handicap: What Is the Difference</h2>
<p>DNB (Draw No Bet) and Asian Handicap 0 are mathematically identical — both refund your stake if the match ends in a draw, and win/lose on the other results. The practical difference is presentation: DNB is listed as a separate market at most bookmakers, while AH 0 appears in the Asian handicap section. Odds may differ slightly between the two due to different margin structures applied to each market. Always compare both when placing a draw-no-bet style wager.</p>
""" + tbl(
    tr_h("Market", "Home win", "Draw", "Away win"),
    tr_n("DNB (back home)", "Win", "Stake refunded", "Lose"),
    tr_a("AH 0 (back home)", "Win", "Stake refunded", "Lose"),
    tr_n("1X2 (back home)", "Win", "Lose", "Lose"),
    tr_a("Double chance (1X)", "Win", "Win", "Lose"),
) + """

<h2>What Does DNB Mean in Betting Ireland</h2>
<p>DNB stands for "Draw No Bet." If you place a DNB bet on Team A and the match ends in a draw, your stake is refunded in full. If Team A wins, you win at the stated odds. If Team A loses, you lose your stake. DNB effectively removes the draw outcome from the equation, giving you a two-way bet on the result. It is popular for betting on slight favourites in closely-matched games where a draw is a realistic outcome.</p>

<h2>What Does Each Way Mean in Horse Racing Ireland</h2>
<p>Each-way (EW) is two bets in one: a win bet and a place bet. Half your stake goes on the horse to win, half on it to place (finish in the top 2, 3, 4, or 5 depending on the race). The place part pays a fraction of the win odds — typically 1/4 or 1/5 depending on the number of runners and the operator's terms. Example: €10 EW on a horse at 10/1 with 1/4 odds, 3 places — if it finishes 3rd: win part loses (€5), place part wins €5 × (10/4 + 1) = €5 × 3.5 = €17.50 total return.</p>
""")

# ── Hacksaw Gaming ─────────────────────────────────────────────────────────────
patch("hacksaw-gaming-casinos-ireland.html", """
<h2>Chaos Crew RTP Ireland</h2>
<p>Chaos Crew (Hacksaw Gaming) has an RTP of 96.00% and very high volatility with a maximum win of 10,000× stake. The hold-and-win mechanic during free spins accumulates multiplier wilds across the grid. As with most Hacksaw titles, the buy-bonus feature may be disabled on GRAI/Revenue-licensed Irish sites — confirm in the in-game menu before depositing.</p>

<h2>Stick 'Em RTP Ireland</h2>
<p>Stick 'Em (Hacksaw Gaming) has an RTP of 96.00% and high volatility with a max win of 5,000× stake. Sticky wilds accumulate across re-spins — the more wilds stick, the larger the multiplier. It is Hacksaw's most beginner-friendly title: lower volatility than Chaos Crew, with more regular small-to-medium wins during the sticky respins feature.</p>
""" + tbl(
    tr_h("Game", "RTP", "Volatility", "Max win", "Key mechanic"),
    tr_n("Chaos Crew", "96.00%", "Very high", "10,000×", "Hold & win multipliers"),
    tr_a("Stick 'Em", "96.00%", "High", "5,000×", "Sticky wild respins"),
    tr_n("Chaos Crew 2", "96.00%", "Very high", "10,000×", "Enhanced hold & win"),
    tr_a("Snake Arena", "96.07%", "High", "10,000×", "Snake path mechanic"),
))

print("\nAll cluster-A patches applied.")
