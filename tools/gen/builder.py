import re, json

shell = open('pages/credit-card-casino-ban-ireland.html', encoding='utf-8').read()

def build(slug, title, desc, keywords, crumb, h1, mins, content, faqs, related):
    s = shell
    s = re.sub(r'<title>.*?</title>', '<title>%s</title>' % title, s, 1, re.S)
    s = re.sub(r'<meta name="description" content="[^"]*">', '<meta name="description" content="%s">' % desc, s, 1)
    s = re.sub(r'<meta name="keywords" content="[^"]*">', '<meta name="keywords" content="%s">' % keywords, s, 1)
    url = 'https://craicbet.com/pages/' + slug
    s = re.sub(r'<link rel="alternate" hreflang="en-IE" href="[^"]*">', '<link rel="alternate" hreflang="en-IE" href="%s">' % url, s, 1)
    s = re.sub(r'<link rel="alternate" hreflang="x-default" href="[^"]*">', '<link rel="alternate" hreflang="x-default" href="%s">' % url, s, 1)
    s = re.sub(r'<link rel="canonical" href="[^"]*">', '<link rel="canonical" href="%s">' % url, s, 1)
    s = re.sub(r'<meta property="og:title" content="[^"]*">', '<meta property="og:title" content="%s">' % title, s, 1)
    s = re.sub(r'<meta property="og:description" content="[^"]*">', '<meta property="og:description" content="%s">' % desc, s, 1)
    s = re.sub(r'<meta property="og:url" content="[^"]*">', '<meta property="og:url" content="%s">' % url, s, 1)
    s = re.sub(r'<meta name="twitter:title" content="[^"]*">', '<meta name="twitter:title" content="%s">' % title, s, 1)
    s = re.sub(r'<meta name="twitter:description" content="[^"]*">', '<meta name="twitter:description" content="%s">' % desc, s, 1)
    faqld = {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
        {"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a,_ in faqs]}
    s = s.replace('</head>', '<script type="application/ld+json">\n%s\n</script>\n</head>' % json.dumps(faqld, ensure_ascii=False, indent=1), 1)
    s = re.sub(r'(&rsaquo; <a href="guides">Guides</a> &rsaquo; )[^\n<]*', r'\g<1>' + crumb, s, 1)
    s = re.sub(r'<h1>.*?</h1>', '<h1>%s</h1>' % h1, s, 1, re.S)
    s = s.replace('&#9201; 6 min read', '&#9201; %d min read' % mins, 1)
    s = s.replace('Updated October 2026', 'Updated November 2026', 1)
    s = s.replace('Updated 31 October 2026', 'Updated 1 November 2026', 1)
    start = s.index('<div class="article-content">') + len('<div class="article-content">')
    end = s.index('</div>\n\n<div class="editorial-box"')
    faq_html = '\n<h2>Frequently Asked Questions</h2>\n' + '\n'.join(
        '<div class="faq-item"><div class="faq-question">%s</div><div class="faq-answer"><p>%s</p></div></div>' % (q, ah) for q,_,ah in faqs)
    s = s[:start] + '\n' + content + faq_html + '\n  ' + s[end:]
    s = re.sub(r'<div style="margin:24px 0;padding:14px 18px;background:#eef6f0;border-radius:8px"><strong>Related:</strong>.*?</div>',
               '<div style="margin:24px 0;padding:14px 18px;background:#eef6f0;border-radius:8px"><strong>Related:</strong> %s</div>' % related, s, 1, re.S)
    open('pages/%s.html' % slug, 'w', encoding='utf-8').write(s)
    print('built', slug)

RB = '<a href="grai-guide">GRAI guide hub</a> &middot; <a href="grai-licence-register-tracker">Live licence register tracker</a> &middot; <a href="grai-online-casino-licences">Casino licence timeline</a>'
