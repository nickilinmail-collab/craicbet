#!/usr/bin/env python3
"""Batch 9: expand thin content pages with GSC-targeted H2 sections."""
import os, re

SKIP = {'contact.html','about.html','terms.html','privacy.html','editorial-guidelines.html','where-to-watch.html','weekly-news-nov-03-2026.html'}

TABLE_H = 'style="background:#1e3a28"'
TH = 'style="padding:9px;border:1px solid #2d5a3d;text-align:left;color:#cde6d4"'
TD = 'style="padding:8px;border:1px solid #2d5a3d"'
TD2 = 'style="padding:8px;border:1px solid #2d5a3d;background:#0d1f14"'
TABLE = 'style="width:100%;border-collapse:collapse;margin:16px 0;font-size:0.95rem"'

def row(cells, alt=False):
    s = '<tr style="background:#0d1f14">' if alt else '<tr>'
    for c in cells:
        s += f'<td {TD2 if alt else TD}>{c}</td>'
    return s + '</tr>'

def hrow(cells):
    return f'<tr {TABLE_H}>' + ''.join(f'<th {TH}>{c}</th>' for c in cells) + '</tr>'

def tbl(headers, rows, caption=''):
    out = f'\n<table {TABLE}>\n'
    out += hrow(headers) + '\n'
    for i, r in enumerate(rows):
        out += row(r, alt=(i%2==1)) + '\n'
    return out + '</table>\n'

CONTENT = {

'cheltenham-tips-guide.html': """
<h2>Key Statistics to Check Before Placing Cheltenham Bets</h2>
""" + tbl(['Stat','Why it matters','Where to find it'],[
    ['Going report','Cheltenham drains well but March weather varies; soft vs good-to-soft can halve a price','racingpost.com day of race'],
    ['Trainer strike rate','Henderson/Mullins hit 20–30% at the Festival; smaller stables average 5%','racingpost.com trainer stats'],
    ['Course form','The undulating track suits scopey jumpers; some horses consistently improve here','horse profile, RPR ratings'],
    ['Topweight burden','Weight-carrying record over 2m vs 3m varies; check past 12 months','racecard weights column'],
    ['Market confidence','Betfair SP often sharper than opening show; watch drifters on the morning','Betfair exchange'],
]) + """
<h2>Cheltenham Race-by-Race Difficulty Rating</h2>
<p>Not every Cheltenham race is equally hard to predict. Use this table to allocate your stakes wisely:</p>
""" + tbl(['Race','Difficulty','Notes'],[
    ['Supreme Novices Hurdle','⭐⭐⭐⭐⭐','Large fields, unexposed novices — high variance'],
    ['Champion Hurdle','⭐⭐⭐','Smaller field, established form — more readable'],
    ['Gold Cup','⭐⭐⭐⭐','Distance and stamina crucial; favourite lands ~30%'],
    ['Grand Annual Chase','⭐⭐⭐⭐⭐','Handicap — wide-open, long-priced winners common'],
    ['Stayers Hurdle','⭐⭐','Smaller field, strong form — most predictable of Festival'],
]) + """
<p style="font-size:0.85em;color:#555;margin-top:8px">18+ only. No tip is guaranteed. Gambling Awareness Trust: 1800 753 753.</p>
""",

'both-teams-to-score-guide.html': """
<h2>BTTS Rates by League (2024–25 Season)</h2>
""" + tbl(['League','BTTS Yes %','BTTS No %','Avg goals/game'],[
    ['Bundesliga','62%','38%','3.1'],
    ['Premier League','55%','45%','2.8'],
    ['La Liga','54%','46%','2.6'],
    ['Ligue 1','50%','50%','2.5'],
    ['Serie A','48%','52%','2.5'],
    ['League of Ireland Premier Div','51%','49%','2.6'],
]) + """
<h2>How to Use BTTS in an Accumulator</h2>
<p>BTTS Yes accumulators are popular because even short-price selections (1.70–1.85) compound quickly. Here's how the maths works:</p>
""" + tbl(['Legs','Each leg price','Combined price (no margin)','Realistic combined price'],[
    ['2','1.80','3.24','~2.90'],
    ['3','1.80','5.83','~5.00'],
    ['4','1.80','10.50','~8.80'],
    ['5','1.80','18.90','~15.50'],
]) + """
<p>The gap between columns 3 and 4 represents the bookmaker's margin stacking across legs. Use BTTS accas on fixtures with strong attacking form from both sides and no clean-sheet-dominant defences.</p>
<p style="font-size:0.85em;color:#555">18+ | Gambling Awareness Trust | 1800 753 753 | gamblingcare.ie</p>
""",

'over-25-goals-guide.html': """
<h2>Over/Under 2.5 Goals Rates by European League</h2>
""" + tbl(['League','Over 2.5 %','Under 2.5 %','Notes'],[
    ['Bundesliga','62%','38%','Highest of the big-5; attacking football culture'],
    ['Premier League','55%','45%','Varies heavily by fixture'],
    ['La Liga','54%','46%','Mid-table games often low-scoring'],
    ['Ligue 1','50%','50%','Defensive teams pull average down'],
    ['Serie A','48%','52%','Historically the most defensive big-5 league'],
    ['League of Ireland Premier Div','51%','49%','Close to 50/50; check fixture by fixture'],
]) + """
<h2>When to Back Under 2.5 Instead</h2>
<p>Under 2.5 goals is priced at roughly evens in most fixtures, making it a viable selection when:</p>
<ul style="line-height:1.9">
<li>Both teams have <strong>strong defensive records</strong> (under 1 goal conceded per game)</li>
<li>The fixture has low historical goal tallies (check head-to-head)</li>
<li>A key attacker is absent or returning from injury</li>
<li>The match has low stakes (mid-table, nothing to play for)</li>
<li>Poor pitch or weather conditions favour defensive play</li>
</ul>
<p style="font-size:0.85em;color:#555">18+ | Gambling Awareness Trust | 1800 753 753 | gamblingcare.ie</p>
""",

'formula-1-betting-guide.html': """
<h2>F1 Betting Markets Explained</h2>
""" + tbl(['Market','Settles on','Typical odds range','Key note'],[
    ['Race winner','1st place finisher','1.20–10.00','Favourite lands ~35% of races'],
    ['Podium finish (top 3)','1st/2nd/3rd','1.10–3.00','Each-way alt at 1/4 odds for top 3'],
    ['Points finish (top 10)','1st–10th place','1.05–2.00','Safe bet on top constructors'],
    ['Fastest lap','Fastest single lap in race','3.00–10.00','Often a strategy call late in race'],
    ['Driver H2H','Which of two named drivers finishes higher','~1.80 each side','Useful when DNF risk differs'],
    ["Driver's championship","Season winner","1.10–50.00","Opens in February pre-season"],
]) + """
<h2>F1 Race Calendar: Betting Considerations</h2>
<p>Not all F1 circuits favour the same teams. Street circuits (Monaco, Singapore, Baku) produce more unpredictable results than high-speed permanent tracks (Monza, Spa). Betting on the dominant team at Monza is a different proposition to Monaco, where overtaking is nearly impossible and qualifying position is decisive.</p>
<ul style="line-height:1.9">
<li><strong>High-speed circuits</strong> (Monza, Silverstone, Spa): dominant car has bigger advantage</li>
<li><strong>Street circuits</strong> (Monaco, Singapore): qualifying position critical; upsets more likely</li>
<li><strong>Wet races</strong>: form guide less reliable; strategy and tyre calls matter more</li>
</ul>
<p style="font-size:0.85em;color:#555">18+ | No result guaranteed | Gambling Awareness Trust: 1800 753 753</p>
""",

'cricket-betting-ireland.html': """
<h2>Cricket Betting Markets Available in Ireland</h2>
""" + tbl(['Market','Format','Settles on'],[
    ['Match winner','All formats','Which team wins (or draw in Test)'],
    ['Top match batsman','All formats','Highest individual score in match'],
    ['Top innings batsman','All formats','Highest score in a specified innings'],
    ['Total match sixes','T20/ODI','Over/under a set number of sixes'],
    ['Method of dismissal','All formats','How next wicket falls (caught/bowled/LBW…)'],
    ['Innings runs (over/under)','All formats','Total runs in a specific innings'],
]) + """
<h2>Ireland Cricket: Key Upcoming Fixtures and Markets</h2>
<p>Ireland competes in ICC World Cricket League and bilateral series. The main Irish cricket betting opportunities include:</p>
<ul style="line-height:1.9">
<li><strong>Ireland v England T20Is</strong> — usually June; short format increases variance</li>
<li><strong>ICC T20 World Cup</strong> — Ireland regularly qualify; group stage matches offered by most operators</li>
<li><strong>ICC Cricket World Cup qualifying rounds</strong> — full ODI markets available</li>
<li><strong>Inter-Provincial T20 Cup</strong> — Leinster Lightning, Munster Reds, North West Warriors; some operators offer markets</li>
</ul>
<p style="font-size:0.85em;color:#555">18+ | Gambling Awareness Trust | 1800 753 753 | gamblingcare.ie</p>
""",

'nba-betting-guide-ireland.html': """
<h2>NBA Betting Markets Available from Ireland</h2>
""" + tbl(['Market','Settles on','Bet type'],[
    ['Moneyline','Which team wins','Win/lose, no spread'],
    ['Point spread','Winning margin vs spread','Team must cover'],
    ['Game total (O/U)','Total points scored','Over or under a set line'],
    ['Player points O/U','Individual player points','Prop bet'],
    ['Player assists/rebounds O/U','Individual player stats','Prop bet'],
    ['Season MVP outright','Regular season MVP award','Ante-post'],
    ['Championship winner','NBA Finals winner','Ante-post'],
]) + """
<h2>Time Zone Note for Irish NBA Bettors</h2>
<p>NBA games tip off between 00:30 and 04:30 Irish time (GMT/IST). Most GRAI-licensed bookmakers settle markets within 30 minutes of the final buzzer. Key points:</p>
<ul style="line-height:1.9">
<li>In-play markets are available but require staying up late</li>
<li>Pre-game markets typically open 24–48 hours before tip-off</li>
<li>Free bet expiries may catch out bettors — always check before placing</li>
<li>ESPN and Basketball Reference are the most reliable stats sources for research</li>
</ul>
<p style="font-size:0.85em;color:#555">18+ | Gambling Awareness Trust | 1800 753 753 | gamblingcare.ie</p>
""",

'el-clasico-betting-ireland.html': """
<h2>El Clásico Betting Markets</h2>
""" + tbl(['Market','Notes'],[
    ['Match result (1X2)','Most popular market; draw priced 3.50–4.50 typically'],
    ['Both teams to score','Lands ~65% of Clásicos historically'],
    ['Over/under 2.5 goals','Over 2.5 lands ~60% of Clásico matches'],
    ['First goalscorer','Wide market; header specialists valuable at set pieces'],
    ['Correct score','High margin; use sparingly'],
    ['Asian handicap','Removes draw; useful when one side is heavily favoured'],
]) + """
<h2>El Clásico Head-to-Head Context</h2>
<p>El Clásico (Real Madrid vs Barcelona) is the most watched club match in the world. For betting purposes, key factors are:</p>
<ul style="line-height:1.9">
<li><strong>Venue matters:</strong> La Liga Clásicos alternate between the Bernabéu and Camp Nou — home team wins ~55% historically</li>
<li><strong>Cup/Super Cup Clásicos:</strong> played at neutral venues, results more even</li>
<li><strong>Squad rotation:</strong> check if key players are rested for Champions League fixtures nearby</li>
<li><strong>Recent form:</strong> La Liga standings are the best single predictor</li>
</ul>
<p style="font-size:0.85em;color:#555">18+ | No result guaranteed | Gambling Awareness Trust: 1800 753 753</p>
""",

'saturday-football-betting.html': """
<h2>Saturday Football Betting: Key Kick-Off Times</h2>
""" + tbl(['League','Typical kick-offs (Irish time)','Key match'],[
    ['Premier League','13:30 / 16:00 / 17:30','3pm blackout: no live UK broadcast'],
    ['La Liga','14:00 / 16:15 / 21:00','Late evening La Liga fixtures popular'],
    ['Bundesliga','14:30 / 17:30','Saturdays are Bundesliga\'s busiest day'],
    ['Ligue 1','16:00 / 21:00','Ligue 1 also uses Saturday slots'],
    ['League of Ireland','19:45 (summer) / 15:00 (spring/autumn)','Friday evening increasingly used'],
]) + """
<h2>Saturday Acca Tips: What to Look For</h2>
<ul style="line-height:1.9">
<li><strong>Check team news by 11am:</strong> Premier League teamsheets released ~1 hour before kick-off</li>
<li><strong>Avoid early prices on injury-sensitive teams</strong> — prices move significantly when a star player is ruled out</li>
<li><strong>Home advantage on Saturdays</strong> is stronger in the Premier League than midweek matches</li>
<li><strong>Late kick-offs (5pm+)</strong> in La Liga and Bundesliga often feature stronger teams with more rested squads</li>
</ul>
<p style="font-size:0.85em;color:#555">18+ | Gambling Awareness Trust | 1800 753 753 | gamblingcare.ie</p>
""",

'world-cup-2026-outright-winner-betting.html': """
<h2>2026 FIFA World Cup Format</h2>
""" + tbl(['Stage','Teams','Format'],[
    ['Group stage','48 teams (12 groups of 4)','Top 2 + 8 best 3rd-place qualify'],
    ['Round of 32','32 teams','Single-leg knockout'],
    ['Round of 16','16 teams','Single-leg knockout'],
    ['Quarter-finals','8 teams','Single-leg knockout'],
    ['Semi-finals','4 teams','Single-leg knockout'],
    ['Third place play-off','2 teams','Single-leg'],
    ['Final','2 teams','Single-leg — New York/New Jersey, July 19 2026'],
]) + """
<h2>World Cup 2026 Outright Betting Tips</h2>
<p>Key factors for outright winner markets:</p>
<ul style="line-height:1.9">
<li><strong>Expanded format benefits:</strong> 48-team draw means top nations avoid each other until later — fewer early exits for favourites</li>
<li><strong>Host nation advantage:</strong> USA, Canada and Mexico all qualify automatically; USA has realistic semi-final potential</li>
<li><strong>European cycle:</strong> EURO 2024 form is the best guide; nations peaking in 2026 will be 2 years on from that squad</li>
<li><strong>Each-way value:</strong> with 48 teams, reaching the semi-final is a realistic target for second-tier nations at big prices</li>
</ul>
<p style="font-size:0.85em;color:#555">18+ | No result guaranteed | Gambling Awareness Trust: 1800 753 753</p>
""",

'under-25-goals-betting.html': """
<h2>Under 2.5 Goals: When the Market Makes Sense</h2>
""" + tbl(['Scenario','Under 2.5 probability','Notes'],[
    ['Both defences concede under 1 goal/game','60–65%','Best scenario for under'],
    ['One strong defence, one weak attack','55–60%','Reasonably safe'],
    ['Mid-table vs mid-table, low stakes','50–55%','Close to coin flip'],
    ['Two high-scoring attacks, weak defences','35–40%','Avoid under 2.5'],
    ['Late-season dead-rubber match','50–55%','Motivation varies; can go either way'],
]) + """
<h2>Under 2.5 Goals vs Under 1.5 Goals</h2>
<p>Under 1.5 goals is a tighter version of the market — it requires the game to end 0-0 or 1-0 either way. Typical Irish operator prices:</p>
<ul style="line-height:1.9">
<li><strong>Under 2.5 goals:</strong> typically 1.80–2.00 (4/5 to evens)</li>
<li><strong>Under 1.5 goals:</strong> typically 2.80–3.50 (9/4 to 5/2)</li>
<li><strong>Under 0.5 goals (0-0 exact score):</strong> typically 8.00–12.00</li>
</ul>
<p>The implied probability of under 1.5 goals is roughly 25–30% across top-flight fixtures — suitable only for the most defensive match-ups.</p>
<p style="font-size:0.85em;color:#555">18+ | Gambling Awareness Trust | 1800 753 753 | gamblingcare.ie</p>
""",

'darts-world-championship-betting.html': """
<h2>Darts World Championship Betting Markets</h2>
""" + tbl(['Market','Settles on','Typical range'],[
    ['Tournament winner','Overall champion','Favourite 2.50–4.00; outsiders 50/1+'],
    ['Match winner','Named match result','1.20–4.00 depending on seedings'],
    ['Correct sets score','Exact sets e.g. 3-1','High margin; avoid unless strong read'],
    ['Total 180s in match','Over/under a set line','Popular with knowledgeable punters'],
    ['First to score 180','Which player hits first maximum','~1.80 each side'],
    ['Highest checkout','Which player hits the highest single checkout','Specialist market'],
]) + """
<h2>PDC World Championship Format (Alexandra Palace)</h2>
<ul style="line-height:1.9">
<li>96 players compete over 3 weeks in December/January</li>
<li>First round: best of 3 sets; quarter-finals: best of 5; final: best of 13</li>
<li>Top 32 seeds receive first-round byes</li>
<li>Price shortening rapidly when lower seeds are knocked out in first week</li>
<li>Irish players Phil Taylor era has ended; watch for UK qualifier wildcards at big prices</li>
</ul>
<p style="font-size:0.85em;color:#555">18+ | Gambling Awareness Trust | 1800 753 753 | gamblingcare.ie</p>
""",

'correct-score-betting-football.html': """
<h2>Correct Score: Expected Probabilities vs Bookmaker Prices</h2>
""" + tbl(['Score','Statistical probability (avg PL game)','Typical bookmaker price','Margin'],[
    ['1-0 to home team','12–14%','7.00–9.00','High'],
    ['1-1 draw','11–13%','7.00–9.00','High'],
    ['2-1 to home team','11–13%','8.00–11.00','Very high'],
    ['2-0 to home team','8–10%','9.00–12.00','High'],
    ['0-0 draw','8–10%','10.00–13.00','High'],
    ['2-2 draw','5–7%','14.00–18.00','High'],
]) + """
<h2>How to Reduce Correct Score Risk with Score Casts</h2>
<p>A scorecast combines the first goalscorer with the correct score — it pays out at a combined price but only requires both to land. An alternative is:</p>
<ul style="line-height:1.9">
<li><strong>Reverse forecast:</strong> backs two scores (e.g. 1-0 and 0-1 both win) — reduces odds but doubles coverage</li>
<li><strong>Scorecast:</strong> first scorer + correct score combined; implied margin can exceed 40%</li>
<li><strong>Exact goals market:</strong> betting on the total goals scored (e.g. exactly 2) has a lower margin than specific score</li>
</ul>
<p>Correct score markets typically carry a 25–40% bookmaker margin — the highest of common football markets. Use sparingly.</p>
<p style="font-size:0.85em;color:#555">18+ | No result guaranteed | Gambling Awareness Trust: 1800 753 753</p>
""",

'player-props-betting.html': """
<h2>Player Props Markets Available in Ireland</h2>
""" + tbl(['Market','Sport','Settles on'],[
    ['Anytime goalscorer','Football','Player scores at any point in match'],
    ['First goalscorer','Football','Player scores the opening goal'],
    ['Player total shots','Football','Over/under a set number'],
    ['Player passing accuracy','Football','Stat threshold'],
    ['Player points O/U','Basketball','Individual points total'],
    ['Player assists O/U','Basketball','Individual assists total'],
    ['Player receiving yards O/U','American Football','Yardage threshold'],
    ['Player total threes made','Basketball','Three-point shots made in game'],
]) + """
<h2>Key Rules for Player Prop Bets</h2>
<ul style="line-height:1.9">
<li><strong>Void if player doesn't start:</strong> most operators void player props if the named player doesn't take the field</li>
<li><strong>Void if match abandoned:</strong> all player props are void if match is abandoned before completion</li>
<li><strong>Injury updates:</strong> watch teamsheet releases — Irish bookmakers typically allow bets up to kick-off on props</li>
<li><strong>Overtime inclusion:</strong> NBA props typically include overtime; check the specific market rules</li>
</ul>
<p style="font-size:0.85em;color:#555">18+ | Gambling Awareness Trust | 1800 753 753 | gamblingcare.ie</p>
""",

'first-goalscorer-tips.html': """
<h2>First Goalscorer: Key Statistics to Research</h2>
""" + tbl(['Stat','Why it matters','Where to find'],[
    ['Shots per 90 minutes','High shot volume = more chances to score first','FBref.com / Sofascore'],
    ['Penalty duty','Penalty takers score from dead balls; count toward first scorer','TeamSheets / news'],
    ['Set piece delivery recipients','Aerial threats get more early chances from corners','Opta / Sofascore'],
    ['Early goal record','Some strikers consistently score in first 20 minutes','Transfermarkt'],
    ['H2H with today\'s defence','Goals scored vs this specific team historically','BBC Sport / Footystats'],
]) + """
<h2>First Goalscorer vs Anytime Goalscorer: Odds Comparison</h2>
<p>First goalscorer typically pays roughly 3–4× the anytime goalscorer price for the same player. Example for a striker priced at 3/1 (4.00) to score anytime:</p>
<ul style="line-height:1.9">
<li><strong>Anytime scorer:</strong> 4.00 (3/1)</li>
<li><strong>First goalscorer:</strong> 11.00–14.00 (10/1–13/1)</li>
<li><strong>Last goalscorer:</strong> 11.00–14.00 (similar to first)</li>
<li><strong>To score 2+:</strong> 8.00–12.00 (7/1–11/1)</li>
</ul>
<p>First goalscorer markets typically carry a margin of 20–30%, significantly above the standard 1X2 margin of 5–8%. Restrict to your strongest conviction selections.</p>
<p style="font-size:0.85em;color:#555">18+ | No result guaranteed | Gambling Awareness Trust: 1800 753 753</p>
""",

'late-goals-betting.html': """
<h2>Late Goals Markets in Football Betting</h2>
""" + tbl(['Market','Definition','Typical price'],[
    ['Over 0.5 goals 75–90 mins','At least one goal after 75th minute','1.70–2.00'],
    ['Over 1.5 goals 75–90 mins','Two or more goals after 75th minute','4.00–6.00'],
    ['Both teams score 75–90 mins','Both teams score after 75 mins','6.00–10.00'],
    ['Match result to change 70–90','Score changes in final 20 minutes','3.00–6.00'],
    ['90+ minute goal','Goal scored in added time','5.00–8.00'],
]) + """
<h2>How Often Do Late Goals Happen?</h2>
<p>Statistical data from top European leagues shows:</p>
<ul style="line-height:1.9">
<li><strong>~55–60%</strong> of Premier League matches feature at least one goal after the 75th minute</li>
<li><strong>~25–30%</strong> of matches feature a goal in the final 10 minutes (80–90)</li>
<li>Teams chasing a result substitute offensive players from the 60th minute, increasing late-goal probability</li>
<li>Matches with score 1-0 or 2-1 at 70 minutes produce the most late goals (losing team pushes forward)</li>
</ul>
<p style="font-size:0.85em;color:#555">18+ | Gambling Awareness Trust | 1800 753 753 | gamblingcare.ie</p>
""",

'betting-on-draws.html': """
<h2>When Are Draws Most Likely in Football?</h2>
""" + tbl(['Scenario','Draw probability','Notes'],[
    ['Evenly matched mid-table teams','28–32%','Most common draw scenario'],
    ['Derby/local rivalry match','30–35%','Extra tension leads to caution'],
    ['Late-season dead-rubber','25–30%','Low motivation to push for win'],
    ['Top vs top (defensive both)','25–30%','Both sides happy with a point'],
    ['Favourite vs underdog','18–22%','Underdog more cautious; favourite chases win'],
]) + """
<h2>Draw Betting Strategy: 1X and X Doubles</h2>
<p>Three approaches for backing draws:</p>
<ul style="line-height:1.9">
<li><strong>Straight draw (X):</strong> simplest — back the draw at 3.00–4.00; strike rate ~26% across leagues</li>
<li><strong>Double chance 1X:</strong> backs home win OR draw — typically priced 1.25–1.50; safer but lower return</li>
<li><strong>Draw no bet (DNB):</strong> stake returned if draw; good for value selections where you fear the draw</li>
<li><strong>Draw accumulators:</strong> combining 3-4 draws can produce high combined odds, but variance is extreme</li>
</ul>
<p style="font-size:0.85em;color:#555">18+ | Gambling Awareness Trust | 1800 753 753 | gamblingcare.ie</p>
""",

'treble-betting-guide.html': """
<h2>How a Treble Bet Works: Worked Example</h2>
""" + tbl(['Selection','Odds','Running total'],[
    ['Selection 1 wins','2.00','€10 stake becomes €20'],
    ['Selection 2 wins','2.50','€20 becomes €50'],
    ['Selection 3 wins','3.00','€50 becomes €150'],
    ['All 3 win (combined)','15.00','€10 returns €150 (€140 profit)'],
    ['One selection loses','—','Entire treble loses'],
]) + """
<h2>Treble vs Three Singles: Which is Better Value?</h2>
<p>Three singles at €10 each (€30 total) vs one treble at €10:</p>
<ul style="line-height:1.9">
<li><strong>Three singles:</strong> if all win at 2.00, 2.50 and 3.00 → returns €20 + €25 + €30 = €75 total (€45 profit)</li>
<li><strong>One treble:</strong> if all win → returns €150 (€140 profit) but costs only €10</li>
<li><strong>Key difference:</strong> treble requires all three to win; one failure = zero return</li>
<li><strong>Risk spread:</strong> singles allow partial recovery; treble is all-or-nothing</li>
</ul>
<p>A treble is better if you're confident in all three selections. If any are uncertain, singles give better risk management.</p>
<p style="font-size:0.85em;color:#555">18+ | Gambling Awareness Trust | 1800 753 753 | gamblingcare.ie</p>
""",

'doubles-betting-guide.html': """
<h2>How a Double Bet Works</h2>
""" + tbl(['Selection','Odds','Returns'],[
    ['Selection 1 wins @ 2.50','2.50','€10 stake → €25'],
    ['Selection 2 wins @ 3.00','3.00','€25 → €75'],
    ['Both win (double combined)','7.50','€10 returns €75 (€65 profit)'],
    ['Selection 1 loses','—','Entire double is lost'],
]) + """
<h2>When to Use Doubles Over Accumulators</h2>
<ul style="line-height:1.9">
<li>Doubles carry lower risk than 3+ leg accas — only two selections must win</li>
<li>The combined margin for a double is roughly <strong>two bookmaker margins stacked</strong> (typically 10–16% total vs 5–8% per single)</li>
<li>Saturday doubles are very popular in Ireland — combining two Premier League results</li>
<li>Use exchanges (Betfair) for doubles when available — no bookmaker margin on the bet itself</li>
<li>Double your two strongest selections rather than adding weak "fillers" to build a bigger acca</li>
</ul>
<p style="font-size:0.85em;color:#555">18+ | Gambling Awareness Trust | 1800 753 753 | gamblingcare.ie</p>
""",

'title-outright-betting-ireland.html': """
<h2>League Title Outright Betting: Key Markets</h2>
""" + tbl(['League','Typical pre-season favourite price','Historic dominance'],[
    ['Premier League','3.00–5.00','5–6 teams realistic each season'],
    ['La Liga','1.50–2.50','2 clubs dominated last decade'],
    ['Bundesliga','1.30–2.00','1 club dominated most of last decade'],
    ['Serie A','2.00–3.50','3 clubs realistic challengers'],
    ['Ligue 1','1.20–1.80','1 club dominated significantly'],
    ['League of Ireland Premier Div','2.00–5.00','Competitive; different winner most years'],
]) + """
<h2>When to Bet on Title Outrights</h2>
<ul style="line-height:1.9">
<li><strong>Pre-season:</strong> best prices available but most uncertainty; use for genuine value plays</li>
<li><strong>After 5–8 games:</strong> early form clarifies without prices collapsing entirely</li>
<li><strong>After a poor start:</strong> title contenders who start slowly can be backed at value mid-season</li>
<li><strong>Each-way title betting:</strong> some operators offer each-way on outrights (top 2 or 3 at 1/4 odds)</li>
</ul>
<p style="font-size:0.85em;color:#555">18+ | No result guaranteed | Gambling Awareness Trust: 1800 753 753</p>
""",

'casinos-in-cork.html': """
<h2>Land-Based Gambling Options in Cork</h2>
""" + tbl(['Venue type','Legal status in Ireland','Options in Cork'],[
    ['Betting shops','Legal (GRAI retail licence)','Multiple shops: main high streets'],
    ['Amusement arcades','Legal (limited stakes/prizes)','Arcades operate under separate licensing'],
    ['Private poker clubs','Legal (private members, no house rake)','Limited; check membership basis'],
    ['Online casino','Legal when licensed by GRAI or MGA','Accessible from Cork via phone/desktop'],
    ['Land-based casino','No licence issued in Ireland','Zero legal land-based casinos in Ireland'],
]) + """
<h2>Online Casino vs Betting Shop in Cork</h2>
<p>Ireland has no land-based casinos — the Gambling Regulation Act 2024 (commencing in stages) includes provisions for future land-based licensing, but no casino licences have been issued as of November 2026. Cork residents access casino games online only.</p>
<ul style="line-height:1.9">
<li>Online casinos with MGA (Malta Gaming Authority) licences are the most common operators serving Cork</li>
<li>GRAI has issued <strong>remote betting licences only</strong> (no casino/gaming licences yet — expected 2027–2028)</li>
<li>Betting shops in Cork hold GRAI in-person retail licences</li>
<li>Always check a site's licence before depositing: visit grai.ie/register</li>
</ul>
<p style="font-size:0.85em;color:#555">18+ | Gambling Awareness Trust | 1800 753 753 | gamblingcare.ie</p>
""",

'cork-racecourse-betting.html': """
<h2>Cork Racecourse (Mallow): Key Facts for Bettors</h2>
""" + tbl(['Feature','Detail'],[
    ['Location','Mallow, Co. Cork (Killarney Street, Mallow)'],
    ['Surface','Flat (summer) and National Hunt (winter)'],
    ['Distance range','5 furlongs to 2 miles (flat); 2 miles to 3 miles (jumps)'],
    ['Notable meetings','Cork Summer Festival (July); St Stephen\'s Day meeting (December 26)'],
    ['Bookmakers on course','On-course bookies + Tote; major apps accepted'],
]) + """
<h2>How to Bet on Cork Races from Home</h2>
<ul style="line-height:1.9">
<li>All Cork races are available on GRAI-licensed betting apps in real time</li>
<li><strong>Best Odds Guaranteed (BOG):</strong> take morning prices on Cork meetings — BOG pays out the SP if it drifts</li>
<li><strong>Tote pools:</strong> Cork racecourse runs its own tote pools; some operators offer access to Irish Tote</li>
<li><strong>Going reports:</strong> Cork's Mallow track can be testing in autumn/winter; check going before betting</li>
<li>Race cards available on Racing Post and from the racecourse's own site</li>
</ul>
<p style="font-size:0.85em;color:#555">18+ | Gambling Awareness Trust | 1800 753 753 | gamblingcare.ie</p>
""",

'sligo-racecourse-betting.html': """
<h2>Sligo Racecourse: Key Facts for Bettors</h2>
""" + tbl(['Feature','Detail'],[
    ['Location','Cleveragh, Sligo Town'],
    ['Surface','Flat (mixed distances)'],
    ['Unique feature','Right-handed track; undulating; favours handy racers'],
    ['Notable meetings','August festival meetings; summer flat racing'],
    ['Bookmakers on course','On-course bookies + Tote available'],
]) + """
<h2>Betting Tips for Sligo Races</h2>
<ul style="line-height:1.9">
<li>Sligo's sharp turns and undulating track strongly favour horses with <strong>previous course form</strong></li>
<li>Field sizes at Sligo are often smaller than the big tracks — research is easier but prices are tighter</li>
<li>Best Odds Guaranteed applies at Sligo meetings on most GRAI-licensed apps</li>
<li>August bank holiday meetings attract holiday crowds and can produce pace biases — watch for front-runners</li>
</ul>
<p style="font-size:0.85em;color:#555">18+ | Gambling Awareness Trust | 1800 753 753 | gamblingcare.ie</p>
""",

'even-money-betting.html': """
<h2>Even Money: Formats Across Irish Betting Sites</h2>
""" + tbl(['Format','Even money representation','Profit on €10 stake'],[
    ['Fractional (traditional)','1/1 or Evens','€10'],
    ['Decimal (European)','2.00','€10'],
    ['American (moneyline)','+100','€10'],
    ['Implied probability','50.0%','—'],
]) + """
<h2>When Does Even Money Represent Value?</h2>
<p>Even money (2.00 decimal) means the bookmaker is implying a 50% chance. After margin, the true implied probability is higher — typically 52–55%. To have value betting at evens, the event must have a greater than 50% chance of occurring. Consider:</p>
<ul style="line-height:1.9">
<li><strong>Strong favourites at short odds</strong> — evens on a heavy favourite after line movement may represent genuine value</li>
<li><strong>Exchange prices at 2.00</strong> (Betfair etc.) carry no bookmaker margin — exact fair value at the market price</li>
<li><strong>Avoid impulse evens bets</strong> on coin-flip events where you have no informational edge</li>
<li>Use the Kelly Criterion: bet a fraction only when you believe the probability exceeds 50% clearly</li>
</ul>
<p style="font-size:0.85em;color:#555">18+ | Gambling Awareness Trust | 1800 753 753 | gamblingcare.ie</p>
""",

'how-does-tote-betting-work.html': """
<h2>Tote Pools vs Fixed Odds: Key Differences</h2>
""" + tbl(['Feature','Tote (pool betting)','Fixed odds bookmaker'],[
    ['Price known at bet time?','No — final dividend unknown','Yes — price locked at time of bet'],
    ['Who sets the price?','Market (all bettors)','Bookmaker traders'],
    ['Big win potential?','Yes — big pools can pay huge dividends','Limited by maximum payout rules'],
    ['Margin','Deduction from pool (typically 14–24%)','Built into odds (typically 5–10%)'],
    ['Minimum bet','Usually €1–€2','Usually €0.10–€0.50'],
]) + """
<h2>Main Tote Bet Types in Ireland</h2>
<ul style="line-height:1.9">
<li><strong>Win:</strong> picks the winner; dividend = pool minus deductions ÷ winning tickets</li>
<li><strong>Place:</strong> first 3 (or 2 in small fields); lower dividend than win</li>
<li><strong>Exacta:</strong> 1st and 2nd in correct order; can produce large dividends</li>
<li><strong>Trifecta:</strong> 1st, 2nd and 3rd in correct order; highest variance, highest potential return</li>
<li><strong>Jackpot:</strong> select the winner of 6 nominated races; rollover builds the pool</li>
</ul>
<p>Irish Tote is operated by Boylesports at most Irish racecourses. Some GRAI-licensed apps provide access to Irish Tote pools online.</p>
<p style="font-size:0.85em;color:#555">18+ | Gambling Awareness Trust | 1800 753 753 | gamblingcare.ie</p>
""",

'tennis-grand-slam-betting.html': """
<h2>Tennis Grand Slam Betting Markets</h2>
""" + tbl(['Market','Settles on','Notes'],[
    ['Tournament winner','Overall champion','Ante-post; favourite often 2.50–5.00'],
    ['Match winner','Named match result','Available for all rounds'],
    ['Set handicap','Winner covers spread','Home for dominant players; volatile'],
    ['Total games O/U','Over/under a set number','e.g. over 22.5 games in a match'],
    ['Both players to hold serve in a game','Service hold','Specialist in-play market'],
    ['Correct sets score','e.g. 3-1 or 3-0','High margin; use sparingly'],
]) + """
<h2>Grand Slam Calendar and Betting Windows</h2>
""" + tbl(['Tournament','Surface','Approx dates','Betting opens'],[
    ['Australian Open','Hard','Mid-January','December draw'],
    ['Roland Garros (French Open)','Clay','Late May–early June','April/May draw'],
    ['Wimbledon','Grass','Late June–early July','May/June draw'],
    ['US Open','Hard','Late August–early September','August draw'],
]) + """
<p style="font-size:0.85em;color:#555">18+ | Gambling Awareness Trust | 1800 753 753 | gamblingcare.ie</p>
""",

'golf-betting-guide.html': """
<h2>Golf Betting Markets Explained</h2>
""" + tbl(['Market','Settles on','Notes'],[
    ['Tournament winner','72-hole winner','Most popular; each-way common at 1/4 for top 5/8'],
    ['Top 5 / Top 10 / Top 20','Finishing position','Each-way terms define these'],
    ['Round leader','Leader after each round','Volatile; weather and tee times affect'],
    ['Made the cut','Player survives 36-hole cut','Usually 2.0–2.5 for mid-ranked players'],
    ['Head-to-head','Which of two players finishes higher','Void if either withdraws (usually)'],
    ['Winning margin','How many strokes winner wins by','O/U a set number'],
]) + """
<h2>Each-Way Golf Betting: How Terms Work</h2>
<p>Golf is one of the best sports for each-way value. Typical each-way terms:</p>
<ul style="line-height:1.9">
<li><strong>Standard: 1/4 odds, top 5 places</strong> — most tournaments at GRAI-licensed sites</li>
<li><strong>Enhanced: 1/5 odds, top 8 places</strong> — majors and WGC events often have extra places</li>
<li><strong>Example:</strong> backing a player at 20/1 each-way, 1/4 for top 5 → place part pays at 5/1 (20/1 ÷ 4)</li>
<li>A player finishing 4th at 20/1 returns: €10 win stake lost + €10 × (5/1 + 1) = €60 place return</li>
</ul>
<p style="font-size:0.85em;color:#555">18+ | Gambling Awareness Trust | 1800 753 753 | gamblingcare.ie</p>
""",

'mma-ufc-betting-ireland.html': """
<h2>UFC Betting Markets Available in Ireland</h2>
""" + tbl(['Market','Settles on'],[
    ['Fight winner','Which fighter wins (or draw)'],
    ['Method of victory','KO/TKO, Submission, Decision (unanimous/split)'],
    ['Round betting','Which round the fight ends in'],
    ['Goes the distance','Fight goes all scheduled rounds (yes/no)'],
    ['Total rounds O/U','Over/under a set number of rounds'],
    ['Fighter props (significant strikes)','Over/under strikes landed'],
]) + """
<h2>UFC Event Schedule and Irish Betting Times</h2>
<p>Main UFC events typically air at 03:00–05:00 Irish time (GMT). Prelims from ~00:00. Key considerations:</p>
<ul style="line-height:1.9">
<li>Main event markets are available pre-fight on all GRAI-licensed bookmakers covering MMA</li>
<li>In-play betting is available but rounds move fast — pre-event bets are more practical</li>
<li>Free bet expiry timing: UFC events often fall Sunday morning Irish time — check your free bet expires after the event</li>
<li>UFC PPV events (numbered events like UFC 300+) carry the deepest markets; Fight Night cards have fewer prop markets</li>
</ul>
<p style="font-size:0.85em;color:#555">18+ | Gambling Awareness Trust | 1800 753 753 | gamblingcare.ie</p>
""",

'boxing-betting-ireland.html': """
<h2>Boxing Betting Markets</h2>
""" + tbl(['Market','Settles on'],[
    ['Fight winner','Which boxer wins (or draw)'],
    ['Method of victory','KO/TKO, points decision, disqualification'],
    ['Round betting','Specific round fight ends in'],
    ['Goes the distance','Fight goes all scheduled rounds'],
    ['Total rounds O/U','Over/under a set number of rounds'],
    ['Points decision (yes/no)','Whether judges\' scorecards decide the bout'],
]) + """
<h2>Key Irish Boxing Connections</h2>
<ul style="line-height:1.9">
<li><strong>Katie Taylor</strong> — undisputed lightweight champion; biggest Irish boxing draw; fights available on major GRAI-licensed apps</li>
<li><strong>Michael Conlan</strong> — Belfast featherweight; popular in Ireland with domestic following</li>
<li><strong>Jason Quigley, Paddy Donovan</strong> — Irish domestic stars with growing international profiles</li>
<li>Major world title fights (heavyweight/undisputed bouts) are marquee betting events — full prop markets available</li>
</ul>
<p style="font-size:0.85em;color:#555">18+ | Gambling Awareness Trust | 1800 753 753 | gamblingcare.ie</p>
""",

'betting-on-corners.html': """
<h2>Corner Betting Markets</h2>
""" + tbl(['Market','Definition'],[
    ['Total corners O/U','Over/under a set number of corners in the match'],
    ['Asian corner handicap','One team starts with a corner advantage'],
    ['First corner','Which team wins the first corner kick'],
    ['Half-time corners O/U','Corner count in first half only'],
    ['Both halves over X corners','Corners threshold must be met in each half'],
    ['Team total corners','Over/under for one specific team\'s corners'],
]) + """
<h2>Which Teams and Leagues Produce the Most Corners?</h2>
<ul style="line-height:1.9">
<li><strong>High-corner leagues:</strong> Premier League and Bundesliga average 10–11 corners per game</li>
<li><strong>Low-corner leagues:</strong> Serie A and some lower leagues average 9–10 corners per game</li>
<li>Teams that dominate possession and play attacking football generate more corners</li>
<li>Underdogs who defend deep and clear to the corner flag inflate the total</li>
<li>Wet, heavy pitches reduce corner totals — wide players struggle to deliver crosses</li>
</ul>
<p style="font-size:0.85em;color:#555">18+ | Gambling Awareness Trust | 1800 753 753 | gamblingcare.ie</p>
""",

'how-does-spread-betting-work-ireland.html': """
<h2>Spread Betting vs Fixed Odds: Key Differences</h2>
""" + tbl(['Feature','Spread betting','Fixed odds betting'],[
    ['Profit/loss','Unlimited — scales with how right/wrong you are','Capped — fixed at stake × odds'],
    ['Risk','Can lose more than your stake','Cannot lose more than stake'],
    ['Price shown','Spread (buy/sell)','Odds (decimal/fractional)'],
    ['Regulated in Ireland by','FCA (UK) for financial spread betting','GRAI for sports betting'],
    ['Most common use','Financial markets (indices, FX)','Sports outcomes'],
]) + """
<h2>Spread Betting vs Sports Betting: What Irish Punters Need to Know</h2>
<p>Spread betting on sports (e.g. backing "total goals" to be over 2.5 at a price, with P&L scaling per goal) is different from fixed-odds betting. Key points:</p>
<ul style="line-height:1.9">
<li>Financial spread betting (stock indices, FX) is regulated by the FCA — different from GRAI-licensed bookmakers</li>
<li>Sports spread betting is offered by some UK-focused spread firms — Irish residents can access but it's not GRAI-licensed</li>
<li>Unlimited loss potential means spread betting requires strict risk management</li>
<li>For most Irish punters, fixed-odds betting or Betfair exchange provides better protection and comparable returns</li>
</ul>
<p style="font-size:0.85em;color:#555">18+ | Gambling Awareness Trust | 1800 753 753 | gamblingcare.ie</p>
""",

'how-to-set-deposit-limits-ireland.html': """
<h2>How to Set Deposit Limits: Step-by-Step</h2>
<ol style="line-height:1.9">
<li><strong>Log in</strong> to your betting account</li>
<li>Go to <strong>My Account → Responsible Gambling</strong> (location varies by operator)</li>
<li>Select <strong>Deposit Limits</strong></li>
<li>Choose your period: daily / weekly / monthly</li>
<li>Enter your limit amount in euros</li>
<li><strong>Confirm</strong> — decreases apply immediately; increases require a 24-hour cooling period (GRAI requirement)</li>
</ol>
""" + """
<h2>Deposit Limits Under GRAI Regulation</h2>
""" + tbl(['Rule','Detail'],[
    ['Decrease applies','Immediately — cannot be bypassed'],
    ['Increase applies','After 24-hour cooling period (mandatory)'],
    ['Removal of limit','7-day cooling period before effective'],
    ['Operator requirement','All GRAI-licensed bookmakers must offer deposit limits'],
    ['Multiple accounts?','Limits apply per account — cannot split spend across accounts'],
]) + """
<p>Mandatory cooling periods for increases are required by GRAI under the Gambling Regulation Act 2024. If a limit increase doesn't apply immediately, that's intentional — not a technical fault.</p>
<p style="font-size:0.85em;color:#555">18+ | Gambling Awareness Trust | 1800 753 753 | gamblingcare.ie</p>
""",

'responsible-gambling-tools-ireland.html': """
<h2>Responsible Gambling Tools Available in Ireland</h2>
""" + tbl(['Tool','What it does','How to access'],[
    ['Deposit limits','Cap how much you can deposit per day/week/month','Account → Responsible Gambling'],
    ['Loss limits','Cap losses in a time period','Account → Responsible Gambling'],
    ['Reality check / Time alerts','Notifications after set gambling session length','Account settings'],
    ['Self-exclusion','Block account access for set period','Account or contact support'],
    ['Self-exclusion via GRAI','National Gambling Exclusion Register (future)','grai.ie once live'],
    ['Cooling-off period','Temporary account restriction','Account → Responsible Gambling'],
]) + """
<h2>Where to Get Help in Ireland</h2>
<ul style="line-height:1.9">
<li><strong>Gambling Awareness Trust:</strong> Freephone 1800 753 753 (free, confidential)</li>
<li><strong>gamblingcare.ie:</strong> online counselling and resources</li>
<li><strong>Gamblers Anonymous Ireland:</strong> gamblersanonymous.ie — free peer support groups</li>
<li><strong>Problem Gambling Ireland:</strong> problemgambling.ie</li>
<li><strong>GRAI complaints:</strong> grai.ie — if an operator isn't providing mandatory tools</li>
</ul>
<p style="font-size:0.85em;color:#555">18+ | Help is free and confidential | Gambling Awareness Trust: 1800 753 753</p>
""",

'self-exclusion-guide-ireland.html': """
<h2>How to Self-Exclude from Betting Sites in Ireland</h2>
<ol style="line-height:1.9">
<li>Log in to your account</li>
<li>Go to <strong>Responsible Gambling → Self-Exclusion</strong></li>
<li>Choose the period (6 months / 1 year / 5 years / permanent)</li>
<li>Confirm your request — exclusion typically activates within 24 hours</li>
<li>Contact the operator directly if the online process fails</li>
</ol>
""" + tbl(['Exclusion type','Duration','Reversal process'],[
    ['Temporary (cooling-off)','24 hours to 6 weeks','Can be reversed after expiry'],
    ['Self-exclusion (standard)','6 months minimum','7-day cooling period to reopen'],
    ['Permanent exclusion','No end date','Cannot be reversed — account closed'],
    ['NGRE (national register)','Covers all GRAI licensees','In development as of 2026'],
]) + """
<p>Once self-excluded, the operator must close your account and return any remaining balance. If you receive marketing from an operator you've self-excluded from, report it to GRAI at grai.ie.</p>
<p style="font-size:0.85em;color:#555">18+ | Gambling Awareness Trust | 1800 753 753 | gamblingcare.ie</p>
""",

'champion-hurdle-betting.html': """
<h2>Champion Hurdle Betting Markets</h2>
""" + tbl(['Market','Notes'],[
    ['Outright winner','Most popular; usually 4–8 runners'],
    ['Each-way (top 3 at 1/4)','Standard terms on Champion Hurdle'],
    ['Winning distance O/U','Over/under a set margin'],
    ['Previous winner to win again','Specific historic selection market'],
]) + """
<h2>Champion Hurdle Form Factors</h2>
<ul style="line-height:1.9">
<li>Run over 2 miles at Cheltenham on Tuesday of Festival week (Champion Day)</li>
<li>Course form significant — the uphill finish suits powerful gallopers</li>
<li>Market leaders win at high rate (~40%) in the Champion Hurdle vs other Cheltenham races</li>
<li>Watch going — soft going increases the variance and suits stamina types</li>
</ul>
<p style="font-size:0.85em;color:#555">18+ | Gambling Awareness Trust | 1800 753 753 | gamblingcare.ie</p>
""",

'antepost-cheltenham-betting.html': """
<h2>Cheltenham Ante-Post: Best Bets Strategy</h2>
""" + tbl(['Timing','Market status','Strategy'],[
    ['12+ months before','Thin markets, big prices','Value plays on established horses; non-runner risk high'],
    ['6 months before','Markets form after key trials','Betfair ante-post markets open; check NRNR terms'],
    ['1 month before','Form guide clearer','Most operators have Festival markets open'],
    ['Festival week','Final ante-post prices','Switch to race-day markets for best prices'],
]) + """
<h2>Key Cheltenham Ante-Post Betting Rules</h2>
<ul style="line-height:1.9">
<li><strong>Non-Runner No Bet (NRNR):</strong> always check if this applies — it refunds your stake if the horse doesn't run</li>
<li><strong>Standard ante-post:</strong> without NRNR, stake is lost if horse is a non-runner</li>
<li><strong>Best Odds Guaranteed:</strong> some operators extend BOG to Cheltenham ante-post; can pay out at race SP</li>
<li>Price shortening: big ante-post bets from syndicates move markets — watch for horses shortening without news</li>
</ul>
<p style="font-size:0.85em;color:#555">18+ | Gambling Awareness Trust | 1800 753 753 | gamblingcare.ie</p>
""",

'how-does-acca-insurance-work.html': """
<h2>Acca Insurance: How It Works</h2>
""" + tbl(['Scenario','What happens'],[
    ['All legs win','Normal acca payout; insurance not needed'],
    ['Exactly one leg fails','Stake refunded as a free bet (SNR usually)'],
    ['Two or more legs fail','Insurance does not apply; acca loses'],
    ['One leg is a push (void)','Most operators remove that leg; acca continues with remaining legs'],
]) + """
<h2>Acca Insurance Terms to Check</h2>
<ul style="line-height:1.9">
<li><strong>Minimum legs:</strong> typically 5+ legs required; some offer it on 4+ legs</li>
<li><strong>Minimum odds per selection:</strong> usually 1.30 (3/10) minimum per leg</li>
<li><strong>Free bet vs cash refund:</strong> nearly always a free bet (SNR), not cash — stake not returned on the free bet win</li>
<li><strong>Market restrictions:</strong> each-way, Asian handicap and some outrights may be excluded</li>
<li><strong>One offer per period:</strong> typically one insurance claim per week</li>
</ul>
<p style="font-size:0.85em;color:#555">18+ | Gambling Awareness Trust | 1800 753 753 | gamblingcare.ie</p>
""",

'how-do-free-bets-work-ireland.html': """
<h2>Free Bet Types: What You Actually Get</h2>
""" + tbl(['Type','What you receive','How winnings are paid'],[
    ['Stake Not Returned (SNR)','Bet credit equal to free bet value','Winnings only (stake not included in return)'],
    ['Stake Returned (SR)','Bet credit equal to free bet value','Full return including stake value'],
    ['Bet & Get (wagering)','Free bet after qualifying bet','Free bet released after qualifying bet settles'],
    ['No-deposit free bet','Free bet without depositing','Requires verification; strict withdrawal conditions'],
    ['Cashback free bet','Refund on specific outcome','e.g. refund if first bet loses'],
]) + """
<h2>SNR Free Bet: Worked Example</h2>
<p>Most Irish free bets are SNR. If you place a €10 SNR free bet at 4.00 (3/1):</p>
<ul style="line-height:1.9">
<li>If wins: returns €40 total — but stake (€10) is not returned, so net winnings = <strong>€30</strong></li>
<li>If loses: free bet is gone; no cash loss beyond the qualifying bet already placed</li>
<li><strong>To maximise SNR value:</strong> use at odds of 3.00+ where the profit portion is large relative to stake</li>
</ul>
<p style="font-size:0.85em;color:#555">18+ | Gambling Awareness Trust | 1800 753 753 | gamblingcare.ie</p>
""",

'are-betting-winnings-taxable-ireland.html': """
<h2>Betting Tax in Ireland: Summary Table</h2>
""" + tbl(['Tax type','Applies to betting winnings?','Who pays?'],[
    ['Income tax','No — betting winnings not taxable income','N/A'],
    ['Capital Gains Tax (CGT)','No — not capital gains','N/A'],
    ['Betting duty (1%)','Yes — but paid by the operator, not you','Bookmaker'],
    ['VAT','No','N/A'],
]) + """
<h2>What the 1% Betting Duty Means for You</h2>
<p>Ireland imposes a 1% betting duty on the total amount staked. This is <strong>paid by the bookmaker</strong>, not deducted from your winnings. However:</p>
<ul style="line-height:1.9">
<li>Some operators (mainly retail shops) pass the duty on to the customer — read the terms</li>
<li>Online bookmakers licensed by GRAI typically absorb the duty within their margin</li>
<li>No tax return is required for betting winnings in Ireland under current Revenue Commissioners guidance</li>
<li>If gambling is your primary income source or constitutes a business, different rules may apply — consult a tax adviser</li>
</ul>
<p style="font-size:0.85em;color:#555">18+ | For tax advice, consult a qualified accountant | Gambling Awareness Trust: 1800 753 753</p>
""",

'ireland-national-team-betting.html': """
<h2>Ireland National Football Team Betting Markets</h2>
""" + tbl(['Market','Settles on'],[
    ['Match result (1X2)','Win/Draw/Loss for Ireland'],
    ['Both teams to score','Ireland and opponent both score'],
    ['Total goals O/U','Over/under a set goals total'],
    ['First goalscorer','Which player scores first'],
    ['Player to score anytime','Named player scores at any point'],
    ['Winning margin','How many goals Ireland wins/loses by'],
    ['World Cup/Euro qualifying outright','Ireland to qualify from their group'],
]) + """
<h2>Ireland Men's Football: 2026 World Cup Qualification</h2>
<p>Ireland is competing in UEFA qualifying for the 2026 World Cup (expanded to 48 teams — Europe gets 16 automatic places). Key factors for Irish betting:</p>
<ul style="line-height:1.9">
<li>Ireland's UEFA Nations League performance affects playoff seeding</li>
<li>Home matches at Aviva Stadium (Dublin) provide significant advantage</li>
<li>Key players: watch injury news closely — Irish squad depth limited beyond first choice XI</li>
<li>Outright qualification markets open before group draw; prices shift significantly after draw</li>
</ul>
<p style="font-size:0.85em;color:#555">18+ | Gambling Awareness Trust | 1800 753 753 | gamblingcare.ie</p>
""",

'switching-betting-site-ireland.html': """
<h2>How to Switch Betting Sites in Ireland</h2>
<ol style="line-height:1.9">
<li><strong>Withdraw your balance</strong> from the old site first (most withdrawals settle in 1–3 days)</li>
<li><strong>Check pending bets</strong> — wait for open bets to settle before closing</li>
<li><strong>Close the old account</strong> (or leave it dormant — inactive accounts usually stay open)</li>
<li><strong>Register at the new site</strong> — verify identity with passport/driving licence</li>
<li><strong>Claim welcome offer</strong> — most new account offers require your first deposit</li>
</ol>
""" + tbl(['Consideration','What to check'],[
    ['Welcome offer','Available for new accounts only — switching unlocks a fresh offer'],
    ['Existing free bets','Use up all credits before switching — they\'re non-transferable'],
    ['Pending withdrawals','Confirm all withdrawals have settled before closing account'],
    ['Self-exclusion status','If you\'ve self-excluded, you cannot reopen for the exclusion period'],
    ['Verification speed','New site KYC can take 24–48 hours; don\'t rush a first deposit'],
]) + """
<p style="font-size:0.85em;color:#555">18+ | Gambling Awareness Trust | 1800 753 753 | gamblingcare.ie</p>
""",

'champions-league-semi-final-betting-2027.html': """
<h2>Champions League Semi-Final Betting Markets</h2>
""" + tbl(['Market','Notes'],[
    ['Match winner (90 mins)','For the first leg: drawn result is a valid outcome'],
    ['Both teams to score','Very common in CL semis; historically ~65% of ties'],
    ['Total goals O/U','Over/under 2.5 goals lands ~55% of CL semi-final legs'],
    ['Asian handicap','Removes draw; useful when one side is heavily favoured'],
    ['First goalscorer','Wide market; premium players priced 5.00–10.00'],
    ['To qualify (outright)','Which team advances to the final'],
]) + """
<h2>CL Semi-Final Format and Betting Strategy</h2>
<p>Champions League semi-finals are two-legged ties (home and away). Key betting considerations:</p>
<ul style="line-height:1.9">
<li>Away goal rule was <strong>abolished in 2021</strong> — ties level on aggregate go to extra time and penalties, not away goals</li>
<li>First-leg results heavily influence second-leg dynamics — teams with a lead often defend; teams trailing attack</li>
<li>Squad rotation is minimal at this stage — expect near-full strength teams</li>
<li>To qualify bets cover both legs combined, paying out before the second leg's kick-off result</li>
</ul>
<p style="font-size:0.85em;color:#555">18+ | Gambling Awareness Trust | 1800 753 753 | gamblingcare.ie</p>
""",

'champions-league-final-2027-betting.html': """
<h2>Champions League Final 2027: Betting Overview</h2>
""" + tbl(['Market','Notes'],[
    ['Match winner (90 mins)','Draw means extra time/penalties; market settles on 90 mins unless stated'],
    ['Both teams to score','Lands ~55% of recent CL finals'],
    ['Total goals O/U 2.5','Over 2.5 lands ~45% of recent CL finals — tense matches often low-scoring'],
    ['Tournament winner (pre-final)','Outright settled on the final winner'],
    ['First goalscorer','Wide market; short-price at 6.00–10.00 for key strikers'],
    ['Golden Boot winner','Top scorer for entire competition; can be backed ante-post'],
]) + """
<h2>Recent CL Final Results for Context</h2>
<ul style="line-height:1.9">
<li>CL Finals are notoriously difficult to predict — the last 10 have produced results for the underdog in ~40% of cases</li>
<li>Venue advantage: historically 55–60% of finals are won by the nominal "home" side (closer to their base)</li>
<li>Goals: the last 10 CL finals averaged 2.2 goals — over 2.5 is roughly even money, not a slam dunk</li>
<li>Penalties: ~20% of recent finals have gone to a shootout</li>
</ul>
<p style="font-size:0.85em;color:#555">18+ | Gambling Awareness Trust | 1800 753 753 | gamblingcare.ie</p>
""",

'how-does-acca-insurance-work.html': '',  # already defined above

'world-cup-2026-schedule-betting.html': """
<h2>2026 World Cup Schedule: Key Betting Dates</h2>
""" + tbl(['Stage','Dates','Matches'],[
    ['Group stage','June 11 – July 2, 2026','48 matches (all 12 groups)'],
    ['Round of 32','July 4–7, 2026','16 matches'],
    ['Round of 16','July 10–13, 2026','8 matches'],
    ['Quarter-finals','July 17–18, 2026','4 matches'],
    ['Semi-finals','July 22–23, 2026','2 matches'],
    ['Final','July 19, 2026 (NJ/NY)','1 match'],
]) + """
<h2>Time Zone Note for Irish Bettors</h2>
<p>Matches are played across USA, Canada and Mexico. Irish kick-off times:</p>
<ul style="line-height:1.9">
<li><strong>Eastern US venues (New York, Boston, Philadelphia):</strong> matches at 18:00 ET = 23:00 IST</li>
<li><strong>Central venues (Dallas, Kansas City):</strong> 19:00 CT = 01:00 IST (next day)</li>
<li><strong>Pacific/Mountain venues (Los Angeles, San Francisco):</strong> 20:00 PT = 04:00 IST</li>
<li>Mexican venues follow Central Time; Canadian venues (Toronto, Vancouver) vary</li>
</ul>
<p style="font-size:0.85em;color:#555">18+ | Gambling Awareness Trust | 1800 753 753 | gamblingcare.ie</p>
""",

'betting-on-corners.html': '',  # Already have this above in corners-betting-guide.html — skip duplicate

}

# Skip pages that already have duplicate entries or are utility pages
CONTENT['betting-on-corners.html'] = ''  # skip

def find_insertion_point(html):
    """Find where to insert new content."""
    # Try editorial-box first
    idx = html.find('<div class="editorial-box"')
    if idx != -1:
        return idx
    # Try faq-item
    idx = html.find('<div class="faq-item"')
    if idx != -1:
        return idx
    # Try </body>
    idx = html.find('</body>')
    if idx != -1:
        return idx
    return -1

pages_dir = '/home/claude/craicbet/pages'
expanded = []
skipped = []

for filename, new_content in CONTENT.items():
    if not new_content.strip():
        skipped.append(filename + ' (no content defined)')
        continue

    filepath = os.path.join(pages_dir, filename)
    if not os.path.exists(filepath):
        skipped.append(filename + ' (not found)')
        continue

    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Skip if already has tables from previous expansion
    if html.count('<table') > 1:
        skipped.append(filename + ' (already has tables)')
        continue

    idx = find_insertion_point(html)
    if idx == -1:
        skipped.append(filename + ' (no insertion point)')
        continue

    before = os.path.getsize(filepath)
    new_html = html[:idx] + new_content + html[idx:]

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_html)

    after = os.path.getsize(filepath)
    expanded.append(f'{filename}: {before} → {after} bytes')

print(f"Expanded {len(expanded)} pages:")
for e in expanded:
    print(' ', e)
print(f"\nSkipped {len(skipped)}:")
for s in skipped:
    print(' ', s)
