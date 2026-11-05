#!/usr/bin/env python3
"""Add exact long-tail query H2 sections to target pages."""
import re, os

BASE = "/home/claude/craicbet/pages"

TABLE_STYLE = "width:100%;border-collapse:collapse;margin:16px 0;font-size:0.95rem"
TH = "padding:9px;border:1px solid #2d5a3d;text-align:left;color:#cde6d4"
TD = "padding:8px;border:1px solid #2d5a3d"
TR_HEAD = "background:#1e3a28"
TR_ALT  = "background:#0d1f14"

def th(t): return f'<th style="{TH}">{t}</th>'
def td(t): return f'<td style="{TD}">{t}</td>'
def tr_h(*cells): return f'<tr style="{TR_HEAD}">{"".join(th(c) for c in cells)}</tr>'
def tr_n(*cells): return f'<tr>{"".join(td(c) for c in cells)}</tr>'
def tr_a(*cells): return f'<tr style="{TR_ALT}">{"".join(td(c) for c in cells)}</tr>'
def tbl(*rows):   return f'<table style="{TABLE_STYLE}">{"".join(rows)}</table>'

def insert_before(html, marker, content):
    idx = html.find(marker)
    if idx == -1:
        return html, False
    return html[:idx] + content + html[idx:], True

def patch(filename, new_html):
    path = os.path.join(BASE, filename)
    if not os.path.exists(path):
        print(f"SKIP (not found): {filename}")
        return False
    with open(path, encoding="utf-8") as f:
        html = f.read()
    result, ok = insert_before(html, '<div class="editorial-box"', new_html)
    if not ok:
        result, ok = insert_before(html, '<div class="faq-item"', new_html)
    if not ok:
        # append before </main> or </article>
        for end_tag in ['</main>', '</article>', '</body>']:
            result, ok = insert_before(html, end_tag, new_html)
            if ok:
                break
    if not ok:
        print(f"SKIP (no insertion point): {filename}")
        return False
    with open(path, "w", encoding="utf-8") as f:
        f.write(result)
    print(f"OK: {filename}")
    return True

# ─── CLUSTER 9: Best betting site for X ───────────────────────────────────────
c9_best_app = """
<h2>Best Betting App for iPhone Ireland 2026</h2>
<p>iPhone users in Ireland need a betting app that works without side-loading: a native App Store download that holds a GRAI remote betting licence. As of November 2026, the best iOS betting apps in Ireland offer Touch/Face ID login, Apple Pay deposits, and push notifications for live odds. Download from the App Store, search the operator name, and check the footer for the licence number before depositing.</p>
<p>Key features to look for in an iPhone betting app: live streaming availability, cash-out speed, and whether the app supports bet builders on GAA and Premier League markets.</p>

<h2>Best Betting App for Android Ireland 2026</h2>
<p>Most Android betting apps in Ireland are not on the Google Play Store — operators distribute APK files directly from their websites due to Google's historical advertising policies. Download only from the official operator website, enable "Install from unknown sources" temporarily, and check that the app connects to the same GRAI-licensed account as the desktop site.</p>""" + tbl(
    tr_h("Feature", "iOS App Store", "Android APK"),
    tr_n("Availability", "Direct from App Store", "Operator website only"),
    tr_a("Install method", "Standard download", "Enable unknown sources"),
    tr_n("Face/fingerprint ID", "Yes (most operators)", "Yes (most operators)"),
    tr_a("Apple/Google Pay", "Apple Pay", "Google Pay"),
    tr_n("Auto-update", "Yes", "Manual re-download"),
) + """

<h2>Best Betting Site for Accumulators Ireland 2026</h2>
<p>Accumulator-focused Irish bettors should prioritise sites offering acca insurance (stake back if one leg fails), acca boost (enhanced odds on 4+ folds), and a wide range of markets to build from. GAA, Premier League, Champions League, and horse racing are the most popular acca legs for Irish punters.</p>
<p>Check the terms: acca insurance typically refunds as a free bet (SNR), not cash. A 5-fold with one failed leg returns the stake as a free bet, not the full refund. Minimum odds per selection (usually 1.3–1.5 decimal) also apply.</p>

<h2>Best Betting Site for Horse Racing Ireland 2026</h2>
<p>Irish horse racing bettors need Best Odds Guaranteed (BOG), non-runner no-bet (NRNB), and early prices on Irish and UK racing. BOG means if the SP is bigger than your early price, you get the SP — a significant edge on ante-post bets. Check BOG availability: some operators apply it to UK racing only, excluding Irish tracks like Leopardstown and the Curragh.</p>

<h2>Best Betting Site for GAA Ireland 2026</h2>
<p>GAA betting requires markets on county championship, provincial finals, and All-Ireland series. The best Irish betting sites for GAA offer correct score, first scorer, winning margin, and live in-play markets even on club championship games. Not all GRAI-licensed sites cover club GAA — check before the season starts.</p>

<h2>Best Betting Site for In-Play Betting Ireland 2026</h2>
<p>Live betting quality depends on three things: how fast odds update (latency), what markets stay open in-play, and whether live streaming is included. For football, cash-out availability mid-match is essential. For horse racing, in-play betting is restricted by law in Ireland — it closes at the off and settles at SP.</p>

<h2>Best Betting Site for Free Bets Ireland 2026</h2>
<p>Welcome free bets in Ireland range from €10 to €50. Under GRAI advertising rules (from July 2026), inducements cannot be promoted in watershed advertising, but they remain available on-site. Always check: is the free bet SNR (stake not returned) or SR (stake returned)? A €20 SNR free bet at evens returns €20 profit; a €20 SR free bet at evens returns €40 total.</p>
"""

patch("best-betting-app-ireland-2026.html", c9_best_app)

# ─── CLUSTER 10: Can I questions ───────────────────────────────────────────────
c10_18 = """
<h2>Can I Bet Online in Ireland Under 18</h2>
<p>No. Online betting is strictly 18+ in Ireland. The Gambling Regulation Act 2024 and GRAI licensing conditions require all operators to verify that customers are at least 18 before allowing any deposit or bet. Operators must complete age verification — usually by checking a passport, driving licence, or public records database — before the account is approved. Attempting to bet underage using a parent's or sibling's account is a breach of operator terms and can result in permanent account closure and forfeit of all funds.</p>
<p>If you are under 18 and experiencing gambling urges, Gambling Awareness Trust Ireland offers confidential support: freephone 1800 753 753.</p>
"""
patch("betting-at-18-ireland.html", c10_18)

c10_crypto = """
<h2>Can I Bet with Crypto in Ireland Legally</h2>
<p>Betting with cryptocurrency is a legal grey area in Ireland. No GRAI remote betting licence explicitly authorises crypto-only betting sites — licences are issued to operators handling regulated currency (EUR). Crypto betting platforms operating without a GRAI licence are unlicensed from an Irish regulatory perspective, meaning no consumer protection, no dispute resolution, and no KYC guarantees. Irish residents can technically access them, but do so without the safeguards that apply to GRAI-licensed sites.</p>
<p>Tax note: any winnings from betting — crypto or fiat — are not subject to income tax in Ireland if betting is recreational. However, converting crypto winnings to EUR may trigger a Capital Gains Tax event on any gain from the crypto itself.</p>

<h2>Can I Bet on Credit Card in Ireland</h2>
<p>Since April 2020, most major GRAI/Revenue-licensed operators have voluntarily removed credit card deposits following the UK's ban, and some Irish banks block gambling transactions on credit cards regardless. Debit cards (Visa Debit, Mastercard Debit) remain the standard — they draw from your account balance, not borrowed credit. If your credit card is declined at a betting site, switch to your debit card or use Revolut, PayPal, or a bank transfer.</p>

<h2>Can I Have Two Betting Accounts in Ireland</h2>
<p>Having two accounts at the same operator is a breach of their terms and conditions and can result in both accounts being closed and funds confiscated. Having accounts at two different operators is permitted and common — there is no legal restriction. Many Irish bettors hold 3–5 accounts to access the best odds across operators (line shopping) and to claim multiple welcome bonuses.</p>

<h2>Can I Use a VPN to Access Blocked Betting Sites Ireland</h2>
<p>Using a VPN to access a site that is blocked in Ireland, or that does not accept Irish customers, violates the site's terms and conditions. If your account is discovered to be using a VPN, it will be closed and winnings forfeited. Additionally, an unlicensed site operating outside GRAI oversight offers no consumer protection — disputes cannot be escalated to the GRAI or any Irish authority. The risk is entirely on the player.</p>

<h2>Can I Withdraw to a Different Card Than I Deposited Ireland</h2>
<p>Under anti-money laundering (AML) rules, most operators require withdrawals to return to the same payment method used to deposit. If you deposited with Visa Debit, the withdrawal must go back to that card. Only after the deposit amount is returned can you withdraw remaining winnings to a bank account or e-wallet. This is a regulatory requirement, not an operator choice — it prevents money laundering through betting accounts.</p>

<h2>Can I Keep My Winnings If My Account Is Closed Ireland</h2>
<p>If an operator closes your account for breaching their terms (bonus abuse, multiple accounts, matched betting flagged as abusive), they may void bets and confiscate funds. If closure is at your request (self-exclusion or cooling-off), your balance is returned minus any pending bonuses with active wagering requirements. For disputes, the GRAI provides a formal complaints process — file at grai.ie before escalating further.</p>
"""
patch("are-betting-winnings-taxable-ireland.html", c10_crypto)

c10_legal = """
<h2>Is Matched Betting Legal in Ireland</h2>
<p>Matched betting itself — placing bets and lay bets to cover all outcomes and extract free bet value — is not illegal in Ireland. However, it breaches most operators' terms and conditions. If detected, accounts are gubbed (stake-limited) or closed. The practice is legal from a criminal law perspective but carries the practical risk of losing access to promotional offers and having accounts restricted.</p>

<h2>Is Arbitrage Betting Legal in Ireland</h2>
<p>Arbitrage betting (arbing) — exploiting odds differences between operators to guarantee a profit — is legal under Irish law. It is not illegal gambling; it is a form of mathematical trading. Operators, however, consider it a breach of terms and will restrict or close accounts of known arbers. Using multiple GRAI-licensed accounts at different operators to arb is legal but commercially risky (account restriction).</p>

<h2>Is Daily Fantasy Sports Legal in Ireland</h2>
<p>Daily fantasy sports (DFS) platforms like DraftKings are not explicitly regulated under the Gambling Regulation Act 2024 in Ireland, as the Act primarily covers traditional fixed-odds betting and casino games. The legal status of DFS as a game of skill vs. chance remains unresolved in Irish law. GRAI has not issued DFS-specific licences. Players participate at their own risk with no formal Irish consumer protection framework.</p>

<h2>Is Spread Betting Legal in Ireland</h2>
<p>Financial spread betting is regulated by the Central Bank of Ireland, not GRAI. Sports spread betting occupies a grey area — it is not covered by standard GRAI betting licences. Operators offering sports spread betting to Irish residents need appropriate authorisation. Most Irish-facing operators do not offer sports spread betting; it remains more common in the UK market.</p>

<h2>Is Poker Legal in Ireland Online</h2>
<p>Online poker is legal in Ireland when played on a licensed platform. The Gambling Regulation Act 2024 covers poker as a gaming product, requiring a GRAI gaming licence. Casino gaming licences — which cover poker — are expected to be issued from 2027–2028. Until then, Irish players access online poker via operators holding licences from other EU jurisdictions (Malta, Gibraltar, Isle of Man) or unexpired Revenue permissions.</p>

<h2>Is Bingo Legal Online in Ireland</h2>
<p>Online bingo is legal in Ireland under the transitional arrangements of the Gambling Regulation Act 2024. Operators with valid Revenue permissions continue to offer bingo during the transition. GRAI gaming licences (which will cover bingo) are expected from 2027–2028. Always check that the platform displays a valid licence in its footer before depositing.</p>
"""
patch("is-online-casino-illegal-ireland.html", c10_legal)

# ─── CLUSTER 12: Horse races ───────────────────────────────────────────────────
c12_horseracing = """
<h2>Cheltenham Gold Cup 2027 Betting Odds Ireland</h2>
<p>The Cheltenham Gold Cup is run on the Friday of the festival (Gold Cup Day) in March 2027 over 3 miles 2½ furlongs. Ante-post markets open in October–November of the preceding year. Irish trainers (Willie Mullins, Gordon Elliott, Henry de Bromhead) have dominated the Gold Cup in recent years. Ante-post punters should check NRNB (non-runner no-bet) status — many ante-post Gold Cup markets are NRNB, refunding stakes if your selection does not run.</p>""" + tbl(
    tr_h("Market type", "When available", "Typical margin", "NRNB?"),
    tr_n("Ante-post outright", "Oct–Mar", "8–12%", "Yes (most books)"),
    tr_a("Festival each-way", "Race week", "14–18%", "No"),
    tr_n("In-play", "Race day", "15–25%", "N/A"),
) + """

<h2>Cheltenham Champion Hurdle 2027 Tips Ireland</h2>
<p>The Champion Hurdle is the feature race of Champion Day (Tuesday). Run over 2 miles, it suits sharp, speedy hurdlers rather than stayers. Irish runners have won the Champion Hurdle regularly. When assessing ante-post tips, check the horse's Grade 1 form at Leopardstown (Christmas and Dublin Racing Festival) — these are the key form guides for Cheltenham Champion Hurdle contenders.</p>

<h2>Grand National 2027 Each Way Tips Ireland</h2>
<p>The Grand National at Aintree in April 2027 is the most bet-on horse race in Ireland. Each-way terms are typically 1/4 odds, first 5 or 6 places depending on the operator. With 40 runners and extreme conditions, each-way value lies in horses priced 20/1–50/1 with proven jumping ability and a previous National or quality chase win. Ante-post each-way bets should be placed with NRNB operators to protect against late scratchings.</p>

<h2>Irish Grand National 2027 Tips Ireland</h2>
<p>The Irish Grand National runs at Fairyhouse on Easter Monday. It is a handicap chase over 3½ miles and is Ireland's most popular domestic National Hunt race for betting. Each-way terms: 1/4 odds, 1–4 places (ante-post) or 1–5 places (day of race). Irish trainers dominate — look for Willie Mullins and Gordon Elliott entries announced in March.</p>

<h2>Punchestown Festival 2027 Betting Tips Ireland</h2>
<p>Punchestown in late April/early May is the culmination of the Irish National Hunt season. Many Cheltenham winners run again at Punchestown, often in similar Grade 1 contests. Ante-post markets open after Cheltenham. The Champion Chase, Gold Cup equivalent (Punchestown Gold Cup), and Champion Hurdle rematch are the key betting races. BOG is widely available from Irish operators for Punchestown.</p>

<h2>Leopardstown Christmas Festival 2027 Tips Ireland</h2>
<p>Leopardstown Christmas Festival (26–29 December) is the busiest betting period of the Irish horse racing year. The Irish Gold Cup, Leopardstown Chase, and Deloitte Novice Hurdle are the marquee races. Many Gold Cup and Champion Hurdle contenders run here as a Cheltenham prep. Prices are often generous 10–12 weeks before Cheltenham, making Christmas Leopardstown the best ante-post window of the year for Irish punters.</p>

<h2>Galway Races 2027 Betting Tips Ireland</h2>
<p>The Galway Festival (late July/early August) is the biggest flat and mixed meeting in Ireland by betting volume. The Galway Plate (handicap chase) and Galway Hurdle (handicap hurdle) are the most heavily bet races. High-draw bias and competitive handicaps make Galway notoriously hard to solve — focus on market movers on race morning and horses proven at the track.</p>
"""
patch("horse-racing-ante-post.html", c12_horseracing)

# ─── CLUSTER 13: How much / how long ──────────────────────────────────────────
c13_tax = """
<h2>How Much Can You Win on a Bet Ireland Tax Free</h2>
<p>Betting winnings in Ireland are not subject to income tax, Capital Gains Tax, or any other tax when betting is recreational. There is no upper limit — you can win €1,000, €100,000, or €1 million on a single bet and owe zero tax to Revenue. The only tax on betting is the 1% betting duty paid by the operator (included in the margin), not the punter. This is one of the most punter-friendly tax regimes in Europe.</p>
<p>Exception: if the Revenue Commissioners determine that betting is your primary business activity (professional gambler), winnings may be treated as income. This is rare and applies to very few individuals. For the vast majority of recreational bettors, all winnings are completely tax-free.</p>
""" + tbl(
    tr_h("Bet type", "Tax on winnings", "Who pays duty"),
    tr_n("Sports betting", "None for punter", "Operator pays 1% duty"),
    tr_a("Horse racing", "None for punter", "Operator pays 1% duty"),
    tr_n("Online casino", "None for punter", "Operator pays gaming tax"),
    tr_a("Poker", "None for punter (recreational)", "Operator pays gaming tax"),
    tr_n("Professional gambling", "Potential income tax", "Individual + operator"),
) + """

<h2>How Long Does a Withdrawal Take from Betting Site Ireland</h2>
<p>Withdrawal times in Ireland vary by payment method. E-wallets (PayPal, Skrill, Neteller) are fastest: typically 2–24 hours once approved. Debit card withdrawals take 1–5 business days. Bank transfers take 3–5 business days. First withdrawals always take longer due to KYC verification — allow 24–72 hours extra for the initial ID check.</p>

<h2>How Long Does KYC Verification Take Betting Ireland</h2>
<p>KYC (Know Your Customer) verification at Irish betting sites typically takes 24–72 hours for standard documents (passport or driving licence + proof of address). Some operators use automated ID verification that completes in under 10 minutes. GRAI-licensed operators must complete KYC before allowing withdrawals. If KYC is taking longer than 5 business days, contact customer support directly — common delays are caused by blurry document photos or mismatched address details.</p>

<h2>How Much Do You Need to Deposit to Get Free Bet Ireland</h2>
<p>Welcome free bet offers in Ireland typically require a minimum qualifying deposit of €10–€20 and a qualifying bet at minimum odds of 1.5–2.0 (evens). The free bet is credited after the qualifying bet settles. Example: "Bet €10 get €30 free bet" — deposit €10, place a €10 bet at odds of 2.0+, then receive a €30 free bet token (SNR). Always read the minimum odds and time limits before depositing.</p>
"""
patch("are-betting-winnings-taxable-ireland.html", c13_tax)

c13_withdrawal = """
<h2>How Much Is the Minimum Bet in Ireland</h2>
<p>The minimum stake at most Irish online betting sites is €0.10–€0.50 for singles. Accumulator minimum stakes are typically the same. For some markets (Asian handicaps, exotic horse racing bets), minimums may be higher at €1–€2. Phone betting and in-shop betting minimums vary by operator. There is no legal minimum — it is set entirely by the operator.</p>
""" + tbl(
    tr_h("Bet type", "Typical minimum stake", "Typical maximum stake"),
    tr_n("Football single", "€0.10–€0.50", "€10,000–€100,000+"),
    tr_a("Horse racing single", "€0.10–€1.00", "€10,000–€50,000"),
    tr_n("Accumulator (4+ legs)", "€0.10–€0.50", "€2,000–€10,000"),
    tr_a("Correct score", "€1.00", "€2,000"),
    tr_n("Asian handicap", "€1.00–€2.00", "€20,000"),
) + """

<h2>How Long Does a Withdrawal Take from Betting Site Ireland</h2>
<p>Processing times start once the operator approves the withdrawal request (typically within business hours). E-wallets are fastest; bank transfers slowest.</p>
""" + tbl(
    tr_h("Method", "Processing time", "Notes"),
    tr_n("PayPal / Skrill", "2–24 hours", "Fastest option"),
    tr_a("Debit card (Visa/MC)", "1–5 business days", "Card issuer processing"),
    tr_n("Bank transfer", "3–5 business days", "Slowest but no limit"),
    tr_a("Revolut", "2–24 hours", "Treated as debit card"),
    tr_n("First-time withdrawal", "+24–72 hours", "KYC check required"),
)
patch("minimum-withdrawal-betting-ireland.html", c13_withdrawal)

c13_freebets = """
<h2>How Long Are Free Bets Valid Ireland</h2>
<p>Free bet expiry varies by operator and offer type. Welcome free bets typically expire 7 days after being credited. Ongoing promotional free bets (weekend reload, acca insurance) often expire within 24–48 hours. Free spins on casino have similar short windows. Always check the offer terms — the expiry timer usually starts from when the free bet is credited to your account, not from when you requested it.</p>
""" + tbl(
    tr_h("Free bet type", "Typical validity", "What happens if unused"),
    tr_n("Welcome free bet", "7 days", "Automatically removed"),
    tr_a("Acca insurance refund", "24–48 hours", "Automatically removed"),
    tr_n("Weekly reload free bet", "7 days", "Automatically removed"),
    tr_a("Refer-a-friend free bet", "7–30 days", "Automatically removed"),
    tr_n("Free spins", "24–72 hours", "Automatically removed"),
) + """
<p>To avoid losing free bets: check your account's "Bonuses" or "Promotions" section regularly, enable email notifications for credits, and use free bets on the first suitable qualifying market rather than waiting for a preferred event.</p>
"""
patch("how-long-free-bet-valid-ireland.html", c13_freebets)

# ─── CLUSTER 14: Specific slot RTP questions ──────────────────────────────────
c14_pragmatic = """
<h2>Gates of Olympus Maximum Win Ireland</h2>
<p>Gates of Olympus (Pragmatic Play) has a maximum win of 5,000× stake. On a €1 spin, the maximum payout is €5,000. At €5 per spin, maximum win is €25,000. The game achieves this through cascading multipliers that stack during free spins — multipliers of 2×, 3×, 5×, 10× or 500× land randomly and accumulate. RTP is 96.5% in standard mode; some operators offer a 96.5% or reduced 94% version — check the in-game info screen.</p>
<p>Gates of Olympus 1000, the sequel, raises the maximum win to 10,000× stake. This version is not available on all Irish sites due to the buy-feature restriction — Pragmatic's buy bonus feature is disabled on many GRAI/Revenue-licensed sites.</p>

<h2>Sweet Bonanza 1000 Buy Bonus Ireland</h2>
<p>Sweet Bonanza 1000 (Pragmatic Play) offers a maximum win of 10,000× stake and features a buy-bonus option to trigger free spins directly. However, the buy-bonus feature is disabled on most GRAI-licensed Irish betting and casino sites, as GRAI/Revenue licence conditions restrict instant-trigger bonus purchases. If you see the buy-bonus button, the site may be operating under a different jurisdiction's licence — check the footer before depositing.</p>

<h2>Big Bass Bonanza RTP and Volatility</h2>
<p>Big Bass Bonanza (Pragmatic Play) has an RTP of 96.71% and high volatility. The fish collector mechanic in free spins multiplies winnings — each fish collected adds a multiplier to subsequent wins. The base game pays infrequently; most value comes from the free spins feature triggered by 3+ scatter symbols. Maximum win is 2,100× stake — lower than Gates of Olympus, making it a steadier high-volatility option.</p>
""" + tbl(
    tr_h("Game", "RTP", "Volatility", "Max win", "Buy bonus (Ireland)"),
    tr_n("Gates of Olympus", "96.5%", "Very high", "5,000×", "Usually disabled"),
    tr_a("Sweet Bonanza 1000", "96.5%", "Very high", "10,000×", "Usually disabled"),
    tr_n("Big Bass Bonanza", "96.71%", "High", "2,100×", "No"),
    tr_a("Sugar Rush 1000", "96.5%", "Very high", "10,000×", "Usually disabled"),
    tr_n("Starlight Princess", "96.5%", "Very high", "5,000×", "Usually disabled"),
)
patch("pragmatic-play-casinos-ireland.html", c14_pragmatic)

c14_nolimit = """
<h2>Fire in the Hole xBomb RTP Ireland</h2>
<p>Fire in the Hole xBomb (Nolimit City) is a high-volatility slot with an RTP of 96.00% and a maximum win of 60,000× stake — one of the highest max wins available in slots accessible to Irish players. The xBomb mechanic destroys adjacent symbols on each spin, creating cascading wins and growing multipliers. The game is 18+ and classified as very high risk — budget accordingly and expect long losing streaks between big wins.</p>

<h2>Mental Slot RTP Nolimit City Ireland</h2>
<p>Mental (Nolimit City) has an RTP of 96.00% and extreme volatility with a maximum win of 70,183× stake. The xNudge Wild mechanic and bonus buy (where available) make it one of Nolimit's most volatile titles. The buy-bonus feature may be disabled on GRAI/Revenue-licensed Irish sites — confirm in the in-game paytable before depositing.</p>

<h2>San Quentin xWays RTP Ireland</h2>
<p>San Quentin xWays (Nolimit City) holds an RTP of 96.00% and a maximum win of 150,000× stake — the highest of any widely-available slot title. This is an extreme-volatility game aimed at high-risk players with a large bankroll. The xWays mechanic expands symbols to reveal 2–4 symbols per reel position, creating massive win potential. Expect very long base-game dead spells — the max win is achievable but statistically rare.</p>
""" + tbl(
    tr_h("Game", "RTP", "Volatility", "Max win"),
    tr_n("Fire in the Hole xBomb", "96.00%", "Extreme", "60,000×"),
    tr_a("Mental", "96.00%", "Extreme", "70,183×"),
    tr_n("San Quentin xWays", "96.00%", "Extreme", "150,000×"),
    tr_a("Tombstone RIP", "96.08%", "Very high", "10,000×"),
    tr_n("Deadwood xNudge", "96.03%", "Very high", "10,000×"),
)
patch("nolimit-city-casinos-ireland.html", c14_nolimit)

c14_netent = """
<h2>Dead or Alive 2 High Noon RTP Ireland</h2>
<p>Dead or Alive 2 (NetEnt) has three free spin modes with dramatically different RTPs and volatility. The standard RTP is 96.82%. High Noon Saloon, the highest volatility option, pays the same RTP but concentrates wins into fewer, larger payouts — suitable for players chasing the 100,000× maximum win. Train Heist is medium volatility with more frequent wins. Old Saloon is the lowest volatility option with the most regular small wins.</p>
""" + tbl(
    tr_h("Mode", "Volatility", "What it does"),
    tr_n("Old Saloon", "Medium", "Sticky wilds, frequent small wins"),
    tr_a("Train Heist", "High", "Expanding wilds, medium wins"),
    tr_n("High Noon Saloon", "Very high", "Sticky + expanding wilds, rare massive wins"),
) + """

<h2>Reactoonz 2 RTP and Max Win</h2>
<p>Reactoonz 2 (Play'n GO) has an RTP of 96.20% and a maximum win of 4,570× stake. It uses a cluster pays mechanic (5+ adjacent symbols to win) rather than paylines. The Quantumeter fills during play and triggers one of four modifiers: Implosion, Incision, Alteration, or Demolition — each of which can clear large portions of the grid and restart cascades. Volatility is high.</p>

<h2>Starburst RTP Paytable Explained</h2>
<p>Starburst (NetEnt) has an RTP of 96.09% and low volatility — it pays frequently but in small amounts. It uses a 5×3 reel layout with paylines paying left-to-right AND right-to-left (10 total). Wild Starburst symbols expand to cover an entire reel and trigger a free re-spin (up to 3 times). Maximum win is 500× stake — the lowest of major slots, but Starburst's value is consistent, low-variance entertainment rather than jackpot chasing.</p>
"""
patch("netent-casinos-ireland.html", c14_netent)

# ─── CLUSTER 15: Responsible gambling ─────────────────────────────────────────
c15_rg = """
<h2>How to Self-Exclude from All Betting Sites Ireland</h2>
<p>Ireland's national self-exclusion register is managed by the GRAI (Gambling Regulatory Authority of Ireland). When GRAI's interoperable exclusion register is fully operational, a single self-exclusion will cover all GRAI-licensed operators. Until then, you must self-exclude individually with each operator using their responsible gambling settings — typically found in Account &gt; Responsible Gambling &gt; Self-Exclusion.</p>
<p>Self-exclusion periods in Ireland: minimum 6 months, options typically 1 year, 3 years, 5 years, or permanent. Permanent self-exclusion cannot be reversed. During the exclusion period, the operator must refuse you service and return your balance.</p>

<h2>GRAI Self-Exclusion Register Ireland How It Works</h2>
<p>Under the Gambling Regulation Act 2024, GRAI is building a national self-exclusion register that will allow Irish residents to exclude from all GRAI-licensed operators with a single registration. As of late 2026, the register is in development — a timeline for full launch has not been officially confirmed. Meanwhile, GRAI has an interim complaints and exclusion process — contact grai.ie for the current procedure.</p>

<h2>Gambling Awareness Trust Ireland Phone Number</h2>
<p>The Gambling Awareness Trust Ireland helpline is <strong>1800 753 753</strong> (freephone, available Monday–Friday 9am–5pm). The trust also provides referrals to free counselling services nationwide. Online resources are at gamblingcare.ie. For 24/7 crisis support, Samaritans Ireland is available at 116 123 (freephone).</p>
""" + tbl(
    tr_h("Organisation", "Contact", "Service"),
    tr_n("Gambling Awareness Trust", "1800 753 753", "Helpline, counselling referral"),
    tr_a("gamblingcare.ie", "gamblingcare.ie", "Online resources, self-help tools"),
    tr_n("Gamblers Anonymous Ireland", "gamblers-anonymous.ie", "Free peer support meetings"),
    tr_a("GRAI", "grai.ie", "Regulatory complaints, exclusion"),
    tr_n("Samaritans Ireland", "116 123", "24/7 crisis support"),
) + """

<h2>How to Set Deposit Limits on Betting Site Ireland</h2>
<p>All GRAI-licensed betting sites must offer deposit limits. To set one: go to Account &gt; Responsible Gambling &gt; Deposit Limits, enter your daily/weekly/monthly limit, and confirm. Reductions take effect immediately. Increases require a cooling-off period (typically 24–72 hours) to prevent impulsive limit raises. GRAI-licensed operators cannot process deposits above your confirmed limit.</p>

<h2>How to Request Gambling Treatment Ireland Free</h2>
<p>Free gambling treatment is available through the HSE's National Gambling Service — a dedicated, free-of-charge counselling service for people affected by gambling problems. Referrals can be self-made (no GP required): contact the Gambling Awareness Trust at 1800 753 753 for a referral. The National Gambling Service offers one-to-one counselling and group support across Ireland. Waiting times vary by location; online and phone counselling options are available with shorter waits.</p>

<h2>Gamblers Anonymous Ireland Meetings</h2>
<p>Gamblers Anonymous (GA) holds free peer-support meetings across Ireland — Dublin, Cork, Galway, Limerick, and other cities. Meetings are anonymous and open to anyone with a gambling problem; no referral is needed. Find local meeting times and locations at gamblers-anonymous.ie. GA also offers a Gam-Anon programme for family members affected by someone else's gambling.</p>
"""
patch("national-gambling-exclusion-register.html", c15_rg)

print("\nAll patches applied.")
