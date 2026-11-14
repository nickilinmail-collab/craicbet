# CraicBet — craicbet.com

Static English/Irish/Polish site (betting & casino guide for Ireland), plain HTML on GitHub Pages.
Funnel: two partner links, both rel="nofollow" target="_blank". Never invent a third.
- GRAI-licensed partner bookmaker (licence GRAI-0191-RB-26-0001) — https://plusfind.info/go/2e7c17f7eb1e426bd9fae5242aaa9b3e365b64d1eb0a0b0b/
  The default for every CTA, and the only one used as the primary button.
- Non-GRAI provider — https://gameslnk.cc/go/2e7c17f7e91e426ba3e5e5242aaa9b3e365b64d1eb0a0b0b/
  Secondary button, currently on 1782 pages. Its own label must say the operator is not GRAI-licensed
  (current wording: "Explore Non-GRAI Provider"); never presented as licensed or regulated in Ireland.
  One per card, never twice in the same card.
  Open question (13 Nov 2026): it also sits on 683 betting pages, including
  grai-licensed-betting-sites-ireland, where a non-GRAI operator sits beside licensed ones.
  Owner to decide whether it belongs there; until then leave existing placements alone.

## Strategy (as of 1 Nov 2026) — BETTING FIRST
The site started casino-first; the priority is now BETTING + GRAI, because the partner operator's only Irish licence is a GRAI
remote betting licence. In every choice (new content, ordering, nav, homepage, internal links, indexing lists, social posts):
betting and GRAI topics come first, casino second. Casino content stays maintained (it carries current search demand) but new
investment goes to betting. Positioning phrase: "Ireland's independent betting & casino guide" (betting named first). Trust asset:
the operator's licence number GRAI-0191-RB-26-0001 — cite it; never claim any GRAI casino licence exists (zero issued, expected 2027–2028).

## Editorial rules (MUST follow)
- NEVER use operator brand names in URLs, <title>, H1/H2, meta description, keywords or schema. This covers the partner brand
  (TonyBet) AND all GRAI-licensed brands (bet365, Paddy Power, Betfair, Betdaq, 888, William Hill, Tote, Fitzdares, DragonBet,
  Kwiff, Dabble, 32Red, Unibet, NetBet, etc.). A factual sentence inside body text may name a brand; headings/keys may not.
  Scope, settled 14 Nov 2026: this covers BOOKMAKER brands only. Casino brands, slot titles and software
  providers are NOT covered — pages/brands/ (120 pages), pages/slots/ (468) and pages/providers/ (10) may
  carry those names in their URLs and headings, and do. They rank well on the long tail (DublinBet 8.9,
  Slotanza 4.0, Golden Star 1.0 in mid-November) and are left alone. "Tote betting" in a heading means
  pool betting, the bet type, and is not the brand The Tote: the three pages using it that way are correct.
- NEVER claim any casino holds a GRAI licence: GRAI issues remote BETTING licences only (since 1 July 2026). Casino (gaming)
  licences are expected 2027–2028 — zero issued. Our operator holds betting licence GRAI-0191-RB-26-0001 (16 Sep 2026–15 Sep 2029).
- No fake reviews, no invented RTP/stats/odds, no "guaranteed wins", no fabricated facts. Unverified figures are "reported".
- Always 18+ and responsible gambling line (Gambling Awareness Trust, 1800 753 753, gamblingcare.ie). Keep existing RG blocks.
- Honest maths is the house style: margins, stakes-not-returned, wagering costs — explained, not hidden.
- Clean URLs: all internal links WITHOUT .html (GitHub Pages serves them). Canonicals/sitemap use clean URLs.
- No cloaking, no geo-variant content.

## Structure
- `pages/*.html` — EN pages; `ga/`, `pl/` — Irish/Polish; `pages/slots/` — slot pages; `pages/news/` — weekly digests.
- `tools/gen/builder.py` — page generator (reads pages/credit-card-casino-ban-ireland.html as shell). See tools/gen/README.md.
- `sitemap.xml` — append every new page (clean URL, lastmod).
- Scheduled tasks live on this repo: daily GRAI tracker update, daily indexing list, weekly news roundup, betting conveyor, daily sports engine.

## Outreach to journalists (MUST follow)
- NEVER send email. Not once, not "obviously approved", not when the owner has asked for letters earlier
  in the conversation. Prepare the text, or a Gmail draft, and stop. The owner sends. A standing request
  like "send 10 letters" is a request to WRITE 10 letters.
- Mail goes from mark@craicbet.com ("Mark Craic"), a send-as alias on the nickilinmail@gmail.com account.
  The Gmail tool has no "from" field — it uses whatever Gmail has as default send-as. Verify before relying on it.
- NO links in the body, and no mention of the domain in the body either (mail clients auto-link a bare
  domain, so it reads as a link request and the pitch dies). Disclose the commercial interest in words
  without the address: "I edit a trade guide that earns affiliate commission". Domain belongs in the
  signature only. Offer data as an attached CSV, never as a page to visit.
- A link is what a journalist adds when the story is worth it. Asking for one in a first email shows
  why you wrote and devalues everything else in the letter.
- Give the journalist a question for the regulator, not a conclusion. State the innocent explanation too
  — a pitch with no caveat reads as PR.
- Check Gmail's sent mail before writing: someone may already have been contacted. A second cold email
  the same day burns the contact. Follow up in the existing thread instead.

## Checks before any push
- Internal links resolve to existing files; JSON-LD parses; no brand names in titles/headings (grep); page renders (header/footer intact).
- Commit messages end with the attribution lines given in system reminders.
