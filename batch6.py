#!/usr/bin/env python3
import os

TS = 'style="width:100%;border-collapse:collapse;margin:16px 0;font-size:0.95rem"'
TH = 'style="padding:9px;border:1px solid #2d5a3d;text-align:left;color:#cde6d4"'
TD = 'style="padding:8px;border:1px solid #2d5a3d"'
TRH = 'style="background:#1e3a28"'
TRA = 'style="background:#0d1f14"'

def th(t): return '<th ' + TH + '>' + str(t) + '</th>'
def td(t): return '<td ' + TD + '>' + str(t) + '</td>'
def trh(*c): return '<tr ' + TRH + '>' + ''.join(c) + '</tr>'
def trn(*c): return '<tr>' + ''.join(c) + '</tr>'
def tra(*c): return '<tr ' + TRA + '>' + ''.join(c) + '</tr>'
def tbl(*rows): return '<table ' + TS + '>' + ''.join(rows) + '</table>'

def h2(t): return '<h2>' + t + '</h2>'
def p(t): return '<p>' + t + '</p>'

def insert(content, html):
    for marker in ['<div class="editorial-box"', '<div class="faq-item"', '<h2>Frequently Asked Questions</h2>']:
        if marker in content:
            return content.replace(marker, html + '\n' + marker, 1)
    return content + html

expansions = {}

# 1. Ligue 1
expansions['pages/ligue-1-betting-ireland.html'] = (
    h2('Ligue 1 Betting Markets for Irish Punters') +
    tbl(
        trh(th('Market'), th('Description'), th('Typical Margin')),
        trn(td('1X2 Match Result'), td('Home win / draw / away win on 90 minutes'), td('7-9%')),
        tra(td('Asian Handicap'), td('Level the field with fractional goal lines'), td('5-6%')),
        trn(td('Over/Under Goals'), td('Total goals above or below 2.5 / 3.5'), td('6-7%')),
        tra(td('Both Teams to Score'), td('Yes/No on both sides netting'), td('7-8%')),
        trn(td('Outright Winner'), td('Season-long market, ante-post from August'), td('12-18%')),
        tra(td('Top Scorer'), td('Most goals in Ligue 1 - high margins'), td('15-20%')),
    ) +
    h2('Key Ligue 1 Clubs for Irish Bettors') +
    tbl(
        trh(th('Club'), th('Strength'), th('Note for Bettors')),
        trn(td('Paris Saint-Germain'), td('Dominant'), td('Short prices on most matchdays; value elsewhere')),
        tra(td('Olympique de Marseille'), td('Strong'), td('High-scoring; good for BTTS markets')),
        trn(td('AS Monaco'), td('Consistent top-4'), td('Good European record')),
        tra(td('Lille OSC'), td('Tactically solid'), td('Low-scoring; under-2.5 potential')),
        trn(td('OGC Nice'), td('Top-6 candidate'), td('Home record worth checking')),
    ) +
    p('Ligue 1 is available in Ireland via beIN Sports (Sky Sports add-on or streaming). Amazon Prime Video also holds UK/Ireland rights for select Ligue 1 fixtures. Kick-off times in Irish time are typically 20:00 on Fridays, 17:00 or 21:00 on Saturdays, and 20:45 on Sundays. 18+.')
)

# 2. Conference League
expansions['pages/conference-league-betting-ireland.html'] = (
    h2('UEFA Conference League Format and Betting Implications') +
    tbl(
        trh(th('Stage'), th('Format'), th('Betting Approach')),
        trn(td('League Phase'), td('6 group matches per club'), td('Outright winner ante-post; goals markets popular')),
        tra(td('Play-off Round'), td('Two-legged tie'), td('Asian handicap on aggregate; first-leg draw common')),
        trn(td('Round of 16'), td('Two legs'), td('Home advantage historically decisive')),
        tra(td('Quarter-Finals'), td('Two legs'), td('Top seeds win approximately 70% of QFs')),
        trn(td('Semi-Finals'), td('Two legs'), td('Second leg usually tighter')),
        tra(td('Final'), td('Single match, neutral'), td('Each-way outright value from QF stage')),
    ) +
    h2('Conference League - Which Nations Compete Well') +
    tbl(
        trh(th('Country'), th('Historical Performance'), th('Typical Outright Range')),
        trn(td('England'), td('2 of last 3 winners'), td('3/1 - 7/1 for top-4 PL clubs')),
        tra(td('Netherlands'), td('Final in 2021'), td('8/1 - 14/1')),
        trn(td('Portugal'), td('Consistent semi-finalists'), td('10/1 - 20/1')),
        tra(td('Greece'), td('Panathinaikos/Olympiakos reach QFs'), td('16/1 - 25/1')),
        trn(td('Czech Republic'), td('Slavia/Sparta regular runners'), td('20/1 - 33/1')),
    )
)

# 3. Scottish Premiership
expansions['pages/scottish-premiership-betting-ireland.html'] = (
    h2('Scottish Premiership Betting Markets') +
    tbl(
        trh(th('Market'), th('Description'), th('Irish Bettor Notes')),
        trn(td('Outright Winner'), td('Season champion ante-post'), td('Celtic or Rangers win approximately 95% of titles')),
        tra(td('Top 6 Finish'), td('European qualification group'), td('Hearts, Hibs, Aberdeen compete annually')),
        trn(td('Relegation'), td('Bottom 2 from 12 teams'), td('Newly promoted sides most vulnerable')),
        tra(td('Match 1X2'), td('Standard result market'), td('Wider margins than EPL - typically 8-10%')),
        trn(td('Scottish Cup'), td('Knockout competition'), td('Runs February to May')),
        tra(td('Old Firm Derby'), td('Celtic vs Rangers specific'), td('4-5 times per season; most bet-on Scottish fixture')),
    ) +
    p('Celtic win approximately 60% of matches at Celtic Park; Rangers win roughly 55% at Ibrox. Draws occur in around 25% of derbies. BTTS (both teams to score) lands approximately 65% of Old Firm games. First scorer and total cards are also popular Old Firm markets. 18+.')
)

# 4. League Cup
expansions['pages/league-cup-ireland-betting.html'] = (
    h2('EFL League Cup Rounds and Betting Strategy') +
    tbl(
        trh(th('Round'), th('Stage'), th('Betting Notes')),
        trn(td('1-2'), td('Lower-league clubs enter; EPL sides with large squads'), td('Giant-killings common; each-way on underdogs has value')),
        tra(td('3-4'), td('All 20 EPL clubs enter; rotation heavy'), td('Team news crucial - rested starters change market')),
        trn(td('QF'), td('8 clubs remain'), td('Big clubs field stronger sides; shorter prices')),
        tra(td('SF'), td('Two-legged tie'), td('Aggregate markets available; first leg often cautious')),
        trn(td('Final'), td('Single match at Wembley'), td('Ante-post from QF stage viable')),
    ) +
    h2('League Cup vs FA Cup for Irish Bettors') +
    tbl(
        trh(th('Factor'), th('League Cup'), th('FA Cup')),
        trn(td('Upsets'), td('More frequent (rotation lineups)'), td('Moderate')),
        tra(td('Each-way value'), td('Good in rounds 1-3'), td('Good in rounds 3-4')),
        trn(td('Irish TV'), td('Sky Sports'), td('BBC/ITV via streaming in Ireland')),
        tra(td('Prestige'), td('Lower - clubs prioritise EPL'), td('Higher - older competition')),
    )
)

# 5. Euro 2028
expansions['pages/euro-2028-host-nations-betting.html'] = (
    h2('Euro 2028 Host Nations: Venues and Irish Interest') +
    tbl(
        trh(th('Country'), th('Confirmed Host'), th('Note')),
        trn(td('Republic of Ireland'), td('Yes - co-host'), td('Automatic qualification; Aviva Stadium, Dublin')),
        tra(td('England'), td('Yes'), td('Auto-qualifies; Wembley Stadium final venue')),
        trn(td('Scotland'), td('Yes'), td('Auto-qualifies; Hampden Park, Glasgow')),
        tra(td('Wales'), td('Yes'), td('Auto-qualifies; Cardiff City Stadium')),
        trn(td('Northern Ireland'), td('Yes'), td('Auto-qualifies; Windsor Park, Belfast')),
    ) +
    h2('Euro 2028 Outright Betting: Early Markets') +
    tbl(
        trh(th('Nation'), th('Form Trend'), th('Indicative Early Odds')),
        trn(td('Spain'), td('Reigning Euro champion (2024)'), td('5/1 - 8/1')),
        tra(td('France'), td('Consistent finalist'), td('6/1 - 9/1')),
        trn(td('England'), td('Improving squad depth'), td('7/1 - 12/1')),
        tra(td('Germany'), td('Host of Euro 2024'), td('8/1 - 14/1')),
        trn(td('Republic of Ireland'), td('Host; squad rebuilding'), td('50/1 - 100/1 ante-post')),
    ) +
    p('As co-hosts, Ireland benefit from playing group matches at the Aviva Stadium in Dublin with home support. Historical context: host nations have won the Euros 3 times (Spain 1964, Italy 1968, France 1984). 18+.')
)

# 6. Wimbledon 2027
expansions['pages/wimbledon-2027-betting-ireland.html'] = (
    h2('Wimbledon 2027 Betting Markets') +
    tbl(
        trh(th('Market'), th('Description'), th('Notes')),
        trn(td("Outright Winner - Men's"), td('Champion over 7 rounds'), td('Top seeds dominate Wimbledon more than other Slams')),
        tra(td("Outright Winner - Women's"), td("Women's champion"), td('More unpredictable; each-way value in draw')),
        trn(td('Match Winner'), td('Individual match 2-way'), td('No draw; most common Wimbledon bet')),
        tra(td('Set Betting'), td('Exact set score'), td('High margins 15-20%; small stakes only')),
        trn(td('Total Games'), td('Over/under total games'), td('Good for form players on specific surfaces')),
        tra(td('Each-Way Outright'), td('Usually top 4 or finalist'), td('Ask bookmaker for each-way terms before placing')),
    ) +
    p("Key pre-Wimbledon grass events include Queen's Club (men's) and Eastbourne/Berlin (women's). A win at Queen's is a strong Wimbledon indicator. Players ranked 1-4 win the men's title in roughly 65% of editions. For the women's draw, the top seed wins around 40% of the time - each-way value often exists at 10/1+ for in-form grass-court players. 18+.")
)

# 7. Open Championship 2027
expansions['pages/open-championship-2027-betting-ireland.html'] = (
    h2('The Open Championship 2027: Betting Markets') +
    tbl(
        trh(th('Market'), th('Description'), th('Irish Bettor Tip')),
        trn(td('Outright Winner'), td('72-hole stroke play champion'), td('Each-way 1/5 odds, 8 places common')),
        tra(td('Top 10 / Top 20 Finish'), td('Place markets without win needed'), td('Better value for quality fields')),
        trn(td('Round Leader'), td('Best score after each round'), td('High variance; small stakes')),
        tra(td('Nationality Specials'), td('Best European, Best Irish player'), td('Good value if Irish player in strong form')),
        trn(td('Hole-in-One'), td('Any player makes hole-in-one'), td('Usually 2/1 to 7/4 depending on course')),
        tra(td('Cut/No Cut'), td('Whether player makes 36-hole cut'), td('Form + links experience key factors')),
    ) +
    p('Wind is the defining factor at the Open Championship. Players with strong ball-striking below the wind gain significant advantage. Check the weather forecast 48 hours before tee-off. Rory McIlroy, as an Irish fan favourite, generates substantial betting interest among Irish punters. His links record and Open pedigree make him a fixture in Irish betting slips. Historical Open courses include Royal Troon, St Andrews, Royal Liverpool (Hoylake), and Royal Portrush. 18+.')
)

# 8. Tour de France 2027
expansions['pages/tour-de-france-2027-betting-ireland.html'] = (
    h2('Tour de France 2027 Betting Markets') +
    tbl(
        trh(th('Market'), th('Description'), th('Notes')),
        trn(td('GC Winner'), td('Overall race winner after 21 stages'), td('Ante-post from January')),
        tra(td('Points Classification'), td('Green jersey winner'), td('Usually a sprinter specialist')),
        trn(td('King of the Mountains'), td('Polka dot jersey - best climber'), td('Often a breakaway specialist')),
        tra(td('Best Young Rider'), td('White jersey for under-25 riders'), td('Good each-way option')),
        trn(td('Stage Winner (most stages)'), td('Who wins the most individual stages'), td('Sprinters vs climbers differ')),
        tra(td('Daily Stage Winner'), td('Who wins each individual stage'), td('Sprint vs mountain stage profiles differ')),
    ) +
    p('Each-way terms of 1/4 odds, 4 places are standard for the Tour de France GC outright. Colombian, Slovenian, and Danish riders have dominated recent editions. The final Paris stage is traditionally ceremonial (no attacks by convention). Check the route announcement each October for the 2027 race to identify key mountain stages. 18+.')
)

# 9. Curragh Spring Cup
expansions['pages/curragh-spring-cup-2027-betting.html'] = (
    h2('Curragh Spring Cup 2027: Race Details') +
    tbl(
        trh(th('Detail'), th('Information')),
        trn(td('Venue'), td('The Curragh Racecourse, Co. Kildare')),
        tra(td('Distance'), td('1 mile (Group 3 flat race)')),
        trn(td('Surface'), td('Flat turf')),
        tra(td('Time of Year'), td('Spring - typically April')),
        trn(td('Field Size'), td('Usually 8-14 runners')),
        tra(td('Each-Way Places'), td('Typically 3 places (1/4 odds) for 8+ runners')),
    ) +
    p("The Curragh is Ireland's premier flat racing venue and home to all five Irish Classics. The Spring Cup is an early-season Group 3 indicator race, often used as a prep for the Irish 2000 Guineas in May. Horses from Aidan O'Brien's Ballydoyle stable are perennial market movers. Each-way value often exists at prices of 6/1 or bigger in a full field. 18+.")
)

# 10. Summer betting
expansions['pages/summer-betting-ireland.html'] = (
    h2('Summer Betting Calendar for Irish Punters') +
    tbl(
        trh(th('Month'), th('Key Events'), th('Irish Interest')),
        trn(td('June'), td('Irish Derby (Curragh), test cricket'), td('Irish Derby is the highlight')),
        tra(td('July'), td('Wimbledon final week, Tour de France, Open Championship'), td('Rory McIlroy in Open; tennis on RTE')),
        trn(td('August'), td('GAA All-Ireland semi-finals, Premier League pre-season'), td('GAA dominates Irish sports calendar')),
        tra(td('Late July/August'), td('Galway Races Festival'), td('Galway Plate and Hurdle attract massive Irish betting volume')),
    ) +
    p('The Galway Races Festival is the peak of the Irish betting summer. Key races: the Galway Plate (Wednesday, 2m1f handicap hurdle) and Galway Hurdle (Thursday, 2m flat handicap). Fields are large (20-30 runners). Each-way is essential at 1/5 odds, 5 places or 1/4 odds, 4 places. Willie Mullins, Gordon Elliott, and Jessica Harrington have strong Galway records. 18+.')
)

# Cheltenham races - reusable template
def chelt(race, distance, day, notes):
    return (
        h2(race + ': Key Facts') +
        tbl(
            trh(th('Detail'), th('Information')),
            trn(td('Race'), td(race)),
            tra(td('Festival Day'), td(day)),
            trn(td('Distance'), td(distance)),
            tra(td('Field Size'), td('Usually 10-20 runners')),
            trn(td('Each-Way Terms'), td('4 places at 1/4 odds for 8+ runners')),
        ) +
        h2('Ante-Post Betting Strategy') +
        p(notes + ' 18+. No pronostic is guaranteed.')
    )

expansions['pages/cheltenham-2027-ryanair-chase-betting.html'] = chelt(
    'Ryanair Chase', '2m5f (Grade 1)', 'Wednesday - Festival Wednesday',
    'The Ryanair Chase sits between the Champion Chase (2m) and Gold Cup (3m2f) - attracting bold front-runners and versatile chasers. Irish stables (Mullins, Elliott) dominate market movers. Ante-post markets open in autumn; early prices carry non-runner risk.'
)
expansions['pages/cheltenham-2027-mares-hurdle-betting.html'] = chelt(
    "Mares Hurdle", '2m1f (Grade 2)', 'Tuesday - Champion Day',
    'The Mares Hurdle is a Grade 2 for mares-only. Willie Mullins-trained mares have a dominant record. Market often features a short-priced favourite. Each-way at 5/1+ can offer value in a full field.'
)
expansions['pages/cheltenham-2027-county-hurdle-betting.html'] = chelt(
    'County Hurdle', '2m1f (Grade 3 handicap)', 'Friday - Gold Cup Day',
    'The County Hurdle is a large-field handicap - one of the hardest races to predict. Fields regularly exceed 24 runners. Each-way betting essential. Market movers on festival morning are worth tracking in this competitive handicap.'
)
expansions['pages/cheltenham-2027-stayers-hurdle-betting.html'] = chelt(
    'Stayers Hurdle', '3m1f (Grade 1)', "Thursday - St. Patrick's Thursday",
    'The Stayers Hurdle is for the best staying hurdlers over three miles. Stamina is paramount. The pace often starts slowly then frantic from 3 out - position in the final mile is critical.'
)
expansions['pages/cheltenham-2027-grand-annual-betting.html'] = chelt(
    'Grand Annual Chase', '2m (Grade 3 handicap)', 'Friday - Gold Cup Day',
    'The Grand Annual is a 2m handicap chase - the fastest race of the week. Low weights can win; course specialists with form at Cheltenham have strong records. Watch for Irish market movers late in the week.'
)
expansions['pages/cheltenham-2027-triumph-hurdle-betting.html'] = chelt(
    'Triumph Hurdle', '2m1f (Grade 1)', 'Friday - Gold Cup Day',
    'The Triumph Hurdle is exclusively for 4-year-olds. French-trained horses have a strong record. Spot unbeaten juveniles in January trials - they often start as market leaders by March.'
)
expansions['pages/cheltenham-2027-hunter-chase-betting.html'] = chelt(
    'Foxhunter Chase', '3m2f (amateur riders)', 'Friday - Gold Cup Day',
    'The Foxhunter Chase is ridden by amateur jockeys. Former point-to-point horses with strong hunter chase form are the target profile. Irish point-to-point graduates are well represented.'
)
expansions['pages/cheltenham-2027-gold-cup-day-betting.html'] = (
    h2('Cheltenham Gold Cup Day 2027: Race Schedule') +
    tbl(
        trh(th('Race'), th('Distance'), th('Type')),
        trn(td('JCB Triumph Hurdle'), td('2m1f'), td('Grade 1 - 4-year-olds')),
        tra(td('Albert Bartlett Novices Hurdle'), td('3m1f'), td('Grade 1 - staying novice hurdlers')),
        trn(td('Grand Annual Chase'), td('2m'), td('Grade 3 handicap')),
        tra(td('Foxhunter Chase'), td('3m2f'), td('Amateur riders')),
        trn(td('County Hurdle'), td('2m1f'), td('Grade 3 handicap - 24+ runners typical')),
        tra(td('Cheltenham Gold Cup'), td('3m2f'), td('Grade 1 - the festival showpiece')),
    ) +
    p('The Gold Cup is the pinnacle of National Hunt racing - a 3m2f Grade 1 chase. Typically attracts 15-20 runners. Irish trainers (Mullins, Elliott, de Bromhead) have dominated in recent years. Each-way with 4 places at 1/4 odds is standard. 18+.')
)
expansions['pages/cheltenham-2027-champion-day-betting.html'] = (
    h2('Cheltenham Champion Day 2027: Race Guide') +
    tbl(
        trh(th('Race'), th('Distance'), th('Type')),
        trn(td('Supreme Novices Hurdle'), td('2m half f'), td('Grade 1 - novice hurdlers')),
        tra(td('Arkle Novices Chase'), td('2m'), td('Grade 1 - novice chasers')),
        trn(td('Ultima Handicap Chase'), td('3m1f'), td('Grade 3 - large handicap')),
        tra(td('Champion Hurdle'), td('2m half f'), td('Grade 1 - best hurdlers')),
        trn(td('Mares Hurdle'), td('2m1f'), td('Grade 2 - mares only')),
        tra(td('Cheltenham Plate'), td('2m4 half f'), td('Grade 3 - handicap chase')),
    ) +
    p('The Champion Hurdle is the fastest-run Grade 1 of the week. Hurdlers who have shown brilliance in the Fighting Fifth Hurdle (November) or Christmas Hurdle tend to open as favourites. Horses aged 5-8 have the best record. Each-way value exists at 8/1+ in a 10-horse field. 18+.')
)
expansions['pages/cheltenham-2027-mares-novices-hurdle.html'] = chelt(
    "Mares Novices Hurdle", '2m half f (Grade 2)', 'Wednesday - Festival Wednesday',
    'The Mares Novices Hurdle is a Grade 2 for mares in their first or second season over hurdles. Willie Mullins dominates this race. If a leading Mullins mare is unbeaten in novice company, she typically starts at a short price.'
)
expansions['pages/cheltenham-2027-albert-bartlett-betting.html'] = chelt(
    'Albert Bartlett Novices Hurdle', '3m1f (Grade 1)', 'Friday - Gold Cup Day',
    'The Albert Bartlett is for staying novice hurdlers over 3 miles. Horses who have shown stamina in bumpers or early novice hurdles over 2m4f+ are the profile. The race often features big-price winners - each-way betting attractive. A double-figure winner is common.'
)
expansions['pages/cheltenham-2027-novices-hurdle-betting.html'] = chelt(
    'Supreme Novices Hurdle', '2m half f (Grade 1)', 'Tuesday - Champion Day (opening race)',
    'The Supreme Novices Hurdle is the first race of the Festival - a Grade 1 for novice hurdlers. Mullins and Elliott regularly dominate the market. Watch for heavily-backed Irish challengers in the week before.'
)

# GAA
expansions['pages/gaa-2027-munster-hurling-championship.html'] = (
    h2('Munster Hurling Championship 2027: Counties') +
    tbl(
        trh(th('County'), th('Recent Form'), th('Betting Note')),
        trn(td('Limerick'), td('Dominant 2020-2024'), td('Often short price; value elsewhere')),
        tra(td('Clare'), td('All-Ireland title 2024'), td('Tony Kelly leads scoring records')),
        trn(td('Cork'), td('Consistent Munster contender'), td('Tactical evolution underway')),
        tra(td('Tipperary'), td('Rebuilding post-2019 era'), td('Watch youth development')),
        trn(td('Waterford'), td('Dark horses in provincial round-robin'), td('Emerging talent worth monitoring')),
    ) +
    p('The Munster Championship runs May to late June in a round-robin format, with the top two progressing to the Munster Final. The round-robin means early-round results are not always do-or-die - this can suppress motivation and affect markets. For best value, focus on individual match markets rather than the outright championship winner. 18+.')
)

expansions['pages/gaa-2027-football-favourites-betting.html'] = (
    h2('All-Ireland Football Championship 2027: Outright Markets') +
    tbl(
        trh(th('County'), th('Provincial'), th('All-Ireland Wins (last 10 yrs)'), th('Outright Range')),
        trn(td('Dublin'), td('Leinster'), td('7 (2013-2023 dynasty)'), td('4/1 - 7/1')),
        tra(td('Kerry'), td('Munster'), td('3 (2014, 2022, 2023)'), td('3/1 - 6/1')),
        trn(td('Galway'), td('Connacht'), td('1 (2022)'), td('10/1 - 20/1')),
        tra(td('Mayo'), td('Connacht'), td('0 (5 final appearances since 2004)'), td('12/1 - 25/1')),
        trn(td('Derry'), td('Ulster'), td('1 (2023)'), td('16/1 - 30/1')),
        tra(td('Tyrone'), td('Ulster'), td('1 (2021)'), td('14/1 - 25/1')),
    ) +
    p('Kerry and Dublin are the two perennial powers - between them they have won 10 of the last 15 All-Irelands. For value, look at Ulster counties (Derry, Armagh, Tyrone, Donegal) who consistently reach semi-finals. The Super 8s format means a team can lose one match and still advance. 18+.')
)

expansions['pages/gaa-2027-hurling-favourites-betting.html'] = (
    h2('All-Ireland Hurling Championship 2027: Outright Markets') +
    tbl(
        trh(th('County'), th('Liam MacCarthy Wins (last 10 yrs)'), th('Outright Range')),
        trn(td('Limerick'), td('5 (2018, 2020, 2021, 2022, 2023)'), td('2/1 - 5/1')),
        tra(td('Kilkenny'), td('Multiple wins; consistently competitive'), td('4/1 - 8/1')),
        trn(td('Clare'), td('1 (2024)'), td('6/1 - 12/1')),
        tra(td('Cork'), td('0 (2 finals)'), td('10/1 - 18/1')),
        trn(td('Galway'), td('1 (2017)'), td('12/1 - 20/1')),
        tra(td('Tipperary'), td('1 (2019)'), td('14/1 - 25/1')),
    ) +
    p('For individual match betting, over 1.5 goals (3-pointer type) is usually priced around even money. Total points markets (over/under 45.5 total points) are increasingly popular. Home advantage in provincial games is significant - especially Munster semi-finals in Thurles. 18+.')
)

expansions['pages/leinster-championship-betting-ireland.html'] = (
    h2('Leinster GAA Championship 2027: Football and Hurling') +
    tbl(
        trh(th('Code'), th('Format'), th('Key Counties')),
        trn(td('Football'), td('Round-robin + provincial final'), td('Dublin, Meath, Kildare, Louth, Westmeath')),
        tra(td('Hurling'), td('Round-robin + provincial final'), td('Kilkenny, Galway, Wexford, Dublin, Laois')),
    ) +
    p("Dublin's footballers dominated Leinster for over a decade (13 consecutive titles 2011-2023). Their provincial price is frequently sub-1/4 (1.25) in outright markets. For betting value, Meath, Kildare, and Louth have all competed in Leinster finals. The Leinster hurling championship is more competitive - Kilkenny typically favoured, but Galway and Wexford regularly reach the final. Leinster finals at Croke Park (82,300 capacity) draw large crowds. 18+.")
)

# Payments
expansions['pages/how-long-do-withdrawals-take-ireland.html'] = (
    h2('Withdrawal Timeframes by Payment Method') +
    tbl(
        trh(th('Method'), th('Typical Time'), th('Notes')),
        trn(td('Debit Card (Visa/Mastercard)'), td('1-5 business days'), td('Bank processing adds 1-3 days after site approves')),
        tra(td('PayPal'), td('Within 24 hours'), td('Instant to PayPal wallet; then 1-3 days to bank')),
        trn(td('Skrill / Neteller'), td('Within 24 hours'), td('E-wallet to e-wallet is fast')),
        tra(td('Revolut'), td('1-2 business days'), td('Treated as a Mastercard')),
        trn(td('Bank Transfer'), td('3-7 business days'), td('Slowest; used for large withdrawals')),
        tra(td('Apple Pay / Google Pay'), td('1-3 business days'), td('Linked to debit card speed')),
    ) +
    p('Delays typically fall into three categories: (1) KYC verification - if your account is not fully verified, all withdrawals are held until checks pass; (2) Withdrawal limit queues - some platforms batch withdrawals daily; (3) Bank processing - the betting site approves the payment but your bank clearing adds 1-3 days. If your withdrawal has not arrived within 7 business days, contact customer support with your withdrawal reference number. GRAI-licensed operators must process verified withdrawals promptly. 18+.')
)

expansions['pages/best-casino-apple-pay-ireland.html'] = (
    h2('How to Deposit with Apple Pay at an Irish Casino') +
    tbl(
        trh(th('Step'), th('Action')),
        trn(td('1'), td('Go to the casino cashier / deposit section')),
        tra(td('2'), td('Select Apple Pay from payment options')),
        trn(td('3'), td('Enter deposit amount (minimum typically 10-20 euro)')),
        tra(td('4'), td('Authenticate with Face ID, Touch ID, or device passcode')),
        trn(td('5'), td('Funds credited to casino account instantly')),
    ) +
    h2('Apple Pay Casino Limits and Considerations') +
    tbl(
        trh(th('Factor'), th('Detail')),
        trn(td('Minimum Deposit'), td('Typically 10-20 euro')),
        tra(td('Maximum Deposit'), td('Usually 500-2500 euro per transaction; daily limits set by your bank')),
        trn(td('Withdrawal via Apple Pay'), td('Most sites cannot pay back via Apple Pay; use debit card or e-wallet')),
        tra(td('Credit Card Restriction'), td('Credit card betting banned in Ireland under GRAI rules - only debit cards work')),
        trn(td('Bonus Eligibility'), td('Usually qualifies for welcome bonus; check casino T&Cs')),
    )
)

expansions['pages/best-casino-revolut-ireland.html'] = (
    h2('Using Revolut at Irish Online Casinos') +
    tbl(
        trh(th('Feature'), th('Standard Revolut'), th('Premium/Metal')),
        trn(td('Works at most casinos'), td('Yes - Mastercard accepted'), td('Yes')),
        tra(td('Gambling category block'), td('Available (toggle in app)'), td('Available')),
        trn(td('Instant deposit'), td('Yes'), td('Yes')),
        tra(td('Withdrawal to Revolut'), td('1-2 business days'), td('1-2 business days')),
        trn(td('Spending analytics'), td('Shows gambling category'), td('More detailed breakdown')),
    ) +
    '<h2>How to Block Gambling on Revolut</h2><ol style="margin:12px 0;padding-left:20px"><li style="margin-bottom:8px">Open the Revolut app and go to <strong>Hub</strong> or <strong>Settings</strong></li><li style="margin-bottom:8px">Select <strong>Control my spending</strong> or <strong>Card controls</strong></li><li style="margin-bottom:8px">Toggle off <strong>Gambling</strong> or <strong>Betting</strong> merchant category</li><li style="margin-bottom:8px">Confirm the block - takes effect immediately</li></ol>' +
    p('Revolut adds a 24-hour delay when re-enabling gambling, as a cooling-off protection. Gambling Awareness Trust: 1800 753 753 (free). 18+.')
)

expansions['pages/best-casino-without-account-ireland.html'] = (
    h2('No-Account Casinos: Traditional vs Pay N Play') +
    tbl(
        trh(th('Step'), th('Traditional Casino'), th('No-Account Casino')),
        trn(td('Sign-up'), td('Form with email, address, DOB'), td('No form - bank login only')),
        tra(td('Verification'), td('Upload ID document'), td('Bank-based KYC via open banking')),
        trn(td('Deposit'), td('Choose payment, enter details'), td('Bank login then amount then instant')),
        tra(td('Withdraw'), td('Request then 1-5 days'), td('Instant to your bank account')),
        trn(td('Bonus'), td('Welcome offer on signup'), td('Usually no bonus (or reduced)')),
    ) +
    p('No-account casinos use Trustly open banking system for instant verification. Under GRAI regulations (from July 2026), all operators serving Irish players must hold a GRAI licence. Check the GRAI public register at grai.ie before depositing at any no-account casino. 18+. Gambling Awareness Trust: 1800 753 753.')
)

expansions['pages/best-casino-poker-ireland.html'] = (
    h2('Casino Hold\'em vs Texas Hold\'em') +
    tbl(
        trh(th('Factor'), th('Casino Hold\'em'), th('Texas Hold\'em')),
        trn(td('Played against'), td('The house (dealer)'), td('Other players')),
        tra(td('Skill element'), td('Low - basic strategy exists'), td('High - bluffing, pot odds')),
        trn(td('House edge'), td('Approximately 2-3% with optimal play'), td('Rake taken from pot')),
        tra(td('Minimum bet'), td('Usually 1-5 euro'), td('Varies by table stakes')),
        trn(td('Speed'), td('Fast - dealer-managed'), td('Slower - player decisions dominate')),
        tra(td('Live version'), td('Evolution Gaming live tables'), td('Live poker rooms or tournaments')),
    ) +
    p('Typical poker variants at Irish licensed casinos: Casino Hold\'em (player vs dealer), Three Card Poker (fastest), Caribbean Stud Poker (5-card, progressive jackpot), and Ultimate Texas Hold\'em (raise early or late). For serious poker players, most live casinos also offer tournaments and Sit & Go formats. 18+.')
)

expansions['pages/best-casino-new-ireland-2026.html'] = (
    h2('What to Check Before Joining a New Casino in Ireland') +
    tbl(
        trh(th('Check'), th('What to Look For'), th('Where to Verify')),
        trn(td('GRAI Licence'), td('Remote betting/gaming licence from July 2026'), td('grai.ie public register')),
        tra(td('Payment Methods'), td('Debit card, PayPal, Revolut, Paysafecard'), td('Casino cashier page')),
        trn(td('Bonus Terms'), td('Wagering 35x or under, 30-day expiry minimum'), td('Casino T&Cs')),
        tra(td('Mobile App'), td('iOS/Android native app or mobile site'), td('App Store / Google Play')),
        trn(td('Customer Support'), td('Live chat available, Irish support hours'), td('Support page test')),
        tra(td('RG Tools'), td('Deposit limits, session limits, self-exclusion'), td('Responsible gambling page')),
    ) +
    p('Under the Gambling Regulation Act 2024 and GRAI oversight from July 2026, inducements (bonuses) to Irish residents have new restrictions. Bonuses cannot be marketed to players who have set deposit limits or are in a cooling-off period. Focus on no-wagering cashback or low-wagering offers for genuine value. 18+.')
)

expansions['pages/best-casino-crash-games-ireland.html'] = (
    h2('Crash Game Mechanics Explained') +
    tbl(
        trh(th('Element'), th('How It Works')),
        trn(td('Multiplier'), td('Starts at 1x and rises - sometimes slowly, sometimes fast')),
        tra(td('Cash Out'), td('Player clicks to collect at any point before crash')),
        trn(td('Crash Point'), td('Random - determined by provably fair algorithm before round starts')),
        tra(td('Auto Cash Out'), td('Set a target multiplier (e.g. 2x) - game auto-collects')),
        trn(td('House Edge'), td('Typically 4-5% per round; multiple rounds per minute means fast losses')),
        tra(td('Variance'), td('Extreme - most rounds crash below 2x; rare 10x+ events')),
    ) +
    p('Crash games (Aviator, JetX, Spaceman) are classified as casino/gaming products. GRAI has not yet issued gaming licences - these are expected 2027/2028. Until then, crash games may only be offered by operators holding a valid licence from another EU/EEA jurisdiction. Always verify an operator licence at grai.ie. Set session time limits and loss limits before playing. 18+. Gambling Awareness Trust: 1800 753 753.')
)

# Wagering pages
expansions['pages/casino-wagering-requirement-explained.html'] = (
    h2('Wagering Requirement: Worked Examples') +
    tbl(
        trh(th('Bonus'), th('Wagering'), th('Total Bets Required'), th('Withdrawal Available After')),
        trn(td('50 euro bonus'), td('30x'), td('1500 euro'), td('Any remaining bonus + winnings')),
        tra(td('100 euro bonus'), td('35x'), td('3500 euro'), td('Any remaining bonus + winnings')),
        trn(td('20 euro free spins (SNR)'), td('40x on winnings only'), td('400 euro if you win 10 euro'), td('Real cash after turnover')),
        tra(td('200 euro deposit match'), td('20x deposit+bonus'), td('6000 euro'), td('After 6k wagered')),
        trn(td('10 euro no-deposit'), td('50x'), td('500 euro'), td('Usually capped at 100 euro max withdrawal')),
    ) +
    h2('How Game Contributions Affect Wagering') +
    tbl(
        trh(th('Game Type'), th('Typical Wagering Contribution')),
        trn(td('Slots (most)'), td('100%')),
        tra(td('Live Casino (Blackjack, Roulette)'), td('10% or 0%')),
        trn(td('Video Poker'), td('10-20%')),
        tra(td('Scratchcards'), td('50%')),
        trn(td('Sports Betting'), td('Varies; often 25-50%')),
    )
)

expansions['pages/what-is-wagering-requirement-ireland.html'] = (
    h2('Wagering Requirement vs No-Wagering: Comparison') +
    tbl(
        trh(th('Bonus Type'), th('Wagering'), th('Real Value on 100 euro Bonus')),
        trn(td('Standard 35x bonus'), td('35x = 3500 euro to wager'), td('Approximately 40-60 euro expected value with 2% slots loss')),
        tra(td('No-wagering cashback 20%'), td('None'), td('20 euro real cash on 100 euro losses')),
        trn(td('10x low-wager match'), td('10x = 1000 euro to wager'), td('Approximately 80 euro expected value')),
        tra(td('SNR free bet'), td('No wager - stake not returned'), td('Odds minus 1 divided by odds times bet')),
    ) +
    p('Simple formula: Bonus Value = Bonus Amount minus (Wagering Requirement times House Edge). For a 100 euro bonus at 35x wagering, with a 3% average house edge: 100 minus (3500 times 0.03) = minus 5 euro. This means you are statistically expected to lose more than the bonus gives you. Bonuses become positive-value when: wagering is 20x or under, house edge is 2% or under, or no wagering. 18+.')
)

expansions['pages/casino-self-exclusion-ireland.html'] = (
    h2('Casino Self-Exclusion Options in Ireland') +
    tbl(
        trh(th('Option'), th('Duration'), th('Coverage'), th('How to Apply')),
        trn(td('Site-level self-exclusion'), td('30 days to 5+ years'), td('That casino only'), td('Account settings then Responsible Gambling')),
        tra(td('GRAI Register (when available)'), td('TBC'), td('All GRAI-licensed operators'), td('grai.ie')),
        trn(td('Gambling Awareness Trust'), td('No time limit'), td('Support service'), td('gamblingcare.ie or 1800 753 753')),
        tra(td('Bank gambling block'), td('Reversible (24-hour delay on removal)'), td('All gambling transactions'), td('App settings (Revolut, AIB, BOI, etc.)')),
    ) +
    p('When you self-exclude from an Irish licensed casino, the operator must: immediately suspend your account, remove you from marketing lists, refund any remaining balance (minus active bonus), and not reactivate your account for the chosen period. Under the Gambling Regulation Act 2024, GRAI is building a national self-exclusion register. Free, confidential support: Gambling Awareness Trust, 1800 753 753, gamblingcare.ie. 18+.')
)

expansions['pages/casino-holdem-ireland.html'] = (
    h2('Casino Hold\'em: Optimal Strategy') +
    tbl(
        trh(th('Hand Strength'), th('Action'), th('Reason')),
        trn(td('Pair or better'), td('Call'), td('Strong equity vs dealer')),
        tra(td('Four to a flush'), td('Call'), td('Good draw')),
        trn(td('Open-ended straight draw (8+ outs)'), td('Call'), td('Approximately 32% to hit')),
        tra(td('Any pair on board (match)'), td('Call'), td('Use community cards')),
        trn(td('Two overcards (A-K or A-Q)'), td('Call'), td('Good top-pair potential')),
        tra(td('Weak hand, no draws'), td('Fold'), td('Save ante bet loss beyond this')),
    ) +
    p('Casino Hold\'em pays 1:1 on the Call bet when you beat the dealer. The dealer must have at least a pair of 4s to qualify. The base house edge with optimal strategy is approximately 2.16%. The optional AA+ side bet has a house edge of around 6.4% - not recommended for value-conscious players. 18+.')
)

expansions['pages/cash-out-explained.html'] = (
    h2('Cash Out: How the Price Is Calculated') +
    tbl(
        trh(th('Factor'), th('Effect on Cash Out Price')),
        trn(td('Current probability of your selection winning'), td('Higher probability = higher cash out')),
        tra(td('Bookmaker margin applied twice'), td('You pay margin when placing and when cashing out')),
        trn(td('Time remaining in event'), td('More time = more uncertainty = lower cash out ratio')),
        tra(td('Number of legs remaining (accas)'), td('More legs = lower cash out per original stake')),
        trn(td('Live score/game state'), td('Goal scored for you = cash out rises; against = drops')),
    ) +
    p('Partial cash out lets you sell part of your bet and let the rest run. Example: 20 euro acca with 3 legs remaining, cash out available at 60 euro. Partial cash out at 50% = collect 30 euro now, let 30 euro ride. This locks in profit while keeping upside. Avoid partial cash out simply due to nerves - the mathematical cost of repeated cash outs compounds quickly. 18+.')
)

expansions['pages/how-do-welcome-bonuses-work-ireland.html'] = (
    h2('Welcome Bonus Types at Irish Betting Sites') +
    tbl(
        trh(th('Bonus Type'), th('How It Works'), th('Common At')),
        trn(td('Deposit Match'), td('Casino matches first deposit up to a cap (e.g. 100% up to 200 euro)'), td('Online casinos')),
        tra(td('Free Bet (SNR)'), td('Bet returned as free bet token (stake not returned on win)'), td('Sports betting')),
        trn(td('No-Deposit Bonus'), td('Small credit given on registration, no deposit needed'), td('Casino - rare in Ireland now')),
        tra(td('Free Spins'), td('Set number of spins on specified slot games'), td('Casino slot promotions')),
        trn(td('Bet and Get'), td('Place qualifying bet then receive free bet or bonus credit'), td('Sports betting')),
        tra(td('Cashback Bonus'), td('Percentage of losses returned as bonus or real cash'), td('Casino and sports')),
    ) +
    p('Before claiming any welcome bonus, check: (1) Wagering requirement - 30-40x is industry average; under 20x is good value; (2) Time limit - most bonuses expire in 7-30 days; (3) Game restrictions - table games often count at 10% or 0% toward wagering; (4) Max bet rule - most bonuses restrict bets to 5-10 euro per spin while wagering is active; (5) Withdrawal cap - no-deposit bonuses often cap winnings at 100-200 euro. Under GRAI regulations, Irish operators must display all bonus terms clearly before you opt in. 18+.')
)

expansions['pages/what-is-an-accumulator-ireland.html'] = (
    h2('Accumulator Types: Legs Required and Example Odds') +
    tbl(
        trh(th('Bet Type'), th('Legs'), th('Example Combined Odds')),
        trn(td('Double'), td('2'), td('2/1 x 2/1 = 8/1')),
        tra(td('Treble'), td('3'), td('2/1 x 2/1 x 2/1 = 26/1')),
        trn(td('4-fold Accumulator'), td('4'), td('2/1 x 2/1 x 2/1 x 2/1 = 80/1')),
        tra(td('5-fold Accumulator'), td('5'), td('5 selections at 2/1 each = 242/1')),
        trn(td('Yankee'), td('4 (11 bets)'), td('Covers all doubles, trebles, 4-fold')),
        tra(td('Lucky 15'), td('4 (15 bets)'), td('All doubles, trebles, 4-fold plus all 4 singles')),
    ) +
    p('Each leg of an accumulator multiplies both the potential winnings and the bookmaker margin. With a 5% margin per leg, a 5-leg acca has an effective combined margin of approximately 23% - meaning the expected return is 77p in every 1 euro staked. Reduce legs to 3-4 maximum for best value. 18+.')
)

expansions['pages/how-to-complain-to-grai.html'] = (
    h2('How to File a Complaint with GRAI') +
    tbl(
        trh(th('Step'), th('Action')),
        trn(td('1'), td('Complain to the operator first (required before escalating to GRAI)')),
        tra(td('2'), td('Allow 8 weeks for the operator to respond')),
        trn(td('3'), td('If unresolved, file with GRAI at grai.ie in the Complaints section')),
        tra(td('4'), td('Provide: account details, complaint summary, evidence (screenshots), operator response')),
        trn(td('5'), td('GRAI acknowledges within 5 working days')),
        tra(td('6'), td('Resolution timeline varies (weeks to months depending on complexity)')),
    ) +
    p('GRAI can investigate: failure to pay out from a licensed operator, breach of GRAI licence conditions, misleading advertising, failure to implement self-exclusion. GRAI cannot: compel an unlicensed offshore site to pay you, resolve individual bet settlements (unless systemic). For urgent help, contact Gambling Awareness Trust (1800 753 753). 18+.')
)

expansions['pages/crypto-betting-without-verification-ireland.html'] = (
    h2('Crypto Betting Without Verification: What This Actually Means') +
    tbl(
        trh(th('Claim'), th('Reality for Irish Players')),
        trn(td('No KYC betting site'), td('Site may still require ID at withdrawal or above certain thresholds')),
        tra(td('Anonymous crypto betting'), td('Blockchain transactions are pseudonymous, not anonymous - traceable')),
        trn(td('No licence required'), td('False - GRAI requires a licence to serve Irish residents')),
        tra(td('Instant withdrawal'), td('Crypto withdrawals can be fast but blockchain confirmation takes minutes')),
        trn(td('Tax-free'), td('False - Irish Revenue may treat crypto gambling winnings as taxable income')),
    ) +
    p('Sites advertising no verification or anonymous crypto betting often operate without an Irish licence. Under the Gambling Regulation Act 2024, any operator serving Irish residents must hold a GRAI licence (from July 2026 onwards). Using an unlicensed site means: no protection if the site refuses to pay, no recourse via GRAI. Before depositing, verify the licence at grai.ie. 18+.')
)

expansions['pages/bonus-abuse-ireland.html'] = (
    h2('What Counts as Bonus Abuse at Irish Casinos') +
    tbl(
        trh(th('Activity'), th('Classified As'), th('Risk')),
        trn(td('Claiming same bonus via multiple accounts'), td('Bonus abuse - terms violation'), td('Account closure, bonus voided')),
        tra(td('Matched betting (using free bets to cover all outcomes)'), td('Technically permitted but frowned on'), td('Account may be gubbed')),
        trn(td('Playing low-edge games to clear wagering faster'), td('Usually permitted - check T&Cs'), td('Some bonuses exclude blackjack for this reason')),
        tra(td('Depositing to claim bonus then immediately withdrawing'), td('Flagged if pattern repeated'), td('Restricted from future bonuses')),
        trn(td('Creating family member accounts to claim same offer'), td('Bonus abuse'), td('All related accounts closed')),
    ) +
    p('Irish casinos have automated systems that flag unusual patterns. Legitimate bonus play means: claiming offers as intended (one per household/IP address), playing the stipulated wagering on games permitted by the T&Cs. Bonus abuse risks account closure and forfeiture of all funds - including genuine deposits in some cases. 18+. Gambling Awareness Trust: 1800 753 753.')
)

expansions['pages/high-roller-casino-ireland.html'] = (
    h2('High Roller Table Limits at Irish Online Casinos') +
    tbl(
        trh(th('Game'), th('Standard Table'), th('VIP High-Roller Table')),
        trn(td('Live Blackjack'), td('0.50 - 500 euro'), td('200 - 25000+ euro')),
        tra(td('Live Roulette'), td('0.20 - 1000 euro'), td('100 - 20000+ euro')),
        trn(td('Live Baccarat'), td('1 - 1000 euro'), td('100 - 50000 euro')),
        tra(td('Slots (max bet per spin)'), td('Usually 5 - 50 euro'), td('Some slots cap at 100-500 euro per spin')),
        trn(td('Live Poker'), td('5 - 500 euro'), td('200 - 10000 euro')),
    ) +
    p('High-roller accounts typically offer: dedicated account manager, faster withdrawal processing (some same-day), personalised limits, exclusive tournaments, and cashback on losses (5-15% for elite tiers). Important: GRAI-licensed operators must assess player affordability under the Gambling Regulation Act 2024. High-volume players may be asked to provide proof of income or source of funds - this is a regulatory requirement, not optional. 18+.')
)

expansions['pages/all-ireland-final-weekend-betting.html'] = (
    h2('All-Ireland Final Weekend: Schedule and Markets') +
    tbl(
        trh(th('Event'), th('Typical Date'), th('Venue'), th('Key Markets')),
        trn(td('All-Ireland Hurling Final'), td('Second Sunday in July'), td('Croke Park, Dublin'), td('Outright, HT/FT, first scorer, winning margin')),
        tra(td('All-Ireland Football Final'), td('Fourth Sunday in July'), td('Croke Park, Dublin'), td('Outright, most scores, winning margin, top scorer')),
        trn(td('Camogie All-Ireland Final'), td('Mid-July'), td('Croke Park'), td('Limited market availability')),
    ) +
    p('All-Ireland Finals are played at Croke Park - 82,300 capacity, the third-largest stadium in Europe. The neutral venue means no traditional home advantage. The winning margin market is popular - over 7 points is quite common in hurling finals; football finals are typically tighter. 18+.')
)

expansions['pages/grand-national-week-betting.html'] = (
    h2('Aintree Grand National Festival: Day-by-Day Guide') +
    tbl(
        trh(th('Day'), th('Key Race'), th('Distance'), th('Betting Highlight')),
        trn(td('Thursday - Day 1'), td('Manifesto Novices Chase'), td('2m4f Grade 1'), td('Premier novice chase')),
        tra(td('Friday - Ladies Day'), td('Aintree Hurdle'), td('2m4f Grade 1'), td('Quality hurdlers')),
        trn(td('Friday'), td('Mildmay Novices Chase'), td('3m1f Grade 1'), td('Stayers novice form')),
        tra(td('Saturday - Grand National Day'), td('Grand National'), td('4m2f handicap'), td('Most famous horse race in the world')),
    ) +
    p('The Grand National is a 4m2f handicap over 30 fences at Aintree. With fields of 40 runners, it is statistically the hardest race to win in UK/Irish racing. Each-way is essential - bookmakers offer 1/5 odds, 5-8 places on the National. Each-way value often exists at prices of 20/1-40/1 for well-handicapped runners with strong Cheltenham form. Irish trainers (Willie Mullins, Gordon Elliott) have excellent modern records. 18+. No pronostic is guaranteed.')
)

expansions['pages/new-years-day-betting-ireland.html'] = (
    h2("New Year's Day Racing in Ireland") +
    tbl(
        trh(th('Venue'), th('Type'), th('Note')),
        trn(td('Tramore Racecourse, Co. Waterford'), td('National Hunt'), td('Traditional holiday meeting')),
        tra(td('Punchestown Racecourse, Co. Kildare'), td('National Hunt'), td('Grade B hurdle and chase cards')),
        trn(td('UK - Cheltenham'), td('NH (new year fixture)'), td('Trials ahead of Festival')),
        tra(td('ITV Racing / RTE'), td('TV coverage'), td('Bank holiday racing broadcast in Ireland')),
    ) +
    p("New Year's Day is a bank holiday in Ireland - multiple race meetings run, and betting shops are open. Tramore is the most traditionally Irish New Year's fixture, often featuring local runners. The ground in January is typically soft-to-heavy in Ireland, heavily favouring stamina-based horses with proven soft-ground form. 18+.")
)

expansions['pages/easter-monday-betting-ireland.html'] = (
    h2('Easter Monday Racing and Betting in Ireland') +
    tbl(
        trh(th('Venue'), th('Meeting Type'), th('Note')),
        trn(td('Fairyhouse Racecourse'), td('Irish Grand National (Easter Monday)'), td("Ireland's most famous spring handicap chase")),
        tra(td('Leopardstown'), td('Spring flat card'), td('Transition from jumps to flat season')),
        trn(td('UK - Kempton'), td('Bank holiday flat card'), td('Watched widely by Irish bettors via ITV')),
        tra(td('UK - Lingfield'), td('All-weather'), td('Additional betting opportunities')),
    ) +
    p("The Irish Grand National takes place on Easter Monday at Fairyhouse, Co. Meath - a Grade A handicap chase over 3m5f. Fields of 20-30 runners. Each-way with 4-5 places is essential. Irish trainers (Willie Mullins, Gordon Elliott, Jessica Harrington) regularly target this race. Ground in April varies between good-to-yielding and yielding-to-soft. High-weight horses rarely win. 18+. Gambling Awareness Trust: 1800 753 753.")
)

expansions['pages/world-cup-2026-host-nations-betting.html'] = (
    h2('FIFA World Cup 2026: Host Nations Overview') +
    tbl(
        trh(th('Country'), th('Host Cities'), th('Group Stage Note')),
        trn(td('United States'), td('16 cities including New York, LA, Dallas, Miami'), td('Largest hosts; big stadiums')),
        tra(td('Canada'), td('Toronto, Vancouver'), td('Less traditional football country; novelty factor')),
        trn(td('Mexico'), td('Mexico City, Guadalajara, Monterrey'), td('Azteca Stadium - huge home crowd pressure')),
    ) +
    p('Host nations have won the World Cup 6 times (Uruguay 1930, Italy 1934, England 1966, West Germany 1974, Argentina 1978, France 1998). In recent tournaments, hosts have underperformed their opening odds. The United States has the strongest squad of the three 2026 hosts and may have genuine knockout potential. For outright betting, focus on European powers and Brazil/Argentina. 18+. No pronostic is guaranteed.')
)

expansions['pages/world-cup-2026-group-stage-betting.html'] = (
    h2('World Cup 2026 Group Stage Format') +
    tbl(
        trh(th('Detail'), th('Information')),
        trn(td('Teams'), td('48 teams (expanded from 32 in 2022)')),
        tra(td('Groups'), td('12 groups of 4 teams')),
        trn(td('Qualification'), td('Top 2 from each group plus 8 best third-placed teams = 32 advance')),
        tra(td('Total Group Matches'), td('72 group-stage matches')),
        trn(td('Host Cities'), td('USA (16), Mexico (3), Canada (2)')),
        tra(td('Kick-off Times (Irish)'), td('Evening games typically 3pm, 6pm, or 9pm IST')),
    ) +
    p('For betting, consider: (1) Group winner - the top seed usually wins their group, but not always; (2) To qualify (top 2) - a safer bet than outright group winner; (3) Total group goals - groups featuring high-scoring favourites against weaker opponents offer over-goal value. The 8 best third-placed teams also advance in 2026 - a team can lose 2 games and still reach the round of 32. 18+.')
)

# Apply all expansions
results = []
for filepath, new_html in expansions.items():
    if not os.path.exists(filepath):
        results.append('SKIP: ' + filepath)
        continue
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    orig_size = len(content)
    new_content = insert(content, new_html)
    if len(new_content) == orig_size:
        results.append('WARN: ' + filepath)
        continue
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    results.append('OK: ' + filepath + ' (' + str(orig_size) + '->' + str(len(new_content)) + ')')

for r in results:
    print(r)
print('Done: ' + str(sum(1 for r in results if r.startswith('OK'))) + ' expanded')
