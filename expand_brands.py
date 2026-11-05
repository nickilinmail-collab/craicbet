#!/usr/bin/env python3
"""Expand thin brand pages with long-tail keyword H2 sections."""
import os, re

BRANDS_DIR = "/home/claude/craicbet/pages/brands"

# Map slug patterns to brand names
def get_brand_name(filename):
    slug = filename.replace('.html', '')
    # Remove suffixes
    for suffix in ['-bonus', '-alternative', '-casino']:
        slug = slug.replace(suffix, '')
    # Title case with spaces
    return slug.replace('-', ' ').title()

def brand_type(filename):
    if '-alternative' in filename:
        return 'alternative'
    return 'bonus'

NEW_SECTIONS_BONUS = """
<h2>Is {brand} Available in Ireland 2026</h2>
<p>{brand} is an offshore casino operator that accepts registrations from Irish players. However, it does not hold a GRAI (Gambling Regulatory Authority of Ireland) remote betting licence. Since 1 July 2026, the GRAI has been issuing remote betting licences under the Gambling Regulation Act 2024 — but remote casino (gaming) licences are separate and expected from 2027–2028, with zero issued as of late 2026. Irish players can technically access {brand}, but without GRAI oversight, player protections differ from licensed sites.</p>
<table style="width:100%;border-collapse:collapse;margin:16px 0;font-size:0.95rem">
<tr style="background:#1e3a28"><th style="padding:9px;border:1px solid #2d5a3d;text-align:left;color:#cde6d4">Factor</th><th style="padding:9px;border:1px solid #2d5a3d;text-align:left;color:#cde6d4">{brand}</th><th style="padding:9px;border:1px solid #2d5a3d;text-align:left;color:#cde6d4">GRAI Licensed Site</th></tr>
<tr><td style="padding:8px;border:1px solid #2d5a3d">Irish Licence</td><td style="padding:8px;border:1px solid #2d5a3d">Not GRAI licensed</td><td style="padding:8px;border:1px solid #2d5a3d">GRAI or Revenue permit</td></tr>
<tr style="background:#0d1f14"><td style="padding:8px;border:1px solid #2d5a3d">Dispute Resolution</td><td style="padding:8px;border:1px solid #2d5a3d">Operator only</td><td style="padding:8px;border:1px solid #2d5a3d">GRAI complaints process</td></tr>
<tr><td style="padding:8px;border:1px solid #2d5a3d">Responsible Gambling Tools</td><td style="padding:8px;border:1px solid #2d5a3d">Varies</td><td style="padding:8px;border:1px solid #2d5a3d">GRAI-mandated (deposit limits, self-exclusion)</td></tr>
<tr style="background:#0d1f14"><td style="padding:8px;border:1px solid #2d5a3d">Player Fund Protection</td><td style="padding:8px;border:1px solid #2d5a3d">Not guaranteed</td><td style="padding:8px;border:1px solid #2d5a3d">Segregated funds required</td></tr>
</table>

<h2>Does {brand} Have a GRAI Licence</h2>
<p>No. {brand} does not hold a GRAI remote betting licence or any Irish Revenue remote bookmaker permission as of November 2026. The GRAI began issuing remote betting licences on 1 July 2026 under the Gambling Regulation Act 2024. Casino (gaming) licences are a separate category — zero have been issued, with the first expected in 2027–2028. To verify any site's licence status, check the public GRAI register at grai.ie. If a site claims a GRAI licence it cannot hold yet, that is a red flag.</p>

<h2>{brand} Minimum Deposit Ireland</h2>
<p>{brand}'s minimum deposit varies by payment method. Offshore casinos typically accept card payments (Visa/Mastercard debit), e-wallets (Skrill, Neteller), and sometimes crypto. Standard minimums run from €10 to €20 for card and e-wallet deposits, with crypto sometimes lower. Note that some Irish banks and Revolut have gambling blocks that may affect deposits — check your card settings before attempting to deposit at any unlicensed site.</p>
<table style="width:100%;border-collapse:collapse;margin:16px 0;font-size:0.95rem">
<tr style="background:#1e3a28"><th style="padding:9px;border:1px solid #2d5a3d;text-align:left;color:#cde6d4">Payment Method</th><th style="padding:9px;border:1px solid #2d5a3d;text-align:left;color:#cde6d4">Typical Min Deposit</th><th style="padding:9px;border:1px solid #2d5a3d;text-align:left;color:#cde6d4">Typical Speed</th></tr>
<tr><td style="padding:8px;border:1px solid #2d5a3d">Visa/Mastercard Debit</td><td style="padding:8px;border:1px solid #2d5a3d">€10–€20</td><td style="padding:8px;border:1px solid #2d5a3d">Instant</td></tr>
<tr style="background:#0d1f14"><td style="padding:8px;border:1px solid #2d5a3d">Skrill / Neteller</td><td style="padding:8px;border:1px solid #2d5a3d">€10</td><td style="padding:8px;border:1px solid #2d5a3d">Instant</td></tr>
<tr><td style="padding:8px;border:1px solid #2d5a3d">Bitcoin / Crypto</td><td style="padding:8px;border:1px solid #2d5a3d">Varies by coin</td><td style="padding:8px;border:1px solid #2d5a3d">10–60 minutes</td></tr>
<tr style="background:#0d1f14"><td style="padding:8px;border:1px solid #2d5a3d">Bank Transfer</td><td style="padding:8px;border:1px solid #2d5a3d">€20–€50</td><td style="padding:8px;border:1px solid #2d5a3d">1–3 business days</td></tr>
</table>

<h2>{brand} Withdrawal Time Ireland</h2>
<p>Withdrawal times at offshore casinos like {brand} typically range from 24 hours for e-wallets to 3–5 business days for card withdrawals. Before processing a withdrawal, most offshore casinos require KYC (Know Your Customer) verification — uploading a passport/driving licence and proof of address. First-time withdrawals may take longer due to verification. At GRAI-licensed sites, withdrawal timelines are governed by licence conditions; offshore sites set their own rules.</p>
"""

NEW_SECTIONS_ALT = """
<h2>Is {brand} a Safe Alternative for Irish Players</h2>
<p>Irish players searching for {brand} alternatives are often looking for sites that offer similar features while operating legally under Irish gambling regulations. The key factor is GRAI (Gambling Regulatory Authority of Ireland) licensing — since 1 July 2026, sites require a GRAI remote licence to legally take bets from Irish residents. GRAI-licensed sites offer mandatory player protections: deposit limits, self-exclusion, segregated funds, and a formal complaints process via grai.ie.</p>
<table style="width:100%;border-collapse:collapse;margin:16px 0;font-size:0.95rem">
<tr style="background:#1e3a28"><th style="padding:9px;border:1px solid #2d5a3d;text-align:left;color:#cde6d4">What to Look For</th><th style="padding:9px;border:1px solid #2d5a3d;text-align:left;color:#cde6d4">{brand} (Offshore)</th><th style="padding:9px;border:1px solid #2d5a3d;text-align:left;color:#cde6d4">GRAI Licensed Alternative</th></tr>
<tr><td style="padding:8px;border:1px solid #2d5a3d">Irish Licence</td><td style="padding:8px;border:1px solid #2d5a3d">No GRAI licence</td><td style="padding:8px;border:1px solid #2d5a3d">GRAI or Revenue permit</td></tr>
<tr style="background:#0d1f14"><td style="padding:8px;border:1px solid #2d5a3d">Player Funds</td><td style="padding:8px;border:1px solid #2d5a3d">Not regulated</td><td style="padding:8px;border:1px solid #2d5a3d">Segregated — protected</td></tr>
<tr><td style="padding:8px;border:1px solid #2d5a3d">Complaints</td><td style="padding:8px;border:1px solid #2d5a3d">Operator only</td><td style="padding:8px;border:1px solid #2d5a3d">Escalate to GRAI</td></tr>
<tr style="background:#0d1f14"><td style="padding:8px;border:1px solid #2d5a3d">Responsible Gambling</td><td style="padding:8px;border:1px solid #2d5a3d">Self-imposed</td><td style="padding:8px;border:1px solid #2d5a3d">GRAI-mandated tools</td></tr>
<tr><td style="padding:8px;border:1px solid #2d5a3d">Bonus Terms</td><td style="padding:8px;border:1px solid #2d5a3d">Unregulated</td><td style="padding:8px;border:1px solid #2d5a3d">Must be fair and clear</td></tr>
</table>

<h2>{brand} vs GRAI Licensed Sites: Key Differences for Irish Players</h2>
<p>When comparing {brand} to GRAI-licensed alternatives, the main practical differences come down to accountability and Irish law. Under the Gambling Regulation Act 2024, licensed operators must maintain segregated player funds, respond to GRAI audits, and provide mandatory responsible gambling tools. Offshore operators like {brand} are not subject to these requirements. That does not mean they are all unsafe — many hold licences from other jurisdictions (Malta MGA, Gibraltar, Curaçao) — but Irish player protections are weaker without GRAI oversight.</p>

<h2>Does {brand} Accept Irish Players in 2026</h2>
<p>{brand} typically accepts Irish players as it does not geo-block Ireland. However, operating without an Irish GRAI licence means it is not formally authorised to offer gambling services to Irish residents under the Gambling Regulation Act 2024. The GRAI's enforcement approach in 2026 focuses first on advertising compliance and licensed operators; individual player access to offshore sites is not currently criminalised. Players should be aware of the reduced protections and consider licensed alternatives where available. For problem gambling support, contact the Gambling Awareness Trust on 1800 753 753 or visit gamblingcare.ie.</p>
"""

def expand_brand_page(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    filename = os.path.basename(filepath)
    brand = get_brand_name(filename)
    btype = brand_type(filename)

    # Choose sections based on page type
    if btype == 'alternative':
        new_html = NEW_SECTIONS_ALT.format(brand=brand)
    else:
        new_html = NEW_SECTIONS_BONUS.format(brand=brand)

    # Find insertion point
    insert_before = None
    if '<div class="editorial-box"' in content:
        insert_before = '<div class="editorial-box"'
    elif '<div class="faq-item"' in content:
        insert_before = '<div class="faq-item"'

    if not insert_before:
        return False

    # Check if already expanded (look for our marker)
    if 'GRAI Licence\n</h2>' in content or 'Does {brand} Have a GRAI Licence' in content or 'Does ' + brand + ' Have a GRAI Licence' in content:
        return False

    # Insert
    new_content = content.replace(insert_before, new_html + '\n' + insert_before, 1)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return True

# Find all thin brand pages
import subprocess
result = subprocess.run(
    'find /home/claude/craicbet/pages/brands -name "*.html" | xargs wc -c 2>/dev/null | sort -n | awk \'$1 < 16000 {print $2}\'',
    shell=True, capture_output=True, text=True
)
pages = [p.strip() for p in result.stdout.strip().split('\n') if p.strip() and p.strip() != 'total']

expanded = []
skipped = []
for page in pages:
    if os.path.exists(page):
        ok = expand_brand_page(page)
        if ok:
            expanded.append(page)
        else:
            skipped.append(page)

print(f"Expanded: {len(expanded)} pages")
print(f"Skipped (already done or no insertion point): {len(skipped)}")
for p in expanded[:10]:
    print(f"  + {os.path.basename(p)}")
