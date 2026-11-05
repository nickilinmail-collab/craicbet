#!/usr/bin/env python3
"""Batch 9c: remaining thin content pages."""
import os

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

def tbl(headers, rows):
    out = f'\n<table {TABLE}>\n'
    out += hrow(headers) + '\n'
    for i, r in enumerate(rows):
        out += row(r, alt=(i%2==1)) + '\n'
    return out + '</table>\n'

RG = '<p style="font-size:0.85em;color:#555;margin-top:12px">18+ only. Gambling Awareness Trust: 1800 753 753 | gamblingcare.ie</p>\n'

CONTENT = {

'betting-shops-dublin.html': """
<h2>Dublin Betting Shops: What to Expect</h2>
""" + tbl(['Area','Key bookmakers present'],[
    ['City Centre (O\'Connell St, Henry St)','Multiple major chains; highest footfall'],
    ['Rathmines / Rathgar','Suburban shops; quieter atmosphere'],
    ['Tallaght / Clondalkin','Retail parks; newer-format shops with self-service terminals'],
    ['Ballyfermot / Crumlin','Traditional neighbourhood betting shops'],
    ['Dún Laoghaire','Mixed retail; several major chains'],
]) + """
<h2>Online Betting vs Dublin Betting Shops</h2>
<ul style="line-height:1.9">
<li><strong>Betting shops:</strong> cash accepted; immediate settlement; social atmosphere for horse racing</li>
<li><strong>Online:</strong> BOG (best odds guaranteed), live streaming, cash-out, wider markets, in-play betting</li>
<li>Many Dublin punters use both — shops for atmosphere on big race days; online for value and convenience</li>
<li>All Dublin betting shops must hold a GRAI retail licence; online operators need a GRAI remote betting licence</li>
</ul>
""" + RG,

'betting-site-comparison-ireland.html': """
<h2>How to Compare Betting Sites</h2>
""" + tbl(['Feature','What good looks like'],[
    ['Licence','GRAI remote betting licence (grai.ie/register) or MGA/UKGC'],
    ['Odds margin','5–6% on 1X2 markets (compare the same game across sites)'],
    ['Irish sports','GAA (football + hurling), horse racing, Leagues of Ireland, rugby'],
    ['Welcome offer T&Cs','Wagering requirement under 5x; short odds minimum'],
    ['Withdrawal methods','Revolut, card, bank transfer — all with no fee'],
    ['Responsible gambling','Deposit limits, self-exclusion, reality checks — mandatory under GRAI'],
]) + """
<h2>Quick Odds Comparison Method</h2>
<ul style="line-height:1.9">
<li>Pick any Premier League match at the weekend and check the 1X2 odds on two sites</li>
<li>Add the implied probabilities (1 ÷ each decimal odd) — the lower the total, the lower the margin</li>
<li>A total of 1.055 = 5.5% margin; 1.08 = 8% margin — 2.5 percentage points difference adds up over a season</li>
<li>BOG (best odds guaranteed) on horse racing is a free upgrade — always use it when available</li>
</ul>
""" + RG,

'betting-sites-carlow.html': """
<h2>Online Betting from Carlow</h2>
""" + tbl(['Option','Detail'],[
    ['GRAI-licensed sites','Full access from Carlow — all major operators serve Republic of Ireland'],
    ['Deposit methods','Card, Revolut, bank transfer, PayPal — all work from Carlow'],
    ['Local GAA coverage','Carlow GAA club and county matches available on GRAI-licensed apps'],
    ['Horse racing','Gowran Park is the nearest racecourse — markets open from early morning'],
]) + """
<h2>What to Look for in an Online Betting Site</h2>
<ul style="line-height:1.9">
<li>Verify GRAI remote betting licence at grai.ie/register</li>
<li>Check it covers GAA football and hurling, plus Irish horse racing ante-post</li>
<li>Revolut and card deposits are instant — no waiting for funds to appear</li>
<li>Responsible gambling tools: deposit limits and self-exclusion are mandatory for GRAI licensees</li>
</ul>
""" + RG,

'fai-cup-betting.html': """
<h2>FAI Cup Betting Markets</h2>
""" + tbl(['Market','Notes'],[
    ['Match winner','Draw means replay (later rounds: extra time + penalties — confirm format)'],
    ['Both teams to score','Land ~52% of FAI Cup matches'],
    ['Total goals O/U','Over 2.5 is roughly even money in FAI Cup games'],
    ['Tournament winner (outright)','Shamrock Rovers, Dundalk, Shelbourne, St Patrick\'s Athletic — regular contenders'],
    ['First scorer','Wide market; League of Ireland strikers priced 4.00–10.00'],
]) + """
<h2>FAI Cup: Format Overview</h2>
<ul style="line-height:1.9">
<li>Open to all clubs affiliated with the Football Association of Ireland — including lower league clubs</li>
<li>Premier Division clubs enter at the last 32 stage — potential upset opportunities in early rounds</li>
<li>Final played at the Aviva Stadium (capacity ~51,700) — a prestige venue for Irish football</li>
<li>Past winners: Shamrock Rovers and Dundalk dominate but upsets happen — Bohemians, Derry City, St Patrick\'s Athletic win regularly</li>
</ul>
""" + RG,

'handicap-betting-explained.html': """
<h2>Types of Handicap Betting</h2>
""" + tbl(['Type','How it works'],[
    ['European handicap (whole numbers)','e.g. -1 handicap: team must win by 2+ for your bet to win; win by 1 = push'],
    ['Asian handicap (half-line)','e.g. -1.5: team must win by 2+ for your bet to win; no push (draw impossible)'],
    ['Asian handicap (split-line)','e.g. -1 / -1.5: stake split between two lines'],
    ['GAA points handicap','-3.5 points: team must win by 4+ for your bet to win'],
    ['Rugby points handicap','-7.5 points: team must win by 8+ for your bet to win'],
]) + """
<h2>When to Use Handicap vs Standard Match Result</h2>
<ul style="line-height:1.9">
<li><strong>Use handicap:</strong> when one team is heavily favoured at short odds (1.20–1.40) — handicap gives better value</li>
<li><strong>Use Asian handicap:</strong> when you want to avoid the draw — the -0.5 line removes it entirely</li>
<li><strong>Use standard 1X2:</strong> for closely matched games where the draw is a live outcome you want to include</li>
<li>Handicap margin is typically 2–4% vs 5–8% for standard 1X2 — better value on the same event</li>
</ul>
""" + RG,

'how-odds-are-set.html': """
<h2>How Bookmakers Set Their Odds</h2>
""" + tbl(['Step','What happens'],[
    ['1. Base probability model','Statistical model using form, stats, Elo ratings, market data'],
    ['2. Adjust for news','Injuries, suspensions, weather, team news updated in real time'],
    ['3. Apply margin','Overround added to implied probabilities (total > 100%)'],
    ['4. Market comparison','Prices aligned with competitors to avoid being badly out of line'],
    ['5. Live adjustment','Prices change as bets come in (liability management)'],
]) + """
<h2>What Moves Odds: The Main Factors</h2>
<ul style="line-height:1.9">
<li><strong>Injury news:</strong> a star player ruled out can shorten a team\'s odds from 2.20 to 1.70 in minutes</li>
<li><strong>Bet volumes:</strong> heavy money on one side shortens that side; bookmakers lay off or adjust prices</li>
<li><strong>Sharp money:</strong> bets from known professional punters move odds faster than recreational money</li>
<li><strong>Market alignment:</strong> bookmakers watch exchange prices (Betfair) and each other constantly</li>
<li>Taking the early price before team news is a key advantage for experienced punters</li>
</ul>
""" + RG,

'how-to-download-betting-app-ireland.html': """
<h2>How to Download a Betting App in Ireland</h2>
<ol style="line-height:1.9">
<li>Find a GRAI-licensed betting site (verify at grai.ie/register)</li>
<li>Visit the official website on your phone browser</li>
<li><strong>iPhone:</strong> search the App Store, or use the site\'s direct App Store link</li>
<li><strong>Android:</strong> most operators provide a direct APK download — download only from the official site, never a third-party store</li>
<li>Enable "Install from unknown sources" in Android settings if prompted (Android security setting)</li>
<li>Log in with your existing account or register — KYC required before first withdrawal</li>
</ol>
""" + tbl(['Platform','Where to get the app'],[
    ['iOS (iPhone/iPad)','App Store — search the operator name, or use the site\'s App Store link'],
    ['Android','Direct APK download from operator\'s official site (not Play Store for most)'],
    ['Mobile web','No download needed — the mobile site works without an app'],
]) + RG,

'ireland-international-football-betting.html': """
<h2>Republic of Ireland International Football: Key Betting Markets</h2>
""" + tbl(['Market','Notes'],[
    ['Match winner (1X2)','Available for all friendly and competitive matches'],
    ['Both teams to score','Ireland average ~1.2 goals per game — BTTS varies by opposition'],
    ['Correct score','Ireland often involved in tight 1-0 or 0-0 results in competitive football'],
    ['Tournament outright','Euro qualification, World Cup qualification — ante-post markets'],
    ['Top scorer (campaign)','Wide market; priced 4.00–12.00 for Irish strikers'],
]) + """
<h2>Recent Ireland Performance Context</h2>
<ul style="line-height:1.9">
<li>Republic of Ireland ranked in the 40s–50s in FIFA rankings — competitive in European qualifying but rarely favourites</li>
<li>Home matches at the Aviva Stadium (Dublin) — 51,700 capacity; Ireland benefit from home support</li>
<li>Key players: typically mid-table Premier League and Championship performers — form check is essential before betting</li>
<li>Stephen Kenny era ended 2023; check current manager and style before placing outright bets</li>
</ul>
""" + RG,

'lay-betting-guide.html': """
<h2>How Lay Betting Works</h2>
""" + tbl(['Scenario','Back bet','Lay bet'],[
    ['Team wins the match','You win if they win','You win if they DON\'T win'],
    ['Horse wins the race','You win if it wins','You win if it doesn\'t win'],
    ['Liability','Fixed to your stake','Up to (odds - 1) × stake'],
]) + """
<h2>Key Lay Betting Terms</h2>
<ul style="line-height:1.9">
<li><strong>Lay price:</strong> the price you offer to pay if the selection wins (you are the bookmaker)</li>
<li><strong>Liability:</strong> (decimal odds - 1) × stake. E.g. laying at 5.0 for €10: liability = €40</li>
<li><strong>Exchanges:</strong> Betfair Exchange is the main platform for lay betting in Ireland — 2–5% commission on net winnings</li>
<li><strong>When to lay:</strong> when you believe a selection is overpriced (odds too short for the true chance of winning)</li>
<li>Lay betting involves unlimited liability in theory — the horse could win at 100/1 when you laid it</li>
</ul>
""" + RG,

'new-years-day-betting-ireland.html': """
<h2>New Year\'s Day Betting: What\'s On in Ireland</h2>
""" + tbl(['Sport','Key events on 1 January'],[
    ['Horse racing','Tramore Races — most popular Irish racing day of the year'],
    ['Football','Premier League fixtures (most years); La Liga/Serie A resume'],
    ['GAA','No major GAA on 1 January'],
    ['NFL','Week 17–18 of NFL season; multiple games'],
    ['Rugby','Festive derbies in Premiership Rugby (UK)'],
]) + """
<h2>New Year\'s Day Betting Tips</h2>
<ul style="line-height:1.9">
<li><strong>Tramore:</strong> BOG available at all major Irish bookmakers; quality fields on New Year\'s Day</li>
<li><strong>Premier League:</strong> fixture release gives good advance notice — form guides are well-established by game week 20</li>
<li><strong>NFL:</strong> late-season games carry playoff seeding implications — motivations are clearer than mid-season</li>
<li>Responsible gambling reminder: set a budget for the day before you start — the holiday atmosphere can lead to larger stakes</li>
</ul>
""" + RG,

'six-nations-2027-top-scorer-betting.html': """
<h2>Six Nations Top Points Scorer: Betting Guide</h2>
""" + tbl(['Points source','Value'],[
    ['Try','5 points'],
    ['Conversion','2 points'],
    ['Penalty goal','3 points'],
    ['Drop goal','3 points'],
]) + """
<h2>Key Considerations for Six Nations Top Scorer Betting</h2>
<ul style="line-height:1.9">
<li>Fly-halves and full-backs dominate this market — kickers accumulate points across all 5 games</li>
<li>A kicker from a top team (Ireland, England, France) in a good run will beat a try scorer from a weaker nation</li>
<li>Try scorers offer value as dark horses — a winger on a great run can score 4–5 tries across the tournament</li>
<li>Joint top scorer rule varies by operator — check if they pay full or fractional for ties</li>
<li>Ireland, France and England have dominated Six Nations in recent years — back their kickers as base</li>
</ul>
""" + RG,

'six-nations-2027-wooden-spoon-betting.html': """
<h2>Six Nations Wooden Spoon: What It Is and How to Bet</h2>
""" + tbl(['Scenario','Notes'],[
    ['Wooden spoon','Last place in the final Six Nations table (5 games, fewest points'],
    ['Grand slam','Win all 5 games — positive equivalent of wooden spoon'],
    ['Outright last','Settles at end of tournament — mid-tournament changes affect prices significantly'],
]) + """
<h2>Key Wooden Spoon Contenders</h2>
<ul style="line-height:1.9">
<li>Italy and Scotland are historically most likely to be wooden spoon contenders — but both have improved significantly</li>
<li>Italy have been competitive in recent editions — no longer automatic wooden spoon candidates</li>
<li>Wales have struggled in the mid-2020s — often in wooden spoon contention</li>
<li>Wooden spoon at 3/1–6/1 for weaker nations can be backed as a hedge against a good run from that nation</li>
<li>Price shortens rapidly if a team loses their first 2–3 games — best value is pre-tournament</li>
</ul>
""" + RG,

'what-is-accumulator-bet-ireland.html': """
<h2>How an Accumulator Works</h2>
""" + tbl(['Legs','Minimum name','How winnings accumulate'],[
    ['2','Double','Winnings from leg 1 become stake for leg 2'],
    ['3','Treble','Winnings from legs 1+2 become stake for leg 3'],
    ['4','Fourfold','Continuing accumulation'],
    ['5+','Fivefold, sixfold...','Each leg multiplies the running return'],
]) + """
<h2>Accumulator Example: 5-team Acca</h2>
<p>Backing 5 football matches, each at 2.00 (evens), €10 stake:</p>
<ul style="line-height:1.9">
<li>All 5 win: €10 × 2 × 2 × 2 × 2 × 2 = <strong>€320</strong></li>
<li>4 of 5 win: total loss (€10 gone) — the fourth leg kills the acca</li>
<li>The combined probability (at fair odds): 50% × 50% × 50% × 50% × 50% = 3.1%</li>
<li>With bookmaker margin (~5% per leg): combined chance of winning drops to ~2.5%</li>
<li>The expected value is negative — but the high potential return is the appeal</li>
</ul>
""" + RG,

'world-cup-2026-group-stage-betting.html': """
<h2>World Cup 2026 Group Stage: Format and Betting</h2>
""" + tbl(['Feature','Detail'],[
    ['Teams','48 teams (expanded from 32)'],
    ['Groups','12 groups of 4 teams'],
    ['Qualification','Top 2 from each group + 8 best third-placed teams → Round of 32'],
    ['Games','3 group stage games per team'],
    ['Hosts','USA, Canada, Mexico (all automatic qualifiers)'],
]) + """
<h2>Key Group Stage Betting Markets</h2>
<ul style="line-height:1.9">
<li><strong>Group winner:</strong> ante-post from group draw; most popular group stage market</li>
<li><strong>To qualify:</strong> which 2 teams advance from each group — wider margin but more achievable</li>
<li><strong>Match result (1X2):</strong> individual group stage game markets open 2–4 weeks before kick-off</li>
<li><strong>Total goals:</strong> group stage games often produce goals — favourites tend to win comfortably vs weaker opponents</li>
<li>With 48 teams, more mismatches expected — heavy handicap betting (+3.5 goals) can represent value in some group games</li>
</ul>
""" + RG,

'bc-game-vs-mystake-ireland.html': """
<h2>Crypto Gambling Sites in Ireland: Key Checks</h2>
""" + tbl(['Check','Why it matters'],[
    ['Licence','MGA, UKGC or GRAI licence; Curaçao licence = minimal Irish protection'],
    ['Crypto payment methods','Which coins accepted (BTC, ETH, USDT, etc.)'],
    ['Fiat deposit option','Can you deposit with EUR/card as well as crypto?'],
    ['KYC requirements','Fully anonymous vs KYC required for large withdrawals'],
    ['Irish player acceptance','Not all crypto sites explicitly accept Irish residents'],
]) + """
<h2>Risks Specific to Crypto Gambling Sites</h2>
<ul style="line-height:1.9">
<li>No GRAI casino licence exists yet — crypto casino sites serve Ireland under offshore licences</li>
<li>Crypto transactions are irreversible — chargebacks impossible if site refuses to pay</li>
<li>Exchange rate risk: depositing 0.01 BTC and withdrawing later at a lower rate = net loss in EUR terms</li>
<li>Tax: Capital Gains Tax may apply to crypto gains made before depositing — consult a tax adviser</li>
<li>Many crypto gambling sites use Curaçao licences — the weakest consumer protection available</li>
</ul>
""" + RG,

'champions-league-dark-horse-betting.html': """
<h2>Champions League Dark Horse Betting Strategy</h2>
""" + tbl(['Attribute','What to look for in a dark horse'],[
    ['Favourable group','Easy opponents = maximum group stage goals and confidence'],
    ['Tournament experience','Clubs with recent CL semi-final/final experience surprise less often'],
    ['Striker form','A hot striker carries teams deep into the tournament'],
    ['Draw luck','Potential to avoid the top 2–3 seeds until the semi-final'],
    ['Domestic form','Champions League dark horses are usually flying in their league'],
]) + """
<h2>Historical Dark Horse Examples</h2>
<ul style="line-height:1.9">
<li>Ajax 2018-19: 100/1 pre-season, reached the semi-final; huge value for ante-post bettors</li>
<li>Monaco 2016-17: beat Manchester City and Dortmund; reached the semi-final</li>
<li>Dark horse bets are best placed pre-tournament or at the group stage draw — prices collapse after each round</li>
<li>Target clubs priced 20/1–50/1 with realistic paths through the draw — not 500/1 outliers</li>
</ul>
""" + RG,

'champions-league-outright-betting.html': """
<h2>Champions League Winner Betting: Key Markets</h2>
""" + tbl(['Market','Timing','Notes'],[
    ['Outright winner (ante-post)','Pre-season to final','Void if the team you back is eliminated — stake returned at some operators, not others'],
    ['To reach the final','After QFs','Both finalists are live — good value mid-tournament'],
    ['Group stage winner','After group stage draw','12 group markets; favourite usually 1.30–2.50'],
    ['Tournament top scorer','Available from pre-season','See top scorer betting guide'],
]) + """
<h2>Champions League Outright Betting Tips</h2>
<ul style="line-height:1.9">
<li>The CL winner has come from the last 4 teams standing in every season — backing a semi-finalist at the QF stage is statistically sensible</li>
<li>Spanish and English clubs have dominated since 2010 — La Liga and Premier League clubs command shorter prices</li>
<li>Non-runner rule varies: if your backed club is drawn against a giant in the round of 16, check if your bet voids if eliminated</li>
<li>Exchanges (Betfair) carry better odds with 2–5% commission vs 8–12% bookmaker margin on CL outrights</li>
</ul>
""" + RG,

'cheltenham-2027-county-hurdle-betting.html': """
<h2>County Hurdle: Race Facts</h2>
""" + tbl(['Feature','Detail'],[
    ['Distance','2 miles 1 furlong'],
    ['Type','Handicap hurdle — competitive handicap with large fields'],
    ['Grade','Listed (not graded — a handicap)'],
    ['Day','Friday (Gold Cup Day)'],
]) + """
<h2>County Hurdle Betting Strategy</h2>
<ul style="line-height:1.9">
<li>Large field (20–28 runners) — a handicap with the entire field given an equal chance on paper</li>
<li>High draw bias can apply at Cheltenham over this trip — check recent draw stats before betting</li>
<li>Irish raiders dominate this race — Willie Mullins and Gordon Elliott regularly supply the first 3 home</li>
<li>Price: winners regularly priced 10/1–20/1; favourites win occasionally but big-field handicaps favour value</li>
</ul>
""" + RG,

'cheltenham-2027-grand-annual-betting.html': """
<h2>Grand Annual Chase: Race Facts</h2>
""" + tbl(['Feature','Detail'],[
    ['Distance','2 miles 87 yards (minimum trip chase)'],
    ['Type','Handicap chase'],
    ['Grade','Listed handicap'],
    ['Day','Friday (Gold Cup Day)'],
]) + """
<h2>Grand Annual Betting Tips</h2>
<ul style="line-height:1.9">
<li>Minimum trip chase — fast, athletic horses with speed rather than stamina excel</li>
<li>Large field (12–18 runners); low-weight horses often competitive</li>
<li>Nicky Henderson, Paul Nicholls and Irish yards all competitive in this race</li>
<li>Price range: 8/1–20/1 for most winners — favourites at 4/1 occasionally land it but not reliably</li>
</ul>
""" + RG,

'cheltenham-2027-hunter-chase-betting.html': """
<h2>Foxhunter Challenge Cup (Hunter Chase): Race Facts</h2>
""" + tbl(['Feature','Detail'],[
    ['Distance','3 miles 2 furlongs'],
    ['Type','Hunter chase — horses must qualify through point-to-point racing'],
    ['Grade','Listed'],
    ['Day','Friday (Gold Cup Day)'],
]) + """
<h2>Hunter Chase Betting: What Makes It Unique</h2>
<ul style="line-height:1.9">
<li>Horses must have qualified through point-to-point racing — amateur riders compete</li>
<li>Many horses unknown at traditional form services — specialist point-to-point form guides essential</li>
<li>Winners often priced 10/1–33/1 — genuine novelty market for Cheltenham punters</li>
<li>Irish point-to-point horses dominate — Willie Mullins and other top Irish yards field hunters regularly</li>
</ul>
""" + RG,

'cheltenham-2027-mares-novices-hurdle.html': """
<h2>Mares Novices Hurdle: Race Facts</h2>
""" + tbl(['Feature','Detail'],[
    ['Distance','2 miles 179 yards'],
    ['Grade','Grade 2'],
    ['Day','Thursday (St Patrick\'s Day)'],
    ['Restricted to','Mares; novice hurdlers'],
]) + """
<h2>Mares Novices Hurdle Betting Tips</h2>
<ul style="line-height:1.9">
<li>Often a Willie Mullins advantage — his novice mares are unbeaten at the Cheltenham Festival in many editions</li>
<li>Smaller field than the open novice hurdle — form is more readable; favourites win more reliably</li>
<li>Key prep races: Grade 1 mares novice hurdles at Leopardstown and Fairyhouse</li>
<li>Favourite wins at high rate (~40%) — this is a race where backing the market leader can be justified</li>
</ul>
""" + RG,

'cheltenham-2027-ryanair-chase-betting.html': """
<h2>Ryanair Chase: Race Facts</h2>
""" + tbl(['Feature','Detail'],[
    ['Distance','2 miles 5 furlongs (intermediate trip)'],
    ['Grade','Grade 1'],
    ['Day','Wednesday (Ladies Day)'],
    ['Notable','Alternative to the Gold Cup for top 2m5f chasers'],
]) + """
<h2>Ryanair Chase Betting Strategy</h2>
<ul style="line-height:1.9">
<li>The Ryanair often attracts the second-string Gold Cup horses who prefer this shorter trip</li>
<li>Grade 1 quality — typically won by a horse rated 165+</li>
<li>Field size: 8–12 runners — smaller than the Gold Cup; form easier to assess</li>
<li>Key Irish trials: Leopardstown Christmas Festival and Punchestown January Festival</li>
<li>Willie Mullins dominates this race as much as any other Cheltenham Grade 1</li>
</ul>
""" + RG,

'cheltenham-2027-stayers-hurdle-betting.html': """
<h2>Stayers Hurdle: Race Facts</h2>
""" + tbl(['Feature','Detail'],[
    ['Distance','3 miles (longest hurdle race at Cheltenham)'],
    ['Grade','Grade 1'],
    ['Day','Thursday (St Patrick\'s Day)'],
    ['Also known as','The World Hurdle'],
]) + """
<h2>Stayers Hurdle Betting Tips</h2>
<ul style="line-height:1.9">
<li>The staying hurdle discipline — stamina is the primary requirement over speed</li>
<li>Field of 10–16 runners — smaller than the Champion Hurdle; form is more concentrated</li>
<li>High repeat winner rate — horses who win this race often run in it again the following year</li>
<li>Key prep races: Long Walk Hurdle (Ascot), Cleeve Hurdle (Cheltenham, January)</li>
<li>Irish raiders competitive but English stayers (Henderson, Nicholls) also win regularly</li>
</ul>
""" + RG,

'cheltenham-2027-triumph-hurdle-betting.html': """
<h2>Triumph Hurdle: Race Facts</h2>
""" + tbl(['Feature','Detail'],[
    ['Distance','2 miles 87 yards'],
    ['Grade','Grade 1'],
    ['Day','Friday (Gold Cup Day)'],
    ['Restricted to','4-year-old hurdlers only'],
]) + """
<h2>Triumph Hurdle Betting Strategy</h2>
<ul style="line-height:1.9">
<li>Exclusively for 4-year-olds — a juvenile hurdle; often a wide-open betting race</li>
<li>Large field (14–20 runners) — first-season hurdlers with limited form; huge uncertainty</li>
<li>French imports dominate some years — horses with flat form from France transfer to hurdles</li>
<li>Key prep races: Triumph Hurdle trials at Leopardstown, Cheltenham Open (November), Finale Hurdle</li>
<li>Market can swing wildly — late betting moves for last-minute revelations are common</li>
</ul>
""" + RG,

'downpatrick-racecourse-betting.html': """
<h2>Downpatrick Racecourse: Key Facts</h2>
""" + tbl(['Feature','Detail'],[
    ['Location','Downpatrick, Co. Down, Northern Ireland'],
    ['Surface','National Hunt (jumps racing)'],
    ['Notable feature','Undulating, challenging track; highest point-to-point in Ireland view'],
    ['Licence','Operates under Horse Racing Ireland / INHS (National Hunt) rules'],
]) + """
<h2>Betting on Downpatrick Races</h2>
<ul style="line-height:1.9">
<li>Downpatrick is a unique, challenging track — course specialists win regularly; always check previous course form</li>
<li>Northern Ireland location: accessible from Dublin (2 hours) and Belfast (45 minutes)</li>
<li>BOG available at most major GRAI-licensed bookmakers for Downpatrick fixtures</li>
<li>Live streaming available on Racing TV for most Downpatrick meetings</li>
</ul>
""" + RG,

'iron-dog-studio-casinos-ireland.html': """
<h2>Iron Dog Studio: What Irish Players Need to Know</h2>
""" + tbl(['Feature','Detail'],[
    ['Provider type','Game developer (B2B) — does not operate casinos directly'],
    ['Licence','MGA-licensed game provider'],
    ['Irish player access','Available on MGA-licensed online casinos serving Ireland'],
    ['Game types','Video slots, primarily'],
    ['RTP range','Typically 95–97% — check individual game info pages'],
]) + """
<h2>How to Find Iron Dog Studio Games</h2>
<ul style="line-height:1.9">
<li>Search for "Iron Dog Studio" in the game library of any major MGA-licensed online casino</li>
<li>RTP for each slot is listed in the game\'s "i" or info button — always check before playing</li>
<li>No GRAI casino licence has been issued yet — online casinos serve Ireland under MGA/UKGC licences</li>
<li>Set a session budget before playing any slots — RNG games have no form guide or strategy</li>
</ul>
""" + RG,

'leinster-championship-betting-ireland.html': '',  # already in batch9b

'best-betting-app-ireland-2026.html': '',  # already in batch9b

}

SKIP_PATTERNS = ['about.html','contact.html','terms.html','privacy.html',
    'editorial-guidelines.html','where-to-watch.html','weekly-news',
    'betting-sites-cavan.html','betting-sites-clare.html',
    'betting-sites-cork.html','betting-sites-donegal.html',
    'betting-sites-galway.html','betting-sites-kerry.html',
    'betting-sites-kildare.html','betting-sites-kilkenny.html',
    'betting-sites-laois.html','betting-sites-leitrim.html',
    'betting-sites-limerick.html','betting-sites-longford.html',
    'betting-sites-louth.html','betting-sites-mayo.html',
    'betting-sites-meath.html','betting-sites-monaghan.html',
    'betting-sites-offaly.html','betting-sites-roscommon.html',
    'betting-sites-sligo.html','betting-sites-tipperary.html',
    'betting-sites-waterford.html','betting-sites-westmeath.html',
    'betting-sites-wexford.html','betting-sites-wicklow.html',
    ]

def find_insertion_point(html):
    for marker in ['<div class="editorial-box"', '<div class="faq-item"', '</body>']:
        idx = html.find(marker)
        if idx != -1:
            return idx
    return -1

pages_dir = '/home/claude/craicbet/pages'
expanded = []
skipped = []

for filename, new_content in CONTENT.items():
    if any(filename == s for s in SKIP_PATTERNS) or not new_content.strip():
        skipped.append(filename)
        continue

    filepath = os.path.join(pages_dir, filename)
    if not os.path.exists(filepath):
        skipped.append(filename + ' (not found)')
        continue

    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

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
    expanded.append(filename)
    print(f'  {filename}: {before} → {after}')

print(f"\n✓ Expanded: {len(expanded)}")
print(f"○ Skipped: {len(skipped)}")
