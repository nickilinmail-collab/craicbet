<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
  xmlns:atom="http://www.w3.org/2005/Atom">
<xsl:output method="html" encoding="UTF-8" indent="yes"/>

<xsl:template match="/rss">
<html lang="en">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  <title><xsl:value-of select="channel/title"/></title>
  <meta name="robots" content="noindex, follow"/>
  <style>
    :root{--green:#152b1e;--green2:#1e3d2a;--orange:#F26522;--body:#1f2937;--muted:#6a7a70;--line:#e3e8e4}
    *{box-sizing:border-box}
    body{margin:0;background:#f6f8f6;color:var(--body);
         font:16px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
    .wrap{max-width:760px;margin:0 auto;padding:0 20px 64px}
    header{background:var(--green);color:#fff;padding:36px 0 30px;margin-bottom:28px}
    header .wrap{padding-bottom:0}
    .brand{font-size:15px;letter-spacing:.14em;text-transform:uppercase;color:#8abba0;margin:0 0 10px}
    .brand b{color:#fff}.brand i{color:var(--orange);font-style:normal}
    h1{margin:0 0 10px;font-size:30px;line-height:1.2}
    .sub{margin:0;color:#b8d4c3;font-size:15px}
    .note{background:#fff;border:1px solid var(--line);border-left:4px solid var(--orange);
          border-radius:8px;padding:16px 18px;margin:0 0 26px;font-size:14.5px}
    .note b{display:block;margin-bottom:4px}
    .note code{background:#f2f5f2;padding:2px 6px;border-radius:4px;font-size:13px;word-break:break-all}
    .meta{color:var(--muted);font-size:13.5px;margin:0 0 22px}
    article{background:#fff;border:1px solid var(--line);border-radius:10px;
            padding:20px 22px;margin:0 0 14px}
    article h2{margin:0 0 6px;font-size:18px;line-height:1.35}
    article h2 a{color:var(--green2);text-decoration:none}
    article h2 a:hover{text-decoration:underline}
    time{display:block;color:var(--muted);font-size:13px;margin-bottom:10px}
    article p{margin:0;font-size:15px}
    footer{margin-top:30px;padding-top:18px;border-top:1px solid var(--line);
           color:var(--muted);font-size:13.5px}
    footer a{color:var(--green2)}
  </style>
</head>
<body>
  <header>
    <div class="wrap">
      <p class="brand"><b>Craic</b><i>Bet</i></p>
      <h1><xsl:value-of select="channel/title"/></h1>
      <p class="sub"><xsl:value-of select="channel/description"/></p>
    </div>
  </header>

  <div class="wrap">
    <div class="note">
      <b>This page is a feed.</b>
      It updates whenever the GRAI register changes. To follow it, paste
      <code>https://craicbet.com/grai-tracker.xml</code> into any feed reader.
      The full log, with sources, is on the
      <a href="https://craicbet.com/pages/grai-licence-register-tracker">tracker page</a>.
    </div>

    <p class="meta">
      Last updated <xsl:value-of select="channel/lastBuildDate"/>
      · <xsl:value-of select="count(channel/item)"/> entries
    </p>

    <xsl:for-each select="channel/item">
      <article>
        <h2><a href="{link}"><xsl:value-of select="title"/></a></h2>
        <time><xsl:value-of select="pubDate"/></time>
        <p><xsl:value-of select="description"/></p>
      </article>
    </xsl:for-each>

    <footer>
      Published by <a href="https://craicbet.com">CraicBet</a>, an independent
      betting &amp; casino guide for Ireland. Figures come from the official
      register at grai.ie and each entry names its source.
      <br/>18+ · Gambling Awareness Trust 1800 753 753 · gamblingcare.ie
    </footer>
  </div>
</body>
</html>
</xsl:template>
</xsl:stylesheet>
