#!/usr/bin/env python3
import re

with open('pages/what-does-dnb-mean-betting.html', 'r') as f:
    shell = f.read()

pages = [
    {
        'slug': 'anytime-goalscorer-ireland.html',
        'title': 'Anytime Goalscorer Betting Ireland: How It Works',
        'desc': 'Anytime goalscorer betting Ireland explained: rules, settlement, how it differs from first scorer, and tips for using it in accumulators.',
        'h1': 'Anytime Goalscorer Betting Ireland: How It Works',
        'body': '''<p>Anytime goalscorer betting means backing a player to score at any point during the match — first, second, last, it doesn't matter. As long as they score, your bet wins. It's one of the most popular football markets for Irish punters because the odds are more achievable than first goalscorer while still offering good value.</p>

<h2>Anytime Goalscorer vs First Goalscorer: What Is the Difference</h2>
<p>The key difference is timing. First goalscorer requires your player to score the opening goal of the match — if they score second or third, your bet loses. Anytime goalscorer only requires one goal at any point.</p>
<table style="width:100%;border-collapse:collapse;margin:16px 0;font-size:0.95rem">
<tr style="background:#1e3a28"><th style="padding:9px;border:1px solid #2d5a3d;text-align:left;color:#cde6d4">Market</th><th style="padding:9px;border:1px solid #2d5a3d;text-align:left;color:#cde6d4">When It Wins</th><th style="padding:9px;border:1px solid #2d5a3d;text-align:left;color:#cde6d4">Typical Odds (top striker)</th><th style="padding:9px;border:1px solid #2d5a3d;text-align:left;color:#cde6d4">Void Rule</th></tr>
<tr><td style="padding:8px;border:1px solid #2d5a3d">Anytime Goalscorer</td><td style="padding:8px;border:1px solid #2d5a3d">Player scores any goal</td><td style="padding:8px;border:1px solid #2d5a3d">Evens–2/1</td><td style="padding:8px;border:1px solid #2d5a3d">Player doesn't play</td></tr>
<tr style="background:#0d1f14"><td style="padding:8px;border:1px solid #2d5a3d">First Goalscorer</td><td style="padding:8px;border:1px solid #2d5a3d">Player scores the 1st goal</td><td style="padding:8px;border:1px solid #2d5a3d">3/1–6/1</td><td style="padding:8px;border:1px solid #2d5a3d">Player doesn't play or scores 2nd+</td></tr>
<tr><td style="padding:8px;border:1px solid #2d5a3d">Last Goalscorer</td><td style="padding:8px;border:1px solid #2d5a3d">Player scores the final goal</td><td style="padding:8px;border:1px solid #2d5a3d">3/1–8/1</td><td style="padding:8px;border:1px solid #2d5a3d">Player doesn't play</td></tr>
<tr style="background:#0d1f14"><td style="padding:8px;border:1px solid #2d5a3d">To Score 2+ Goals</td><td style="padding:8px;border:1px solid #2d5a3d">Player scores 2 or more</td><td style="padding:8px;border:1px solid #2d5a3d">5/1–12/1</td><td style="padding:8px;border:1px solid #2d5a3d">Player doesn't play</td></tr>
</table>

<h2>Anytime Goalscorer Settlement Rules Ireland</h2>
<p>Standard settlement rules across Irish-licensed betting sites:</p>
<ul>
<li><strong>Void if player doesn't participate</strong> — if your selection doesn't play (not even as a substitute), the bet is void and your stake is returned.</li>
<li><strong>Own goals don't count</strong> — an own goal does not count as a goalscorer market winner for any player.</li>
<li><strong>Extra time and penalties</strong> — goals in extra time usually count; penalties in a shootout usually do not (check site T&Cs).</li>
<li><strong>Shirt-off rule</strong> — some sites void first/last scorer bets if the player removes their shirt after scoring, but this rarely affects anytime goalscorer markets.</li>
</ul>

<h2>How to Use Anytime Goalscorer in Accumulators Ireland</h2>
<p>Anytime goalscorer bets combine well in accumulators because the odds are high enough to build an attractive payout without the near-impossibility of picking first scorers across multiple matches. A four-fold anytime acca with four strikers at Evens each returns 15/1 on a €10 stake — €150 if all four score.</p>
<p>Strategy tips: target strikers in home games against weaker defences; check team news before kick-off (a player who starts on the bench has much lower odds of scoring); use stat sites to check shots per game and big-chance conversion rates before picking.</p>'''
    },
    {
        'slug': 'handicap-betting-football-ireland.html',
        'title': 'Handicap Betting Football Ireland: How It Works',
        'desc': 'Handicap betting in football explained for Ireland: European handicap vs Asian handicap, +1/-1 examples, 3-way handicap, and when to use each.',
        'h1': 'Handicap Betting Football Ireland: How It Works',
        'body': '''<p>Handicap betting levels the playing field between mismatched teams. The bookmaker gives one side a virtual head start (or deficit) before kick-off, making the contest more even and offering better odds than a straightforward match result market.</p>

<h2>European Handicap vs Asian Handicap: What Is the Difference</h2>
<p>There are two main types of football handicap available on Irish betting sites, and they settle differently.</p>
<table style="width:100%;border-collapse:collapse;margin:16px 0;font-size:0.95rem">
<tr style="background:#1e3a28"><th style="padding:9px;border:1px solid #2d5a3d;text-align:left;color:#cde6d4">Type</th><th style="padding:9px;border:1px solid #2d5a3d;text-align:left;color:#cde6d4">Lines Offered</th><th style="padding:9px;border:1px solid #2d5a3d;text-align:left;color:#cde6d4">Draw Option</th><th style="padding:9px;border:1px solid #2d5a3d;text-align:left;color:#cde6d4">Void Possible</th></tr>
<tr><td style="padding:8px;border:1px solid #2d5a3d">European (3-way)</td><td style="padding:8px;border:1px solid #2d5a3d">Whole numbers (−1, +1, −2)</td><td style="padding:8px;border:1px solid #2d5a3d">Yes (handicap draw)</td><td style="padding:8px;border:1px solid #2d5a3d">No</td></tr>
<tr style="background:#0d1f14"><td style="padding:8px;border:1px solid #2d5a3d">Asian (2-way)</td><td style="padding:8px;border:1px solid #2d5a3d">Quarter lines (−0.5, −0.75, −1.5)</td><td style="padding:8px;border:1px solid #2d5a3d">No (eliminates draw)</td><td style="padding:8px;border:1px solid #2d5a3d">Half-stake (on 0 or .5 lines)</td></tr>
<tr><td style="padding:8px;border:1px solid #2d5a3d">Draw No Bet</td><td style="padding:8px;border:1px solid #2d5a3d">0 handicap (level)</td><td style="padding:8px;border:1px solid #2d5a3d">Void/refund on draw</td><td style="padding:8px;border:1px solid #2d5a3d">Yes (on draw)</td></tr>
</table>

<h2>How Handicap +1 and −1 Work in Football Ireland</h2>
<p><strong>Team A −1</strong>: Team A starts with a virtual one-goal deficit. They must win by two or more goals for your bet to win. If they win by exactly one goal, the handicap result is a draw (and your bet loses on the 2-way market, or the handicap draw wins on the 3-way market).</p>
<p><strong>Team B +1</strong>: Team B starts with a virtual one-goal lead. Your bet wins if Team B wins, draws, or loses by exactly one goal. It loses only if Team B loses by two or more goals.</p>

<h2>When to Use Handicap Betting in Football Ireland</h2>
<p>Handicap betting is most useful when the match odds on the favourite are too short to offer value. For example, if a strong club is priced at 1/4 to win a home game, backing them on the −1 or −1.5 Asian handicap typically offers 10/11 or Evens — a much better return if you believe they'll win comfortably. It's particularly popular for Premier League, Champions League, and La Liga matches followed by Irish punters.</p>'''
    },
    {
        'slug': 'wincast-betting-ireland.html',
        'title': 'Wincast Betting Ireland: What Is a Wincast',
        'desc': 'Wincast betting Ireland explained: how it works, settlement rules, odds calculation, and how it differs from scorecast. 18+.',
        'h1': 'Wincast Betting Ireland: What Is a Wincast',
        'body': '''<p>A wincast is a combined bet on a team to win a match and a specific player to score during that match. Both parts must come true for the bet to win. It's simpler than a scorecast (which requires a correct score) but still delivers boosted odds compared to betting on each outcome separately.</p>

<h2>How Wincast Odds Are Calculated in Ireland</h2>
<p>Bookmakers calculate the wincast price by multiplying the implied probabilities of the team winning and the player scoring, then converting back to odds. The resulting price is usually slightly lower than the theoretical combination due to the bookmaker margin, but still significantly higher than backing either selection alone.</p>
<table style="width:100%;border-collapse:collapse;margin:16px 0;font-size:0.95rem">
<tr style="background:#1e3a28"><th style="padding:9px;border:1px solid #2d5a3d;text-align:left;color:#cde6d4">Bet Type</th><th style="padding:9px;border:1px solid #2d5a3d;text-align:left;color:#cde6d4">Requirements to Win</th><th style="padding:9px;border:1px solid #2d5a3d;text-align:left;color:#cde6d4">Typical Odds (example)</th></tr>
<tr><td style="padding:8px;border:1px solid #2d5a3d">Match Result</td><td style="padding:8px;border:1px solid #2d5a3d">Team wins</td><td style="padding:8px;border:1px solid #2d5a3d">4/5</td></tr>
<tr style="background:#0d1f14"><td style="padding:8px;border:1px solid #2d5a3d">Anytime Goalscorer</td><td style="padding:8px;border:1px solid #2d5a3d">Player scores</td><td style="padding:8px;border:1px solid #2d5a3d">6/4</td></tr>
<tr><td style="padding:8px;border:1px solid #2d5a3d">Wincast</td><td style="padding:8px;border:1px solid #2d5a3d">Team wins + player scores</td><td style="padding:8px;border:1px solid #2d5a3d">11/4</td></tr>
<tr style="background:#0d1f14"><td style="padding:8px;border:1px solid #2d5a3d">Scorecast</td><td style="padding:8px;border:1px solid #2d5a3d">First scorer + correct score</td><td style="padding:8px;border:1px solid #2d5a3d">16/1–33/1</td></tr>
</table>

<h2>Wincast Settlement Rules Ireland</h2>
<p>Key rules that apply to wincasts on Irish-licensed betting sites: the player must score (own goals don't count); the team must win in 90 minutes (extra time goals usually don't count unless specified); if the player doesn't take part in the match, most sites void the entire wincast and return the stake. Always check the specific T&Cs before placing, as settlement can vary between operators.</p>'''
    },
    {
        'slug': 'scorecast-betting-ireland.html',
        'title': 'Scorecast Betting Ireland: How Scorecast Works',
        'desc': 'Scorecast betting Ireland explained: first scorer plus correct score, how odds are set, settlement rules, and comparison with wincast. 18+.',
        'h1': 'Scorecast Betting Ireland: How Scorecast Works',
        'body': '''<p>A scorecast combines two predictions in one bet: who will score the first goal, and what the final score will be. Both must be correct. Because both parts are genuinely difficult to predict, scorecast odds are typically very high — ranging from 12/1 to 50/1 or more for common selections.</p>

<h2>Scorecast vs Wincast vs First Goalscorer: Comparison</h2>
<table style="width:100%;border-collapse:collapse;margin:16px 0;font-size:0.95rem">
<tr style="background:#1e3a28"><th style="padding:9px;border:1px solid #2d5a3d;text-align:left;color:#cde6d4">Market</th><th style="padding:9px;border:1px solid #2d5a3d;text-align:left;color:#cde6d4">Requirements</th><th style="padding:9px;border:1px solid #2d5a3d;text-align:left;color:#cde6d4">Typical Odds</th><th style="padding:9px;border:1px solid #2d5a3d;text-align:left;color:#cde6d4">Difficulty</th></tr>
<tr><td style="padding:8px;border:1px solid #2d5a3d">First Goalscorer</td><td style="padding:8px;border:1px solid #2d5a3d">Player scores 1st goal</td><td style="padding:8px;border:1px solid #2d5a3d">3/1–8/1</td><td style="padding:8px;border:1px solid #2d5a3d">Medium</td></tr>
<tr style="background:#0d1f14"><td style="padding:8px;border:1px solid #2d5a3d">Wincast</td><td style="padding:8px;border:1px solid #2d5a3d">Team wins + player scores</td><td style="padding:8px;border:1px solid #2d5a3d">2/1–6/1</td><td style="padding:8px;border:1px solid #2d5a3d">Medium</td></tr>
<tr><td style="padding:8px;border:1px solid #2d5a3d">Scorecast</td><td style="padding:8px;border:1px solid #2d5a3d">First scorer + exact final score</td><td style="padding:8px;border:1px solid #2d5a3d">12/1–50/1</td><td style="padding:8px;border:1px solid #2d5a3d">High</td></tr>
</table>

<h2>How Scorecast Odds Are Set in Ireland</h2>
<p>The bookmaker multiplies the implied probability of the first goalscorer market and the correct score market, then applies a margin. The 2-1 home win is typically the most backed correct score and therefore often carries a slightly compressed price in scorecasts. Scores like 3-0 or 2-0 with the same first scorer tend to offer better value because they're less popular selections.</p>

<h2>Scorecast Settlement Rules Ireland</h2>
<p>Standard rules: own goals do not count as a first scorer; the bet settles on 90 minutes only (extra time and penalties don't change the scorecast result for most operators); if your named player doesn't appear in the match, the bet is void. Always check whether the operator uses "first scorer" or "anytime scorer" as the goalscorer component — a small number of operators offer anytime scorecast variants which are slightly easier to land.</p>'''
    },
    {
        'slug': 'racing-post-tips-ireland.html',
        'title': 'Racing Post Tips Ireland: Alternative Free Tip Sources',
        'desc': 'Find free horse racing tips for Ireland: alternatives to Racing Post, how to evaluate tipster records, and what to look for in a reliable source. 18+.',
        'h1': 'Racing Post Tips Ireland: Alternative Free Tip Sources',
        'body': '''<p>The Racing Post is the best-known source of horse racing tips and form in Britain and Ireland, covering every race card in detail. However, it operates a paid subscription model for premium content. This guide covers what the Racing Post offers for free, plus the best alternatives for Irish punters who want quality tips without a subscription.</p>

<h2>What Racing Post Offers Free vs Paid in Ireland</h2>
<table style="width:100%;border-collapse:collapse;margin:16px 0;font-size:0.95rem">
<tr style="background:#1e3a28"><th style="padding:9px;border:1px solid #2d5a3d;text-align:left;color:#cde6d4">Content</th><th style="padding:9px;border:1px solid #2d5a3d;text-align:left;color:#cde6d4">Free</th><th style="padding:9px;border:1px solid #2d5a3d;text-align:left;color:#cde6d4">Paid (Digital Pass)</th></tr>
<tr><td style="padding:8px;border:1px solid #2d5a3d">Race cards (basic)</td><td style="padding:8px;border:1px solid #2d5a3d">✓</td><td style="padding:8px;border:1px solid #2d5a3d">✓ Full form</td></tr>
<tr style="background:#0d1f14"><td style="padding:8px;border:1px solid #2d5a3d">Tips (nap of the day)</td><td style="padding:8px;border:1px solid #2d5a3d">Limited</td><td style="padding:8px;border:1px solid #2d5a3d">All tipsters</td></tr>
<tr><td style="padding:8px;border:1px solid #2d5a3d">Speed figures / RPR</td><td style="padding:8px;border:1px solid #2d5a3d">✗</td><td style="padding:8px;border:1px solid #2d5a3d">✓</td></tr>
<tr style="background:#0d1f14"><td style="padding:8px;border:1px solid #2d5a3d">Irish racing coverage</td><td style="padding:8px;border:1px solid #2d5a3d">Basic</td><td style="padding:8px;border:1px solid #2d5a3d">Full</td></tr>
</table>

<h2>Free Alternatives to Racing Post for Irish Racing Tips</h2>
<p><strong>At The Races (attheracces.com)</strong> — free tips and race previews for all Irish fixtures, with live streaming available. Strong on Irish track coverage including Leopardstown, Fairyhouse, and the Curragh.</p>
<p><strong>Racing TV</strong> — similar to At The Races, free tips on the website with previews from track reporters covering Irish meetings. Best for Cheltenham and Galway festival previews.</p>
<p><strong>Horse Racing Ireland (hri.ie)</strong> — official HRI site with race fixtures, entries, and draw information. No tips, but essential for checking declarations and going conditions at Irish tracks.</p>
<p><strong>Irish Examiner / Irish Independent sport sections</strong> — free racing columns from Irish journalists for major meetings, particularly Cheltenham and the Irish classics.</p>

<h2>How to Evaluate a Tipster's Record Ireland</h2>
<p>Before following any tipster's selections, check their track record over a minimum of 100 tips: look for ROI (return on investment) above 0% at industry average odds, strike rate relative to average starting price, and whether results are independently verified. A tipster with a 20% strike rate at average odds of 5/1 is profitable over time; one with 50% strike rate at 1/2 is not. No tipster, including professional Racing Post journalists, wins consistently — treat tips as one input, not a guarantee. Gambling should always be entertainment, not income. 18+ only.</p>'''
    },
    {
        'slug': 'oddschecker-ireland.html',
        'title': 'Oddschecker Ireland: Odds Comparison for Irish Punters',
        'desc': 'How to use odds comparison sites in Ireland to find the best price, hunt value, and maximise returns. Free tools for Irish bettors. 18+.',
        'h1': 'Oddschecker Ireland: Odds Comparison for Irish Punters',
        'body': '''<p>Odds comparison sites let you see the prices offered by multiple bookmakers on the same event in one place, so you can quickly find the best available price before placing your bet. Getting the best odds consistently is one of the most effective ways to improve your long-term returns — even small differences compound significantly over hundreds of bets.</p>

<h2>How to Use Odds Comparison in Ireland</h2>
<p>The process is straightforward: search for your event on a comparison site, look across the row of bookmaker prices, and open an account with the one offering the highest odds. For regular punters, maintaining accounts with several Irish-licensed operators means you can almost always get the best price available without switching sites frequently.</p>
<table style="width:100%;border-collapse:collapse;margin:16px 0;font-size:0.95rem">
<tr style="background:#1e3a28"><th style="padding:9px;border:1px solid #2d5a3d;text-align:left;color:#cde6d4">Step</th><th style="padding:9px;border:1px solid #2d5a3d;text-align:left;color:#cde6d4">Action</th></tr>
<tr><td style="padding:8px;border:1px solid #2d5a3d">1</td><td style="padding:8px;border:1px solid #2d5a3d">Search the event (match, race, or market)</td></tr>
<tr style="background:#0d1f14"><td style="padding:8px;border:1px solid #2d5a3d">2</td><td style="padding:8px;border:1px solid #2d5a3d">Compare all bookmaker prices in the row</td></tr>
<tr><td style="padding:8px;border:1px solid #2d5a3d">3</td><td style="padding:8px;border:1px solid #2d5a3d">Click the highest price to open the bet slip</td></tr>
<tr style="background:#0d1f14"><td style="padding:8px;border:1px solid #2d5a3d">4</td><td style="padding:8px;border:1px solid #2d5a3d">Check the price hasn't moved before confirming</td></tr>
</table>

<h2>What Odds Comparison Sites Don't Show Ireland</h2>
<p>Comparison sites typically show the headline match odds market but may not cover all niche markets (correct score, first scorer, specials). They also don't account for existing promotional prices, personal enhanced odds offered to your account, or reload bonuses that could affect the effective price. For horse racing, they often include Best Odds Guaranteed indicators — useful for identifying which sites will upgrade your price if the SP is bigger than your early price.</p>

<h2>Limitations for Irish Punters</h2>
<p>Not all operators available to Irish punters appear on every comparison site. Only operators holding a GRAI remote betting licence (from 1 July 2026) or a valid Revenue remote bookmaker permission are legally able to accept bets from Irish residents. When a comparison site lists an operator, verify its Irish licence status before depositing — the GRAI public register is the definitive source. Unlicensed operators have no consumer protection obligations under Irish law.</p>'''
    },
    {
        'slug': 'matched-betting-ireland-guide.html',
        'title': 'Matched Betting Ireland: Step-by-Step Guide 2026',
        'desc': 'Matched betting Ireland 2026: how it works, is it legal, step-by-step example, and realistic expectations for Irish bettors. 18+.',
        'h1': 'Matched Betting Ireland: Step-by-Step Guide 2026',
        'body': '''<p>Matched betting is a technique that uses free bets and bonuses from bookmakers to generate a profit with minimal risk. By placing a back bet at a bookmaker and an offsetting lay bet at a betting exchange, you cover all outcomes and profit from the bonus value. It is legal in Ireland and widely practised.</p>

<h2>Is Matched Betting Legal in Ireland</h2>
<p>Yes. Matched betting is not illegal under Irish law. There is no statute that prohibits using bookmaker promotions in combination with exchange lay bets. Bookmakers reserve the right to restrict or close accounts they identify as matched bettors, but that is a commercial decision, not a legal one. Winnings from matched betting are generally not subject to Irish income tax for recreational bettors, though anyone treating it as a trade should seek professional advice.</p>

<h2>How Matched Betting Works: Step-by-Step Example</h2>
<p>The core mechanism uses a "qualifying bet" to unlock a free bet, then uses the free bet to generate profit.</p>
<table style="width:100%;border-collapse:collapse;margin:16px 0;font-size:0.95rem">
<tr style="background:#1e3a28"><th style="padding:9px;border:1px solid #2d5a3d;text-align:left;color:#cde6d4">Step</th><th style="padding:9px;border:1px solid #2d5a3d;text-align:left;color:#cde6d4">Action</th><th style="padding:9px;border:1px solid #2d5a3d;text-align:left;color:#cde6d4">Amount</th></tr>
<tr><td style="padding:8px;border:1px solid #2d5a3d">1. Qualifying bet</td><td style="padding:8px;border:1px solid #2d5a3d">Back selection at bookmaker (€10 @ 2.0)</td><td style="padding:8px;border:1px solid #2d5a3d">−€0.50 (small qualifying loss)</td></tr>
<tr style="background:#0d1f14"><td style="padding:8px;border:1px solid #2d5a3d">1. Lay bet</td><td style="padding:8px;border:1px solid #2d5a3d">Lay same selection at exchange (1.95)</td><td style="padding:8px;border:1px solid #2d5a3d">Covers qualifying loss</td></tr>
<tr><td style="padding:8px;border:1px solid #2d5a3d">2. Free bet</td><td style="padding:8px;border:1px solid #2d5a3d">Use €10 SNR free bet (@ 5.0)</td><td style="padding:8px;border:1px solid #2d5a3d">Returns €40 (stake not returned)</td></tr>
<tr style="background:#0d1f14"><td style="padding:8px;border:1px solid #2d5a3d">2. Lay free bet</td><td style="padding:8px;border:1px solid #2d5a3d">Lay same selection at exchange</td><td style="padding:8px;border:1px solid #2d5a3d">Lock in ~€7–8 profit</td></tr>
</table>

<h2>Realistic Expectations for Matched Betting Ireland 2026</h2>
<p>Welcome offer profits are highest (€20–€100 per operator) and are genuinely low-risk when executed correctly. Ongoing reload offers are smaller and require more time to find and process. Account restrictions from bookmakers become more frequent over time as matched betting accounts are identified through betting patterns. Most serious matched bettors in Ireland exhaust welcome offers within 3–6 months, then face a diminishing return as accounts get limited. It is not a long-term substitute for income, and no pronostic or technique guarantees profit. Treat it as supplemental entertainment with an edge, not a business. 18+ only.</p>'''
    },
    {
        'slug': 'trebles-betting-ireland.html',
        'title': 'Trebles Betting Ireland: How a Treble Bet Works',
        'desc': 'Treble bet explained for Ireland: how it works, minimum winners needed, comparison with Trixie and 3 singles, and worked examples. 18+.',
        'h1': 'Trebles Betting Ireland: How a Treble Bet Works',
        'body': '''<p>A treble is a single bet combining three selections. All three must win for the bet to pay out. If any one leg loses, the entire treble loses. The odds of all three selections are multiplied together to give the treble price, which is why trebles offer significantly higher returns than betting on each selection individually.</p>

<h2>Treble vs Trixie vs 3 Singles: Which Is Better Ireland</h2>
<p>The right choice depends on your confidence level and risk tolerance. A treble is all-or-nothing; a Trixie (4 bets: 3 doubles + 1 treble) returns something if only two legs win; three singles let you profit even if only one wins.</p>
<table style="width:100%;border-collapse:collapse;margin:16px 0;font-size:0.95rem">
<tr style="background:#1e3a28"><th style="padding:9px;border:1px solid #2d5a3d;text-align:left;color:#cde6d4">Bet Type</th><th style="padding:9px;border:1px solid #2d5a3d;text-align:left;color:#cde6d4">Number of Bets</th><th style="padding:9px;border:1px solid #2d5a3d;text-align:left;color:#cde6d4">Minimum Winners for Return</th><th style="padding:9px;border:1px solid #2d5a3d;text-align:left;color:#cde6d4">€10 Total Stake</th></tr>
<tr><td style="padding:8px;border:1px solid #2d5a3d">3 Singles</td><td style="padding:8px;border:1px solid #2d5a3d">3</td><td style="padding:8px;border:1px solid #2d5a3d">1 of 3</td><td style="padding:8px;border:1px solid #2d5a3d">€3.33 per bet</td></tr>
<tr style="background:#0d1f14"><td style="padding:8px;border:1px solid #2d5a3d">Trixie</td><td style="padding:8px;border:1px solid #2d5a3d">4</td><td style="padding:8px;border:1px solid #2d5a3d">2 of 3</td><td style="padding:8px;border:1px solid #2d5a3d">€2.50 per line</td></tr>
<tr><td style="padding:8px;border:1px solid #2d5a3d">Patent</td><td style="padding:8px;border:1px solid #2d5a3d">7</td><td style="padding:8px;border:1px solid #2d5a3d">1 of 3</td><td style="padding:8px;border:1px solid #2d5a3d">€1.43 per line</td></tr>
<tr style="background:#0d1f14"><td style="padding:8px;border:1px solid #2d5a3d">Treble</td><td style="padding:8px;border:1px solid #2d5a3d">1</td><td style="padding:8px;border:1px solid #2d5a3d">3 of 3 (all)</td><td style="padding:8px;border:1px solid #2d5a3d">€10 on one bet</td></tr>
</table>

<h2>Treble Worked Example Ireland</h2>
<p>Three selections at 2/1, 3/1, and Evens (2.0 decimal): multiplied together = 3.0 × 4.0 × 2.0 = 24.0 decimal odds. A €10 treble returns €240 (€230 profit) if all three win. The same three selections as singles at €3.33 each returns a maximum of €40.56 if all win, but returns something if only one or two win. The treble offers higher upside but nothing if even one leg fails.</p>'''
    },
]

for page in pages:
    content = shell
    content = re.sub(r'<title>[^<]*</title>', f'<title>{page["title"]} | CraicBet</title>', content)
    content = re.sub(r'<meta name="description" content="[^"]*"', f'<meta name="description" content="{page["desc"]}"', content)
    content = re.sub(r'<h1[^>]*>[^<]*</h1>', f'<h1>{page["h1"]}</h1>', content)
    # Replace canonical
    content = re.sub(r'<link rel="canonical"[^>]*/>', f'<link rel="canonical" href="https://craicbet.com/{page["slug"].replace(".html","")}" />', content)
    # Replace og:url
    content = re.sub(r'<meta property="og:url"[^>]*/>', f'<meta property="og:url" content="https://craicbet.com/{page["slug"].replace(".html","")}" />', content)
    # Replace og:title
    content = re.sub(r'<meta property="og:title"[^>]*/>', f'<meta property="og:title" content="{page["title"]}" />', content)
    # Replace schema name
    content = re.sub(r'"name": "What Does DNB Mean[^"]*"', f'"name": "{page["title"]}"', content)

    # Find the article content area and replace body content
    # Replace everything between first <p> after h1 and before editorial-box
    # Insert body before the first faq-item or editorial-box
    insert_marker = '<div class="editorial-box"'
    if insert_marker not in content:
        insert_marker = '<div class="faq-item"'

    if insert_marker in content:
        idx = content.index(insert_marker)
        # Find where existing article body starts (after h1)
        h1_end = content.index('</h1>') + 6
        # Find next block after h1 to replace
        content = content[:h1_end] + '\n' + page['body'] + '\n\n' + content[idx:]

    with open(f'pages/{page["slug"]}', 'w') as f:
        f.write(content)
    print(f'Created: pages/{page["slug"]}')

print('All pages created.')
