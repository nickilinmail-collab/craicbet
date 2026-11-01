import re, json

shell = open('pl/podatek-od-hazardu.html', encoding='utf-8').read()

def build_pl(slug, title, desc, keywords, crumb, label, h1, mins, content, faqs, related):
    s = shell
    s = re.sub(r'<title>.*?</title>', '<title>%s</title>' % title, s, 1, re.S)
    s = re.sub(r'<meta name="description" content="[^"]*">', '<meta name="description" content="%s">' % desc, s, 1)
    s = re.sub(r'<meta name="keywords" content="[^"]*">', '<meta name="keywords" content="%s">' % keywords, s, 1)
    url = 'https://craicbet.com/pl/' + slug
    s = re.sub(r'<link rel="canonical" href="[^"]*">', '<link rel="canonical" href="%s">' % url, s, 1)
    s = re.sub(r'\s*<link rel="alternate" hreflang="[^"]*" href="[^"]*">', '', s)
    for pat, val in [('og:title', title), ('og:description', desc), ('og:url', url), ('twitter:title', title), ('twitter:description', desc)]:
        s = re.sub(r'(<meta (?:property|name)="%s" content=")[^"]*(")' % pat, lambda m: m.group(1) + val + m.group(2), s, 1)
    faqld = {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
        {"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a,_ in faqs]}
    s = s.replace('</head>', '<script type="application/ld+json">%s</script>\n</head>' % json.dumps(faqld, ensure_ascii=False), 1)
    s = re.sub(r'(&rsaquo; <a href="poradniki">Poradniki</a> &rsaquo; )[^\n<]*', r'\g<1>' + crumb, s, 1)
    s = re.sub(r'<span class="section-label">[^<]*</span>', '<span class="section-label">%s</span>' % label, s, 1)
    s = re.sub(r'<h1>.*?</h1>', '<h1>%s</h1>' % h1, s, 1, re.S)
    s = re.sub(r'&#9201; \d+ min czytania', '&#9201; %d min czytania' % mins, s, 1)
    s = s.replace('Aktualizacja Październik 2026', 'Aktualizacja Listopad 2026')
    start = s.index('<div class="article-content">') + len('<div class="article-content">')
    end = s.index('</article>')
    # find last </div> closing article-content before </article>
    body_close = s.rindex('</div>', start, end)
    faq_html = '\n<h2>Najczęstsze pytania</h2>\n' + '\n'.join(
        '<div class="faq-item"><div class="faq-question">%s<span>&#9662;</span></div><div class="faq-answer"><p>%s</p></div></div>' % (q, ah) for q,_,ah in faqs)
    rel = '\n<div style="margin:24px 0;padding:14px 18px;background:#eef6f0;border-radius:8px"><strong>Zobacz też:</strong> %s</div>\n' % related
    s = s[:start] + '\n' + content + faq_html + rel + '\n' + s[body_close:]
    open('pl/%s.html' % slug, 'w', encoding='utf-8').write(s)
    print('built pl/' + slug)
