#!/usr/bin/env python3
"""Batch 6: Expand 50 thin pages with GSC-targeted content."""

import re

TABLE_STYLE = 'style="width:100%;border-collapse:collapse;margin:16px 0;font-size:0.95rem"'
TH_STYLE = 'style="padding:9px;border:1px solid #2d5a3d;text-align:left;color:#cde6d4"'
TD_STYLE = 'style="padding:8px;border:1px solid #2d5a3d"'
TR_HEAD = 'style="background:#1e3a28"'
TR_ALT = 'style="background:#0d1f14"'

def th(text): return f'<th {TH_STYLE}>{text}</th>'
def td(text): return f'<td {TD_STYLE}>{text}</td>'
def tr_head(*cells): return f'<tr {TR_HEAD}>{" ".join(cells)}</tr>'
def tr_norm(*cells): return f'<tr>{" ".join(cells)}</tr>'
def tr_alt(*cells): return f'<tr {TR_ALT}>{" ".join(cells)}</tr>'

def table(*rows): return f'<table {TABLE_STYLE}>{"".join(rows)}</table>'

def insert_before_faq(content, new_html):
    # Try editorial-box first
    if '<div class="editorial-box"' in content:
        return content.replace('<div class="editorial-box"', new_html + '\n<div class="editorial-box"', 1)
    # Try faq-item
    if '<div class="faq-item"' in content:
        return content.replace('<div class="faq-item"', new_html + '\n<div class="faq-item"', 1)
    # Try FAQ h2 heading
    if '<h2>Frequently Asked Questions</h2>' in content:
        return content.replace('<h2>Frequently Asked Questions</h2>', new_html + '\n<h2>Frequently Asked Questions</h2>', 1)
    return content + new_html


EXPANSIONS = {}

# 1. Ligue 1
EXPANSIONS['pages/ligue-1-betting-ireland.html'] = """
<h2>Ligue 1 Markets Available to Irish Bettors</h2>
<table {TABLE_STYLE}>
{tr_head(th('Market'), th('Description'), th('Typical Margin'))}
{tr_norm(td('1X2 Match Result'), td('Home win / draw / away win on 90 minutes'), td('7–9%'))}
{tr_alt(td('Asian Handicap'), td('Level the field with fractional goal lines'), td('5–6%'))}
{tr_norm(td('Over/Under Goals'), td('Total goals above or below 2.5 / 3.5'), td('6–7%'))}
{tr_alt(td('Both Teams to Score'), td('Yes/No on both sides netting'), td('7–8%'))}
{tr_norm(td('Outright Winner'), td('Season-long market, ante-post from August'), td('12–18%'))}
{tr_alt(td('Top Scorer'), td('Erling Haaland equivalents in France — high margins'), td('15–20%'))}
{tr_norm(td('Half-Time Result'), td('Popular single-match specials'), td('9–11%'))}
</table>

<h2>Key Ligue 1 Teams for Irish Bettors in 2026/27</h2>
<table {TABLE_STYLE}>
{tr_head(th('Club'), th('Strength'), th('Note for Bettors'))}
{tr_norm(td('Paris Saint-Germain'), td('Dominant'), td('Short prices on most matchdays; value elsewhere'))}
{tr_alt(td('Olympique de Marseille'), td('Strong'), td('High-scoring, good for BTTS markets'))}
{tr_norm(td('Olympique Lyonnais'), td('Rebuilding'), td('Mid-table variance; watch team news'))}
{tr_alt(td('AS Monaco'), td('Consistent top-4'), td('Good European football record'))}
{tr_norm(td('Lille OSC'), td('Tactically solid'), td('Low-scoring, under-2.5 potential'))}
{tr_alt(td('OGC Nice'), td('Top-6 candidate'), td('Home record worth checking'))}
</table>

<h2>Watching Ligue 1 in Ireland: Broadcast Guide</h2>
<p>Ligue 1 coverage in Ireland is primarily through <strong>beIN Sports</strong> (available via Sky Sports add-on or streaming packages). Canal+ Afrique has French domestic rights for some markets. Amazon Prime Video also holds UK/Ireland rights for select fixtures. Check your satellite or streaming provider for the current season schedule. Kick-off times in Irish Standard Time (IST) are typically 20:00 on Fridays, 17:00 or 21:00 on Saturdays, and 16:00 or 20:45 on Sundays.</p>
"""

# 2. Conference League
EXPANSIONS['pages/conference-league-betting-ireland.html'] = """
<h2>UEFA Conference League Format and Betting Implications</h2>
<table {TABLE_STYLE}>
{tr_head(th('Stage'), th('Matches'), th('Best Betting Approach'))}
{tr_norm(td('Group/League Phase'), td('6 group matches per club'), td('Outright winner ante-post, over 2.5 goals common'))}
{tr_alt(td('Play-off Round'), td('Two-legged tie'), td('Asian handicap on aggregate; first-leg draw common'))}
{tr_norm(td('Round of 16'), td('Two legs'), td('Away goals no longer apply; second leg draws frequent'))}
{tr_alt(td('Quarter-Finals'), td('Two legs'), td('Home advantage historically decisive'))}
{tr_norm(td('Semi-Finals'), td('Two legs'), td('Top seeds win ~70% of semis'))}
{tr_alt(td('Final'), td('Single match, neutral venue'), td('Each-way outright value in Round of 16'))}
</table>

<h2>Conference League Outright Betting Strategy</h2>
<p>The Conference League attracts mid-tier European clubs and strong domestic champions from smaller leagues. Irish clubs (Shamrock Rovers, Bohemians, Shelbourne) have qualified in recent seasons via the Europa League qualifiers. For outright betting, clubs from the Netherlands, Portugal, and Greece consistently perform well. English clubs (Aston Villa, Chelsea) have won the competition recently, often at short prices. For value, look at sides from Czech Republic, Austria, and Scotland who regularly reach the knockout stages.</p>
<table {TABLE_STYLE}>
{tr_head(th('Country'), th('Historical Performance'), th('Typical Outright Odds Range'))}
{tr_norm(td('England'), td('2 of last 3 winners'), td('3/1 – 7/1 for top-4 PL clubs'))}
{tr_alt(td('Netherlands'), td('Final in 2021'), td('8/1 – 14/1 depending on club'))}
{tr_norm(td('Portugal'), td('Consistent semi-finalists'), td('10/1 – 20/1'))}
{tr_alt(td('Greece'), td('Panathinaikos/Olympiakos reach QFs'), td('16/1 – 25/1'))}
{tr_norm(td('Czech Republic'), td('Slavia/Sparta regular runners'), td('20/1 – 33/1'))}
</table>
"""

# 3. Scottish Premiership
EXPANSIONS['pages/scottish-premiership-betting-ireland.html'] = """
<h2>Scottish Premiership Betting Markets</h2>
<table {TABLE_STYLE}>
{tr_head(th('Market'), th('What It Covers'), th('Irish Bettor Notes'))}
{tr_norm(td('Outright Winner'), td('Season champion ante-post'), td('Celtic or Rangers win ~95% of titles; value in top-6'))}
{tr_alt(td('Top 4 Finish'), td('European qualification places'), td('Hearts, Hibs, Aberdeen compete annually'))}
{tr_norm(td('Relegation'), td('Bottom 2 play-offs or automatic'), td('Newly promoted sides most vulnerable'))}
{tr_alt(td('Match 1X2'), td('Standard result market'), td('Wider margins than EPL — typically 8–10%'))}
{tr_norm(td('Scottish Cup Outright'), td('Knockout competition'), td('Runs February to May; Celtic/Rangers dominate'))}
{tr_alt(td('Top Scorer'), td('Golden Boot equivalent'), td('Rangers and Celtic strikers typically battle for award'))}
</table>

<h2>Old Firm Derby Betting</h2>
<p>The Celtic vs Rangers derby (Old Firm) is the most bet-on Scottish club fixture among Irish punters. It typically takes place 4–5 times per season across league and cup. Key notes: matches at Celtic Park see Celtic win around 60% of time; at Ibrox, Rangers win roughly 55%. Draw occurs in approximately 25% of all Old Firm meetings. The first scorer market is popular, as is corners, cards, and both teams to score (BTTS lands ~65% of derbies). Check if the match falls under the Scottish Football Association's category A protected fixture — in-play betting is available but suspension rules apply strictly.</p>

<h2>Scottish Premiership Season Calendar for Irish Bettors</h2>
<table {TABLE_STYLE}>
{tr_head(th('Month'), th('Key Events'))}
{tr_norm(td('July/August'), td('Season starts; European qualifying rounds'))}
{tr_alt(td('November'), td('Winter break approaches; form guide critical'))}
{tr_norm(td('January'), td('January transfer window; team strength changes'))}
{tr_alt(td('February–March'), td('Scottish Cup fifth round and quarter-finals'))}
{tr_norm(td('April'), td('Title race, relegation six-pointers'))}
{tr_alt(td('May'), td('Final day; Scottish Cup final at Hampden Park'))}
</table>
"""

# 4. League Cup Ireland / Carabao Cup
EXPANSIONS['pages/league-cup-ireland-betting.html'] = """
<h2>EFL League Cup Betting: What Irish Punters Need to Know</h2>
<table {TABLE_STYLE}>
{tr_head(th('Round'), th('Stage'), th('Betting Notes'))}
{tr_norm(td('Round 1–2'), td('Lower-league clubs enter; EPL sides with large squads'), td('Giant-killings common; each-way on underdogs has value'))}
{tr_alt(td('Round 3–4'), td('All 20 EPL clubs enter; rotation heavy'), td('Team news crucial — rested starters change market'))}
{tr_norm(td('Quarter-Finals'), td('8 clubs remain'), td('Big clubs field stronger sides; shorter prices'))}
{tr_alt(td('Semi-Finals'), td('Two-legged tie'), td('Aggregate markets; first leg often cautious'))}
{tr_norm(td('Final'), td('Single match at Wembley'), td('Neutral venue; ante-post from QF stage viable'))}
</table>

<h2>League Cup vs FA Cup: Which Is Better for Betting?</h2>
<table {TABLE_STYLE}>
{tr_head(th('Factor'), th('League Cup'), th('FA Cup'))}
{tr_norm(td('Upsets'), td('More frequent (rotation lineups)'), td('Moderate (Conference League clubs enter)'))}
{tr_alt(td('Each-way value'), td('Good in rounds 1–3'), td('Good in rounds 3–4'))}
{tr_norm(td('In-play betting'), td('Usually available'), td('Usually available'))}
{tr_alt(td('Prestige'), td('Lower — clubs prioritise EPL'), td('Higher — older competition'))}
{tr_norm(td('Irish TV coverage'), td('Sky Sports'), td('BBC/ITV via streaming in Ireland'))}
</table>
"""

# 5. Euro 2028 host nations
EXPANSIONS['pages/euro-2028-host-nations-betting.html'] = """
<h2>Euro 2028 Host Nations: Venues and Irish Interest</h2>
<table {TABLE_STYLE}>
{tr_head(th('Country'), th('Confirmed Host'), th('Irish Qualification Route'))}
{tr_norm(td('Republic of Ireland'), td('Yes — co-host'), td('Automatic qualification as host'))}
{tr_alt(td('United Kingdom (England, Scotland, Wales, Northern Ireland)'), td('Yes — co-host'), td('All four home nations auto-qualify'))}
{tr_norm(td('Spain'), td('Possible additional venues'), td('Qualified on merit for all recent tournaments'))}
</table>

<h2>Euro 2028 Outright Betting: Early Markets</h2>
<p>Euro 2028 outright markets are typically opened by major bookmakers 3–4 years before the tournament. As host, the Republic of Ireland will carry additional sentimental support. Historical context: host nations have won the tournament 3 times (Spain 1964, Italy 1968, France 1984). Co-hosting is different — Ireland's group-stage matches at Dublin's Aviva Stadium give them a significant home advantage. For early value, look at nations currently in strong qualifying form — Spain, France, Germany, and England are typically favoured.</p>
<table {TABLE_STYLE}>
{tr_head(th('Nation'), th('Form Trend'), th('Early Outright Range (indicative)'))}
{tr_norm(td('Spain'), td('Reigning Euro champion (2024)'), td('5/1 – 8/1'))}
{tr_alt(td('France'), td('Consistent finalist'), td('6/1 – 9/1'))}
{tr_norm(td('England'), td('Improving squad depth'), td('7/1 – 12/1'))}
{tr_alt(td('Germany'), td('Host of Euro 2024, strong rebuild'), td('8/1 – 14/1'))}
{tr_norm(td('Republic of Ireland'), td('Host; squad rebuilding'), td('50/1 – 100/1 ante-post'))}
</table>
"""

# 6. Wimbledon 2027
EXPANSIONS['pages/wimbledon-2027-betting-ireland.html'] = """
<h2>Wimbledon 2027 Betting Markets</h2>
<table {TABLE_STYLE}>
{tr_head(th('Market'), th('Description'), th('Notes'))}
{tr_norm(td('Outright Winner — Men\'s Singles'), td('Winner of main draw'), td('Top seeds dominate Wimbledon more than other Slams'))}
{tr_alt(td('Outright Winner — Women\'s Singles'), td('Women\'s champion'), td('More unpredictable; each-way value in draw'))}
{tr_norm(td('Set Betting'), td('Exact set score prediction'), td('High margins 15–20%; for small stakes only'))}
{tr_alt(td('Match Winner'), td('Individual match 2-way market'), td('No draw; most common Wimbledon bet'))}
{tr_norm(td('Total Games'), td('Over/under total games in match'), td('Good for form players on specific surfaces'))}
{tr_alt(td('Each-Way Outright'), td('Usually top 4 or finalist'), td('Ask your bookmaker for each-way terms before placing'))}
</table>

<h2>Wimbledon Grass Court Form Guide for Irish Bettors</h2>
<p>Wimbledon form is unique. Players who excel on clay (Roland Garros) often underperform on grass, while fast-court specialists thrive. Key pre-Wimbledon grass events include Queen's Club (men's) and Eastbourne/Berlin (women's). A win at Queen's is a strong indicator for Wimbledon. Historically, players ranked 1–4 win the men's title in roughly 65% of editions. For the women's draw, the top seed wins around 40% of the time — far more variance, meaning each-way value often exists at 10/1+ for in-form players. 18+. Responsible betting.</p>
"""

# 7. Open Championship 2027
EXPANSIONS['pages/open-championship-2027-betting-ireland.html'] = """
<h2>The Open Championship 2027: Betting Markets and Format</h2>
<table {TABLE_STYLE}>
{tr_head(th('Market'), th('Description'), th('Irish Bettor Tip'))}
{tr_norm(td('Outright Winner'), td('72-hole stroke play champion'), td('Each-way 1/5 odds, 8 places common'))}
{tr_alt(td('Top 10 / Top 20 Finish'), td('Place markets without win needed'), td('Better value than outright for quality fields'))}
{tr_norm(td('Round Leader'), td('Best score after each round'), td('High variance; small stakes only'))}
{tr_alt(td('Nationality Specials'), td('Best European, Best Irish player etc.'), td('Good value if Irish player in strong form'))}
{tr_norm(td('Hole-in-One'), td('Any player makes hole-in-one during week'), td('Usually 2/1 to 7/4 depending on course'))}
{tr_alt(td('Cut/No Cut'), td('Whether player makes the 36-hole cut'), td('Form + links experience key factors'))}
</table>

<h2>Links Golf and Betting Considerations</h2>
<p>The Open Championship is played on links courses — typically in England, Scotland, or Northern Ireland. Wind is the defining factor: check forecast 48 hours before first tee. Players with strong ball-striking below the wind (knockdown shots) gain a significant advantage. Rory McIlroy, as an Irish fan favourite, generates substantial interest among Irish bettors. His links record and Open pedigree make him a fixture in Irish betting slips. Historical Open courses include Royal Troon, St Andrews, Royal Liverpool (Hoylake), and Royal Portrush — which hosted in 2019. 18+.</p>
"""

# 8. Tour de France 2027
EXPANSIONS['pages/tour-de-france-2027-betting-ireland.html'] = """
<h2>Tour de France 2027 Betting Markets</h2>
<table {TABLE_STYLE}>
{tr_head(th('Market'), th('Description'), th('Notes'))}
{tr_norm(td('General Classification (GC) Winner'), td('Overall race winner after 21 stages'), td('Most popular market; ante-post from January'))}
{tr_alt(td('Stage Winner (Outright)'), td('Who wins the most stages overall'), td('Sprinters vs climbers — different stage types matter'))}
{tr_norm(td('Points Classification'), td('Green jersey winner'), td('Usually a sprinter specialist'))}
{tr_alt(td('King of the Mountains'), td('Polka dot jersey — best climber'), td('Often a breakaway specialist, not GC contender'))}
{tr_norm(td('Best Young Rider'), td('White jersey for under-25 riders'), td('Good each-way option on emerging talent'))}
{tr_alt(td('Daily Stage Winner'), td('Who wins each individual stage'), td('Sprint stages (flat) vs mountain stages have different profiles'))}
</table>

<h2>Tour de France GC Betting Strategy</h2>
<p>General Classification (GC) betting at the Tour de France is dominated by team strategy. The leading GC contenders typically race for climbers — riders who can limit time losses on flat stages and attack on mountain finishes. Each-way terms of 1/4 odds, 4 places are standard for the GC outright. Colombian, Slovenian, and Danish riders have dominated recent editions. Stage 17–21 (Alpine and Pyrenean finishes) typically determine the GC — if your selection survives to the final week in yellow or close to it, the final Paris stage is traditionally ceremonial (no attacks by convention). Check the route announcement each October for the 2027 race to identify key mountain stages.</p>
"""

# 9. Curragh Spring Cup 2027
EXPANSIONS['pages/curragh-spring-cup-2027-betting.html'] = """
<h2>Curragh Spring Cup 2027: Race Details and Betting Guide</h2>
<table {TABLE_STYLE}>
{tr_head(th('Detail'), th('Information'))}
{tr_norm(td('Venue'), td('The Curragh Racecourse, Co. Kildare'))}
{tr_alt(td('Distance'), td('1 mile (Group 3 flat race)'))}
{tr_norm(td('Surface'), td('Flat turf'))}
{tr_alt(td('Time of Year'), td('Spring — typically April'))}
{tr_norm(td('Field Size'), td('Usually 8–14 runners'))}
{tr_alt(td('Each-Way Places'), td('Typically 3 places (1/4 odds) for 8+ runners'))}
</table>

<h2>Betting the Curragh Spring Calendar</h2>
<p>The Curragh is Ireland's premier flat racing venue and home to all five Irish Classics. The Spring Cup is an early-season Group 3 indicator race, often used as a prep for the Irish 2000 Guineas in May. Horses from Aidan O'Brien's Ballydoyle stable and Joseph O'Brien's yard are perennial market movers. For ante-post betting, track how horses come out of their seasonal debut — a smooth win on good-to-firm ground is a positive indicator. Each-way value often exists at prices of 6/1 or bigger in a full field. Check the Curragh website or Racing Post for 2027 fixtures once published. 18+.</p>
"""

# 10. Summer betting
EXPANSIONS['pages/summer-betting-ireland.html'] = """
<h2>Summer Betting Calendar for Irish Punters</h2>
<table {TABLE_STYLE}>
{tr_head(th('Month'), th('Key Events'), th('Irish Interest'))}
{tr_norm(td('June'), td('Irish Derby (Curragh), Euro football (if summer), test cricket'), td('Irish Derby is the highlight'))}
{tr_alt(td('July'), td('Wimbledon final week, Tour de France, Open Championship'), td('Rory McIlroy interest in Open; tennis coverage on RTE'))}
{tr_norm(td('August'), td('GAA All-Ireland Football semi-finals, Premier League pre-season'), td('GAA dominates Irish sports calendar'))}
{tr_alt(td('August bank holiday'), td('Galway Races (last week July/first August), PPL double header'), td('Galway Festival: Galway Plate and Galway Hurdle attract huge Irish betting volume'))}
</table>

<h2>Galway Races Summer Festival Betting Guide</h2>
<p>The Galway Races (Galway Festival) is the peak of the Irish betting summer — a week of mixed flat and jump racing with enormous public participation. Key races: the Galway Plate (Wednesday, 2m1f handicap hurdle) and Galway Hurdle (Thursday, 2m flat handicap hurdle). Fields are large (20–30 runners), making these high-variance bets. Each-way is essential at 1/5 odds, 5 places or 1/4 odds, 4 places depending on the bookmaker. Trainers with strong Galway records include Willie Mullins, Gordon Elliott, and Jessica Harrington. Watch for market movers on festival morning — Galway is well-known for punted-on winners. 18+.</p>
"""

# Cheltenham 2027 races — write a template function
def cheltenham_expansion(race_name, distance, description, key_contenders):
    return f"""
<h2>{race_name}: Key Facts for Betters</h2>
<table {TABLE_STYLE}>
{tr_head(th('Detail'), th('Information'))}
{tr_norm(td('Race'), td(race_name))}
{tr_alt(td('Festival Day'), td(description))}
{tr_norm(td('Distance'), td(distance))}
{tr_alt(td('Type'), td('Grade 1 / Grade 2 National Hunt'))}
{tr_norm(td('Field Size'), td('Usually 10–20 runners'))}
{tr_alt(td('Each-Way Terms'), td('Typically 4 places at 1/4 odds for 8+ runners'))}
</table>

<h2>Ante-Post Betting Strategy</h2>
<p>{race_name} ante-post markets open in autumn and tighten significantly by January. Early prices offer the best value but carry non-runner risk — if your selection doesn't start, most bets are lost (unless NRNB/non-runner money-back is offered). Bookmakers regularly offer each-way ante-post specials closer to the festival. {key_contenders} 18+. No bet is guaranteed to win.</p>
"""

EXPANSIONS['pages/cheltenham-2027-ryanair-chase-betting.html'] = cheltenham_expansion(
    'Ryanair Chase',
    '2m5f (Grade 1)',
    'Wednesday — Festival Wednesday',
    'The Ryanair Chase sits between the Champion Chase (2m) and Gold Cup (3m2f) — attracting bold front-runners and versatile chasers who lack the pace for 2m but don\'t stay the Gold Cup trip. Irish stables (Mullins, Elliott) dominate market movers.'
)

EXPANSIONS['pages/cheltenham-2027-mares-hurdle-betting.html'] = cheltenham_expansion(
    'Mares\' Hurdle',
    '2m1f (Grade 2)',
    'Tuesday — Champion Day',
    'The Mares\' Hurdle is a Grade 2 for mares-only. Willie Mullins-trained mares have a dominant record. Market often features a short-priced favourite. Each-way at 5/1+ can offer value in a full field.'
)

EXPANSIONS['pages/cheltenham-2027-county-hurdle-betting.html'] = cheltenham_expansion(
    'County Hurdle',
    '2m1f (Grade 3 handicap)',
    'Friday — Gold Cup Day',
    'The County Hurdle is a large-field handicap — one of the most difficult to win and to predict. Fields regularly exceed 24 runners. Each-way betting essential. Market movers on festival morning are worth tracking in this competitive handicap.'
)

EXPANSIONS['pages/cheltenham-2027-stayers-hurdle-betting.html'] = cheltenham_expansion(
    'Stayers\' Hurdle (World Hurdle)',
    '3m1f (Grade 1)',
    'Thursday — St. Patrick\'s Thursday',
    'The Stayers\' Hurdle is for the best staying hurdlers over three miles. Stamina is paramount. The pace is often slow early then frantic from 3 out — position in the final mile matters more than any other race.'
)

EXPANSIONS['pages/cheltenham-2027-grand-annual-betting.html'] = cheltenham_expansion(
    'Grand Annual Chase',
    '2m (Grade 3 handicap)',
    'Friday — Gold Cup Day',
    'The Grand Annual is a 2m handicap chase — the fastest race of the week. Low weights can win; course specialists with form at Cheltenham have strong records. Watch for Irish market movers late in the week.'
)

EXPANSIONS['pages/cheltenham-2027-triumph-hurdle-betting.html'] = cheltenham_expansion(
    'Triumph Hurdle',
    '2m1f (Grade 1)',
    'Friday — Gold Cup Day',
    'The Triumph Hurdle is exclusively for 4-year-olds making their hurdling debut or early in their career. French-trained horses (from champion trainers like Guillaume Macaire) have a strong record. Spot the unbeaten juveniles in January trials — they often start as market leaders by March.'
)

EXPANSIONS['pages/cheltenham-2027-hunter-chase-betting.html'] = cheltenham_expansion(
    'Foxhunter Chase',
    '3m2f (amateur riders)',
    'Friday — Gold Cup Day',
    'The Foxhunter Chase (often called the amateur Gold Cup) is ridden by amateur jockeys. Former point-to-point horses with strong hunter chase form are the target profile. Irish point-to-point graduates are well represented.'
)

EXPANSIONS['pages/cheltenham-2027-gold-cup-day-betting.html'] = """
<h2>Cheltenham Gold Cup Day: Race Schedule 2027</h2>
<table {TABLE_STYLE}>
{tr_head(th('Race'), th('Distance'), th('Type'))}
{tr_norm(td('JCB Triumph Hurdle'), td('2m1f'), td('Grade 1 — 4-year-olds'))}
{tr_alt(td('Albert Bartlett Novices\' Hurdle'), td('3m1f'), td('Grade 1 — staying novice hurdlers'))}
{tr_norm(td('Grand Annual Chase'), td('2m'), td('Grade 3 handicap'))}
{tr_alt(td('Foxhunter Chase'), td('3m2f'), td('Amateur riders'))}
{tr_norm(td('County Hurdle'), td('2m1f'), td('Grade 3 handicap — 24+ runners typical'))}
{tr_alt(td('Gold Cup'), td('3m2f'), td('Grade 1 — the festival showpiece'))}
</table>

<h2>Cheltenham Gold Cup Betting Guide</h2>
<p>The Gold Cup is the pinnacle of National Hunt racing — a 3m2f Grade 1 chase at the Cheltenham Festival. The race typically attracts 15–20 runners. Irish trainers (Willie Mullins, Gordon Elliott, Henry de Bromhead) have dominated in recent years. Key betting notes: the Gold Cup is a strongly run staying test — horses who stay every yard of 3m2f over fences. Horses with a Grade 1 chase win over 2m4f+ are the profile. Ante-post markets open in October; by January the market is often concentrated in the top 4–5. Each-way with 4 places at 1/4 odds is standard. 18+. No pronostic is guaranteed.</p>
"""

EXPANSIONS['pages/cheltenham-2027-champion-day-betting.html'] = """
<h2>Cheltenham Champion Day 2027: Race Guide</h2>
<table {TABLE_STYLE}>
{tr_head(th('Race'), th('Distance'), th('Type'))}
{tr_norm(td('Supreme Novices\' Hurdle'), td('2m½f'), td('Grade 1 — novice hurdlers'))}
{tr_alt(td('Arkle Novices\' Chase'), td('2m'), td('Grade 1 — novice chasers'))}
{tr_norm(td('Ultima Handicap Chase'), td('3m1f'), td('Grade 3 — large handicap'))}
{tr_alt(td('Champion Hurdle'), td('2m½f'), td('Grade 1 — the best hurdlers'))}
{tr_norm(td('Mares\' Hurdle'), td('2m1f'), td('Grade 2 — mares only'))}
{tr_alt(td('Cheltenham Plate'), td('2m4½f'), td('Grade 3 — handicap chase'))}
</table>

<h2>Champion Hurdle Betting Strategy</h2>
<p>The Champion Hurdle is the fastest-run Grade 1 of the week — a 2m½f test of pure speed and jumping. The best 2-mile hurdlers in Britain and Ireland compete. Recent market trends: hurdlers who have shown brilliance in the Fighting Fifth Hurdle (Newcastle, November) or Christmas Hurdle (Kempton) tend to open as Champion Hurdle favourites. Horses aged 5–8 have the best record. Older horses (9+) rarely win. The favourite wins the Champion Hurdle around 35% of the time — good each-way value exists at 8/1+ in a 10-horse field. 18+.</p>
"""

EXPANSIONS['pages/cheltenham-2027-mares-novices-hurdle.html'] = cheltenham_expansion(
    'Mares\' Novices\' Hurdle',
    '2m½f (Grade 2)',
    'Wednesday — Festival Wednesday',
    'The Mares\' Novices\' Hurdle is a Grade 2 for mares in their first or second season over hurdles. Willie Mullins dominates this race. If a leading Mullins mare is unbeaten in novice company, she typically starts at a short price. Each-way value exists in second-string Irish runners who have strong form behind the top mare.'
)

EXPANSIONS['pages/cheltenham-2027-albert-bartlett-betting.html'] = cheltenham_expansion(
    'Albert Bartlett Novices\' Hurdle',
    '3m1f (Grade 1)',
    'Friday — Gold Cup Day',
    'The Albert Bartlett is for staying novice hurdlers over 3 miles — the longest novice hurdle of the week. Horses who have shown stamina in bumpers or early novice hurdles over 2m4f+ are the profile. The race often features big prices winning — a double-figure winner is common, making each-way betting attractive.'
)

EXPANSIONS['pages/cheltenham-2027-novices-hurdle-betting.html'] = cheltenham_expansion(
    'Supreme Novices\' Hurdle',
    '2m½f (Grade 1)',
    'Tuesday — Champion Day (opening race)',
    'The Supreme Novices\' Hurdle is the first race of the Festival — a Grade 1 for novice hurdlers. The opening race attracts significant betting attention. Willie Mullins and Gordon Elliott regularly dominate the market. Watch the racing post for market moves in the week before — the Supreme often features a heavily-backed Irish challenger.'
)

# GAA 2027
EXPANSIONS['pages/gaa-2027-munster-hurling-championship.html'] = """
<h2>Munster Hurling Championship 2027: Clubs and Format</h2>
<table {TABLE_STYLE}>
{tr_head(th('County'), th('Recent Form'), th('Key Players to Watch'))}
{tr_norm(td('Limerick'), td('Dominant 2020–2024'), td('Cian Lynch, Gearóid Hegarty profile'))}
{tr_alt(td('Kilkenny'), td('Strong — enters via Leinster but meets Munster sides in All-Ireland'), td('TJ Reid the established star'))}
{tr_norm(td('Cork'), td('Consistent Munster contender'), td('Strong club base, tactical evolution'))}
{tr_alt(td('Clare'), td('All-Ireland title 2024'), td('Tony Kelly leads scoring records'))}
{tr_norm(td('Tipperary'), td('Rebuilding post-2019 era'), td('Watching youth development'))}
{tr_alt(td('Waterford'), td('Dark horses in provincial round-robin'), td('Aussie rules crossover talent emerging'))}
</table>

<h2>Munster Hurling Betting Markets</h2>
<p>The Munster Hurling Championship runs from May to late June in a round-robin format, with the top two sides progressing to the Munster Final. Betting markets open in January for the Munster Championship outright. Limerick's dynasty (5 All-Irelands in 6 years, 2018–2023) means they often open as short-priced favourites. The round-robin format means early-round results aren't always do-or-die — this can suppress motivation and affect betting markets. For best value, focus on individual match markets rather than outright championship winner. GAA games carry significant Irish identity — attendance in Thurles and Pairc Ui Chaoimh is worth factoring into home advantage calculations. 18+.</p>
"""

EXPANSIONS['pages/gaa-2027-football-favourites-betting.html'] = """
<h2>All-Ireland Football Championship 2027: Outright Betting Guide</h2>
<table {TABLE_STYLE}>
{tr_head(th('County'), th('Provincial Base'), th('All-Ireland Wins (last 10 yrs)'), th('Outright Range'))}
{tr_norm(td('Dublin'), td('Leinster'), td('7 (2013–2023 dynasty)'), td('4/1 – 7/1 depending on form'))}
{tr_alt(td('Kerry'), td('Munster'), td('3 (2014, 2022, 2023)'), td('3/1 – 6/1'))}
{tr_norm(td('Galway'), td('Connacht'), td('1 (2022)'), td('10/1 – 20/1'))}
{tr_alt(td('Mayo'), td('Connacht'), td('0 (5 final appearances since 2004)'), td('12/1 – 25/1'))}
{tr_norm(td('Derry'), td('Ulster'), td('1 (2023)'), td('16/1 – 30/1'))}
{tr_alt(td('Tyrone'), td('Ulster'), td('1 (2021)'), td('14/1 – 25/1'))}
</table>

<h2>All-Ireland Football Betting Tips for 2027</h2>
<p>The All-Ireland Senior Football Championship uses a combined provincial and national league structure. Sam Maguire outright ante-post markets typically open in December/January. Kerry and Dublin are the two perennial powers — between them they have won 10 of the last 15 All-Irelands. For value, look at Ulster counties (Derry, Armagh, Tyrone, Donegal) who consistently reach semi-finals. Connacht (Galway, Mayo) are well-supported among Irish bettors. The Super 8s format means groups of 4 play round-robin before semi-finals — a team can lose one match and still advance. This complicates outright predictions. 18+. Responsible gambling.</p>
"""

EXPANSIONS['pages/gaa-2027-hurling-favourites-betting.html'] = """
<h2>All-Ireland Hurling Championship 2027: Outright Markets</h2>
<table {TABLE_STYLE}>
{tr_head(th('County'), th('Liam MacCarthy Wins (last 10 yrs)'), th('Provincial'), th('Outright Range'))}
{tr_norm(td('Limerick'), td('5 (2018, 2020, 2021, 2022, 2023)'), td('Munster'), td('2/1 – 5/1'))}
{tr_alt(td('Kilkenny'), td('1 (2022 pending further wins)'), td('Leinster'), td('4/1 – 8/1'))}
{tr_norm(td('Clare'), td('1 (2024)'), td('Munster'), td('6/1 – 12/1'))}
{tr_alt(td('Cork'), td('0 (2 finals)'), td('Munster'), td('10/1 – 18/1'))}
{tr_norm(td('Galway'), td('1 (2017)'), td('Leinster/Connacht'), td('12/1 – 20/1'))}
{tr_alt(td('Tipperary'), td('1 (2019)'), td('Munster'), td('14/1 – 25/1'))}
</table>

<h2>Hurling Betting Strategy: Key Markets</h2>
<p>Hurling is Ireland's most uniquely-bet sport — almost all betting volume comes from Irish punters. Limerick's dominance has suppressed ante-post value since 2018. For 2027, the question is whether Clare, Kilkenny, or Galway can mount a sustained challenge. For individual match betting, hurling carries the highest scoring rate of any field sport — over 1.5 goals (3-pointer type) is usually priced around even money. Total points markets (over/under 45.5 total points) are increasingly popular. Home advantage in provincial games is significant — especially Munster semi-finals in Thurles. 18+.</p>
"""

EXPANSIONS['pages/leinster-championship-betting-ireland.html'] = """
<h2>Leinster GAA Championship 2027: Football and Hurling</h2>
<table {TABLE_STYLE}>
{tr_head(th('Code'), th('Format'), th('Key Counties'))}
{tr_norm(td('Football'), td('Round-robin + provincial final'), td('Dublin, Meath, Kildare, Louth, Westmeath'))}
{tr_alt(td('Hurling'), td('Round-robin + provincial final'), td('Kilkenny, Galway, Wexford, Dublin, Laois'))}
</table>

<h2>Dublin in Leinster Football: Betting Context</h2>
<p>Dublin's footballers dominated Leinster for over a decade (13 consecutive Leinster titles 2011–2023). Their provincial price is frequently sub-1/4 (1.25) in outright markets. For betting value, the Leinster football final often delivers tight margins — Meath, Kildare, and Louth have all competed. The Leinster hurling championship is more competitive — Kilkenny typically favoured, but Galway (who qualify through Connacht or via qualifier) and Wexford regularly reach the final. Leinster finals are played at Croke Park — largest stadium in Ireland, 82,300 capacity. Atmosphere is a factor in some high-profile finals. 18+.</p>
"""

# Withdrawals and payments
EXPANSIONS['pages/how-long-do-withdrawals-take-ireland.html'] = """
<h2>Withdrawal Timeframes by Payment Method</h2>
<table {TABLE_STYLE}>
{tr_head(th('Method'), th('Typical Time'), th('Notes'))}
{tr_norm(td('Debit Card (Visa/Mastercard)'), td('1–5 business days'), td('Bank processing adds 1–3 days after site approves'))}
{tr_alt(td('PayPal'), td('Within 24 hours'), td('Instant to PayPal wallet; then 1–3 days to bank'))}
{tr_norm(td('Skrill / Neteller'), td('Within 24 hours'), td('E-wallet to e-wallet is fast; slower to bank card'))}
{tr_alt(td('Revolut'), td('1–2 business days'), td('Treated as a Mastercard; some sites faster'))}
{tr_norm(td('Bank Transfer'), td('3–7 business days'), td('Slowest option; used for large withdrawals'))}
{tr_alt(td('Apple Pay / Google Pay'), td('1–3 business days'), td('Linked to debit card; depends on underlying card speed'))}
</table>

<h2>Why Withdrawals Are Sometimes Delayed</h2>
<p>Delays beyond the standard timeframe typically fall into three categories: (1) KYC verification — if your account is not fully verified (ID + proof of address submitted and approved), all withdrawals are held until checks pass; (2) Withdrawal limit queues — some platforms batch withdrawals and process daily or twice daily; (3) Bank processing — the betting site approves the payment but your bank's internal clearing adds 1–3 days. If your withdrawal has not arrived within 7 business days, contact customer support with your withdrawal reference number. GRAI-licensed operators must process verified withdrawals promptly. 18+.</p>
"""

EXPANSIONS['pages/best-casino-apple-pay-ireland.html'] = """
<h2>How Apple Pay Works at Irish Online Casinos</h2>
<table {TABLE_STYLE}>
{tr_head(th('Step'), th('Action'))}
{tr_norm(td('1'), td('Go to the casino cashier / deposit section'))}
{tr_alt(td('2'), td('Select Apple Pay from payment options'))}
{tr_norm(td('3'), td('Enter deposit amount (check minimum, usually €10–€20)'))}
{tr_alt(td('4'), td('Authenticate with Face ID, Touch ID, or device passcode'))}
{tr_norm(td('5'), td('Funds credited to casino account instantly'))}
</table>

<h2>Apple Pay Casino Deposits: Limits and Considerations</h2>
<table {TABLE_STYLE}>
{tr_head(th('Factor'), th('Detail'))}
{tr_norm(td('Minimum Deposit'), td('Typically €10–€20 (varies by casino)'))}
{tr_alt(td('Maximum Deposit'), td('Usually €500–€2,500 per transaction; daily limits set by your bank'))}
{tr_norm(td('Withdrawal via Apple Pay'), td('Most sites cannot pay back via Apple Pay; use debit card or e-wallet'))}
{tr_alt(td('Linked Card'), td('Apple Pay uses your linked Visa/Mastercard debit card'))}
{tr_norm(td('Credit Card Restriction'), td('Credit card betting banned in Ireland under GRAI rules — only debit cards work'))}
{tr_alt(td('Bonus Eligibility'), td('Usually qualifies for welcome bonus; check casino T&Cs'))}
</table>
"""

EXPANSIONS['pages/best-casino-revolut-ireland.html'] = """
<h2>Using Revolut at Irish Online Casinos</h2>
<table {TABLE_STYLE}>
{tr_head(th('Feature'), th('Standard Revolut'), th('Revolut Premium/Metal'))}
{tr_norm(td('Works at most casinos'), td('Yes — Mastercard accepted'), td('Yes'))}
{tr_alt(td('Gambling category block'), td('Available (toggle in app)'), td('Available'))}
{tr_norm(td('Instant deposit'), td('Yes'), td('Yes'))}
{tr_alt(td('Withdrawal to Revolut'), td('1–2 business days'), td('1–2 business days'))}
{tr_norm(td('No foreign exchange fees'), td('Up to monthly limit'), td('No limit on no-FX rate'))}
{tr_alt(td('Spending analytics'), td('Shows gambling category'), td('More detailed breakdown'))}
</table>

<h2>How to Block Gambling Transactions on Revolut</h2>
<ol style="margin:12px 0;padding-left:20px">
<li style="margin-bottom:8px">Open the Revolut app and go to <strong>Hub</strong> or <strong>Settings</strong></li>
<li style="margin-bottom:8px">Select <strong>Control my spending</strong> or <strong>Card controls</strong></li>
<li style="margin-bottom:8px">Toggle off <strong>Gambling</strong> or <strong>Betting</strong> merchant category</li>
<li style="margin-bottom:8px">Confirm the block — takes effect immediately</li>
</ol>
<p>This block prevents Revolut from processing transactions at merchants categorised as gambling. It is reversible but Revolut adds a 24-hour delay when re-enabling gambling, as a cooling-off protection. If you need help with gambling, contact Gambling Awareness Trust: 1800 753 753 (free). 18+.</p>
"""

EXPANSIONS['pages/best-casino-without-account-ireland.html'] = """
<h2>No-Account (Pay N Play) Casinos in Ireland: How They Work</h2>
<table {TABLE_STYLE}>
{tr_head(th('Step'), th('Traditional Casino'), th('No-Account Casino'))}
{tr_norm(td('Sign-up'), td('Form with email, address, DOB'), td('No form — bank login only'))}
{tr_alt(td('Verification'), td('Upload ID document'), td('Bank-based KYC via Trustly/open banking'))}
{tr_norm(td('Deposit'), td('Choose payment, enter details'), td('Bank login → amount → instant'))}
{tr_alt(td('Withdraw'), td('Request → 1–5 days'), td('Instant to your bank account'))}
{tr_norm(td('Bonus'), td('Welcome offer on signup'), td('Usually no bonus (or reduced)'))  }
</table>

<h2>No-Account Casino Availability in Ireland</h2>
<p>No-account casinos (sometimes called Pay N Play or instant casinos) use Trustly's open banking system for instant verification and payments. The player logs into their bank, the casino checks name and account details against ID registers, and play can begin immediately. In Ireland, the GRAI licensing regime (from July 2026 onwards) requires all operators serving Irish players to hold a GRAI remote betting or gaming licence. No-account casinos are legal to operate in Ireland if licensed — check the GRAI public register at grai.ie before depositing. The main trade-off: no-account casinos rarely offer generous bonuses because there's no traditional onboarding process to incentivise. 18+. Gambling Awareness Trust: 1800 753 753.</p>
"""

EXPANSIONS['pages/best-casino-poker-ireland.html'] = """
<h2>Casino Hold'em vs Texas Hold'em: Key Differences</h2>
<table {TABLE_STYLE}>
{tr_head(th('Factor'), th('Casino Hold\'em'), th('Texas Hold\'em Poker'))}
{tr_norm(td('Played against'), td('The house (dealer)'), td('Other players'))}
{tr_alt(td('Skill element'), td('Low — basic strategy exists'), td('High — bluffing, reads, pot odds'))}
{tr_norm(td('House edge'), td('~2–3% with optimal play'), td('Rake taken from pot (not house edge)'))}
{tr_alt(td('Minimum bet'), td('Usually €1–€5'), td('Varies by table stakes'))}
{tr_norm(td('Speed'), td('Fast — dealer-managed'), td('Slower — player decisions dominate'))}
{tr_alt(td('Live version'), td('Evolution Gaming live tables'), td('Live poker rooms or tournaments'))}
</table>

<h2>Poker Variants Available at Irish Online Casinos</h2>
<p>Irish licensed casinos typically offer: <strong>Casino Hold'em</strong> (player vs dealer with community cards), <strong>Three Card Poker</strong> (3 cards vs dealer, fastest variant), <strong>Caribbean Stud Poker</strong> (5-card hand, progressive jackpot common), and <strong>Ultimate Texas Hold'em</strong> (player can raise early or late). For serious poker players, most live casinos also offer <strong>Poker Tournaments</strong> and <strong>Sit & Go</strong> formats via their poker client (separate software to the casino). The best poker rooms for Irish players are typically offshore-licensed platforms that accept Irish players — check the GRAI register to confirm any operator's licence status. 18+.</p>
"""

EXPANSIONS['pages/best-casino-new-ireland-2026.html'] = """
<h2>What to Check Before Joining a New Casino in Ireland</h2>
<table {TABLE_STYLE}>
{tr_head(th('Check'), th('What to Look For'), th('Where to Verify'))}
{tr_norm(td('GRAI Licence'), td('Remote betting/gaming licence from July 2026'), td('grai.ie public register'))}
{tr_alt(td('Payment Methods'), td('Debit card, PayPal, Revolut, Paysafecard'), td('Casino cashier page'))}
{tr_norm(td('Bonus Terms'), td('Wagering ≤35x, 30-day expiry minimum'), td('Casino T&Cs PDF'))}
{tr_alt(td('Mobile App'), td('iOS/Android native app or mobile site'), td('App Store / Google Play'))}
{tr_norm(td('Customer Support'), td('Live chat available, Irish support hours'), td('Support page test'))}
{tr_alt(td('RG Tools'), td('Deposit limits, session limits, self-exclusion'), td('Responsible gambling page'))}
</table>

<h2>New Irish Casino Bonuses in 2026: What's Changed</h2>
<p>Under the Gambling Regulation Act 2024 and GRAI oversight from July 2026, inducements (bonuses) to Irish residents have new restrictions. Bonuses cannot be marketed to players who have set deposit limits or are in a cooling-off period. Free spins must be granted on specific games, not as open-ended credits. Wagering requirements must be clearly disclosed before the player opts in. These changes protect players but mean the era of large headline bonuses (€1,000 match, 500 free spins) is ending in Ireland. Focus on no-wagering cashback or low-wagering (≤10x) offers for genuine value. 18+. Gambling Awareness Trust: 1800 753 753.</p>
"""

EXPANSIONS['pages/best-casino-crash-games-ireland.html'] = """
<h2>Crash Game Mechanics Explained</h2>
<table {TABLE_STYLE}>
{tr_head(th('Element'), th('How It Works'))}
{tr_norm(td('Multiplier'), td('Starts at 1x and rises — sometimes slowly, sometimes fast'))}
{tr_alt(td('Cash Out'), td('Player clicks to collect at any point before crash'))}
{tr_norm(td('Crash Point'), td('Random — determined by provably fair algorithm before round starts'))}
{tr_alt(td('Auto Cash Out'), td('Set a target multiplier (e.g. 2x) — game cashes out automatically'))}
{tr_norm(td('House Edge'), td('Typically 4–5% per round; multiple rounds per minute means fast losses'))}
{tr_alt(td('Variance'), td('Extreme — most rounds crash below 2x; rare 10x+ events'))}
</table>

<h2>Crash Games and Irish Gambling Rules</h2>
<p>Crash games (Aviator, JetX, Spaceman, etc.) are classified as casino/gaming products. Under GRAI rules, operators offering crash games to Irish players need a gaming licence — which GRAI has not yet issued (expected 2027/2028). Until Irish gaming licences are issued, crash games may only be offered by operators holding a valid licence from another EU/EEA jurisdiction. Always verify an operator's licence at grai.ie before playing. The fast-paced nature of crash games (many rounds per minute) makes responsible gambling tools essential — set a session time limit and a loss limit before playing. 18+. Gambling Awareness Trust: 1800 753 753.</p>
"""

# Wagering requirements
EXPANSIONS['pages/casino-wagering-requirement-explained.html'] = """
<h2>Wagering Requirement: Worked Examples</h2>
<table {TABLE_STYLE}>
{tr_head(th('Bonus'), th('Wagering'), th('Total Bets Required'), th('Withdrawal Available After'))}
{tr_norm(td('€50 bonus'), td('30x'), td('€1,500'), td('Any remaining bonus + winnings'))}
{tr_alt(td('€100 bonus'), td('35x'), td('€3,500'), td('Any remaining bonus + winnings'))}
{tr_norm(td('€20 free spins (SNR)'), td('40x on winnings only'), td('€400 if you win €10'), td('Real cash after turnover'))}
{tr_alt(td('€200 deposit match'), td('20x deposit+bonus'), td('€6,000'), td('After €6k wagered'))}
{tr_norm(td('€10 no-deposit'), td('50x'), td('€500'), td('Usually capped at €100 max withdrawal'))}
</table>
"""

EXPANSIONS['pages/what-is-wagering-requirement-ireland.html'] = """
<h2>Wagering Requirement vs No-Wagering: Which Is Better?</h2>
<table {TABLE_STYLE}>
{tr_head(th('Bonus Type'), th('Wagering'), th('Real Value on €100 Bonus'))}
{tr_norm(td('Standard 35x bonus'), td('35x = €3,500 to wager'), td('~€40–60 expected value with 2% slots RTP loss'))}
{tr_alt(td('No-wagering cashback 20%'), td('None'), td('€20 real cash on €100 losses'))}
{tr_norm(td('10x low-wager match'), td('10x = €1,000 to wager'), td('~€80 expected value'))}
{tr_alt(td('SNR free bet'), td('No wager — just stake not returned'), td('€X × (odds-1) / odds'))}
</table>

<h2>How to Calculate if a Casino Bonus Is Worth Taking</h2>
<p>Simple formula: <strong>Bonus Value = Bonus Amount − (Wagering Requirement × House Edge)</strong>. For a €100 bonus at 35x wagering, with a 3% average house edge on eligible slots: €100 − (€3,500 × 0.03) = €100 − €105 = <strong>−€5</strong>. This means you're statistically expected to lose €5 more than you get from the bonus — it's a negative-value offer. Bonuses become positive-value when: wagering ≤ 20x, house edge ≤ 2% (high-RTP slots count toward playthrough), or no wagering at all. Always read full T&Cs before opting in. 18+.</p>
"""

EXPANSIONS['pages/casino-self-exclusion-ireland.html'] = """
<h2>Casino Self-Exclusion Options in Ireland</h2>
<table {TABLE_STYLE}>
{tr_head(th('Option'), th('Duration'), th('Coverage'), th('How to Apply'))}
{tr_norm(td('Site-level self-exclusion'), td('30 days to 5 years+'), td('That casino only'), td('Account settings → Responsible Gambling'))}
{tr_alt(td('GRAI Self-Exclusion Register (when available)'), td('TBC'), td('All GRAI-licensed operators'), td('grai.ie (register in development)'))}
{tr_norm(td('Gambling Awareness Trust counselling'), td('No time limit'), td('Support service'), td('gamblingcare.ie or 1800 753 753'))}
{tr_alt(td('Bank gambling block'), td('Reversible (24-hour delay on removal)'), td('All gambling transactions from that card'), td('App settings (Revolut, AIB, BOI, etc.)'))}
</table>

<h2>What Happens During Self-Exclusion</h2>
<p>When you self-exclude from an Irish licensed casino, the operator is required to: immediately suspend your account, remove you from marketing lists, refund any remaining balance (minus any active bonus), and not reactivate your account for the chosen period. If you approach the site to re-open your account during exclusion, they must decline. Under the Gambling Regulation Act 2024, GRAI is building a national self-exclusion register — when live, one registration will cover all GRAI-licensed operators. Until it launches, self-exclude individually at each site you use. For free, confidential support: Gambling Awareness Trust, 1800 753 753, gamblingcare.ie. 18+.</p>
"""

EXPANSIONS['pages/casino-holdem-ireland.html'] = """
<h2>Casino Hold'em: Optimal Strategy Table</h2>
<table {TABLE_STYLE}>
{tr_head(th('Hand Strength'), th('Action'), th('Reason'))}
{tr_norm(td('Pair or better (pocket pair)'), td('Call'), td('Strong equity vs dealer'))}
{tr_alt(td('Four to a flush'), td('Call'), td('Good draw; worth continuing'))}
{tr_norm(td('Open-ended straight draw (8+ outs)'), td('Call'), td('Roughly 32% to hit'))}
{tr_alt(td('Any pair on the board (match)'), td('Call'), td('Use community cards'))}
{tr_norm(td('Weak hand, no draws'), td('Fold'), td('Save ante bet loss beyond this'))}
{tr_alt(td('Two overcards (A-K or A-Q)'), td('Call'), td('Good top-pair potential'))}
</table>

<h2>Casino Hold'em House Edge and Payouts</h2>
<p>Casino Hold'em pays 1:1 on the Call bet when you beat the dealer. The dealer must have at least a pair of 4s to qualify; if not, the Call bet pushes and the Ante wins 1:1. The Ante has a bonus pay table: straight flush pays 20:1, four of a kind 10:1, full house 3:1, flush 2:1, straight 1:1. The base house edge with optimal strategy is approximately <strong>2.16%</strong>. The optional AA+ side bet (pays on pair of aces or better) has a significantly higher house edge of around <strong>6.4%</strong> — it is optional and not recommended for value-conscious players. 18+.</p>
"""

EXPANSIONS['pages/cash-out-explained.html'] = """
<h2>Cash Out: How the Price Is Calculated</h2>
<table {TABLE_STYLE}>
{tr_head(th('Factor'), th('Effect on Cash Out Price'))}
{tr_norm(td('Current probability of your selection winning'), td('Higher probability = higher cash out'))}
{tr_alt(td('Bookmaker margin applied twice'), td('You pay margin when placing and when cashing out'))}
{tr_norm(td('Time remaining in event'), td('More time left = more uncertainty = lower cash out ratio'))}
{tr_alt(td('Number of legs remaining (accas)'), td('More legs = lower cash out per original stake'))}
{tr_norm(td('Live score/game state'), td('Goal scored for you = cash out rises; against = drops'))}
</table>

<h2>Partial Cash Out Strategy</h2>
<p>Many bookmakers offer <strong>partial cash out</strong> — you sell part of your bet and let the rest run. Example: €20 acca with 3 legs remaining, cash out available at €60. Partial cash out at 50% = collect €30 now, let €30 ride on the remaining legs. This locks in profit while keeping upside. Useful when: you've hit 3 of 5 acca legs and the remaining two are genuinely uncertain, or when you placed a pre-match bet and new information (injury, weather) makes you uncertain. Avoid partial cash out simply due to nerves — the mathematical cost of repeated cash outs compounds quickly. 18+.</p>
"""

EXPANSIONS['pages/how-do-welcome-bonuses-work-ireland.html'] = """
<h2>Welcome Bonus Types at Irish Betting Sites</h2>
<table {TABLE_STYLE}>
{tr_head(th('Bonus Type'), th('How It Works'), th('Common at'))}
{tr_norm(td('Deposit Match'), td('Casino matches first deposit up to a cap (e.g. 100% up to €200)'), td('Online casinos'))}
{tr_alt(td('Free Bet (SNR)'), td('Bet returned as free bet token (stake not returned on win)'), td('Sports betting'))}
{tr_norm(td('No-Deposit Bonus'), td('Small credit given on registration, no deposit needed'), td('Casino — rare in Ireland now'))}
{tr_alt(td('Free Spins'), td('Set number of spins on specified slot games'), td('Casino slot promotions'))}
{tr_norm(td('Bet & Get'), td('Place qualifying bet → receive free bet or bonus credit'), td('Sports betting'))}
{tr_alt(td('Cashback Bonus'), td('% of losses returned as bonus or real cash'), td('Casino and sports'))}
</table>

<h2>Welcome Bonus Terms: What to Check</h2>
<p>Before claiming any welcome bonus, check: (1) <strong>Wagering requirement</strong> — how many times must you bet the bonus before withdrawing? 30–40x is industry average; under 20x is good value; (2) <strong>Time limit</strong> — most bonuses expire in 7–30 days; (3) <strong>Game restrictions</strong> — table games often count at 10% or 0% toward wagering; (4) <strong>Max bet rule</strong> — most bonuses restrict bets to €5–€10 per spin while wagering is active; (5) <strong>Withdrawal cap</strong> — no-deposit bonuses often cap winnings at €100–€200. Under GRAI regulations, Irish operators must display all bonus terms clearly before you opt in. 18+. Gambling Awareness Trust: 1800 753 753.</p>
"""

EXPANSIONS['pages/what-is-an-accumulator-ireland.html'] = """
<h2>Accumulator Types and Minimum Legs</h2>
<table {TABLE_STYLE}>
{tr_head(th('Bet Type'), th('Legs Required'), th('Example Combined Odds'))}
{tr_norm(td('Double'), td('2'), td('2/1 × 2/1 = 8/1'))}
{tr_alt(td('Treble'), td('3'), td('2/1 × 2/1 × 2/1 = 26/1'))}
{tr_norm(td('4-fold Accumulator'), td('4'), td('2/1 × 2/1 × 2/1 × 2/1 = 80/1'))}
{tr_alt(td('5-fold Accumulator'), td('5'), td('2/1 × 2/1 × 2/1 × 2/1 × 2/1 = 242/1'))}
{tr_norm(td('Yankee'), td('4 (11 bets)'), td('Covers all doubles, trebles, 1×4-fold'))}
{tr_alt(td('Lucky 15'), td('4 (15 bets)'), td('All doubles, trebles, 4-fold + all 4 singles'))}
</table>

<h2>Accumulator Expected Value: The Maths</h2>
<p>Each leg of an accumulator multiplies both the potential winnings <em>and</em> the bookmaker's margin. With a 5% margin per leg, a 5-leg acca has an effective combined margin of approximately 23% — meaning the expected return is 77p in every €1 staked. Accumulators are popular because they offer large payouts from small stakes (€1 five-fold can return €100+), but the statistical cost is high. For value, reduce legs to 3–4 maximum and select outcomes with genuine insight. Avoid "template accas" promoted by betting sites — these often feature their most margined markets. 18+.</p>
"""

EXPANSIONS['pages/how-to-complain-to-grai.html'] = """
<h2>How to File a Complaint with GRAI</h2>
<table {TABLE_STYLE}>
{tr_head(th('Step'), th('Action'))}
{tr_norm(td('1'), td('Complain to the operator first (required before escalating to GRAI)'))}
{tr_alt(td('2'), td('Allow 8 weeks for the operator to respond'))}
{tr_norm(td('3'), td('If unresolved, file with GRAI at grai.ie → Complaints section'))}
{tr_alt(td('4'), td('Provide: account details, complaint summary, evidence (screenshots), operator response'))}
{tr_norm(td('5'), td('GRAI acknowledges within 5 working days'))}
{tr_alt(td('6'), td('Resolution timeline varies (weeks to months depending on complexity)'))}
</table>

<h2>What GRAI Can and Cannot Do</h2>
<p>GRAI (Gambling Regulatory Authority of Ireland) can investigate complaints about: failure to pay out winnings from a licensed operator, breach of GRAI licence conditions, misleading advertising, failure to implement self-exclusion, unfair bonus terms. GRAI cannot: compel an unlicensed offshore site to pay you, resolve disputes about individual bet settlements (unless systemic), or act as an arbitrator in real-time (complaints are retrospective). For bonus disputes, check the operator's T&Cs carefully first — many disputes involve bonus abuse rules or wagering completion. For urgent help, the Gambling Awareness Trust (1800 753 753) can provide support. 18+.</p>
"""

EXPANSIONS['pages/crypto-betting-without-verification-ireland.html'] = """
<h2>Crypto Betting Without Verification: What This Actually Means</h2>
<table {TABLE_STYLE}>
{tr_head(th('Claim'), th('Reality for Irish Players'))}
{tr_norm(td('"No KYC betting site"'), td('Site may still require ID at withdrawal or above certain thresholds'))}
{tr_alt(td('"Anonymous crypto betting"'), td('Blockchain transactions are pseudonymous, not anonymous — traceable'))}
{tr_norm(td('"No licence required"'), td('False — GRAI requires a licence to serve Irish residents'))}
{tr_alt(td('"Instant withdrawal"'), td('Crypto withdrawals can be fast but blockchain confirmation takes minutes to hours'))}
{tr_norm(td('"Tax-free"'), td('False — Irish Revenue treats crypto gambling winnings as taxable income in some cases'))}
</table>

<h2>Risks of Unlicensed Crypto Betting Sites for Irish Players</h2>
<p>Sites that advertise "no verification" or "anonymous" crypto betting often operate without an Irish licence. Under the Gambling Regulation Act 2024, any operator serving Irish residents must hold a GRAI licence (from July 2026 onwards for remote betting). Using an unlicensed site means: no protection if the site refuses to pay, no recourse via GRAI, no guaranteed compliance with responsible gambling standards, and potential issues with Irish Revenue if large winnings are not declared. Before depositing at any site, verify their licence at grai.ie. If they appear on GRAI's blacklisted sites list, they cannot legally take Irish bets. 18+.</p>
"""

EXPANSIONS['pages/bonus-abuse-ireland.html'] = """
<h2>What Counts as Bonus Abuse at Irish Casinos</h2>
<table {TABLE_STYLE}>
{tr_head(th('Activity'), th('Classified As'), th('Risk'))}
{tr_norm(td('Claiming same bonus via multiple accounts'), td('Bonus abuse (terms violation)'), td('Account closure, bonus voided'))}
{tr_alt(td('Matched betting (using free bets to cover all outcomes)'), td('Technically permitted but frowned on'), td('Account may be gubbed (restricted)'))}
{tr_norm(td('Playing low-edge games to clear wagering faster'), td('Usually permitted — check T&Cs'), td('Some bonuses exclude blackjack for this reason'))}
{tr_alt(td('Abusing casino sign-up offer then immediately withdrawing'), td('Bonus abuse if pattern repeated'), td('Flagged by risk team; restricted from future bonuses'))}
{tr_norm(td('Creating family member accounts to claim same offer'), td('Bonus abuse'), td('All related accounts closed'))}
</table>

<h2>Legitimate Bonus Strategy vs Abuse: Where the Line Is</h2>
<p>Irish casinos have automated systems that flag unusual patterns. Legitimate bonus play means: claiming offers as intended (one per household/IP address), playing the stipulated wagering on games permitted by the T&Cs, and accepting that winnings from low-edge games may not fully count toward wagering. Bonus abuse risks account closure and forfeiture of all funds — including genuine deposits in some cases. If you're unsure whether a strategy crosses the line, read the bonus T&Cs carefully or contact customer support before proceeding. 18+. Gambling Awareness Trust: 1800 753 753.</p>
"""

EXPANSIONS['pages/high-roller-casino-ireland.html'] = """
<h2>High Roller Table Limits at Irish Online Casinos</h2>
<table {TABLE_STYLE}>
{tr_head(th('Game'), th('Standard Table'), th('VIP High-Roller Table'))}
{tr_norm(td('Live Blackjack'), td('€0.50 – €500'), td('€200 – €25,000+'))}
{tr_alt(td('Live Roulette'), td('€0.20 – €1,000'), td('€100 – €20,000+'))}
{tr_norm(td('Live Baccarat'), td('€1 – €1,000'), td('€100 – €50,000'))}
{tr_alt(td('Slots (max bet per spin)'), td('Usually €5 – €50'), td('Some slots cap at €100–€500 per spin'))}
{tr_norm(td('Live Poker'), td('€5 – €500'), td('€200 – €10,000'))}
</table>

<h2>VIP Casino Programmes for Irish High Rollers</h2>
<p>High-roller accounts at Irish licensed casinos typically offer: dedicated account manager, faster withdrawal processing (some same-day), personalised deposit and withdrawal limits, invitations to exclusive tournaments, and cashback on losses (5–15% for elite tiers). To access VIP status, you usually need to reach a monthly deposit or wagering threshold — this varies greatly between casinos. Important note: GRAI-licensed operators must assess player affordability under the Gambling Regulation Act 2024. High-volume players may be asked to provide proof of income or source of funds — this is a regulatory requirement, not optional. 18+.</p>
"""

EXPANSIONS['pages/all-ireland-final-weekend-betting.html'] = """
<h2>All-Ireland Final Weekend: Schedule and Betting Markets</h2>
<table {TABLE_STYLE}>
{tr_head(th('Event'), th('Typical Date'), th('Venue'), th('Key Markets'))}
{tr_norm(td('All-Ireland Hurling Final'), td('Second Sunday in July'), td('Croke Park, Dublin'), td('Outright, HT/FT, first scorer, most wides'))}
{tr_alt(td('All-Ireland Football Final'), td('Fourth Sunday in July'), td('Croke Park, Dublin'), td('Outright, most scores, winning margin, top scorer'))}
{tr_norm(td('Camogie All-Ireland Final'), td('Mid-July'), td('Croke Park'), td('Limited market availability'))}
</table>

<h2>Croke Park Betting: What to Know</h2>
<p>All-Ireland Finals are played at Croke Park, Dublin — 82,300 capacity, the third-largest stadium in Europe. Ticket demand massively exceeds supply, so attendance requires county membership or ticket ballot. For betting purposes, the neutral venue means no traditional home advantage applies. However, Dublin (football) and Kilkenny (hurling) fans travel in large numbers regardless, with strong vocal support. First-half vs second-half patterns: leading sides often push harder in the second half once teams separate. The winning margin market is popular — over 7 points is quite common in hurling finals; football finals are typically tighter. 18+.</p>
"""

EXPANSIONS['pages/grand-national-week-betting.html'] = """
<h2>Aintree Grand National Festival: Day-by-Day Guide</h2>
<table {TABLE_STYLE}>
{tr_head(th('Day'), th('Key Race'), th('Distance'), th('Betting Highlight'))}
{tr_norm(td('Thursday — Aintree Day 1'), td('Manifesto Novices\' Chase'), td('2m4f Grade 1'), td('Premier novice chase'))}
{tr_alt(td('Friday — Ladies Day'), td('Aintree Hurdle'), td('2m4f Grade 1'), td('Quality hurdlers'))}
{tr_norm(td('Friday'), td('Mildmay Novices\' Chase'), td('3m1f Grade 1'), td('Stayers novice form'))}
{tr_alt(td('Saturday — Grand National Day'), td('Grand National'), td('4m2f handicap'), td('World\'s most famous horse race'))}
</table>

<h2>Grand National Betting Strategy</h2>
<p>The Grand National is a 4m2f handicap over 30 fences at Aintree. With fields of 40 runners, it is statistically the hardest race to win in UK/Irish racing. Each-way is essential — bookmakers offer 1/5 odds, 5–8 places on the National. Winning chances are more tied to jumping ability, weight, and fitness than raw form. Each-way value often exists at prices of 20/1–40/1 for well-handicapped runners with strong Cheltenham form. The Gold Cup winner is rarely the National favourite — the two tests are different. Irish trainers (Willie Mullins, Gordon Elliott) have excellent modern records. The last-to-leave-the-parade-ring horse often gets market support — a traditional Aintree superstition. 18+. No pronostic is guaranteed.</p>
"""

EXPANSIONS['pages/new-years-day-betting-ireland.html'] = """
<h2>New Year's Day Racing in Ireland: Key Fixtures</h2>
<table {TABLE_STYLE}>
{tr_head(th('Venue'), th('Type'), th('Notable Race'))}
{tr_norm(td('Tramore Racecourse, Co. Waterford'), td('National Hunt'), td('Tramore New Year\'s Day Festival — traditional holiday meeting'))}
{tr_alt(td('Punchestown Racecourse, Co. Kildare'), td('National Hunt'), td('Grade B hurdle and chase cards'))}
{tr_norm(td('Cheltenham'), td('UK NH (New Year\'s Day fixture)'), td('Trials ahead of Festival'))}
{tr_alt(td('ITV Racing / RTE'), td('TV coverage'), td('Bank holiday racing broadcast in Ireland'))}
</table>

<h2>Betting on New Year's Day Racing</h2>
<p>New Year's Day is a bank holiday in Ireland — multiple race meetings run, and betting shops are open. Tramore is the most traditionally Irish New Year's racing fixture, often featuring local runners. The ground in January is typically soft-to-heavy in Ireland, heavily favouring stamina-based horses and those with proven soft-ground form. For betting, check overnight ground conditions (posted on each racecourse's website). Trainers who run horses on New Year's Day are likely prepping for Leopardstown's Faugheen Novice Hurdle or Punchestown's Grade 2 cards later in January. 18+.</p>
"""

EXPANSIONS['pages/easter-monday-betting-ireland.html'] = """
<h2>Easter Monday Racing and Betting in Ireland</h2>
<table {TABLE_STYLE}>
{tr_head(th('Venue'), th('Meeting Type'), th('Note'))}
{tr_norm(td('Fairyhouse Racecourse'), td('Irish Grand National (Easter Saturday)'), td('Ireland\'s most famous spring handicap chase'))}
{tr_alt(td('Leopardstown Racecourse'), td('Spring flat card'), td('Transition from jumps to flat season'))}
{tr_norm(td('UK — Kempton'), td('Bank holiday flat card'), td('Watched widely by Irish bettors via ITV'))}
{tr_alt(td('UK — Lingfield'), td('All-weather'), td('Additional betting opportunities'))}
</table>

<h2>Irish Grand National (Fairyhouse) Betting Guide</h2>
<p>The Irish Grand National takes place on Easter Monday at Fairyhouse, Co. Meath. It is a Grade A handicap chase over 3m5f — shorter and less extreme than Aintree but highly competitive. Fields of 20–30 runners make it a true betting puzzle. Each-way with 4–5 places is essential. Irish trainers dominate — Willie Mullins, Gordon Elliott, and Jessica Harrington regularly target this race. Ground conditions in April vary between good-to-yielding and yielding-to-soft; check in the week before for official ground readings. High-weight horses rarely win — look for well-handicapped runners carrying 10st 10lb or less. 18+. Gambling Awareness Trust: 1800 753 753.</p>
"""

EXPANSIONS['pages/world-cup-2026-host-nations-betting.html'] = """
<h2>FIFA World Cup 2026: Host Nations Overview</h2>
<table {TABLE_STYLE}>
{tr_head(th('Country'), th('Host Cities'), th('Group Stage Advantage'))}
{tr_norm(td('United States'), td('16 cities including New York, LA, Dallas, Miami'), td('Significant home support; large stadiums'))}
{tr_alt(td('Canada'), td('Toronto, Vancouver'), td('Less traditional football country; novelty factor'))}
{tr_norm(td('Mexico'), td('Mexico City, Guadalajara, Monterrey'), td('Azteca Stadium — huge home crowd pressure'))}
</table>

<h2>Host Nation Betting Trends at World Cups</h2>
<p>Host nations automatically qualify for the World Cup. Historical betting context: host nations have won the World Cup 6 times (Uruguay 1930, Italy 1934, England 1966, West Germany 1974, Argentina 1978, France 1998). In recent tournaments, hosts have underperformed their opening odds — South Africa 2010 (eliminated group stage), Brazil 2014 (7-1 loss to Germany), Russia 2018 (quarter-final). The United States has the strongest squad of the three 2026 hosts and may have genuine knockoutstage potential. Canada and Mexico start as longer-priced outsiders. For outright betting, focus on European powers and Brazil/Argentina — the most consistent winners. 18+. No pronostic is guaranteed.</p>
"""

EXPANSIONS['pages/world-cup-2026-group-stage-betting.html'] = """
<h2>World Cup 2026 Group Stage Format</h2>
<table {TABLE_STYLE}>
{tr_head(th('Detail'), th('Information'))}
{tr_norm(td('Teams'), td('48 teams (expanded from 32 in 2022)'))}
{tr_alt(td('Groups'), td('12 groups of 4 teams'))}
{tr_norm(td('Qualification'), td('Top 2 from each group + 8 best third-placed teams = 32 advance'))}
{tr_alt(td('Total Group Matches'), td('72 group-stage matches'))}
{tr_norm(td('Host Cities'), td('USA (16), Mexico (3), Canada (2)'))}
{tr_alt(td('Kick-off Times (Irish)'), td('3pm, 6pm, 9pm IST for evening games; some afternoon starts'))}
</table>

<h2>Group Stage Betting Strategy for World Cup 2026</h2>
<p>With 12 groups of 4 teams, the expanded format means more group games and more variety. For betting, consider: (1) <strong>Group winner</strong> — the top seed usually wins their group, but not always (Germany eliminated at group stage in 2018 and 2022); (2) <strong>To qualify (top 2)</strong> — a safer bet than outright group winner; (3) <strong>Total group goals</strong> — groups featuring high-scoring favourites against weaker opponents offer over-goal value; (4) <strong>Correct score</strong> — wide margins on bet365/Paddy Power so small stakes only. The 8 best third-placed teams also advance in 2026 — this means a team can lose 2 games and still reach the round of 32. This changes the risk calculus for group-stage betting. 18+.</p>
"""

print("All content defined. Now running expansion scripts...")
print(f"Total pages to expand: {len(EXPANSIONS)}")

# Apply all expansions
import os

results = []
for filepath, new_html in EXPANSIONS.items():
    if not os.path.exists(filepath):
        results.append(f"SKIP (not found): {filepath}")
        continue

    # Format the HTML with proper table formatting
    formatted = new_html.format(
        TABLE_STYLE=TABLE_STYLE,
        tr_head=tr_head, tr_norm=tr_norm, tr_alt=tr_alt,
        th=th, td=td
    )

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_size = len(content)
    new_content = insert_before_faq(content, formatted)

    if len(new_content) == original_size:
        results.append(f"WARN (no insertion point): {filepath}")
        continue

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    results.append(f"OK: {filepath} ({original_size} → {len(new_content)} bytes)")

for r in results:
    print(r)
