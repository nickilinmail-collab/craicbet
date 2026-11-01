# Page generator (tools/gen)

`builder.py` exposes `build(slug, title, desc, keywords, crumb, h1, mins, content, faqs, related)`:
writes `pages/<slug>.html` using `pages/credit-card-casino-ban-ireland.html` as the shell
(header/nav/footer/scripts preserved), sets canonical/OG/hreflang to the clean URL, injects a
FAQPage JSON-LD built from `faqs` = [(question, plain_answer_for_schema, html_answer), ...],
replaces the Related block with `related` (HTML links), and sets the byline/dates.
Run from repo root: `PYTHONPATH=tools/gen python3 - <<'PY' ... from builder import build ... PY`

Content conventions for conveyor pages (see CLAUDE.md rules first):
- 5–7 `<h2>` sections, 450–700 words, honest-maths angle from the worklist `brief`.
- One CTA block mid-page:
  `<div style="text-align:center;margin:28px 0"><a href="https://plusfind.info/go/2e7c17f7eb1e426bd9fae5242aaa9b3e365b64d1eb0a0b0b/" rel="nofollow" target="_blank" class="btn btn-primary" style="width:auto;padding:14px 40px;">Visit the Irish-Licensed Bookmaker &#8594;</a></div>`
- `related` links into the betting cluster: betting-sites-ireland, free-bets-ireland, football-betting-ireland, each-way-calculator (+ topical).
- In the nav, mark the Betting item active: replace `<a href="betting-sites-ireland">Betting</a>` with `<a href="betting-sites-ireland" class="active">Betting</a>` on every betting page you build.
- 3 FAQs per page. Irish angle wherever real (competitions, broadcasters, habits). 18+/RG line in the closing section where the topic warrants.
- After building a batch: verify internal links resolve, JSON-LD parses, grep page for banned brand names (CLAUDE.md list),
  append entries to sitemap.xml (clean URLs, today lastmod), add the new links to the "Betting" related block on pages/betting-sites-ireland.html
  (keep it one div), update each item's status to "done" in worklist.json, commit, push.

## Phase 2: translations (worklist_i18n.json)
When worklist.json has no "todo" left, the conveyor switches to worklist_i18n.json: each item = translate pages/<en_slug>.html
into Irish (lang "ga", use gabuilder.py, shell ga/cain-cearrbhachais.html) or Polish (lang "pl", use plbuilder.py, shell
pl/podatek-od-hazardu.html). Translate meaning, not word-for-word: natural native phrasing, Irish-language betting/gambling
terminology (gealltóireacht, cearrbhachas, ceadúnas), Polish diaspora angle where relevant. Slug: localized, lowercase, no accents
in filename. Keep all facts, numbers and the CTA (localize button label). Set reciprocal hreflang across the en/ga/pl trio
(all existing versions + new one; update the EN page's hreflang too). Internal links point to same-language pages where they
exist, otherwise ../pages/<en_slug>. Sitemap append. Then flip status to "done" with the chosen slug saved as "slug".
