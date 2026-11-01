# CraicBet — craicbet.com

Static English/Irish/Polish site (betting & casino guide for Ireland), plain HTML on GitHub Pages.
Funnel: every CTA button links to https://plusfind.info/go/2e7c17f7eb1e426bd9fae5242aaa9b3e365b64d1eb0a0b0b/ (rel="nofollow", target="_blank").

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

## Checks before any push
- Internal links resolve to existing files; JSON-LD parses; no brand names in titles/headings (grep); page renders (header/footer intact).
- Commit messages end with the attribution lines given in system reminders.
