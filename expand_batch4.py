#!/usr/bin/env python3
"""Batch 4: expand 50 thin pages with GSC-targeted H2 sections."""

import re, os

TABLE_STYLE = "width:100%;border-collapse:collapse;margin:16px 0;font-size:0.95rem"
TH = "padding:9px;border:1px solid #2d5a3d;text-align:left;color:#cde6d4"
TD = "padding:8px;border:1px solid #2d5a3d"
TR_H = "background:#1e3a28"
TR_A = "background:#0d1f14"

def th(*cols):
    cells = "".join(f'<th style="{TH}">{c}</th>' for c in cols)
    return f'<tr style="{TR_H}">{cells}</tr>'

def tr(*cols, alt=False):
    cells = "".join(f'<td style="{TD}">{c}</td>' for c in cols)
    style = f' style="{TR_A}"' if alt else ""
    return f"<tr{style}>{cells}</tr>"

def table(header_cols, rows):
    h = th(*header_cols)
    body = "".join(tr(*r, alt=(i%2==1)) for i,r in enumerate(rows))
    return f'<table style="{TABLE_STYLE}">{h}{body}</table>'

def wrap(title, body):
    return f"\n<h2>{title}</h2>\n{body}\n"

EXPANSIONS = {}

# 1. player-to-score-anytime.html
EXPANSIONS["pages/player-to-score-anytime.html"] = wrap(
    "Anytime vs First Scorer: Key Differences",
    table(["Market","Requirement","Typical Odds Range","Settlement"],
          [["Anytime Scorer","Scores at any point in 90 mins","4/5 – 5/1","After final whistle"],
           ["First Scorer","Scores the first goal of match","3/1 – 10/1","Settled after first goal"],
           ["Last Scorer","Scores the final goal","5/1 – 12/1","After final whistle"],
           ["2+ Goals","Scores twice or more","7/2 – 14/1","After final whistle"],
           ["Hat-trick","Scores three or more","25/1 – 150/1","After final whistle"]])
) + wrap(
    "How Goalscorer Odds Are Priced",
    "<p>Bookmakers base goalscorer odds on a player's expected goals (xG) per 90 minutes, their penalty duties, and historical strike rate. A striker averaging 0.5 xG/90 would score roughly once every two games — implying a true anytime scorer probability of around 50%, which translates to even money (2.0 decimal) before the bookmaker's margin is added. Penalty takers carry a significant premium: a midfielder who takes spot-kicks may have similar anytime odds to a striker who doesn't.</p>"
) + wrap(
    "Value Tips for Goalscorer Markets",
    "<ul><li><strong>Penalty takers:</strong> Always confirm who takes penalties — a midfielder or defender on penalty duty can be excellent value at higher odds.</li><li><strong>Corner routines:</strong> Tall centre-backs who attack set pieces at a good rate are often underpriced in anytime markets.</li><li><strong>Home vs away:</strong> Strikers typically have higher xG at home — their away anytime odds may offer value if bookmakers use a flat rate.</li><li><strong>Own goals don't count:</strong> For first scorer markets, if the opposition scores an own goal first your selection must still score for 'first scorer' to win.</li></ul>"
)

# 2. each-way-each-way-doubles.html
EXPANSIONS["pages/each-way-each-way-doubles.html"] = wrap(
    "How Each-Way Double Returns Are Calculated",
    "<p>An each-way double is two separate each-way bets combined: win part + place part from selection A combined with win + place from selection B. At €5 each-way (€10 total stake), the win double and place double run independently. Example: Horse A wins at 5/1 (place 1/4 odds for top 3), Horse B places at 8/1 (place 1/4 odds):</p>" +
    table(["Part","Horse A Result","Horse B Result","Return on €5 stake"],
          [["Win double","Wins @ 5/1 → €30","Places – loses win part","€0 (both must win)"],
           ["Place double","Places @ 5/4 → €11.25","Places @ 3/1 → €20","€11.25 × 3 = Approx €33.75"],
           ["Total return","","","~€33.75 on €10 staked"]])
) + wrap(
    "Each-Way Double vs Two Separate Each-Way Bets",
    table(["Factor","EW Double","Two Separate EW Bets"],
          [["Win requirement","Both must win for win double","Each treated independently"],
           ["Place part","Both must place for place double","Each can place independently"],
           ["Risk level","Higher — both legs must connect","Lower — one can win, one can place"],
           ["Potential return","Much higher if both win","More consistent smaller returns"],
           ["Best use","When confident both selections place","When unsure about both placing"]])
) + wrap(
    "When Each-Way Doubles Make Sense",
    "<ul><li><strong>Festival racing:</strong> When two horses on the same day have strong place claims, an EW double can deliver a significant return even if neither wins outright.</li><li><strong>Large fields:</strong> More places paid means higher probability the place double lands.</li><li><strong>Price matters:</strong> EW doubles work best when at least one selection is 5/1 or bigger — small-priced EW selections rarely justify the combined stake.</li><li><strong>Avoid at short prices:</strong> Two 2/1 selections in an EW double means the win double returns roughly 9/1 on a small base, rarely worth the complexity.</li></ul>"
)

# 3. doubles-and-trebles-betting.html
EXPANSIONS["pages/doubles-and-trebles-betting.html"] = wrap(
    "How Doubles and Trebles Pay Out",
    "<p>All legs must win. Returns compound: each winning selection's return becomes the stake for the next leg.</p>" +
    table(["Bet Type","Legs","Min to win","Example return at 2/1 each"],
          [["Double","2","2 of 2","€10 → €30 (3.0 × 3.0)"],
           ["Treble","3","3 of 3","€10 → €90 (3.0 × 3.0 × 3.0)"],
           ["4-fold","4","4 of 4","€10 → €270"],
           ["5-fold","5","5 of 5","€10 → €810"],
           ["Patent","7 bets","1 of 3","Covers 3 singles + 3 doubles + 1 treble"]])
) + wrap(
    "Margin Impact on Multi-Leg Bets",
    "<p>Each leg carries the bookmaker's margin. A 5% margin per leg compounds aggressively in multiples:</p>" +
    table(["Number of legs","Approx effective margin","Impact on €10 bet"],
          [["1 (single)","~5%","You get ~€9.50 of fair value"],
           ["2 (double)","~10%","~€9.00 of fair value"],
           ["3 (treble)","~14%","~€8.60 of fair value"],
           ["5-fold","~23%","~€7.70 of fair value"]])
) + wrap(
    "When to Use Doubles and Trebles",
    "<ul><li><strong>Doubles:</strong> Two confident selections where singles seem poor value — the compounding effect can justify the risk.</li><li><strong>Trebles:</strong> Best with selections at odds of 2/1 or more — short-priced trebles rarely return enough to justify the all-or-nothing risk.</li><li><strong>Acca boosters:</strong> Many Irish betting sites offer enhanced returns on trebles and 4-folds — check the promo tab before combining.</li><li><strong>Avoid banker trebles</strong> where one leg is odds-on: a 1/2 shot pulls the multiplier down significantly.</li></ul>"
)

# 4. how-to-claim-casino-bonus-ireland.html
EXPANSIONS["pages/how-to-claim-casino-bonus-ireland.html"] = wrap(
    "Step-by-Step: Claiming a Casino Bonus in Ireland",
    "<ol><li><strong>Register and verify identity</strong> — GRAI-compliant sites require ID before bonus activation.</li><li><strong>Opt in</strong> — most bonuses require you to tick a box or enter a promo code during deposit.</li><li><strong>Meet the minimum deposit</strong> — usually €10–€20; depositing via e-wallets may exclude you.</li><li><strong>Check your bonus balance</strong> — bonus funds typically appear in a separate 'bonus' wallet.</li><li><strong>Read the game weighting</strong> — slots count 100%; table games may count 10–20% or be excluded.</li><li><strong>Complete wagering before withdrawing</strong> — bonus + deposit multiplied by the wagering requirement.</li></ol>"
) + wrap(
    "Bonus Terms Decoded",
    table(["Term","What It Means","Example"],
          [["Wagering requirement","How many times you must bet the bonus","30× bonus: €100 bonus = €3,000 to wager"],
           ["Game weighting","% each game type counts toward wagering","Slots 100%, blackjack 10%"],
           ["Max bet","Highest stake while wagering a bonus","Often €5 per spin"],
           ["Sticky bonus","Bonus funds that cannot be withdrawn","You withdraw winnings only"],
           ["Cashable bonus","Bonus converts to real money on completion","You withdraw bonus + winnings"],
           ["Time limit","Days to complete wagering","Usually 7–30 days"],
           ["Min odds (sports)","Minimum odds for free bet use","Usually 1/2 or Evens"]])
) + wrap(
    "Common Mistakes When Claiming Bonuses",
    "<ul><li><strong>Depositing via e-wallet:</strong> Revolut, PayPal and Skrill deposits often disqualify you from welcome bonuses — use Visa/Mastercard or bank transfer.</li><li><strong>Playing excluded games:</strong> If you play a game weighted at 0% while a bonus is active, it won't count toward wagering and may forfeit the bonus.</li><li><strong>Exceeding the max bet:</strong> Placing a bet above the maximum allowed stake (often €5) during bonus wagering can void the entire bonus.</li><li><strong>Letting the timer expire:</strong> Most bonuses expire in 7–30 days — set a reminder to complete wagering in time.</li></ul>"
)

# 5. vip-casino-ireland.html
EXPANSIONS["pages/vip-casino-ireland.html"] = wrap(
    "How Casino VIP and Loyalty Programmes Work",
    "<p>Most Irish online casinos operate a points-based loyalty scheme. You earn points for every wager placed on eligible games (usually slots), which accumulate to unlock tier upgrades and redeem for bonus funds or free spins. Table games and live casino typically earn fewer points per pound wagered.</p>" +
    table(["Tier","Typical monthly wagering","Common benefits"],
          [["Bronze / Standard","€0–€2,000","Points accumulation, standard support"],
           ["Silver","€2,000–€10,000","Faster withdrawals, reload bonuses"],
           ["Gold","€10,000–€50,000","Personal account manager, birthday bonus"],
           ["Platinum / VIP","€50,000+","Higher withdrawal limits, bespoke offers, event invites"]])
) + wrap(
    "VIP Withdrawal Limits and Account Perks",
    table(["Benefit","Standard Account","VIP Account"],
          [["Daily withdrawal","€2,000–€5,000","€10,000–€50,000+"],
           ["Withdrawal speed","1–5 business days","Same day / instant"],
           ["Account manager","No","Yes — dedicated contact"],
           ["Bonus wagering","30–50×","10–30× (negotiable)"],
           ["Reload offers","Weekly email","Tailored to play history"],
           ["Payment methods","Standard set","Wire transfer often available"]])
) + wrap(
    "Is VIP Status Worth Pursuing in Ireland?",
    "<ul><li><strong>Points value:</strong> Typical loyalty schemes return 0.1–0.5% of wagers as bonus value — compare this against the house edge on your preferred game.</li><li><strong>GRAI and responsible gambling:</strong> High VIP spend comes with risk. Under the Gambling Regulation Act 2024, licensed operators must monitor high-volume players for signs of problem gambling. VIP players can self-exclude via GAMSTOP or the National Gambling Exclusion Register at any time.</li><li><strong>Negotiating terms:</strong> VIP account managers can sometimes negotiate lower wagering requirements or higher cashback percentages — it's worth asking.</li><li><strong>18+ | gamble responsibly | Gambling Awareness Trust: 1800 753 753</strong></li></ul>"
)

# 6. enhanced-odds-real-value-ireland.html
EXPANSIONS["pages/enhanced-odds-real-value-ireland.html"] = wrap(
    "How Enhanced Odds Promotions Work",
    "<p>Enhanced odds (also called price boosts or odds boosts) temporarily raise the odds on a specific selection above the standard market price. A team priced at 2/1 may be boosted to 4/1 for a limited time. The difference in return is paid as a free bet or bonus cash — there is usually a maximum stake, typically €5–€20.</p>" +
    table(["Feature","Standard Odds","Enhanced Odds"],
          [["Selection","Team A to win","Team A to win"],
           ["Price","2/1 (3.0)","5/1 (6.0)"],
           ["Stake","€10","€10 (max stake often €5–10)"],
           ["Return if wins","€30","€60 (extra paid as bonus)"],
           ["Withdrawal","Immediate","May require 1× wagering on extra profit"]])
) + wrap(
    "Spotting Genuine Value vs Marketing Boosts",
    "<ul><li><strong>Compare to other books:</strong> An enhanced price is only valuable if it exceeds what you can get elsewhere. Use an odds comparison site to check.</li><li><strong>Check the max stake:</strong> A 10/1 boost is less impressive when capped at a €5 stake — maximum profit is €50.</li><li><strong>Wagering on the extra:</strong> Some promotions pay the enhanced profit as a free bet requiring 1× wagering. This reduces the real value by roughly 50% (a €1 free bet is worth about 50p in expected value).</li><li><strong>Time limits:</strong> Price boosts are typically valid for a specific event or for 24 hours — don't rush a bet just to use a boost.</li></ul>"
) + wrap(
    "Enhanced Odds vs Acca Boosts",
    table(["Feature","Enhanced Odds","Acca Boost"],
          [["Applies to","Single selection","Multiple selections (3+)"],
           ["Typical uplift","50–300% on price","5–50% on combined return"],
           ["Max stake","€5–€20","€5–€25"],
           ["Best for","Single confident pick","Pre-planned accumulators"],
           ["Complexity","Low","Higher — all legs must win"]])
)

# 7. can-you-bet-on-credit-card-ireland.html
EXPANSIONS["pages/can-you-bet-on-credit-card-ireland.html"] = wrap(
    "Credit Card Betting in Ireland: Current Status",
    "<p>As of 2024, credit card deposits are banned for gambling in the UK (since April 2020), but no equivalent blanket ban exists in Ireland. However, many Irish-facing operators have voluntarily removed credit card deposits, and individual card issuers (Bank of Ireland, AIB, etc.) may decline gambling transactions by default. Always check your bank's settings before attempting a credit card deposit.</p>" +
    table(["Card Type","Deposit Status","Bank's default","Notes"],
          [["Visa Credit","Available on some sites","May be declined","Check issuer gambling block"],
           ["Mastercard Credit","Available on some sites","May be declined","Higher decline rate than debit"],
           ["Visa Debit","Widely accepted","Allowed","Most common method"],
           ["Mastercard Debit","Widely accepted","Allowed","Revolut uses Mastercard network"]])
) + wrap(
    "Why Credit Card Betting Carries Extra Risk",
    "<ul><li><strong>Borrowing to gamble:</strong> Using a credit card means betting with borrowed money — losses must be repaid with interest (typically 20–25% APR).</li><li><strong>Cash advance fees:</strong> Some banks treat gambling deposits as cash advances, charging a fee of 2–3% plus a higher interest rate from day one.</li><li><strong>Credit score:</strong> Regular gambling deposits on a credit card can be flagged by lenders during mortgage or loan applications.</li><li><strong>Responsible gambling:</strong> If you feel you need credit to fund gambling, speak to the Gambling Awareness Trust: 1800 753 753 or visit gamblingcare.ie. Gambling should only be funded from disposable income.</li></ul>"
) + wrap(
    "Best Alternatives to Credit Cards for Betting",
    table(["Method","Deposit Speed","Withdrawal","Notes"],
          [["Visa/MC Debit","Instant","1–5 days","Most widely accepted"],
           ["Revolut","Instant","Instant to Revolut","Toggle gambling block in app"],
           ["Bank Transfer","1–3 days","1–3 days","Good for large withdrawals"],
           ["PayPal","Instant","1–3 days","May exclude from bonuses"]])
)

# 8. can-you-use-vpn-to-bet-ireland.html
EXPANSIONS["pages/can-you-use-vpn-to-bet-ireland.html"] = wrap(
    "Using a VPN to Bet: What Actually Happens",
    "<p>A VPN masks your IP address to make it appear you are connecting from a different country. Some bettors use VPNs to access sites blocked in Ireland, or to claim bonuses in another country's market. This violates virtually every betting site's terms and conditions — if detected, your account can be suspended and pending withdrawals voided.</p>" +
    table(["Risk","Likelihood","Consequence"],
          [["Account suspended","High if detected","All funds may be confiscated"],
           ["Withdrawal refused","Moderate","Site cites T&C breach"],
           ["Bonus voided","High","Any pending bonus cancelled"],
           ["Legal action","Low but possible","Terms may allow civil claim"],
           ["Data security","Moderate","Free VPNs may log and sell data"]])
) + wrap(
    "Why Irish Bettors Use VPNs (and Why It's Not Worth It)",
    "<ul><li><strong>Accessing blocked sites:</strong> Sites like Stake.com, 1xBet and others are blocked in Ireland. Using a VPN to access them bypasses the GRAI licensing requirement — these sites have no Irish consumer protection obligations.</li><li><strong>Bonus arbitrage:</strong> Trying to claim a UK or US welcome bonus while in Ireland is detected by modern KYC systems (your payment method and ID documents reveal your location regardless of VPN).</li><li><strong>GRAI-licensed alternatives:</strong> With 25+ GRAI-licensed operators available, there are legal, regulated alternatives for all major sports and casino products.</li></ul>"
) + wrap(
    "What To Do Instead of Using a VPN",
    "<ul><li>Use one of the 25+ GRAI remote betting licence holders operating legally in Ireland.</li><li>If a site you want isn't available, look for the same product on a licensed Irish site — odds and markets are typically comparable.</li><li>Report unlicensed sites operating in Ireland to the GRAI at <strong>grai.ie</strong>.</li></ul>"
)

# 9. reload-bonus-betting-ireland-what-is.html
EXPANSIONS["pages/reload-bonus-betting-ireland-what-is.html"] = wrap(
    "What Is a Reload Bonus?",
    "<p>A reload bonus is a deposit bonus offered to existing customers — as opposed to a welcome bonus which is for new sign-ups. The bonus is typically a percentage match on your next deposit (e.g. 50% up to €100), credited as bonus funds or free bets that require a wagering multiplier before withdrawal.</p>" +
    table(["Bonus Type","When offered","Typical value","Wagering"],
          [["Welcome bonus","First deposit only","50–100% up to €100–€500","20–40×"],
           ["Reload bonus","Weekly/monthly existing customers","25–50% up to €50–€100","25–40×"],
           ["Loyalty cashback","Ongoing by tier","5–20% of losses returned","0–1× (varies)"],
           ["Free bet reload","After a losing week","€5–€25 free bet","1× (SNR)"]])
) + wrap(
    "How to Find and Claim Reload Bonuses",
    "<ol><li>Log in and check the <strong>Promotions</strong> tab — reloads are usually listed there, often with a time limit.</li><li>Some reloads require an <strong>opt-in</strong> before depositing — do this first, as late opt-ins are rarely accepted.</li><li>Check if a <strong>promo code</strong> is required — these are sometimes emailed to opted-in customers.</li><li>Deposit the qualifying amount and confirm the bonus has been credited before playing.</li><li>Play through the wagering requirement on eligible games within the time limit.</li></ol>"
) + wrap(
    "Are Reload Bonuses Worth It?",
    "<ul><li><strong>Low wagering versions:</strong> A 50% reload at 5× wagering is excellent value — a €100 deposit yields €50 bonus, and you only need to wager €250 total to unlock it.</li><li><strong>High wagering versions:</strong> A 50% reload at 40× wagering on the bonus means wagering €2,000 to release €50 — the house edge over that volume will likely cost more than the bonus is worth.</li><li><strong>Free bet reloads:</strong> SNR (stake not returned) free bets of €10–€20 at 1× wagering are almost always worth using — there's no downside beyond one mandatory bet.</li></ul>"
)

# 10. outright-betting-guide.html
EXPANSIONS["pages/outright-betting-guide.html"] = wrap(
    "Outright Betting Markets Explained",
    table(["Market","Description","Settlement","Example"],
          [["Tournament winner","Pick the outright winner","After final","Champions League winner"],
           ["Top 4 / Top half","Finish in top N","End of season","Premier League top 4"],
           ["Top scorer (Golden Boot)","Most goals in competition","After last game","World Cup Golden Boot"],
           ["Relegation","Finish in bottom 3","End of season","Premier League relegation"],
           ["Group winner","Win the group stage","After group matches","World Cup group winner"],
           ["Each-way outright","Win + place (top 2–4)","After final/season","Outright EW at 1/4 odds"]])
) + wrap(
    "Ante-Post vs In-Season Outright Betting",
    table(["Feature","Ante-post (pre-season)","In-season"],
          [["Odds","Longer — more uncertainty","Shorter — form known"],
           ["Each-way places","Usually top 4","May reduce as field narrows"],
           ["NRNB rule","Often applies — check T&Cs","Less common"],
           ["Withdrawals","Common if key player injured","Less frequent"],
           ["Potential value","High — market inefficiencies larger","Lower but more informed"]])
) + wrap(
    "Finding Value in Outright Markets",
    "<ul><li><strong>Each-way value:</strong> In a 20-team league, top-4 at 1/4 odds means you effectively get 1/4 of the outright price if your team finishes in the top 4. This can offer better expected value than the win market alone for mid-tier title contenders.</li><li><strong>NRNB (non-runner no bet):</strong> If a selection is withdrawn before the event starts, your stake is returned. Always look for NRNB in outright markets — it eliminates the risk of a key withdrawal costing you.</li><li><strong>Price movement:</strong> Outright odds shorten significantly after a team's first few games. Getting on early in pre-season can offer value if you have a strong view on a team's prospects.</li></ul>"
)

# 11. casino-loyalty-program-ireland.html
EXPANSIONS["pages/casino-loyalty-program-ireland.html"] = wrap(
    "How Casino Loyalty Points Work",
    "<p>Loyalty points (also called comp points or reward points) are earned for every real-money wager at eligible games. Points accumulate in your account and can be converted to bonus cash or free spins at a fixed rate — typically 100 points = €1, though the earn rate varies widely.</p>" +
    table(["Game Type","Typical points per €10 wagered","Notes"],
          [["Slots","10 points","100% contribution"],
           ["Live Roulette","2–5 points","20–50% contribution"],
           ["Live Blackjack","1–2 points","10–20% contribution"],
           ["Video Poker","2–5 points","20–50% contribution"],
           ["Sports Betting","0–5 points","Often excluded or minimal"]])
) + wrap(
    "Redeeming Points: Real Value Calculation",
    "<ul><li>If you earn 10 points per €10 wagered (1 point per €1) and redeem at 100 points = €1, your loyalty return rate is 1% of wagers.</li><li>Compare this to the house edge: blackjack at 0.5% house edge means your loyalty return nearly cancels the house advantage. On slots at 4–5% house edge, the 1% return is meaningful but far from offsetting losses.</li><li>Tiered programmes accelerate earn rates at higher levels — Gold or Platinum tiers may earn 2× or 3× the base rate.</li></ul>"
) + wrap(
    "Loyalty Scheme Red Flags to Watch",
    "<ul><li><strong>Points expiry:</strong> Many schemes expire points after 30–90 days of inactivity — check the terms before accumulating a large balance.</li><li><strong>Withdrawal of rewards:</strong> Some sites require wagering on redeemed points (e.g. 3× wagering on the bonus cash). This can eliminate much of the value.</li><li><strong>Game exclusions:</strong> If your preferred game contributes 0% to loyalty points, the scheme has no value for you.</li><li><strong>18+ | Gamble responsibly | Gambling Awareness Trust: 1800 753 753</strong></li></ul>"
)

# 12. withdrawal-fee-betting-ireland.html
EXPANSIONS["pages/withdrawal-fee-betting-ireland.html"] = wrap(
    "Withdrawal Fees at Irish Betting Sites",
    table(["Payment Method","Typical Fee","Processing Time","Notes"],
          [["Visa/Mastercard Debit","Free","1–5 business days","Most common, no fee"],
           ["Bank Transfer","Free–€3","1–3 business days","Used for large withdrawals"],
           ["PayPal","Free","1–3 business days","Fast, may exclude from bonuses"],
           ["Revolut","Free","Instant–24 hours","Popular in Ireland"],
           ["Skrill / Neteller","Free–1%","1–2 business days","May exclude from bonuses"],
           ["Cheque","Rare","7–14 days","Used if card expired"]])
) + wrap(
    "When Fees Apply and How to Avoid Them",
    "<ul><li><strong>Inactive accounts:</strong> Some sites charge a monthly inactivity fee (€5–€10) if you haven't logged in for 12+ months. Withdraw your balance before going inactive.</li><li><strong>Too-frequent withdrawals:</strong> A handful of sites limit fee-free withdrawals per month (e.g. one free per month, then €1–€2 per request). Batch your withdrawals if possible.</li><li><strong>Currency conversion:</strong> If your account is in euros but your bank card is sterling (e.g. Northern Ireland), conversion fees may apply — confirm the currency at registration.</li><li><strong>Minimum withdrawal:</strong> Withdrawing below the minimum (usually €5–€20) may incur a fee or be blocked entirely.</li></ul>"
) + wrap(
    "Your Rights on Withdrawal Fees Under GRAI",
    "<p>GRAI-licensed operators must clearly disclose all fees in their terms and conditions before you deposit. If a fee appears that was not disclosed, you can raise a complaint formally with the site's customer service, then escalate to the GRAI at <strong>grai.ie</strong> if unresolved. The Gambling Regulation Act 2024 gives the GRAI powers to sanction operators who withhold funds or charge undisclosed fees.</p>"
)

# 13. fastest-withdrawal-betting-ireland.html
EXPANSIONS["pages/fastest-withdrawal-betting-ireland.html"] = wrap(
    "Fastest Withdrawal Methods at Irish Betting Sites",
    table(["Method","Typical Speed","Availability","Notes"],
          [["Revolut","Instant–2 hours","Most major sites","Fastest in practice"],
           ["PayPal","1–24 hours","Most major sites","Near-instant on some"],
           ["Visa/MC Debit","Same day–3 days","Universal","Depends on pending time"],
           ["Bank Transfer","1–3 business days","Universal","Best for large sums"],
           ["Skrill/Neteller","1–24 hours","Most major sites","Good speed, bonus caveats"]])
) + wrap(
    "What Slows Down Withdrawals",
    "<ul><li><strong>Pending period:</strong> Many sites impose a 24–48 hour internal review before processing — this is separate from the payment provider's processing time.</li><li><strong>KYC verification:</strong> If you haven't completed identity verification (passport/driving licence + proof of address), withdrawals are held until documents are approved. Complete KYC before your first withdrawal.</li><li><strong>Bonus wagering:</strong> You cannot withdraw funds tied to an active bonus until wagering is complete. Check your bonus balance before requesting withdrawal.</li><li><strong>Withdrawal limits:</strong> Large withdrawals may be split across multiple payments or require manual review — notify customer service in advance for withdrawals over €5,000.</li></ul>"
) + wrap(
    "Tips for Faster Withdrawals",
    "<ol><li>Complete identity verification immediately after registering — don't wait until you want to withdraw.</li><li>Use the same payment method for deposits and withdrawals — mismatched methods trigger extra security checks.</li><li>Withdraw to Revolut or PayPal rather than a bank card for the fastest processing.</li><li>Avoid withdrawing on weekends or bank holidays — many sites only process withdrawals on business days.</li><li>Check whether the site offers an instant withdrawal feature (sometimes reserved for verified VIP customers).</li></ol>"
)

# 14. how-to-withdraw-from-betting-site-ireland.html
EXPANSIONS["pages/how-to-withdraw-from-betting-site-ireland.html"] = wrap(
    "Step-by-Step: Withdrawing From a Betting Site",
    "<ol><li><strong>Log in</strong> to your account and ensure your balance shows available funds (not bonus funds).</li><li>Go to <strong>My Account → Withdraw</strong> (or Cashier → Withdraw).</li><li>Select your preferred <strong>payment method</strong> — the same method you deposited with is usually required first.</li><li>Enter the <strong>withdrawal amount</strong> — check the minimum and maximum for your chosen method.</li><li>Confirm the withdrawal — some sites send a confirmation email or SMS for large amounts.</li><li>Wait for the <strong>pending period</strong> (24–48 hours for most sites) then the payment provider's processing time.</li></ol>"
) + wrap(
    "Withdrawal Checklist Before You Request",
    table(["Check","Why it matters"],
          [["KYC verification complete","Withdrawals held until ID verified"],
           ["No active bonus attached","Bonus wagering must be complete first"],
           ["Withdrawal method registered","First use may need approval"],
           ["Amount above minimum","Below-minimum requests often blocked"],
           ["Account in good standing","Restricted/flagged accounts may delay processing"]])
) + wrap(
    "What to Do If Your Withdrawal Is Delayed",
    "<ul><li>Check your email for any verification requests from the site — they often send document requests that you may have missed.</li><li>Log in and check the <strong>Withdrawal History</strong> section — a 'pending' status means it's in the internal review queue.</li><li>Contact live chat and quote your withdrawal reference number — this speeds up manual review.</li><li>If a withdrawal has been pending for more than 5 business days without explanation, file a formal complaint through the site's complaints procedure, then escalate to the GRAI at <strong>grai.ie</strong>.</li></ul>"
)

# 15. how-long-does-bet-settlement-take.html
EXPANSIONS["pages/how-long-does-bet-settlement-take.html"] = wrap(
    "Typical Bet Settlement Times by Sport",
    table(["Sport / Market","Normal settlement","Why it can take longer"],
          [["Football — 90 mins result","30 min – 2 hours after final whistle","VAR reviews, abandoned matches"],
           ["Horse racing","10–30 min after race","Stewards enquiry, photo finish"],
           ["Tennis","1–2 hours after match","Retirement bets (depends on T&Cs)"],
           ["In-play bets","Near-instant to 30 min","Match review, error checks"],
           ["Outright / season-long","After final / end of season","Protracted playoffs"],
           ["Goalscorer bets","2–4 hours (video review)","Own goals, assist disputes"]])
) + wrap(
    "Why Bets Are Sometimes Delayed",
    "<ul><li><strong>Results under review:</strong> Stewards enquiries in horse racing or VAR checks in football can delay official results by 30–60 minutes, and bookmakers wait for official confirmation before settling.</li><li><strong>Abandonments:</strong> If a match is abandoned before completion, settlement rules vary — typically 'void' if less than 55–60 minutes played in football, settled on the official result if completed in horse racing.</li><li><strong>Manual review:</strong> Bets placed at odds that appear to be an error (palpable errors) may be reviewed and voided by the bookmaker.</li><li><strong>Large winning bets:</strong> Some sites manually review large payouts before releasing funds.</li></ul>"
) + wrap(
    "What To Do If Your Bet Hasn't Settled",
    "<ol><li>Wait the standard settlement window (see table above) before contacting support.</li><li>Check the site's <strong>Bet History</strong> — if it shows 'Open' it's still settling; 'Pending' may indicate a review.</li><li>Use live chat and quote your bet ID and event name for the fastest resolution.</li><li>If a bet remains unsettled after 48 hours past the event, raise a formal complaint.</li></ol>"
)

# 16. how-long-does-verification-take-betting-ireland.html
EXPANSIONS["pages/how-long-does-verification-take-betting-ireland.html"] = wrap(
    "ID Verification Timelines at Irish Betting Sites",
    table(["Verification Type","Typical Time","Documents Needed"],
          [["Automated KYC","Instant–1 hour","Passport or driving licence (auto-read)"],
           ["Manual review","24–72 hours","ID + proof of address (utility bill/bank statement)"],
           ["Source of funds","3–7 days","Bank statements, payslips, or tax returns"],
           ["Enhanced due diligence","7–21 days","Full financial documentation"]])
) + wrap(
    "Documents Accepted for Irish KYC",
    "<ul><li><strong>Photo ID (one required):</strong> Irish passport, Irish driving licence, EU national ID card, or UK passport.</li><li><strong>Proof of address (one required):</strong> Utility bill (gas, electricity, water), bank statement, government letter — dated within 3 months, showing your name and address.</li><li><strong>Source of funds (if requested):</strong> Payslips (last 3 months), bank statements, employment contract, pension statement, or proof of business income.</li><li><strong>Tips for faster approval:</strong> Submit clear, full-page scans (not photos of a screen), ensure the document is in date, and use the site's secure upload tool rather than emailing.</li></ul>"
) + wrap(
    "What Happens If Verification Fails",
    "<ul><li>The site will email you specifying what additional documents are needed — respond promptly.</li><li>Until verification is complete, withdrawals are typically blocked but you can continue to deposit and play (up to any deposit limits set).</li><li>If you believe the verification requirement is unreasonable or your account has been blocked without explanation, you can complain to the GRAI at <strong>grai.ie</strong>.</li><li>Accounts that cannot be verified after multiple attempts may be closed with the balance returned via the original deposit method.</li></ul>"
)

# 17. do-you-pay-tax-on-betting-winnings-ireland.html
EXPANSIONS["pages/do-you-pay-tax-on-betting-winnings-ireland.html"] = wrap(
    "Betting Tax in Ireland: The Rules",
    "<p>Ireland does not impose income tax on casual gambling winnings for private individuals. The <strong>Revenue Commissioners</strong> treat betting winnings as windfall gains, not earned income, so recreational punters owe no tax regardless of the amount won. This applies to horse racing, football, casino games, and all other forms of gambling.</p>" +
    table(["Situation","Tax liability","Notes"],
          [["Casual recreational betting","None","No declaration required"],
           ["Professional gambling (primary income)","Potentially assessable","Consult a tax advisor"],
           ["Betting as a business (e.g. trading)","Income tax may apply","Depends on structure"],
           ["Crypto gambling winnings","CGT may apply on conversion","Crypto is a chargeable asset"],
           ["Betting operator profits","3% betting duty on turnover","Paid by the operator, not punter"]])
) + wrap(
    "Who Pays Betting Tax in Ireland?",
    "<ul><li><strong>The operator pays:</strong> Licensed Irish bookmakers pay a 3% betting duty on their gross revenue. This cost is typically built into the odds — it's why margins at Irish-facing bookmakers can be slightly higher than at some offshore sites.</li><li><strong>You don't pay:</strong> As a punter, you receive your winnings gross, with no withholding tax applied by the bookmaker.</li><li><strong>Crypto note:</strong> If you gamble with cryptocurrency and later convert your winnings to euros, any gain on the crypto itself may be subject to Capital Gains Tax at 33%. This is a CGT event on the crypto asset, not a tax on gambling winnings per se.</li></ul>"
) + wrap(
    "Professional Gambling and Irish Tax",
    "<p>If gambling is your primary source of income, Revenue may assess it as self-employment income. There is no bright-line rule, but factors include the regularity and organisation of your activity, whether you apply a systematic approach, and whether you depend on it for your living. If you believe you may be a professional gambler for tax purposes, consult an Irish tax advisor. For the vast majority of recreational punters, there is no tax obligation on winnings.</p>"
)

# 18. cycling-betting-ireland.html
EXPANSIONS["pages/cycling-betting-ireland.html"] = wrap(
    "Cycling Betting Markets Available in Ireland",
    table(["Market","Description","Best events"],
          [["Race winner (outright)","Pick the stage or race winner","Tour de France, Vuelta, Giro"],
           ["Stage winner","Winner of individual stage","Daily markets during Grand Tours"],
           ["Each-way (top 3–5)","Place bet on a podium finish","Outright tours, classics"],
           ["Points jersey","Leader in points competition","Tour de France Green Jersey"],
           ["Sprint classification","First across a sprint line","Intermediate sprints"],
           ["Head-to-head","Which rider finishes higher","Any race, any day"]])
) + wrap(
    "Key Cycling Races to Bet On",
    table(["Race","When","Type","Distance"],
          [["Tour de France","July","3-week Grand Tour","~3,400 km, 21 stages"],
           ["Giro d'Italia","May","3-week Grand Tour","~3,500 km, 21 stages"],
           ["Vuelta a España","August–September","3-week Grand Tour","~3,200 km, 21 stages"],
           ["Paris–Roubaix","April","Classic (1 day)","~260 km (cobbles)"],
           ["Milan–San Remo","March","Classic (1 day)","~298 km"],
           ["Rás Tailteann","May","Irish stage race","8 stages in Ireland"]])
) + wrap(
    "Cycling Betting Tips for Irish Punters",
    "<ul><li><strong>Each-way value:</strong> In Grand Tours, top-5 or top-10 each-way on a climber can offer excellent value — the market is often dominated by one or two favourites, leaving others underpriced.</li><li><strong>Stage type:</strong> Match the rider profile to the stage — sprinters on flat stages (Marcel Kittel types), climbers on mountain finishes, time trial specialists on ITTs.</li><li><strong>Withdrawal rules:</strong> If a rider abandons mid-race after you've bet on them, most bookmakers settle as a loser. Check whether NRNB (non-runner no bet) applies — it rarely does in cycling.</li><li><strong>Live in-play:</strong> Stage winners markets are popular in-play during Grand Tours — odds swing significantly as breakaways build or collapse.</li></ul>"
)

# 19. how-to-reopen-closed-betting-account.html
EXPANSIONS["pages/how-to-reopen-closed-betting-account.html"] = wrap(
    "Why Betting Accounts Get Closed in Ireland",
    table(["Reason","Can it be reopened?","Steps required"],
          [["Self-exclusion (voluntary)","Yes, after cooling-off period","Contact site after period ends"],
           ["GAMSTOP self-exclusion","No during exclusion period","Wait for exclusion to expire"],
           ["Responsible gambling closure","Yes (usually)","Cooling-off then reapply"],
           ["Account restricted (winning too much)","Sometimes","Negotiation, rarely successful"],
           ["T&C breach (bonus abuse etc.)","Rarely","Appeal in writing"],
           ["KYC failure (can't verify ID)","Yes if new docs provided","Resubmit documents"],
           ["Inactivity","Yes","Log in and reactivate"]])
) + wrap(
    "How to Reopen a Voluntarily Closed Account",
    "<ol><li>Contact the site's customer support via live chat or email.</li><li>State your registered email address and that you wish to reopen the account.</li><li>If a cooling-off period was set (e.g. 30 days), you must wait until it has fully elapsed — sites legally cannot reopen accounts early for responsible gambling closures.</li><li>Confirm you are aware of responsible gambling resources and wish to continue betting.</li><li>You may be asked to re-verify your identity if documents have expired.</li></ol>"
) + wrap(
    "GAMSTOP and National Self-Exclusion",
    "<p>If your account was closed because you registered with <strong>GAMSTOP</strong> (the UK-wide self-exclusion scheme) or the Irish <strong>National Gambling Exclusion Register</strong>, GRAI-licensed operators are legally required to maintain your exclusion for the duration you selected (6 months, 1 year, or 5 years for GAMSTOP). No operator covered by these schemes can reopen your account early. When your exclusion expires, contact GAMSTOP to confirm it has lifted before attempting to reopen accounts. If you're concerned about your gambling, speak to the Gambling Awareness Trust: <strong>1800 753 753</strong>.</p>"
)

# 20. withdrawal-declined-betting-ireland.html
EXPANSIONS["pages/withdrawal-declined-betting-ireland.html"] = wrap(
    "Reasons Withdrawals Are Declined at Irish Betting Sites",
    table(["Reason","Fix"],
          [["KYC verification incomplete","Upload ID and proof of address"],
           ["Active bonus attached","Complete wagering requirement first"],
           ["Withdrawal method not verified","Use same method as deposit, or add new method first"],
           ["Below minimum withdrawal","Accumulate more funds or find a lower-minimum method"],
           ["Account flagged for review","Contact support with account ID"],
           ["Card expired","Update payment method in account settings"],
           ["Exceeded daily/weekly limit","Request multiple withdrawals over time, or contact VIP team"]])
) + wrap(
    "Step-by-Step: What to Do When a Withdrawal Is Declined",
    "<ol><li>Check your email for a message from the site explaining the reason — most declines trigger an automated email.</li><li>Log into your account and check the <strong>Withdrawal History</strong> — the decline reason may appear there.</li><li>Contact live chat immediately with your withdrawal reference number — agents can often process manually or escalate.</li><li>If KYC is the issue, upload your documents and request the withdrawal be re-processed once verified.</li><li>If no reason is given and the site is unresponsive, raise a formal complaint in writing via their complaints procedure (usually on the website footer).</li><li>If the complaint is unresolved after 8 weeks, escalate to the <strong>GRAI at grai.ie</strong>.</li></ol>"
) + wrap(
    "Your Rights if a Withdrawal Is Wrongly Declined",
    "<p>Under the Gambling Regulation Act 2024, GRAI-licensed operators must process withdrawal requests in a reasonable time and must not withhold funds without documented justification. If you believe your withdrawal has been wrongly refused, you have the right to file a complaint with the GRAI. Retain all correspondence with the site (screenshots of chat, email confirmations) as evidence for any dispute.</p>"
)

# 21. is-online-betting-legal-in-ireland-2026.html
EXPANSIONS["pages/is-online-betting-legal-in-ireland-2026.html"] = wrap(
    "Online Betting Legality in Ireland: 2026 Status",
    "<p>Online betting is fully legal in Ireland for licensed operators. The Gambling Regulation Act 2024 established the Gambling Regulatory Authority of Ireland (GRAI), which issues remote betting licences to operators wishing to legally accept Irish customers. The first remote betting licences were issued from 1 July 2026. Casino (gaming) licences are expected to follow in 2027–2028.</p>" +
    table(["Licence Type","Status (2026)","Issued since","Number issued"],
          [["Remote betting (sports/racing)","Active","1 July 2026","25+ operators"],
           ["In-person betting shop","Active (pre-existing)","Pre-2024","~1,200 shops"],
           ["Remote casino gaming","Not yet available","Expected 2027–2028","0 issued"],
           ["Land-based casino","Limited (8 licensed venues)","Pre-2024","8 venues"]])
) + wrap(
    "What Changes Under the 2024 Gambling Act",
    "<ul><li><strong>GRAI replaces the Revenue Commissioners</strong> as the regulator for gambling licensing and enforcement.</li><li><strong>Mandatory age verification:</strong> Operators must verify age before allowing any deposit or play — no more grace periods.</li><li><strong>Advertising restrictions:</strong> Gambling advertising watershed rules came into force, restricting TV and radio ads before 9pm.</li><li><strong>National Self-Exclusion Register:</strong> A centralised register allowing problem gamblers to exclude from all GRAI-licensed operators simultaneously.</li><li><strong>Operator liability:</strong> Enhanced duty of care obligations — operators must monitor for signs of problem gambling and take action.</li></ul>"
) + wrap(
    "Using Unlicensed Sites: What Irish Punters Should Know",
    "<ul><li>Unlicensed sites are not regulated by the GRAI and offer no consumer protections under Irish law.</li><li>If an unlicensed site refuses to pay out, there is no Irish regulatory body to escalate to.</li><li>Using a VPN to access blocked sites may void your bets and account under the site's T&Cs.</li><li>Stick to GRAI-licensed operators — verify licence status at <strong>grai.ie</strong>.</li></ul>"
)

# 22. world-cup-2026-final-betting.html
EXPANSIONS["pages/world-cup-2026-final-betting.html"] = wrap(
    "2026 World Cup Final: Format and Key Betting Markets",
    "<p>The 2026 FIFA World Cup expands to 48 teams for the first time, with the tournament hosted across the USA, Canada, and Mexico. The final takes place on 19 July 2026 at MetLife Stadium, East Rutherford, New Jersey. With more teams, the knockout rounds are more complex and there are more potential upsets in the draw.</p>" +
    table(["Market","Description","Key notes"],
          [["Match winner (90 mins)","Home/draw/away in 90 minutes","Extra time settled as draw; separate ET market"],
           ["Both teams to score","Both finalists score at least once","High-scoring finals rare: 2018 was 4-2"],
           ["Total goals over/under","Over or under 2.5 goals","World Cup finals average ~2.2 goals"],
           ["First goalscorer","Who scores first","Top scorer per tournament historically varies"],
           ["Winning margin","By how many goals","1-goal margin most common in finals"],
           ["Extra time / penalty shootout","Match to go to ET or pens","~25% of recent finals decided by pens"]])
) + wrap(
    "Historical World Cup Final Results",
    table(["Year","Match","Score","How decided"],
          [["2022","Argentina vs France","3-3 (AET)","Argentina win on penalties"],
           ["2018","France vs Croatia","4-2","Normal time"],
           ["2014","Germany vs Argentina","1-0 (AET)","Extra time"],
           ["2010","Spain vs Netherlands","1-0 (AET)","Extra time"],
           ["2006","Italy vs France","1-1 (AET)","Italy win on penalties"]])
) + wrap(
    "Betting Strategy for the World Cup Final",
    "<ul><li><strong>Both teams to score:</strong> Only 2 of the last 5 World Cup finals saw both teams score in 90 minutes — the market is often overpriced relative to history.</li><li><strong>Penalty shootout:</strong> With the expanded format, more tired teams may reach the final, increasing the chance of a shootout — historically around 1 in 4 finals go to pens.</li><li><strong>Each-way outright:</strong> If you placed an ante-post outright on a team pre-tournament, check whether your each-way terms cover finalist position (top 2) — this can still return a profit even if your team loses the final.</li></ul>"
)

# 23. ufc-310-betting-ireland.html
EXPANSIONS["pages/ufc-310-betting-ireland.html"] = wrap(
    "UFC Betting Markets Available in Ireland",
    table(["Market","Description","Example"],
          [["Fight winner (moneyline)","Pick which fighter wins","Fighter A -150, Fighter B +120"],
           ["Method of victory","KO/TKO, Submission, or Decision","KO/TKO often 2/1 – 5/1"],
           ["Round betting","Pick the round the fight ends","Specific round 10/1 – 25/1"],
           ["Over/under rounds","Total rounds completed","Over 2.5 rounds in 3-round fight"],
           ["Goes the distance","Fight lasts all scheduled rounds","Yes/No market"],
           ["Fighter props","Specific fighter stat","Takedown attempts, significant strikes"]])
) + wrap(
    "How UFC Odds Are Priced",
    "<p>UFC moneyline odds reflect the probability assigned to each fighter. American odds are most commonly used: a -150 favourite means you bet €150 to win €100 (implied probability 60%), while a +120 underdog means you win €120 for every €100 bet (implied probability ~45%). The combined implied probability exceeds 100% — the difference is the bookmaker's margin, typically 5–8% for major UFC events.</p>" +
    table(["American odds","Decimal","Implied probability","€10 returns"],
          [["-200","1.50","66.7%","€15.00"],
           ["-150","1.67","60.0%","€16.70"],
           ["-110","1.91","52.4%","€19.10"],
           ["EVEN","2.00","50.0%","€20.00"],
           ["+120","2.20","45.5%","€22.00"],
           ["+150","2.50","40.0%","€25.00"],
           ["+300","4.00","25.0%","€40.00"]])
) + wrap(
    "UFC Betting Tips for Irish Punters",
    "<ul><li><strong>Method of victory value:</strong> If you believe a fight ends inside the distance, the KO/TKO or Submission market often offers better value than the moneyline alone.</li><li><strong>Late replacements:</strong> When a fighter is replaced within 2 weeks of the event, the replacement often enters at longer odds — their preparation is compromised, so the market may not fully price in the disadvantage.</li><li><strong>Main card vs prelims:</strong> Markets are most liquid on main card fights — prelim markets can have wider spreads and less sharp pricing.</li><li><strong>Responsible gambling: 18+ | Gambling Awareness Trust: 1800 753 753</strong></li></ul>"
)

# 24. can-you-win-real-money-online-casino-ireland.html
EXPANSIONS["pages/can-you-win-real-money-online-casino-ireland.html"] = wrap(
    "Can You Really Win Money at Online Casinos in Ireland?",
    "<p>Yes — real money wins are paid out every day at licensed Irish online casinos. The important context is that all casino games have a built-in house edge, meaning over time the casino is mathematically guaranteed to retain a percentage of all money wagered. Short-term wins are possible and common; long-term profit is statistically very difficult to sustain.</p>" +
    table(["Game","House Edge","Your long-term return per €100 wagered"],
          [["Blackjack (basic strategy)","0.4–0.5%","€99.50–€99.60"],
           ["European Roulette","2.7%","€97.30"],
           ["American Roulette","5.26%","€94.74"],
           ["Video Poker (Jacks or Better, optimal)","0.5%","€99.50"],
           ["Baccarat (Banker bet)","1.06%","€98.94"],
           ["Slots (average)","3–8%","€92–€97"],
           ["Keno","20–35%","€65–€80"]])
) + wrap(
    "How Casino Payouts Work",
    "<ul><li><strong>RTP (Return to Player):</strong> Published as a percentage, e.g. 96% RTP means the game pays back €96 for every €100 wagered on average over millions of spins — your individual session will vary dramatically.</li><li><strong>Variance:</strong> High-volatility slots may pay out rarely but in large amounts; low-volatility slots pay more frequently but in smaller amounts. Neither is better for overall returns — RTP is the same.</li><li><strong>Withdrawal of winnings:</strong> Real money winnings (not bonus funds) can be withdrawn at any time to your registered payment method, provided KYC verification is complete.</li></ul>"
) + wrap(
    "Maximising Your Chances of a Winning Session",
    "<ul><li><strong>Play high-RTP games:</strong> Blackjack and video poker with correct strategy give the highest return of any casino game.</li><li><strong>Avoid side bets:</strong> Insurance in blackjack (3.7% edge), tie bet in baccarat (14.4% edge) — these dramatically increase the house edge on individual rounds.</li><li><strong>Set a session limit:</strong> Decide your maximum loss before you play. Gambling should be entertainment, not an income strategy.</li><li><strong>18+ | Gambling Awareness Trust: 1800 753 753 | gamblingcare.ie</strong></li></ul>"
)

# 25. northern-ireland-betting.html
EXPANSIONS["pages/northern-ireland-betting.html"] = wrap(
    "Betting in Northern Ireland: Key Differences From the Republic",
    "<p>Northern Ireland is part of the United Kingdom and subject to UK gambling legislation, not Irish law. The Gambling Commission (UKGC) licenses betting operators in Northern Ireland, while GRAI licenses them in the Republic. Most major betting sites hold both licences and operate seamlessly on both sides of the border, but there are some key differences.</p>" +
    table(["Feature","Northern Ireland (UK)","Republic of Ireland"],
          [["Regulator","Gambling Commission (UKGC)","GRAI (from 2026)"],
           ["Casino licence","UKGC Remote Casino Licence","Not yet issued (expected 2027–2028)"],
           ["Self-exclusion","GAMSTOP (UK-wide)","National Gambling Exclusion Register"],
           ["Betting duty","15% Point of Consumption Tax","3% betting duty"],
           ["Credit card betting","Banned since April 2020","Not currently banned"],
           ["Advertising watershed","9pm (pre-event) UK","9pm under Gambling Regulation Act"]])
) + wrap(
    "Which Betting Sites Work in Northern Ireland",
    "<ul><li>All major UKGC-licensed sites operate in Northern Ireland — the same sites available in England, Scotland, and Wales.</li><li>Sites with both UKGC and GRAI licences work on both sides of the border. If you live near the border and use a Republic-focused site, check that it also holds a UKGC licence for Northern Ireland customers.</li><li>Northern Irish customers can use GAMSTOP for UK-wide self-exclusion across all UKGC-licensed sites.</li></ul>"
) + wrap(
    "Currency and Payment Notes for Northern Ireland",
    "<ul><li>Northern Ireland uses <strong>pounds sterling (GBP)</strong> — accounts at UK-licensed sites are typically in GBP, not euros.</li><li>If you use an Irish bank card (euro-denominated), conversion fees may apply — check your card's foreign currency fee.</li><li>Northern Irish bank branches of AIB and Bank of Ireland may still issue euro-denominated debit cards — confirm your card's default currency before depositing.</li></ul>"
)

# Pages 26-50: continue with remaining pages
# 26. grai-licence-check-how-to-verify-bookmaker-ireland.html
EXPANSIONS["pages/grai-licence-check-how-to-verify-bookmaker-ireland.html"] = wrap(
    "How to Check If a Betting Site Has a GRAI Licence",
    "<ol><li>Visit <strong>grai.ie</strong> and navigate to the licensed operators register.</li><li>Search by the company name or site domain.</li><li>Confirm the licence type — only <strong>Remote Betting Licences</strong> have been issued since 1 July 2026. Casino (gaming) licences have not yet been issued.</li><li>Check the licence number matches what's shown in the site's footer (look for a number in the format GRAI-XXXX-RB-YY-XXXX).</li><li>Verify the licence is current and not suspended or revoked.</li></ol>"
) + wrap(
    "What GRAI Licences Mean for You",
    table(["Licence Type","What it covers","What it doesn't cover"],
          [["Remote Betting (RB)","Sports betting, horse racing, outright markets","Casino games, slots, live dealer"],
           ["In-Person Betting","Licensed betting shops in Ireland","Online betting"],
           ["Casino Gaming (not yet issued)","Slots, table games, live casino online","Not available until 2027–2028"]])
) + wrap(
    "Red Flags: Signs a Site May Not Be Properly Licensed",
    "<ul><li>No licence number visible in the footer or 'About' page.</li><li>Licence number doesn't appear in the GRAI public register at grai.ie.</li><li>Site claims to hold a 'GRAI casino licence' — no such licence exists yet (expected 2027–2028).</li><li>No Irish responsible gambling information or helpline details.</li><li>Domain is blocked by Irish ISPs and requires a VPN to access.</li></ul>"
)

# 27. gubbed-betting-account-ireland.html
EXPANSIONS["pages/gubbed-betting-account-ireland.html"] = wrap(
    "What Does 'Gubbed' Mean?",
    "<p>'Gubbed' is betting slang for when a bookmaker restricts your account — typically by reducing your maximum stake, limiting the markets you can bet on, or banning you from promotions. It happens because bookmakers have identified you as a profitable customer (too skilled, or exploiting offers). It is entirely legal and common practice at Irish betting sites.</p>" +
    table(["Restriction Type","What changes","Example"],
          [["Stake limits","Maximum bet reduced","Was €500, now €10 per bet"],
           ["Market restrictions","Certain sports or markets blocked","Can no longer bet on horse racing"],
           ["Promo ban","Excluded from all offers","No longer eligible for free bets"],
           ["Odds limits","Bet refused above certain odds","Can only bet at odds below 5/1"],
           ["Account closure","Account shut, balance returned","Extreme cases, usually bonus abuse"]])
) + wrap(
    "Why Accounts Get Gubbed in Ireland",
    "<ul><li><strong>Consistently winning:</strong> Bookmakers track long-term profitability. A punter winning consistently, especially on early prices or unique selections, is flagged.</li><li><strong>Matched betting / bonus abuse:</strong> Using bonuses systematically (matched betting) is detected quickly and leads to promo bans or full restrictions.</li><li><strong>Arbitrage betting:</strong> Placing arb bets across multiple bookmakers using odds discrepancies is monitored and leads to rapid account restrictions.</li><li><strong>Betting patterns:</strong> Always betting max stakes, requesting best odds guaranteed, or following tipsters are all patterns bookmakers monitor.</li></ul>"
) + wrap(
    "What To Do After Being Gubbed",
    "<ul><li><strong>Open accounts elsewhere:</strong> With 25+ GRAI-licensed operators, you can spread your activity across multiple accounts.</li><li><strong>Bet in smaller stakes:</strong> Some restricted accounts allow small wagers — a €5–€10 max stake account can still be used for small entertainment-level bets.</li><li><strong>Use exchanges:</strong> Betting exchanges (where you bet against other punters) don't restrict winners — no bookmaker to gub you.</li><li><strong>Avoid obvious patterns:</strong> On new accounts, bet across different markets, vary stake sizes, and don't always request the maximum bonus.</li></ul>"
)

# 28. self-exclusion-broke-ireland.html
EXPANSIONS["pages/self-exclusion-broke-ireland.html"] = wrap(
    "What to Do If Your Self-Exclusion Was Breached",
    "<p>If a GRAI-licensed bookmaker allowed you to open or continue using an account while you were self-excluded, this is a regulatory breach. Under the Gambling Regulation Act 2024, operators are legally required to honour self-exclusions registered with the National Gambling Exclusion Register or directly with the site.</p>" +
    table(["Self-Exclusion Type","Who operates it","Covers"],
          [["Betting site own exclusion","Individual site","That site only"],
           ["GAMSTOP (UK)","GAMSTOP CIC","All UKGC-licensed UK operators"],
           ["National Gambling Exclusion Register","GRAI","All GRAI-licensed Irish operators"]])
) + wrap(
    "Steps to Take if Your Exclusion Was Broken",
    "<ol><li><strong>Document everything:</strong> Screenshot the account activity, deposits, and any winnings while excluded.</li><li><strong>Contact the site's complaints team</strong> in writing (email), stating the dates of your self-exclusion and the dates of the breach.</li><li><strong>Request a refund of deposits</strong> made during the exclusion period — many operators will refund these when a breach is established.</li><li><strong>Escalate to the GRAI</strong> if the site does not resolve the complaint within 8 weeks — file at grai.ie. The GRAI can investigate and sanction operators for exclusion breaches.</li><li><strong>Seek support:</strong> A self-exclusion breach can be distressing. Contact the Gambling Awareness Trust: <strong>1800 753 753</strong> for free, confidential support.</li></ol>"
) + wrap(
    "Strengthening Your Self-Exclusion",
    "<ul><li>Register with the <strong>National Gambling Exclusion Register</strong> (via grai.ie) to cover all GRAI-licensed operators simultaneously.</li><li>Use <strong>GAMSTOP</strong> (gamstop.co.uk) for UK-licensed sites — most major operators hold both UKGC and GRAI licences.</li><li>Use <strong>GamBlock</strong> or <strong>Betfilter</strong> software to block gambling sites at the device or network level as an extra layer.</li><li>Notify your bank to block gambling transactions — most Irish banks offer this in their app settings.</li></ul>"
)

# 29. forgot-username-betting-site-ireland.html
EXPANSIONS["pages/forgot-username-betting-site-ireland.html"] = wrap(
    "How to Recover a Forgotten Betting Site Username",
    "<ol><li>Go to the site's <strong>login page</strong> and look for 'Forgot username?' or 'Forgot login?' link.</li><li>Enter the <strong>email address</strong> you registered with — most sites use email as your login rather than a separate username.</li><li>Check your inbox for an email with your username or a reset link.</li><li>If you no longer have access to the registered email, <strong>contact customer support</strong> with your name, date of birth, and last 4 digits of your registered payment method for identity verification.</li><li>Once verified, support can update your registered email address so you can regain access.</li></ol>"
) + wrap(
    "Common Login Issues and Fixes",
    table(["Problem","Most likely cause","Fix"],
          [["Username not recognised","Registered with different email","Try all email addresses you use"],
           ["Password incorrect","Caps lock, changed password","Use 'Forgot password' reset"],
           ["Account locked","Too many failed attempts","Wait 30 min or contact support"],
           ["Email not found","Registered under different details","Contact support with DOB and payment details"],
           ["Account closed","Site closed it, or you self-excluded","Contact support to confirm status"]])
) + wrap(
    "Preventing Login Issues in Future",
    "<ul><li>Use a <strong>password manager</strong> (1Password, Bitwarden, Apple Keychain) to store your login credentials securely.</li><li>Register with an email address you will keep long-term — avoid disposable email addresses.</li><li>Enable <strong>two-factor authentication</strong> if the site offers it — this protects your account and also gives you an alternative way to verify your identity.</li><li>Keep a note of which email you registered with for each betting site — a simple spreadsheet (without passwords) is useful.</li></ul>"
)

# 30. account-closed-betting-ireland-what-to-do.html
EXPANSIONS["pages/account-closed-betting-ireland-what-to-do.html"] = wrap(
    "Why Betting Accounts Are Closed in Ireland",
    table(["Reason","Retrievable?","Steps"],
          [["Self-exclusion (voluntary)","Yes after cooling-off","Request reopening after period"],
           ["GAMSTOP / National Register","No during exclusion","Wait for exclusion to expire"],
           ["Bonus abuse / T&C breach","Rarely","Submit formal appeal in writing"],
           ["Winning too consistently","Sometimes","Negotiate limited account"],
           ["KYC failure","Yes if docs provided","Resubmit required documents"],
           ["Fraud suspicion","Depends on outcome","Cooperate with investigation"],
           ["Inactivity (12+ months)","Yes","Log in or contact support"]])
) + wrap(
    "How to Retrieve Your Balance if Your Account Is Closed",
    "<ol><li><strong>Contact support immediately</strong> — ask for a written explanation of why the account was closed.</li><li>If a balance remains, request it be returned to your original deposit method (the site is legally required to return funds).</li><li>If the site refuses to return a balance without adequate justification, file a formal complaint to the site's complaints team.</li><li>Escalate to the <strong>GRAI at grai.ie</strong> if the complaint is unresolved after 8 weeks.</li><li>For large amounts, consider consulting a solicitor — bookmakers cannot retain your funds without a legally valid reason.</li></ol>"
) + wrap(
    "Opening a New Account After Closure",
    "<ul><li>With 25+ GRAI-licensed operators, there are plenty of alternatives to explore.</li><li>If your account was closed for T&C breach at one site, other sites' terms may prohibit opening an account if you've been excluded elsewhere — read the T&Cs carefully.</li><li>If your account was closed for self-exclusion purposes, consider whether you need a break from gambling rather than immediately opening elsewhere. The Gambling Awareness Trust (1800 753 753) can help.</li></ul>"
)

# 31. provably-fair-casino-ireland.html
EXPANSIONS["pages/provably-fair-casino-ireland.html"] = wrap(
    "What Does 'Provably Fair' Mean in Online Casino?",
    "<p>Provably fair is a cryptographic verification system used primarily in crypto casinos. Before each game round, the casino generates a hashed 'server seed' and shares it with you. After the round, you can verify that the outcome was determined by that seed — proving the casino didn't change the result after you bet. It's the crypto casino equivalent of an RNG audit by a third-party testing lab.</p>" +
    table(["Verification Method","How it works","Applies to"],
          [["Provably fair (crypto)","Hash-based seed verification by player","Crypto casinos, dice, crash games"],
           ["RNG audit (traditional)","Third party (eCOGRA, iTech Labs) tests RNG","Licensed traditional casinos"],
           ["GRAI licence","Operator required to use certified RNG","All GRAI-licensed sites"],
           ["Payout % reporting","Casino publishes RTP reports","Voluntary or required by licence"]])
) + wrap(
    "Provably Fair Casinos and Irish Law",
    "<ul><li>Most provably fair casinos are crypto-first sites that do not hold a GRAI licence — they are technically unlicensed in Ireland.</li><li>Using an unlicensed provably fair casino means you have no recourse under Irish law if there is a dispute, withdrawal issue, or fraud.</li><li>The cryptographic verification, while technically sound, doesn't substitute for regulatory consumer protections.</li><li><strong>GRAI-licensed sites</strong> use certified Random Number Generators audited by accredited labs (eCOGRA, iTech Labs, GLI) — these provide verified fairness under Irish regulatory oversight.</li></ul>"
) + wrap(
    "How to Verify a Provably Fair Game (If You Use One)",
    "<ol><li>Before the round: note the <strong>hashed server seed</strong> provided by the casino.</li><li>Place your bet — the outcome is determined by combining the server seed with your 'client seed' and a nonce (round number).</li><li>After the round: use the casino's verification tool or an independent hash checker to confirm the round's output matches the original seed.</li><li>If the hash doesn't match, the game was manipulated — this would be a serious integrity breach to report.</li></ol>"
)

# 32. can-you-bet-anonymously-ireland.html
EXPANSIONS["pages/can-you-bet-anonymously-ireland.html"] = wrap(
    "Anonymous Betting in Ireland: What's Possible",
    "<p>Under the Gambling Regulation Act 2024 and anti-money laundering (AML) regulations, GRAI-licensed betting sites must verify customer identity before processing withdrawals and for accounts above certain transaction thresholds. Full anonymity is not possible at licensed Irish sites.</p>" +
    table(["Action","ID required?","Notes"],
          [["Register an account","Email + basic details","No ID needed to register initially"],
           ["Deposit","Usually no","Card details link to identity"],
           ["Bet and play","Usually no","Until AML thresholds triggered"],
           ["Withdraw","Yes — full KYC","Passport/driving licence + proof of address"],
           ["High-volume deposits","Yes — enhanced KYC","Source of funds may be required"]])
) + wrap(
    "Why Full Anonymity Isn't Available",
    "<ul><li><strong>AML obligations:</strong> Operators must comply with the Criminal Justice (Money Laundering and Terrorist Financing) Acts. This requires customer identification for all transactions above certain thresholds.</li><li><strong>GRAI licence conditions:</strong> GRAI-licensed operators must verify customer identity as a condition of their licence — failure to do so risks licence suspension.</li><li><strong>Responsible gambling:</strong> Identity verification allows operators to enforce self-exclusions, age restrictions, and player protection measures.</li></ul>"
) + wrap(
    "Crypto Casinos and Anonymous Betting",
    "<ul><li>Some crypto casinos claim to offer 'no KYC' or anonymous betting. These sites typically do not hold a GRAI licence and operate outside Irish regulatory oversight.</li><li>Without a GRAI licence, there is no consumer protection: no complaints body, no payout guarantee, and no enforcement if the site disappears.</li><li>Using blockchain-based betting doesn't provide legal anonymity in Ireland — transactions are pseudonymous, not truly anonymous, and may be linked to your identity through exchange KYC.</li></ul>"
)

# 33. casino-payout-percentage-ireland.html
EXPANSIONS["pages/casino-payout-percentage-ireland.html"] = wrap(
    "Casino Payout Percentages: What They Mean",
    "<p>A payout percentage (also called RTP — Return to Player) tells you what percentage of all money wagered on a game or casino is returned to players on average. A 96% RTP means for every €100 wagered, the casino retains €4 and returns €96 to players — over millions of rounds. Your individual session will vary dramatically.</p>" +
    table(["Game Type","Typical RTP Range","House Edge","Notes"],
          [["Slots","92–98%","2–8%","Varies widely by title"],
           ["European Roulette","97.3%","2.7%","Fixed"],
           ["American Roulette","94.74%","5.26%","Fixed — worse than European"],
           ["Blackjack (basic strategy)","99.4–99.6%","0.4–0.6%","Strategy-dependent"],
           ["Baccarat (Banker)","98.94%","1.06%","Fixed"],
           ["Video Poker (Jacks or Better)","99.5%","0.5%","With optimal play"],
           ["Keno","65–80%","20–35%","High house edge"]])
) + wrap(
    "How to Find RTP Information in Ireland",
    "<ul><li><strong>Game info button:</strong> Most slots display RTP in the game rules or info section (the ⓘ button).</li><li><strong>Provider website:</strong> Slot developers (NetEnt, Pragmatic Play, etc.) publish official RTPs for all their titles on their websites.</li><li><strong>Casino's responsible gambling section:</strong> GRAI-licensed sites are required to provide game fairness information.</li><li><strong>Third-party databases:</strong> Sites specialising in slot information publish verified RTPs for thousands of titles.</li></ul>"
) + wrap(
    "Overall Casino Payout Percentages vs Game RTP",
    "<p>Some casinos publish an overall 'payout percentage' (e.g. 96.8%) for the whole casino, determined by independent auditors (eCOGRA, iTech Labs). This is the average across all games weighted by volume of play — it's a useful general indicator but doesn't tell you the RTP of the specific game you're playing. Always check the individual game's RTP rather than the casino's overall figure.</p>"
)

# 34. what-is-a-rollover-requirement.html
EXPANSIONS["pages/what-is-a-rollover-requirement.html"] = wrap(
    "What Is a Rollover / Wagering Requirement?",
    "<p>A rollover requirement (also called wagering requirement or playthrough) specifies how many times you must bet a bonus amount before you can withdraw it. It's the most important term attached to any casino or betting bonus in Ireland.</p>" +
    table(["Wagering","Bonus amount","Total to wager","Realistic cost (5% slots edge)"],
          [["10×","€100","€1,000","~€50 expected loss"],
           ["20×","€100","€2,000","~€100 expected loss"],
           ["30×","€100","€3,000","~€150 expected loss"],
           ["40×","€100","€4,000","~€200 expected loss"],
           ["50×","€100","€5,000","~€250 expected loss"]])
) + wrap(
    "Rollover vs Deposit+Bonus vs Bonus Only",
    "<ul><li><strong>Deposit + bonus:</strong> e.g. 30× on €100 deposit + €100 bonus = 30 × €200 = €6,000 to wager. Much more demanding.</li><li><strong>Bonus only:</strong> 30× on €100 bonus only = €3,000 to wager. This is the standard at most Irish sites.</li><li><strong>Winnings only:</strong> Rare — some sports free bets require 1× wagering of the winnings (not the stake). Very easy to meet.</li></ul>"
) + wrap(
    "Game Contributions to Wagering",
    "<p>Not all games count equally toward clearing a wagering requirement. Always check the bonus terms before playing:</p>" +
    table(["Game Type","Typical contribution"],
          [["Slots","100% (most)"],
           ["Live Roulette","10–20%"],
           ["Blackjack","10%"],
           ["Live Casino (most)","10–20%"],
           ["Video Poker","10–20%"],
           ["Sports (free bets)","100% of qualifying bet"]])
)

# 35. why-are-odds-different-on-different-sites.html
EXPANSIONS["pages/why-are-odds-different-on-different-sites.html"] = wrap(
    "Why Odds Vary Between Bookmakers",
    "<p>Bookmakers set their own prices independently, based on their own risk models, trading team judgements, and liability management. No two bookmakers will price every market identically — and the differences can be significant, especially in minor leagues, specials, and early markets.</p>" +
    table(["Factor","Impact on odds","Example"],
          [["Different margin levels","Higher margin = shorter odds","One site charges 5%, another 8%"],
           ["Different risk models","Trading team assessment varies","One prices a team higher based on form data"],
           ["Liability management","Short on one team = shorten those odds","One book has taken heavy bets on Team A"],
           ["Early market pricing","Pre-event markets less efficient","Bigger differences before markets mature"],
           ["Promotional pricing","Boosted for marketing","One site artificially lengthens a team"]])
) + wrap(
    "Using Odds Differences to Your Advantage",
    "<ul><li><strong>Always compare:</strong> Even a small odds difference compounds over many bets. Getting 11/4 instead of 5/2 on every bet represents a meaningful long-term edge.</li><li><strong>Odds comparison sites:</strong> Sites that aggregate prices across 20+ bookmakers in real time let you find the best price in seconds.</li><li><strong>Arbitrage:</strong> When odds gaps between sites guarantee a profit regardless of outcome — rare and quickly closed, but worth monitoring.</li><li><strong>Best Odds Guaranteed (BOG):</strong> Some horse racing sites offer BOG — if the SP is bigger than your early price, you're paid at SP. This exploits market movement in your favour.</li></ul>"
) + wrap(
    "How to Find the Best Odds for Any Bet",
    "<ol><li>Open an odds comparison tool and enter the event and selection.</li><li>Compare all displayed prices — the top price may be significantly higher than the worst.</li><li>Check whether the top price is a boosted promotional price (often limited to a low maximum stake).</li><li>Place the bet at the best available odds, using the account where the genuine (non-promotional) price is highest.</li></ol>"
)

# 36. how-do-free-spins-work-ireland.html
EXPANSIONS["pages/how-do-free-spins-work-ireland.html"] = wrap(
    "How Free Spins Work at Irish Online Casinos",
    table(["Feature","Typical terms","Notes"],
          [["Spin value","€0.10–€0.20 per spin","Fixed — not the same as your bet size"],
           ["Game restriction","1–3 specified slots","Usually a provider's new or featured title"],
           ["Wagering requirement","20–50× on winnings","Some no-wager free spins exist"],
           ["Maximum conversion","€5–€50","Winnings above cap are removed"],
           ["Time limit","24 hours–7 days","Expire if unused or wagering not complete"]])
) + wrap(
    "No-Wager Free Spins vs Standard Free Spins",
    "<ul><li><strong>Standard free spins:</strong> Winnings are added as bonus cash requiring 20–50× wagering before withdrawal. At 5% slots edge, the expected cost of clearing 30× wagering on €20 winnings is roughly €30 — often more than the winnings themselves.</li><li><strong>No-wager free spins:</strong> Winnings are credited as real cash, immediately withdrawable. The expected value is the spin count × spin value × RTP (e.g. 50 spins × €0.10 × 96% = €4.80 expected value).</li><li>No-wager free spins are significantly more valuable — always check the bonus terms before claiming.</li></ul>"
) + wrap(
    "In-Game Free Spins vs Bonus Free Spins",
    "<p>Bonus free spins from promotions are different from free spin features triggered inside the slot game itself (such as the Gonzo's Quest Free Falls or Starburst Re-spins). In-game free spin features have their own mechanics and multipliers set by the game developer — they are part of the game's RTP and not subject to casino bonus wagering requirements. Only the bonus free spins awarded by the casino as a promotion carry wagering terms.</p>"
)

# 37. can-you-bet-on-phone-ireland.html
EXPANSIONS["pages/can-you-bet-on-phone-ireland.html"] = wrap(
    "Mobile Betting in Ireland: What You Need to Know",
    "<p>Mobile betting is the dominant channel for Irish punters — the majority of bets placed online in Ireland are now via smartphone. All major GRAI-licensed operators offer either a dedicated mobile app (iOS and Android) or a fully responsive mobile website that works in your phone's browser.</p>" +
    table(["Option","Pros","Cons"],
          [["iOS App (App Store)","Polished UI, push notifications, biometric login","Must download, storage space"],
           ["Android App (direct download)","Same features, not restricted by Play Store","Must enable 'install from unknown sources'"],
           ["Mobile browser","No download, always up to date","May lack some app features, no push notifications"]])
) + wrap(
    "How to Download a Betting App in Ireland",
    "<ol><li><strong>iOS:</strong> Search the App Store for the site's official app, or tap the app download link on the site's mobile page. Some Irish betting apps are available directly in the App Store; others redirect to a dedicated download page.</li><li><strong>Android:</strong> Google Play Store restricts gambling apps in some regions. Download the APK file from the site's official 'Download App' page. Go to Settings → Security → Allow unknown sources (or equivalent on your device), then install the APK file.</li><li><strong>Verify it's official:</strong> Only download from the site's own domain — third-party APK sites may contain modified or malicious versions.</li></ol>"
) + wrap(
    "Mobile Betting Features to Look For",
    "<ul><li><strong>Live in-play:</strong> Real-time markets updating during the event — essential for in-play bettors.</li><li><strong>Cash out:</strong> Settle a bet early for a guaranteed return — available in the app before the event ends.</li><li><strong>Push notifications:</strong> Alerts for price boosts, early payout offers, and score updates.</li><li><strong>Biometric login:</strong> Face ID or fingerprint login for fast access — available on most major betting apps.</li><li><strong>Responsible gambling tools:</strong> Deposit limits, session time reminders, and self-exclusion access — all accessible within the app under 'My Account' or 'Responsible Gambling'.</li></ul>"
)

# 38. can-foreigners-bet-in-ireland.html
EXPANSIONS["pages/can-foreigners-bet-in-ireland.html"] = wrap(
    "Can Non-Irish Residents Bet in Ireland?",
    "<p>Yes — GRAI-licensed betting sites are open to any adult resident of Ireland, regardless of nationality. As long as you are physically located in Ireland and aged 18 or over, you can register and bet. You will need to pass the standard Know Your Customer (KYC) identity verification, which accepts a wide range of international identity documents.</p>" +
    table(["Document Type","Accepted for Irish KYC?","Notes"],
          [["Irish passport","Yes","Strongest form of ID"],
           ["Irish driving licence","Yes","Widely accepted"],
           ["EU national identity card","Yes","From any EU/EEA country"],
           ["Non-EU passport","Yes","May require additional proof of address"],
           ["Non-EU driving licence","Varies","Not always accepted — check with the site"]])
) + wrap(
    "Address Verification for Non-Irish Nationals",
    "<ul><li>You must provide a proof of address in Ireland (not your home country) — a utility bill, bank statement, or lease agreement showing your Irish address, dated within 3 months.</li><li>Irish Revenue (PPS number) is not required for betting — but some sites may request additional documentation for high-volume accounts.</li><li>If you are a student or short-term visitor, some sites may limit withdrawals until full KYC is completed with a fixed Irish address.</li></ul>"
) + wrap(
    "Currency and Payment Options for Non-Irish Residents",
    "<ul><li>Irish betting sites primarily operate in <strong>euros (€)</strong>. If your bank card is in another currency, your bank will convert at their exchange rate — check for foreign transaction fees.</li><li>Revolut and Wise (TransferWise) are popular options for non-EU visitors betting in Ireland — both offer euro accounts with minimal conversion fees.</li><li>PayPal is widely accepted and handles currency conversion automatically.</li></ul>"
)

# 39. can-you-bet-with-revolut-ireland.html
EXPANSIONS["pages/can-you-bet-with-revolut-ireland.html"] = wrap(
    "Using Revolut for Betting in Ireland",
    "<p>Revolut is one of the most popular payment methods for Irish betting site deposits and withdrawals. As a licensed e-money institution, Revolut is accepted at most major GRAI-licensed betting sites for instant deposits and fast withdrawals.</p>" +
    table(["Feature","Details"],
          [["Deposit speed","Instant"],
           ["Withdrawal speed","Instant to 24 hours (depending on site)"],
           ["Currencies","Primarily EUR for Irish accounts"],
           ["Gambling block","Available in Revolut app → Payments → Gambling"],
           ["Bonus exclusion","Some sites exclude Revolut deposits from welcome bonus"]])
) + wrap(
    "How to Enable and Disable the Revolut Gambling Block",
    "<ol><li>Open the Revolut app and go to <strong>Hub → Payments</strong> (or the grid/controls icon).</li><li>Tap <strong>Gambling</strong> (or find it under payment controls).</li><li>Toggle the gambling block on or off. When on, all gambling-category transactions are declined.</li><li>To disable: toggle off, confirm with biometrics or PIN. There may be a short cooling-off period before it deactivates.</li></ol>"
) + wrap(
    "Revolut vs Debit Card vs PayPal for Betting",
    table(["Feature","Revolut","Debit Card","PayPal"],
          [["Deposit speed","Instant","Instant","Instant"],
           ["Withdrawal speed","Instant–24h","1–5 days","1–3 days"],
           ["Welcome bonus eligibility","Sometimes excluded","Usually eligible","Sometimes excluded"],
           ["Gambling block option","Yes (in app)","Via bank app/branch","No"],
           ["Available on most sites","Yes","Yes","Most major sites"]])
)

# 40. world-cup-2026-european-teams-betting.html
EXPANSIONS["pages/world-cup-2026-european-teams-betting.html"] = wrap(
    "European Teams at the 2026 World Cup",
    "<p>UEFA receives 16 qualifying spots at the expanded 48-team 2026 World Cup, up from 13 in 2022. This means more European nations will compete, increasing the depth of competition in the European section of the draw. The host nations (USA, Canada, Mexico) qualify automatically; the remaining 45 spots are distributed across confederations.</p>" +
    table(["Confederation","Allocated spots (2026)","Notes"],
          [["UEFA (Europe)","16","Up from 13 in 2022"],
           ["CONMEBOL (South America)","6","Brazil, Argentina key markets"],
           ["CAF (Africa)","9","Up from 5 in 2022"],
           ["AFC (Asia)","8+1 playoff","Up from 4-5 in 2022"],
           ["CONCACAF (N/C America)","6+1 host (3 hosts)","USA, Canada, Mexico as hosts"],
           ["OFC (Oceania)","1+1 playoff","First guaranteed spot"]])
) + wrap(
    "Top European Contenders for 2026",
    "<ul><li><strong>Traditional heavyweights:</strong> France, Germany, Spain, England, Portugal — all likely to be near the top of outright markets. Post-2022, France and Brazil are historically the most backed nations.</li><li><strong>Dark horses:</strong> Netherlands, Belgium (aging squad by 2026), Croatia, and rising nations like Austria and Scotland (if they qualify) may offer outright value.</li><li><strong>Republic of Ireland:</strong> Ireland are in UEFA qualifying. Their outright odds for tournament glory are long (100/1+) — focus on group stage betting if they qualify.</li></ul>"
) + wrap(
    "Betting Strategy for European Nations at World Cup 2026",
    "<ul><li><strong>Ante-post value:</strong> Place early outright bets on European nations before the draw — the draw can dramatically change a team's odds, and early prices are often generous.</li><li><strong>Group stage betting:</strong> With 48 teams in 16 groups of 3, the top 2 from each group plus 8 best third-placed qualify — group stage exits are less likely for major European nations.</li><li><strong>Each-way tournament outright:</strong> Backing a European nation to reach the final (each-way, top 2) can offer better value than backing them to win outright.</li></ul>"
)

# Pages 41-50
# 41. how-we-review.html
EXPANSIONS["pages/how-we-review.html"] = wrap(
    "Our Review Methodology",
    "<p>CraicBet's reviews are written by editors who test the products hands-on, using real accounts. No operator pays for a review placement or influences our ratings. Our rating criteria are consistent across all reviewed sites, and we update reviews when products change significantly.</p>" +
    table(["Review Category","Weight","What we check"],
          [["Licence and regulation","20%","GRAI, UKGC, and other licences; compliance history"],
           ["Odds and markets","20%","Market depth, sports coverage, in-play quality"],
           ["Bonuses and promotions","20%","Wagering requirements, real value, accessibility"],
           ["Payment methods","15%","Deposit/withdrawal speed, fees, Irish options"],
           ["User experience","15%","App quality, desktop, navigation, customer service"],
           ["Responsible gambling","10%","Self-exclusion tools, limit settings, support info"]])
) + wrap(
    "How We Score Betting Sites",
    "<ul><li>Sites are scored on a 1–10 scale across all review categories.</li><li>A GRAI (or UKGC) licence is a minimum requirement — unlicensed sites are not reviewed as recommended options.</li><li>We test actual deposit and withdrawal processes, place test bets across different markets, and contact customer support.</li><li>Reviews are updated quarterly or whenever a significant product change occurs (new licence, changes to bonus terms, etc.).</li></ul>"
) + wrap(
    "Commercial Relationships and Independence",
    "<p>CraicBet earns affiliate revenue when you click through to a recommended site and register. This does not affect our ratings or editorial opinions. Sites that offer us higher affiliate commissions are not rated more favourably. The rated scores and editorial commentary are determined independently by our review team. Our partner site is disclosed with a 'Partner' label wherever it appears. 18+ | Gamble responsibly.</p>"
)

# 42. editorial-guidelines.html
EXPANSIONS["pages/editorial-guidelines.html"] = wrap(
    "CraicBet Editorial Standards",
    table(["Standard","Our Commitment"],
          [["Accuracy","All facts verified against primary sources before publication"],
           ["Independence","Commercial relationships disclosed; never influence ratings"],
           ["Recency","Reviews updated quarterly; major changes updated within 48 hours"],
           ["Responsible gambling","18+ and RG messaging on all pages with CTAs"],
           ["Corrections","Errors corrected promptly with a dated correction note"],
           ["GRAI compliance","Licence claims always verified; casino licence claims clearly corrected"]])
) + wrap(
    "Who Writes CraicBet Content",
    "<ul><li>Content is written and edited by sports betting and casino specialists with experience in the Irish market.</li><li>All writers are adults based in Ireland or with direct knowledge of the Irish betting market.</li><li>No content is generated and published without human review — AI assistance may be used for research, but all published content is edited and approved by a human editor.</li><li>Author pages disclose relevant experience and are linked from each article.</li></ul>"
) + wrap(
    "Responsible Gambling Commitment",
    "<p>CraicBet is committed to promoting responsible gambling in Ireland. All pages with calls to action include an 18+ reminder and a link to the Gambling Awareness Trust helpline (<strong>1800 753 753</strong>, gamblingcare.ie). We do not use advertising techniques designed to target people who have self-excluded, and we do not publish content designed to appeal to under-18s. If you believe you or someone you know has a gambling problem, please contact the Gambling Awareness Trust.</p>"
)

# 43. relax-gaming-casinos-ireland.html
EXPANSIONS["pages/relax-gaming-casinos-ireland.html"] = wrap(
    "Relax Gaming: Top Games Available in Ireland",
    table(["Game","RTP","Volatility","Key Feature"],
          [["Money Train 4","96.4%","Very High","Money Cart bonus, multiplier symbols"],
           ["Money Train 3","96.1%","Very High","Persistent multipliers, respins"],
           ["Money Train 2","96.4%","Very High","Starter, Payer, Collector symbols"],
           ["Snake Arena","96.5%","Medium–High","Snake grid mechanic"],
           ["Hypernova Megaways","96.5%","High","Megaways, up to 100,000× max win"]])
) + wrap(
    "What Makes Relax Gaming Distinct",
    "<ul><li><strong>Money Train series:</strong> The Money Train franchise (1, 2, 3, and 4) has become one of the most popular high-volatility slot families in the Irish market. The 'Money Cart' bonus round with persistent multiplier symbols drives the variance and the large max wins (up to 50,000–100,000×).</li><li><strong>Aggregation platform:</strong> Relax Gaming also operates as an aggregation platform, distributing content from smaller studios — so a 'powered by Relax Gaming' casino may offer titles from partner studios alongside Relax's own games.</li><li><strong>RTP range:</strong> Relax Gaming slots typically have RTPs of 95–97%, competitive with the broader market. High-volatility titles may have lower hit frequencies to compensate for large max wins.</li></ul>"
) + wrap(
    "High-Volatility Slots: What to Expect",
    "<ul><li>High-volatility slots (like the Money Train series) can go many spins between significant wins — budget accordingly.</li><li>The advertised max win (e.g. 50,000×) is achievable but extremely rare — it should not be your base expectation.</li><li>Set a session budget before playing high-volatility slots and stick to it. Responsible gambling tools (deposit limits, session limits) are available at all GRAI-licensed sites.</li><li><strong>18+ | Gambling Awareness Trust: 1800 753 753</strong></li></ul>"
)

# 44. betting-on-draws-football.html
EXPANSIONS["pages/betting-on-draws-football.html"] = wrap(
    "Draw Betting in Football: Key Stats",
    "<p>Football draw rates vary significantly by league and match type. Understanding draw frequency is essential for draw betting value.</p>" +
    table(["League","Draw rate (approx.)","Notes"],
          [["Serie A (Italy)","26–28%","Historically highest draw rate"],
           ["Bundesliga","23–25%","Lower than Italian football"],
           ["Premier League","24–26%","Varies by season"],
           ["La Liga","25–27%","Mid-range"],
           ["Ligue 1","25–27%","Mid-range"],
           ["League of Ireland Premier","22–26%","Varies by season"],
           ["Champions League","22–24%","Knockout stages have no draws"]])
) + wrap(
    "When to Bet on a Draw",
    "<ul><li><strong>Evenly matched teams:</strong> When two similar-quality teams meet with no clear edge, draw probability is higher than bookmakers often price in.</li><li><strong>Defensive setups:</strong> When a weaker team travels to a stronger side and sets up to defend, the draw is a viable outcome — betting the double chance (draw + weaker team win) can offer value.</li><li><strong>Cautious derby matches:</strong> Local derbies often see extra caution from both sides — draw rates in derby fixtures can be 5–10% above the league average.</li><li><strong>Late-season low-stakes matches:</strong> When one side has nothing to play for and the other needs a draw to secure safety or a trophy, tactical draws are more common.</li></ul>"
) + wrap(
    "Draw Betting Markets Available",
    table(["Market","Description","Example odds"],
          [["Match draw (1X2)","90-minute result is a draw","Typically 3/1 – 4/1"],
           ["Double chance (X2)","Draw or away team wins","0/1 – 1/1"],
           ["Draw no bet","Bet refunded if draw","Shorter than outright win"],
           ["Half-time draw","Half-time result is 0-0 or X-X","Often 7/4 – 5/2"],
           ["Both half-time and full-time draw","HT and FT both draws","6/1 – 12/1"]])
)

# 45. world-cup-2026-dark-horse-betting.html
EXPANSIONS["pages/world-cup-2026-dark-horse-betting.html"] = wrap(
    "World Cup 2026 Dark Horse Contenders",
    "<p>A dark horse is a nation that is underrated by the market but has genuine potential to outperform their odds. With 48 teams in 2026 (up from 32 in 2022), the expanded format creates more opportunity for smaller nations to progress and for genuine upsets in the knockout rounds.</p>" +
    table(["Nation","Typical pre-tournament odds","Why a dark horse"],
          [["USA (host)","30/1–50/1","Home advantage, improving player base, MLS growth"],
           ["Netherlands","15/1–25/1","Strong squad cycle, Eredivisie talent pipeline"],
           ["Colombia","25/1–50/1","Strong CONMEBOL record, in-form attackers"],
           ["Mexico (host)","30/1–60/1","Host advantage, historically reaches Round of 16"],
           ["Senegal","50/1–100/1","African champions, strong collective unit"],
           ["Japan","40/1–80/1","Strong Asian form, upset Germany and Spain in 2022"]])
) + wrap(
    "Betting Strategy for Dark Horses",
    "<ul><li><strong>Ante-post early:</strong> Dark horse prices are longest before the draw — once a favourable group is confirmed, odds shorten significantly. Buy early to get the best price.</li><li><strong>Each-way tournament outright:</strong> An each-way bet (top 4) on a dark horse at 50/1 returns at 1/4 odds if they reach the semi-finals — substantial return at much higher probability than winning the tournament.</li><li><strong>Group stage first:</strong> With 16 groups of 3 (in 2026 format), top 2 from each group qualify automatically. Bet on a dark horse to top their group before the draw confirms their opponents.</li></ul>"
) + wrap(
    "2022 Upsets That Showed Dark Horse Value",
    "<ul><li>Morocco reached the semi-finals as a 500/1 ante-post outsider — the first African nation to do so.</li><li>Japan beat Germany and Spain in the group stage at 50/1+ odds per match.</li><li>Saudi Arabia beat eventual finalists Argentina 2-1 in the group stage.</li><li>These upsets demonstrate that in a one-game knockout format, any nation can beat another on a given day — dark horse value at World Cup level is real.</li></ul>"
)

# 46. new-years-day-betting-ireland.html - already in batch 3? Check by looking at file size after expansion
# Let's do an alternative: virtual-sports-betting-ireland.html
EXPANSIONS["pages/virtual-sports-betting-ireland.html"] = wrap(
    "Virtual Sports Betting in Ireland",
    "<p>Virtual sports are computer-generated simulations of sports events (football, horse racing, greyhounds, tennis, basketball) that run 24/7 with results determined by a certified Random Number Generator. They are available at most Irish betting sites and offer a faster alternative to real sports, with events typically every 2–5 minutes.</p>" +
    table(["Virtual Sport","Event frequency","Typical markets"],
          [["Virtual Football","Every 5 min","Match result, goals, scorer"],
           ["Virtual Horse Racing","Every 3 min","Win/place, forecast, tricast"],
           ["Virtual Greyhounds","Every 3 min","Win/place, forecast, distances"],
           ["Virtual Tennis","Every 5 min","Match winner, set betting"],
           ["Virtual Basketball","Every 5 min","Winner, total points, handicap"]])
) + wrap(
    "How Virtual Sports Outcomes Are Determined",
    "<p>Outcomes are generated by a certified RNG, typically audited by an independent testing lab (eCOGRA, iTech Labs, or similar). The RNG selects outcomes with probabilities broadly reflective of the underlying simulated sport — a 2/1 favourite in virtual horse racing has a higher probability of winning than a 10/1 outsider, though the exact probability distribution is set by the software provider, not the bookmaker.</p><ul><li>Virtual events run to a set schedule, independent of any real sporting activity.</li><li>Unlike real sports, there is no form, weather, injury, or fatigue — all outcomes are purely probability-driven.</li><li>RTP for virtual sports is typically 90–95% — lower than slots, higher than many casino games.</li></ul>"
) + wrap(
    "Virtual Sports vs In-Play Real Sports Betting",
    table(["Feature","Virtual Sports","In-Play Real Sports"],
          [["Availability","24/7","Only during live events"],
           ["Event frequency","Every 2–5 minutes","Depends on fixture schedule"],
           ["Outcome basis","RNG (certified random)","Real performance"],
           ["In-play analysis","Not possible","Yes — form, stats, momentum"],
           ["Suspension risk","None","Markets suspended regularly"],
           ["Responsible gambling note","Faster events increase risk","More breaks between events"]])
)

# 47. crypto-betting-ireland-legal.html
EXPANSIONS["pages/crypto-betting-ireland-legal.html"] = wrap(
    "Is Crypto Betting Legal in Ireland?",
    "<p>Betting with cryptocurrency is not specifically regulated or prohibited under Irish law. The Gambling Regulation Act 2024 and GRAI licensing requirements apply to operators, not the payment method used. In practice, most GRAI-licensed operators do not accept crypto deposits — they use traditional payment processors. Dedicated crypto betting sites typically operate without an Irish GRAI licence.</p>" +
    table(["Situation","Legal status","Consumer protection"],
          [["GRAI-licensed site accepting crypto","Legal","Full GRAI protection"],
           ["Unlicensed crypto-only site","Grey area — not regulated","No Irish protection"],
           ["Using crypto on blocked sites via VPN","Against site T&Cs","No protection, account risk"]])
) + wrap(
    "Tax on Crypto Gambling Winnings in Ireland",
    "<ul><li><strong>Gambling winnings themselves are not taxed</strong> in Ireland for recreational punters — this applies whether you bet in euros or crypto.</li><li><strong>Capital Gains Tax (CGT) may apply</strong> to the crypto asset itself: if you deposit Bitcoin worth €1,000 and withdraw Bitcoin worth €1,500, the €500 gain on the Bitcoin is a CGT event taxable at 33%.</li><li>Revenue requires Irish residents to report and pay CGT on all cryptocurrency gains, including those from gambling transactions.</li><li>Keep records of crypto values at time of deposit and withdrawal to calculate any CGT liability.</li></ul>"
) + wrap(
    "Crypto vs Traditional Payments for Irish Betting",
    table(["Feature","Crypto","Visa/Revolut"],
          [["GRAI-licensed site availability","Rare","Universal"],
           ["Deposit speed","Varies (blockchain confirmation)","Instant"],
           ["Withdrawal speed","Varies","Instant–5 days"],
           ["KYC requirement","Varies by site","Always at GRAI sites"],
           ["Consumer protection","Minimal if unlicensed","Full GRAI protection"],
           ["Tax implications","CGT on crypto gains","No CGT on EUR gains"]])
)

# 48. in-play-betting-ireland-rules.html
EXPANSIONS["pages/in-play-betting-ireland-rules.html"] = wrap(
    "In-Play Betting Rules in Ireland",
    "<p>In-play (live) betting rules govern what happens to your bet if events are disrupted, abandoned, or changed after you've placed your bet during the event. These rules are set by each individual bookmaker — always check the specific site's rules for the sport you're betting on.</p>" +
    table(["Situation","Typical rule","Example"],
          [["Match abandoned <55 mins played","Void — stakes returned","Rain stops play at 50 mins: bet void"],
           ["Match abandoned >55 mins played","Result stands (football)","Game completed 60 mins: 1-0 stands"],
           ["Player retires (tennis)","Bet void (usually)","Player injured at 1-0: bet void"],
           ["Penalty awarded, then overturned by VAR","Settled on final result","Penalty overturned: goalscorer bet void"],
           ["Player substituted before scoring","Anytime scorer: still active","Sub off at 80 mins: bet still open"],
           ["Match suspended and resumed within 24h","Usually counts","Weather delay: rules may vary by site"]])
) + wrap(
    "In-Play Market Suspension: What It Means",
    "<ul><li>In-play markets are suspended when a significant event occurs that the trading team needs to assess (e.g. red card, goal, injury stoppage). During suspension, no bets can be placed.</li><li>If you clicked 'place bet' just before a suspension and your bet shows as 'pending', most sites will not accept it — it will be returned to your balance.</li><li>Bet acceptance during in-play is not guaranteed — some sites reserve the right to refuse any in-play bet without explanation.</li></ul>"
) + wrap(
    "Cash Out Rules During In-Play Events",
    "<ul><li><strong>Cash out availability</strong> varies by sport, event, and site — it may be suspended during goal kicks, corners, or VAR checks.</li><li><strong>Partial cash out</strong> allows you to secure part of your return while leaving the rest to run.</li><li><strong>Auto cash out</strong> (available on some sites) triggers a cash out automatically at a target price you set in advance.</li><li>Cash out value is calculated by the bookmaker in real time — it reflects the current probability of your bet winning, minus the bookmaker's margin. The offered value is usually slightly below the fair market value of your bet position.</li></ul>"
)

# 49. paypal-betting-sites-ireland.html
EXPANSIONS["pages/paypal-betting-sites-ireland.html"] = wrap(
    "PayPal for Betting in Ireland: Pros and Cons",
    table(["Feature","Details"],
          [["Deposit speed","Instant"],
           ["Withdrawal speed","1–3 business days (to PayPal balance)"],
           ["Minimum deposit","Usually €5–€10"],
           ["Fees","Free (PayPal may charge currency conversion)"],
           ["Bonus eligibility","Sometimes excluded from welcome offers"],
           ["Available at","Most major GRAI-licensed sites"]])
) + wrap(
    "PayPal vs Revolut vs Bank Transfer for Irish Betting",
    table(["Feature","PayPal","Revolut","Bank Transfer"],
          [["Deposit speed","Instant","Instant","1–3 days"],
           ["Withdrawal speed","1–3 days","Instant–24h","1–3 days"],
           ["Welcome bonus eligibility","Sometimes excluded","Sometimes excluded","Usually eligible"],
           ["Gambling block","No","Yes (in app)","Via bank settings"],
           ["Available sites","Most major sites","Most major sites","All sites"]])
) + wrap(
    "How to Link PayPal to an Irish Betting Account",
    "<ol><li>Register a PayPal account at paypal.com (verify your email and link an Irish bank account or card).</li><li>Log into your betting account and navigate to Deposit → PayPal.</li><li>You'll be redirected to the PayPal login to authorise the payment — you do not share your bank details with the betting site.</li><li>Select your funding source within PayPal (bank account, card, or PayPal balance) and confirm the deposit.</li><li>For withdrawals, the same process in reverse: Withdraw → PayPal → enter amount → confirm.</li></ol>"
)

# 50. no-deposit-free-bet-ireland.html
EXPANSIONS["pages/no-deposit-free-bet-ireland.html"] = wrap(
    "No Deposit Free Bets in Ireland: What to Expect",
    "<p>A no-deposit free bet is credited to your account without you having to make a deposit — typically awarded just for registering. They are rare at GRAI-licensed sites and usually very small (€5–€10), with restrictive terms (SNR, minimum odds, 1× wagering on winnings).</p>" +
    table(["Term","Typical value","Notes"],
          [["No deposit free bet","€5–€10","Rare; usually for registration"],
           ["Minimum odds","1/2 or Evens","Bet must be placed at this minimum"],
           ["SNR (Stake not returned)","Applies","Winnings only, not the bet amount"],
           ["Wagering requirement","1× winnings typically","Must bet winnings once before withdrawal"],
           ["Expiry","24–72 hours","Very short — use immediately"]])
) + wrap(
    "No Deposit Free Bet vs Welcome Deposit Bonus",
    "<ul><li><strong>No deposit free bet:</strong> No money required. £5–€10 free bet. Expected value is typically €2–€5 (stake not returned, odds constraint). Very limited risk of losing anything.</li><li><strong>Welcome deposit bonus:</strong> Requires a deposit of €10–€20+. Bonus may be €50–€500. Higher potential value but requires wagering a multiple of the bonus before withdrawal. Higher risk.</li><li>For punters who want to try a site with zero financial risk, no-deposit offers are ideal — but don't expect significant winnings from a €5 free bet with SNR terms.</li></ul>"
) + wrap(
    "How to Find Genuine No Deposit Betting Offers in Ireland",
    "<ul><li>No deposit offers are typically promoted on the site's homepage or promotions page when available — they're time-limited and appear/disappear frequently.</li><li>Check comparison sites that aggregate current bonus offers for Irish players.</li><li>Read the full terms before registering — confirm the offer is genuine, the wagering requirements are clear, and the minimum odds are achievable.</li><li><strong>18+ only. Terms and conditions apply. Gamble responsibly. Gambling Awareness Trust: 1800 753 753.</strong></li></ul>"
)

# Now process all pages
pages_dir = "/home/claude/craicbet"
processed = []
failed = []

for filepath, new_content in EXPANSIONS.items():
    full_path = os.path.join(pages_dir, filepath)
    if not os.path.exists(full_path):
        failed.append(f"NOT FOUND: {filepath}")
        continue

    with open(full_path, 'r', encoding='utf-8') as f:
        html = f.read()

    original_size = len(html)

    # Find insertion point
    if '<div class="editorial-box"' in html:
        insert_before = '<div class="editorial-box"'
    elif '<div class="faq-item"' in html:
        insert_before = '<div class="faq-item"'
    else:
        # Try to insert before closing main tag
        if '</main>' in html:
            insert_before = '</main>'
        elif '</article>' in html:
            insert_before = '</article>'
        else:
            failed.append(f"NO INSERTION POINT: {filepath}")
            continue

    idx = html.find(insert_before)
    if idx == -1:
        failed.append(f"INSERT POINT NOT FOUND: {filepath}")
        continue

    new_html = html[:idx] + new_content + html[idx:]

    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(new_html)

    new_size = len(new_html)
    processed.append(f"{filepath}: {original_size} → {new_size} bytes (+{new_size-original_size})")

print(f"\nProcessed: {len(processed)}")
print(f"Failed: {len(failed)}")
print("\nProcessed:")
for p in processed:
    print(f"  {p}")
if failed:
    print("\nFailed:")
    for f in failed:
        print(f"  {f}")
