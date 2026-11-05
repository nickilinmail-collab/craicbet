#!/usr/bin/env python3
"""Generate Groups D+E FAQ pages for craicbet.com"""
import os, json, sys
sys.path.insert(0, '/home/claude/craicbet')
from gen_faq_pages import build, cta_box

# ── GROUP D: Account issues (10 pages) ────────────────────────────────────

build(
    slug="account-restricted-betting-ireland",
    title="Betting Account Restricted in Ireland: Why It Happens and What To Do",
    desc="Why GRAI-licensed bookmakers restrict stakes or accounts, your rights under GRAI rules, and practical options when your account is limited.",
    h1="Betting Account Restricted in Ireland: Causes and Options",
    page_title="Account Restricted Ireland",
    body=f"""<p class="article-intro">Having your betting account restricted &mdash; maximum stakes cut, certain markets blocked, or bonuses withdrawn &mdash; is frustrating but legal. GRAI-licensed bookmakers are private businesses that can limit how much they accept from any customer. Here is why it happens and what you can realistically do.</p>

<h2>Why Bookmakers Restrict Accounts</h2>
<p>Bookmakers restrict accounts that are consistently profitable. The most common triggers:</p>
<ul>
  <li>Consistently backing winners at high odds</li>
  <li>Always finding the best price in the market (line shopping)</li>
  <li>Systematically using bonuses and promotions (matched betting patterns)</li>
  <li>Placing large bets on markets with thin liquidity</li>
  <li>Early-price betting on horse racing (taking value before the market firms up)</li>
</ul>
<p>Operators use software to flag these patterns. A restriction can follow a single large win or build gradually after months of profitability.</p>

{cta_box()}

<h2>Types of Restriction</h2>
<p><strong>Stake limits:</strong> Maximum bet reduced, sometimes to &euro;2&ndash;&euro;5 per bet on certain markets. <strong>Bonus withdrawal:</strong> No longer eligible for promotions. <strong>Market restrictions:</strong> Certain sports or markets blocked. <strong>Full account closure:</strong> Account closed by operator choice.</p>

<h2>Your Rights Under GRAI Rules</h2>
<p>GRAI-licensed operators have the right to refuse bets and restrict accounts commercially. The GRAI does not currently require operators to accept bets of any size from any customer. However, operators must:</p>
<ul>
  <li>Pay out all outstanding winnings from bets accepted before the restriction</li>
  <li>Allow you to withdraw your balance</li>
  <li>Not restrict accounts as a form of punishment for exercising responsible gambling rights (e.g., restricting someone for requesting a deposit limit is not permitted)</li>
</ul>

<h2>Practical Options When Restricted</h2>
<p>Diversify across multiple GRAI-licensed operators. Use exchanges (Betfair, Betdaq) which have no account restrictions by design. For horse racing, compare prices across multiple operators before betting. Some punters find that placing small regular bets on popular markets (accumulators, low-odds match results) alongside profitable bets delays further restriction.</p>

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px 20px;margin:24px 0">
  <strong>Related guides:</strong> <a href="gubbed-betting-account-ireland">Gubbing explained</a> &middot; <a href="account-closed-betting-ireland-what-to-do">Account closed</a> &middot; <a href="grai-complaints-ireland">GRAI complaints</a>
</div>
""",
    faqs=[
        ("Can a GRAI-licensed bookmaker restrict my account?", "Yes — bookmakers are private businesses that can restrict how much they accept from any customer. The GRAI does not require operators to accept bets of any size."),
        ("What can I do if my betting account is restricted?", "Open accounts at other GRAI-licensed operators, use betting exchanges (which have no restrictions), and diversify your betting patterns. The restriction at one operator does not affect your accounts elsewhere."),
        ("Can a bookmaker restrict my account for being profitable?", "Yes — this is legal. Bookmakers can limit any customer for commercial reasons. Only your winnings from bets already accepted are protected; future bets are at the operator's discretion."),
        ("Does being restricted affect my ability to withdraw?", "No — a stake restriction does not affect your right to withdraw your existing balance. You can withdraw at any time regardless of any stake limits on your account."),
        ("Can I appeal a betting account restriction?", "You can contact the operator's support and ask for a review. Success is rare, but sometimes providing proof of recreational betting patterns can result in limits being eased. There is no GRAI right to have restrictions removed."),
    ]
)

build(
    slug="account-closed-betting-ireland-what-to-do",
    title="Betting Account Closed in Ireland: What To Do and Your GRAI Rights",
    desc="If a bookmaker closes your account in Ireland, your balance must be returned. GRAI complaints process, cooling-off vs permanent ban, and what to do next.",
    h1="Betting Account Closed in Ireland: Your Rights and Next Steps",
    page_title="Account Closed Ireland",
    body=f"""<p class="article-intro">If a GRAI-licensed bookmaker closes your account, they must return your balance. This is a licence condition. The reasons for closure, your rights, and what comes next vary depending on whether it was a commercial decision, a compliance issue, or a self-exclusion. Here is the full breakdown.</p>

<h2>Why Bookmakers Close Accounts</h2>
<p><strong>Commercial closure:</strong> The operator has decided you are not a profitable customer (consistently wins, matched betting patterns). Your balance is returned and you can open accounts elsewhere. <strong>Compliance/KYC failure:</strong> Identity verification issues, suspected fraud, or AML concerns. Balance may be temporarily held pending investigation. <strong>Bonus/T&amp;C violation:</strong> Multiple accounts, bonus abuse. Bonus winnings may be voided; real-money balances must be returned. <strong>Regulatory:</strong> GRAI-mandated closure of accounts with certain patterns (e.g., markers of harm).</p>

{cta_box()}

<h2>Getting Your Balance Back</h2>
<p>Under GRAI licence conditions, operators must return your balance upon account closure. This is a legal requirement. If you have an outstanding balance after closure, the operator must pay it out via the same method you last deposited with, or via bank transfer if that method is no longer available. If the operator refuses to return your balance without a valid legal reason, escalate to the GRAI.</p>

<h2>The GRAI Complaints Process for Account Closures</h2>
<ol>
  <li>Get the closure reason in writing from the operator</li>
  <li>Request your balance withdrawal</li>
  <li>If the balance is withheld without valid reason, submit a formal complaint to the operator</li>
  <li>If unresolved in 8 weeks, file a complaint with the GRAI at grai.ie</li>
</ol>

<h2>Cooling-Off vs Permanent Ban vs Self-Exclusion</h2>
<p>A cooling-off period is a temporary restriction you can request at any time (typically 24 hours to 6 weeks). A permanent account closure is usually at operator request. Self-exclusion is a request you make to stop gambling &mdash; under GRAI rules this feeds into the National Gambling Exclusion Register (NGER). Self-exclusion cannot be reversed within the exclusion period &mdash; this is intentional.</p>

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px 20px;margin:24px 0">
  <strong>Related guides:</strong> <a href="account-restricted-betting-ireland">Account restrictions</a> &middot; <a href="how-to-delete-betting-account-ireland">Deleting an account</a> &middot; <a href="grai-complaints-ireland">GRAI complaints</a>
</div>
""",
    faqs=[
        ("Can a GRAI-licensed bookmaker close my account?", "Yes — operators can close accounts for commercial or compliance reasons. They must return your balance under GRAI licence conditions."),
        ("What happens to my money if my betting account is closed?", "Your balance must be returned — this is a GRAI licence condition. The operator should contact you about withdrawal within a reasonable timeframe. If they don't, escalate to the GRAI."),
        ("Can I open a new account after being closed by a bookmaker?", "At the same operator: usually no (you are banned). At other GRAI-licensed operators: yes, unless you are on the National Gambling Exclusion Register."),
        ("What is the GRAI complaints process for account closures?", "Submit a formal complaint to the operator first. If unresolved after 8 weeks, escalate to the GRAI at grai.ie. The GRAI can investigate and mandate balance returns where operators have breached licence conditions."),
        ("How long does a closed account balance take to be returned?", "Operators should process this within the standard withdrawal timeframe (1–5 business days depending on method). If no response within 10 business days, contact support and reference your account closure date."),
    ]
)

build(
    slug="gubbed-betting-account-ireland",
    title="Gubbed Betting Account in Ireland: What It Means and How to Avoid It",
    desc="Gubbing means your betting account has been stake-restricted by a bookmaker. What triggers it, what happens to your free bets, and how to extend account life.",
    h1="Gubbed Betting Account in Ireland: What It Means",
    page_title="Gubbed Account Ireland",
    body=f"""<p class="article-intro">&ldquo;Gubbed&rdquo; is slang for having your betting account&rsquo;s maximum stakes reduced &mdash; typically to tiny amounts (&euro;2&ndash;&euro;10) on most markets. At GRAI-licensed bookmakers in Ireland, this happens when you are identified as a consistently profitable or systematically offer-exploiting customer. Here is what it means and what you can do.</p>

<h2>What Exactly Is Gubbing?</h2>
<p>A gubbed account still exists and can still be used, but maximum stakes are slashed. You might still be able to place &euro;500 on a Cheltenham favourite with no problem, but try to bet &euro;100 on a 10/1 shot and you will be limited to &euro;5. Many gubbed accounts also lose access to promotional offers. The term is widely used in UK and Irish matched betting communities.</p>

{cta_box()}

<h2>What Triggers Gubbing at Irish Bookmakers</h2>
<ul>
  <li>Systematically matched betting all free bet offers</li>
  <li>Consistently backing outsiders that win</li>
  <li>Always taking the best available price, never the default</li>
  <li>High win rate on early prices in horse racing</li>
  <li>Large bets relative to your account history</li>
</ul>
<p>Bookmakers use account profitability metrics and pattern recognition. A single large win rarely triggers gubbing; consistent profitability over weeks or months usually does.</p>

<h2>What Happens to Your Free Bets When Gubbed?</h2>
<p>Existing unspent free bets are usually honoured even on a gubbed account. Future bonus eligibility is typically removed. If the operator withdraws an active free bet from your account without it being used, you can complain and claim its value &mdash; this would be a breach of the agreed promotional T&amp;Cs.</p>

<h2>Strategies to Extend Account Life</h2>
<ul>
  <li>Place occasional &ldquo;mug bets&rdquo; &mdash; recreational bets on popular markets at default odds</li>
  <li>Bet on accumulators occasionally (unprofitable by nature, so they signal recreational behaviour)</li>
  <li>Avoid always taking the best price; accept market odds sometimes</li>
  <li>Keep your win rate from looking suspicious by betting across a range of markets</li>
</ul>

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px 20px;margin:24px 0">
  <strong>Related guides:</strong> <a href="account-restricted-betting-ireland">Account restrictions</a> &middot; <a href="matched-betting-ireland-legal">Matched betting guide</a> &middot; <a href="bonus-abuse-ireland">Bonus abuse rules</a>
</div>
""",
    faqs=[
        ("What does gubbed mean in betting?", "Gubbed means your maximum stake has been severely reduced by the bookmaker — often to €2–€10 on most markets. The account still exists but is essentially useless for profitable betting."),
        ("Why do bookmakers gub accounts in Ireland?", "Because you are identified as a consistently profitable customer. Bookmakers restrict winners to protect their margins. Matched bettors and sharp punters are the most common targets."),
        ("Can I undo a gubbed betting account?", "Rarely. You can contact support and ask for a review. Some operators restore limits if you demonstrate recreational betting patterns over several months. Most gubbed accounts stay restricted."),
        ("Do I lose my free bets when gubbed?", "Existing credited free bets are usually still usable. Future bonus eligibility is typically removed. If the operator takes back an active free bet, you can complain — that would breach the promotional T&Cs."),
        ("Which Irish bookmakers are least likely to gub accounts?", "Betting exchanges (Betfair, Betdaq) never gub accounts — they match punters against each other and welcome winners. Among traditional bookmakers, those with higher liquidity (larger books) tend to tolerate winners longer."),
    ]
)

build(
    slug="how-to-reopen-closed-betting-account",
    title="How to Reopen a Closed Betting Account in Ireland (2026 Guide)",
    desc="Whether you can reopen a closed betting account depends on why it was closed. Cooling-off, temporary suspension, and self-exclusion have different processes.",
    h1="How to Reopen a Closed Betting Account in Ireland",
    page_title="Reopen Closed Betting Account",
    body=f"""<p class="article-intro">Whether you can reopen a closed betting account depends entirely on why it was closed in the first place. A cooling-off period expires automatically; a commercial closure is usually permanent at that operator; a self-exclusion cannot be reversed during the exclusion period under GRAI rules. Here is how each type works.</p>

<h2>Cooling-Off Period: Automatic Reopening</h2>
<p>A cooling-off period is a temporary restriction you apply to your own account. Under GRAI responsible gambling requirements, once a cooling-off period expires, your account should automatically become accessible again &mdash; or you may need to log in and confirm you wish to resume. GRAI rules require that increasing limits (and ending cooling-off) has a mandatory reflection period of at least 24&ndash;48 hours.</p>

{cta_box()}

<h2>Temporary Suspension: Contact Support</h2>
<p>If the operator suspended your account for investigation (unusual activity, payment issues), contact customer support with your account details and a request to reinstate. You will likely need to provide KYC documentation if the suspension was ID-related. Processing typically takes 3&ndash;10 business days.</p>

<h2>Self-Exclusion: Cannot Be Undone Within the Period</h2>
<p>Self-exclusion under GRAI rules is intentionally irreversible during the exclusion period. If you self-excluded for 6 months, you cannot reopen the account for 6 months. This applies to all GRAI-licensed operators enrolled in the National Gambling Exclusion Register (NGER). Once the exclusion period ends, there is typically a mandatory 24-hour reflection period before reactivation.</p>
<p>If you are struggling with gambling and have broken your self-exclusion, contact the Gambling Awareness Trust at 1800 753 753 or gamblingcare.ie for support.</p>

<h2>Commercial Closure: Usually Permanent at That Operator</h2>
<p>If a bookmaker closed your account for commercial reasons (you are too profitable) or for T&amp;C violations, reopening with that specific operator is very unlikely. Your options are other GRAI-licensed operators, which are unaffected by one operator&rsquo;s commercial decision.</p>

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px 20px;margin:24px 0">
  <strong>Related guides:</strong> <a href="self-exclusion-broke-ireland">Self-exclusion broken</a> &middot; <a href="account-closed-betting-ireland-what-to-do">Account closed guide</a> &middot; <a href="how-to-delete-betting-account-ireland">Delete your account</a>
</div>
""",
    faqs=[
        ("Can you reopen a closed betting account in Ireland?", "It depends on why it was closed. Cooling-off periods expire automatically. Self-exclusions cannot be reversed within the exclusion period. Commercial closures are usually permanent at that operator."),
        ("How do I reopen an account after a cooling-off period?", "Log in when the period expires — you may need to confirm you wish to resume. Under GRAI rules, there is a mandatory 24–48 hour reflection period before the account is fully reactivated."),
        ("Can I reopen an account if I self-excluded?", "Not during the exclusion period. GRAI rules make self-exclusion irreversible for the specified duration. After it expires, contact the operator to initiate reactivation with the mandatory reflection period."),
        ("What if I want to reopen an account that was closed for a T&Cs violation?", "Very difficult — operators typically maintain permanent bans for T&Cs violations. You can try contacting support, but most will not reopen accounts for bonus abuse or multi-accounting."),
        ("Does closing one account affect my accounts at other bookmakers?", "No — each bookmaker is independent. A commercial closure at one operator does not affect your accounts at others, unless you are on the NGER (National Gambling Exclusion Register) for self-exclusion reasons."),
    ]
)

build(
    slug="forgot-username-betting-site-ireland",
    title="Forgot Username on a Betting Site in Ireland? How to Recover Access",
    desc="Recovering a forgotten username on an Irish betting site — email recovery, support options, KYC identity confirmation, and what to do if the email is also lost.",
    h1="Forgot Your Username on an Irish Betting Site? Recovery Guide",
    page_title="Forgot Betting Username Ireland",
    body=f"""<p class="article-intro">Most GRAI-licensed Irish betting sites use your email address as your username, so a forgotten username typically means a forgotten registered email. If you remember the email but not the password, recovery is straightforward. If you remember neither, you will need to verify your identity through the operator&rsquo;s support team. Here is how to handle both scenarios.</p>

<h2>If You Remember Your Email</h2>
<p>Most GRAI-licensed bookmakers use your email address as the account identifier. Go to the login page and try &ldquo;Forgot Password&rdquo; with your email. If the email is registered, you will receive a reset link. This is the fastest route and works for the majority of cases.</p>

{cta_box()}

<h2>If You Have Forgotten Your Registered Email</h2>
<p>Contact the operator&rsquo;s customer support (live chat is fastest) and provide:</p>
<ul>
  <li>Your full name as registered on the account</li>
  <li>Date of birth</li>
  <li>Last deposit amount and method (if known)</li>
  <li>Registered address</li>
</ul>
<p>Support can look up your account via these identifiers. You will then be asked to verify identity &mdash; typically providing a photo of your ID document via email. Under GRAI KYC requirements, operators must verify your identity before giving access to account details, which protects you from someone else recovering your account.</p>

<h2>Accounts Created via Social Login</h2>
<p>Some operators offer registration via Google or Apple accounts. If you registered this way and have lost access to that Google or Apple account, recovery becomes more complex. Contact the operator first; they can usually manually link a new email address after full identity verification.</p>

<h2>If You Cannot Access the Account at All</h2>
<p>Provide as much identifying information as possible to support. GRAI rules require operators to verify your identity before providing account access &mdash; this is a consumer protection measure. Processing a manual identity verification typically takes 2&ndash;5 business days. Ensure you have a valid ID document ready.</p>

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px 20px;margin:24px 0">
  <strong>Related guides:</strong> <a href="how-long-does-verification-take-betting-ireland">KYC verification times</a> &middot; <a href="identity-verification-failed-ireland">KYC failed</a> &middot; <a href="how-to-delete-betting-account-ireland">Delete your account</a>
</div>
""",
    faqs=[
        ("How do I recover my betting account username in Ireland?", "Most sites use your email as username. Try 'Forgot Password' with your email. If you've forgotten your email too, contact support with your name, date of birth, and address for identity verification."),
        ("Can support find my account without my username?", "Yes — provide your full name, date of birth, registered address, and optionally last deposit details. After identity verification, support can retrieve your account details."),
        ("How long does account recovery take at an Irish betting site?", "If you have your email: instant via password reset. Manual identity verification through support: 2–5 business days. Provide documentation promptly to speed up the process."),
        ("Is it safe to send my ID to betting site support?", "GRAI-licensed operators must follow data protection rules (GDPR) for all personal data. Sending ID via secure email to official support channels is standard KYC procedure and is safe at licensed operators."),
        ("What if the email address on my account no longer exists?", "Contact support and explain. After full identity verification (which may require a video call or in-person document review in some cases), operators can update the email address on your account."),
    ]
)

build(
    slug="how-to-delete-betting-account-ireland",
    title="How to Delete a Betting Account in Ireland: Your GRAI Rights",
    desc="How to permanently close and delete a betting account at a GRAI-licensed Irish bookmaker, withdraw your balance, and exercise your data protection rights.",
    h1="How to Delete a Betting Account in Ireland",
    page_title="Delete Betting Account Ireland",
    body=f"""<p class="article-intro">You have the right to close and delete your betting account at any GRAI-licensed operator. Under both GRAI rules and GDPR, you can request account closure and deletion of your personal data. Here is the step-by-step process and what to expect.</p>

<h2>Step 1: Withdraw Your Balance First</h2>
<p>Before requesting account closure, withdraw your full balance. Once the account is closed, the operator should still return any outstanding funds, but it is simpler to withdraw first. Use the standard withdrawal process and wait for the funds to clear before initiating closure.</p>

{cta_box()}

<h2>Step 2: Use Any Outstanding Bonuses or Request Their Removal</h2>
<p>Decide whether to use any outstanding free bets or bonus funds before closing. Once the account is closed, unused bonuses are forfeited. If you are closing specifically because you want to stop gambling (self-exclusion), do not use the bonuses &mdash; request immediate closure instead.</p>

<h2>Step 3: Request Account Closure</h2>
<p>Most GRAI-licensed operators offer account closure via:</p>
<ul>
  <li>Account settings &gt; Responsible Gambling &gt; Close Account</li>
  <li>Live chat or email support</li>
  <li>A formal closure form in the responsible gambling section</li>
</ul>
<p>If you are closing for responsible gambling reasons, say so &mdash; the operator must process this under GRAI rules and must not try to retain you with bonus offers.</p>

<h2>Data Protection: Requesting Deletion of Personal Data</h2>
<p>Under GDPR (which applies in Ireland), you have the &ldquo;right to erasure&rdquo; (also called the right to be forgotten). You can request that the operator deletes your personal data after account closure. However, operators are permitted to retain transaction and identity records for AML compliance (typically 7 years) &mdash; they can decline to delete these specific records even after a deletion request, but must delete non-essential data.</p>

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px 20px;margin:24px 0">
  <strong>Related guides:</strong> <a href="self-exclusion-broke-ireland">Self-exclusion in Ireland</a> &middot; <a href="account-closed-betting-ireland-what-to-do">Account closed</a> &middot; <a href="how-to-reopen-closed-betting-account">Reopening a closed account</a>
</div>
""",
    faqs=[
        ("How do I delete my betting account in Ireland?", "Withdraw your balance first, then go to Account Settings > Responsible Gambling > Close Account, or contact live chat. GRAI-licensed operators must process closure requests promptly."),
        ("Do I get my money back when I close a betting account?", "Yes — your balance must be returned when you close an account. This is a GRAI licence condition. Withdraw before closing for the simplest process."),
        ("Can I request deletion of my personal data from a betting site?", "Yes — under GDPR you can request data deletion. Operators may retain AML-required records (up to 7 years) but must delete non-essential personal data."),
        ("Can a bookmaker try to persuade me not to close my account?", "Under GRAI responsible gambling rules, operators cannot use inducements or high-pressure tactics to retain customers seeking to close for responsible gambling reasons. Report any such behaviour to the GRAI."),
        ("How long does account deletion take?", "Account closure typically takes 1–5 business days. GDPR data deletion requests must be responded to within 30 days under Irish data protection law."),
    ]
)

build(
    slug="self-exclusion-broke-ireland",
    title="What Happens if You Bet While Self-Excluded in Ireland? GRAI NGER Rules",
    desc="Betting while self-excluded in Ireland violates your exclusion. GRAI NGER coverage, what happens to bets and winnings, and how to get support.",
    h1="What Happens if You Bet While Self-Excluded in Ireland?",
    page_title="Self-Exclusion Broken Ireland",
    body=f"""<p class="article-intro">If you are on Ireland&rsquo;s National Gambling Exclusion Register (NGER) and place a bet during your exclusion period, the bet and any winnings may be voided. GRAI-licensed operators are required to participate in NGER and check new customers and existing customers against it. This page explains what happens, your options, and where to get support.</p>

<h2>The NGER and How It Works</h2>
<p>The National Gambling Exclusion Register is a database managed by the GRAI. GRAI-licensed operators are required to check the register and refuse bets from, or service accounts of, individuals on the NGER. When fully operational, self-excluding at any single GRAI-licensed operator automatically notifies all participating operators.</p>

{cta_box()}

<h2>What Happens to Bets Placed During Self-Exclusion</h2>
<p>If a GRAI-licensed operator accepts a bet from someone on the NGER, that is a licence breach by the operator. Under GRAI rules, bets placed in breach of a self-exclusion are typically voided and stakes returned &mdash; but winnings are not paid out. The logic: the operator should not have taken the bet; paying out would reward the breach of the exclusion agreement.</p>

<h2>If You Have Broken Your Self-Exclusion</h2>
<p>First: this is not uncommon. Breaking a self-exclusion is a sign that you need additional support, not a reason to feel shame. Contact the <strong>Gambling Awareness Trust</strong> at <strong>1800 753 753</strong> (free, confidential) or visit <strong>gamblingcare.ie</strong>. They can assist with extending your exclusion, accessing counselling, and creating a plan that works.</p>
<p>You can re-register on the NGER at any time. The re-exclusion takes effect within the timeframe specified by the operator (some are immediate; GRAI is working towards a standardised near-immediate implementation).</p>

<h2>If an Operator Failed to Block You</h2>
<p>If you placed a bet during your exclusion period and the operator should have blocked you but did not, the operator may be liable for a GRAI licence breach. Report this to the GRAI at grai.ie. You may also be entitled to have your deposits returned. This does not negate your exclusion &mdash; it makes the operator responsible for the failure.</p>

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px 20px;margin:24px 0">
  <strong>Need help?</strong> Gambling Awareness Trust: <strong>1800 753 753</strong> &middot; <a href="https://www.gamblingcare.ie" target="_blank" rel="noopener">gamblingcare.ie</a><br><br>
  <strong>Related guides:</strong> <a href="how-to-delete-betting-account-ireland">Close your account</a> &middot; <a href="how-to-reopen-closed-betting-account">Reopening after exclusion</a> &middot; <a href="grai-complaints-ireland">GRAI complaints</a>
</div>
""",
    faqs=[
        ("What happens if you bet while self-excluded in Ireland?", "Bets placed during self-exclusion are typically voided and stakes returned, but winnings are not paid. The operator also faces a GRAI licence breach if they failed to block you."),
        ("Does self-exclusion cover all Irish betting sites?", "GRAI-licensed operators participate in the National Gambling Exclusion Register (NGER). When fully operational, self-excluding at one site will register across all GRAI-licensed operators automatically."),
        ("Can I get my deposits back if a site accepted bets during my self-exclusion?", "Yes — if the operator failed to block you despite being on the NGER, you may be entitled to deposit refunds. Report this to the GRAI at grai.ie."),
        ("How do I re-register for self-exclusion after breaking it?", "Contact the GRAI or any GRAI-licensed operator directly to re-register. You can also call the Gambling Awareness Trust (1800 753 753) for guidance on re-exclusion."),
        ("Where can I get help if I've broken my self-exclusion?", "Gambling Awareness Trust: 1800 753 753 (free, confidential). gamblingcare.ie for online resources and counselling referrals."),
    ]
)

build(
    slug="underage-betting-account-discovered",
    title="Underage Betting Account Discovered in Ireland: What Happens?",
    desc="If an underage betting account is discovered by a GRAI-licensed operator, all bets are voided and deposits returned. The operator's obligations and your rights.",
    h1="Underage Betting Account Discovered in Ireland: Operator Obligations",
    page_title="Underage Account Discovered Ireland",
    body=f"""<p class="article-intro">If a GRAI-licensed bookmaker discovers that a customer was under 18 when they opened an account, specific legal obligations are triggered. All bets must be voided, all deposits returned, and the account closed. Here is what happens in detail.</p>

<h2>The Operator&rsquo;s Legal Obligations</h2>
<p>Under the Gambling Regulation Act 2024, allowing underage gambling is a serious licence breach. When an operator discovers or is notified that a customer was underage when they opened an account, they must:</p>
<ul>
  <li>Immediately close the account</li>
  <li>Void all bets placed during the period of underage use</li>
  <li>Return all deposits made to the original payment method</li>
  <li>Not retain any winnings generated during the underage period</li>
  <li>Report the breach to the GRAI as a compliance incident</li>
</ul>

{cta_box()}

<h2>How Operators Discover Underage Accounts</h2>
<p>Most commonly: through ID verification revealing a date of birth showing the customer was under 18 at account creation. Sometimes through reports from parents or family members. Occasionally through GRAI audits. Under GRAI rules, operators must conduct KYC on all new accounts and must age-verify before any gambling activity is permitted.</p>

<h2>What the Customer Receives</h2>
<p>All deposits must be returned, regardless of whether they were used for bets. Winnings from bets are not returned &mdash; the bets are voided. For example, if a customer deposited &euro;100, bet it all and won &euro;500, the &euro;100 deposit is returned but the &euro;500 is not, because the bets were void.</p>

<h2>Family Members or Guardians</h2>
<p>If a parent or guardian discovers their child has opened a betting account, they should report it to the operator directly (and provide evidence of age). The operator&rsquo;s compliance obligations then apply as above. Parents can also report ongoing concerns to the GRAI at grai.ie.</p>

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px 20px;margin:24px 0">
  <strong>Related guides:</strong> <a href="betting-at-18-ireland">Betting age rules Ireland</a> &middot; <a href="grai-complaints-ireland">GRAI complaints</a>
</div>
""",
    faqs=[
        ("What happens if an underage betting account is found in Ireland?", "The operator must void all bets, return all deposits, close the account, and report to the GRAI. This is a legal requirement under the Gambling Regulation Act 2024."),
        ("Does an underage bettor keep their winnings?", "No — bets are voided, so winnings are not paid. Only deposits made are returned. The operator cannot keep the deposits either."),
        ("What should a parent do if their child opened a betting account?", "Report it to the operator immediately with proof of age. The operator must close the account, void all bets, and return all deposits. You can also report concerns to the GRAI at grai.ie."),
        ("Can a GRAI-licensed operator be fined for allowing underage betting?", "Yes — allowing underage gambling is a serious licence breach. The GRAI can investigate and impose sanctions including fines and licence suspension."),
        ("What is the minimum age to bet in Ireland?", "18. This applies to all forms of gambling — online betting, casino, in-person shops, and lotteries — under the Gambling Regulation Act 2024."),
    ]
)

build(
    slug="identity-verification-failed-ireland",
    title="Identity Verification Failed on an Irish Betting Site? How to Fix It",
    desc="Why KYC fails at GRAI-licensed Irish bookmakers, what documents are accepted, common rejection reasons, and how to appeal a failed verification.",
    h1="KYC Identity Verification Failed on an Irish Betting Site: Fix Guide",
    page_title="ID Verification Failed Ireland",
    body=f"""<p class="article-intro">KYC (Know Your Customer) verification failures are common, but most are fixable. The issue is usually a document quality problem, an address mismatch, or an expired document rather than a fundamental problem with your identity. Here is how to diagnose and resolve a failed verification at a GRAI-licensed Irish bookmaker.</p>

<h2>Common Reasons KYC Fails</h2>
<ul>
  <li><strong>Blurry or cropped photo:</strong> The most common cause. Automated systems reject images where text is not clearly readable or document corners are cut off.</li>
  <li><strong>Expired document:</strong> An expired driving licence or passport is not accepted. Use a current, valid document.</li>
  <li><strong>Address mismatch:</strong> Your proof of address does not match the address on your account. Update your registered address first.</li>
  <li><strong>Document older than 3 months:</strong> Utility bills and bank statements used for proof of address must typically be less than 3 months old.</li>
  <li><strong>Unusual lighting or glare:</strong> Flash glare, shadows, or photographing through plastic covers cause failures.</li>
  <li><strong>Name mismatch:</strong> Your document name must exactly match the name on your betting account (including middle names or initials if used at registration).</li>
</ul>

{cta_box()}

<h2>What Documents Are Accepted</h2>
<p><strong>Identity:</strong> Irish passport, Irish driving licence, EU national ID card, UK passport or driving licence. <strong>Proof of address:</strong> Utility bill (electricity, gas, broadband), bank statement, government letter, Revenue document &mdash; all within the past 3 months and showing your full name and registered address.</p>

<h2>How to Resubmit</h2>
<p>Log into your account and go to the verification section. Take a new photo in good natural light, ensuring all document corners are visible and text is sharp. Use your phone&rsquo;s standard camera app rather than a scanning app. Submit as a JPEG or PDF. If the portal is not accepting your documents, email them to the KYC team directly (the address is usually given in the rejection email).</p>

<h2>Appealing a Rejection</h2>
<p>If your documents are genuinely valid but keep being rejected, contact live chat. Explain the situation and ask for manual review. Manual reviews typically take 24&ndash;48 hours but resolve most edge cases that automated systems reject incorrectly. Under GRAI rules, you have the right to have your account access fairly assessed &mdash; if a valid verification is unreasonably refused, you can escalate to the GRAI.</p>

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px 20px;margin:24px 0">
  <strong>Related guides:</strong> <a href="how-long-does-verification-take-betting-ireland">KYC verification times</a> &middot; <a href="how-long-do-withdrawals-take-ireland">Withdrawal times</a> &middot; <a href="grai-complaints-ireland">GRAI complaints</a>
</div>
""",
    faqs=[
        ("Why did my identity verification fail on an Irish betting site?", "Common causes: blurry photo, expired document, address mismatch, document older than 3 months, or name mismatch. Retake in good light with all corners visible and resubmit."),
        ("What ID documents are accepted for KYC in Ireland?", "Passport, national ID card, or driving licence for identity. Utility bill, bank statement, or government letter (less than 3 months old) for proof of address."),
        ("How do I fix a KYC failure on a betting site?", "Identify the specific reason from the rejection message. Retake document photos in natural light, ensure full document is visible, and resubmit. Contact live chat for manual review if automated checks keep failing."),
        ("How long does a manual KYC review take?", "24–48 hours for most manual reviews. Contact support after 48 hours if no response — they can prioritise your case."),
        ("Can I complain to the GRAI about a KYC refusal?", "If you have submitted valid documents and the operator unreasonably refuses to verify your account, you can escalate to the GRAI. This is rare — most KYC failures are documentation quality issues."),
    ]
)

build(
    slug="can-you-use-vpn-to-bet-ireland",
    title="Can You Use a VPN to Bet in Ireland? Risks and Account Void Danger",
    desc="Using a VPN on a GRAI-licensed Irish betting site risks account closure and bet voidance. Geolocation rules, offshore risks, and what Irish law says.",
    h1="Can You Use a VPN to Bet on Irish Betting Sites?",
    page_title="VPN Betting Ireland",
    body=f"""<p class="article-intro">Using a VPN to access betting sites carries significant risks: account closure, bet voidance, and loss of funds. While using a VPN is not itself a crime in Ireland, using it to access a betting site from a blocked country, or to conceal your location, violates operator T&amp;Cs and can cost you your account and winnings. Here is a full honest assessment.</p>

<h2>Why Operators Prohibit VPNs</h2>
<p>GRAI-licensed operators are licensed to take bets from people in specific jurisdictions. If you use a VPN to appear as if you are in a different country, you may be: (a) appearing to be in a jurisdiction the operator is not licensed for, triggering compliance issues; (b) circumventing location-based restrictions the operator has applied; or (c) triggering fraud detection systems that flag IP/location mismatches.</p>
<p>Most operators explicitly state in their T&amp;Cs that VPN use is prohibited. Getting caught &mdash; via IP mismatch with KYC address, payment method location, or detection software &mdash; typically results in immediate account closure and voiding of pending bets.</p>

{cta_box()}

<h2>The Specific Risk: Bet Voidance and Fund Confiscation</h2>
<p>Operators can void all bets placed while a VPN was detected and may confiscate balances built through VPN sessions. Courts have generally upheld operator T&amp;Cs in these cases when the VPN use violated explicit terms. You have limited recourse if the T&amp;Cs you agreed to explicitly prohibit VPN use.</p>

<h2>Offshore Sites and VPNs: Double Risk</h2>
<p>Some punters use VPNs to access offshore sites that do not hold a GRAI licence. This compounds the risk: not only are you violating T&amp;Cs, but offshore sites have no GRAI oversight, no payout obligation under Irish law, and no GRAI complaints route. If an unlicensed offshore operator refuses to pay out, you have no domestic recourse.</p>

<h2>Legitimate Use Cases</h2>
<p>If you are Irish and travelling abroad and want to access your Irish betting account: some GRAI-licensed operators allow this if you have been verified with an Irish KYC. Using a VPN specifically to access your verified Irish account while temporarily abroad is a lower-risk use case, but check your operator&rsquo;s specific terms. When in Ireland, use your real connection &mdash; there is no reason to use a VPN on domestic betting sites.</p>

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px 20px;margin:24px 0">
  <strong>Related guides:</strong> <a href="is-online-betting-legal-in-ireland-2026">Is betting legal in Ireland?</a> &middot; <a href="offshore-betting-sites-ireland">Offshore betting risks</a> &middot; <a href="grai-licensed-betting-sites-ireland">GRAI-licensed bookmakers</a>
</div>
""",
    faqs=[
        ("Is it legal to use a VPN to bet in Ireland?", "Using a VPN is not illegal in Ireland. However, using it to bypass an operator's location restrictions violates T&Cs and can result in account closure and bet voidance. It is a contractual, not criminal, risk."),
        ("Can a betting site detect VPN use?", "Yes — operators use IP analysis, device fingerprinting, and payment method location matching to detect VPNs. Modern detection software flags most commercial VPNs."),
        ("What happens if a bookmaker catches me using a VPN?", "Typically: immediate account closure, voiding of pending bets, and possible confiscation of balances built during VPN sessions. The T&Cs you agreed to usually explicitly permit this."),
        ("Can I use a VPN to access an Irish betting site while abroad?", "Lower risk if your account is fully verified with an Irish KYC document. Check your specific operator's terms — some allow it, others don't. Disclose your travel to support if unsure."),
        ("Should I use a VPN to access offshore betting sites from Ireland?", "No — this doubles your risk: T&Cs violation plus no GRAI consumer protection. If an unlicensed site refuses to pay out, you have no domestic recourse."),
    ]
)

print("Group D done (10 pages)")

# ── GROUP E: Odds and markets (10 pages) ─────────────────────────────────

build(
    slug="why-are-odds-different-on-different-sites",
    title="Why Are Odds Different on Different Betting Sites? Margin and Trading Explained",
    desc="Odds vary between Irish bookmakers because of different margins, trading team judgements, and liquidity. How to find the best price and what the difference actually costs you.",
    h1="Why Are Odds Different on Different Betting Sites?",
    page_title="Why Odds Differ Between Bookmakers",
    body=f"""<p class="article-intro">The same match can have different odds on five different Irish betting sites. This is not random &mdash; it reflects different margin policies, independent trading teams, different liquidity positions, and sometimes different strategic views. Understanding why helps you find better prices.</p>

<h2>The Main Reasons Odds Differ</h2>
<p><strong>Different margin policies:</strong> Each bookmaker builds a different overround (margin) into their markets. A bookmaker running a 4% margin on Premier League football will consistently offer better prices than one running 8%. Margin directly determines the edge you are fighting.</p>
<p><strong>Independent trading teams:</strong> Large bookmakers employ traders whose job is to set and move odds based on information, model outputs, and market intelligence. Two good traders can reach different fair-value estimates for the same match.</p>
<p><strong>Liability management:</strong> If a bookmaker has taken large bets on one outcome, they may shorten those odds to limit further exposure &mdash; regardless of what their model says. This creates temporary price differences.</p>
<p><strong>Liquidity:</strong> Smaller markets (League of Ireland, lower-division racing) have fewer bets, so one large wager can move odds significantly at one operator but not another.</p>

{cta_box()}

<h2>How to Find the Best Odds</h2>
<p>Use an odds comparison tool (many are available freely online) before placing any significant bet. The difference between 11/8 (2.375) and 6/4 (2.5) on a &euro;100 bet is &euro;12.50 &mdash; that is real money, and it compounds over hundreds of bets. Opening accounts at multiple GRAI-licensed bookmakers makes line shopping practical.</p>

<h2>Starting Price vs Early Price</h2>
<p>For horse racing, odds also differ between early-price markets and Starting Price (SP). Early prices can offer better value on some selections, worse on others. If you consistently take early prices and your selections shorten before the off, that is a sign you are finding value.</p>

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px 20px;margin:24px 0">
  <strong>Related guides:</strong> <a href="how-to-read-betting-odds-ireland">Reading betting odds</a> &middot; <a href="implied-probability-guide">Implied probability and value</a> &middot; <a href="bookmaker-margin-explained">Bookmaker margin explained</a>
</div>
""",
    faqs=[
        ("Why do different betting sites have different odds?", "Because of different margin policies, independent trading teams setting their own prices, liability management (shortening odds when too much is bet on one side), and different liquidity on smaller markets."),
        ("Is it worth checking odds at multiple bookmakers?", "Yes — the difference between best and worst odds across GRAI-licensed operators can be 5–15% on the same market. Over many bets, this difference is significant."),
        ("Do GRAI rules require bookmakers to offer fair odds?", "No — GRAI rules do not mandate specific odds levels. Operators set prices commercially. The GRAI focuses on consumer protection and responsible gambling, not odds regulation."),
        ("Why do bookmakers sometimes shorten odds quickly?", "Liability management — if one side of a market is heavily bet, the bookmaker reduces those odds to discourage further bets. This protects their position but can create value on the now-shorter side for the sharp punter."),
        ("What is an odds comparison tool?", "A tool that shows the same market at multiple bookmakers simultaneously, ranked from best to worst price. Free tools exist online. Essential for anyone placing significant regular bets."),
    ]
)

build(
    slug="what-does-evens-mean-betting",
    title="What Does Evens Mean in Betting? 1/1, 2.0 Decimal Explained",
    desc="Evens means a 50% implied probability — you win the same as your stake. How 1/1 fractional, 2.0 decimal and +100 American odds all mean the same thing.",
    h1="What Does Evens Mean in Betting? A Plain-English Explanation",
    page_title="Evens Betting Explained",
    body=f"""<p class="article-intro">Evens &mdash; also written as 1/1 (fractional), 2.0 (decimal), or +100 (American) &mdash; means you win exactly the same amount as your stake if the bet is successful. A &euro;10 bet at evens returns &euro;20 total (&euro;10 profit + &euro;10 stake back). Here is a complete plain-English guide.</p>

<h2>Evens in Three Formats</h2>
<div class="comparison-table" style="overflow-x:auto;margin:20px 0">
  <table>
    <thead><tr><th>Format</th><th>Expression</th><th>Return on €10 stake</th></tr></thead>
    <tbody>
      <tr><td>Fractional (UK/Ireland)</td><td>1/1</td><td>€20 (€10 profit + €10 stake)</td></tr>
      <tr><td>Decimal (European)</td><td>2.0</td><td>€20 (stake &times; 2.0)</td></tr>
      <tr><td>American (moneyline)</td><td>+100</td><td>€110 ... wait, that is +100% profit on $100</td></tr>
    </tbody>
  </table>
</div>
<p>American +100 means you profit $100 on a $100 bet, which is exactly evens. Total return: $200. All three formats express the same thing: equal profit and equal stake.</p>

{cta_box()}

<h2>Implied Probability at Evens</h2>
<p>To convert any odds to implied probability: <strong>1 &divide; decimal odds &times; 100</strong>. At 2.0: 1 &divide; 2.0 &times; 100 = 50%. Pure evens implies the bookmaker believes (or is pricing as if they believe) there is a 50% chance of this outcome. In practice, the market includes a margin, so a 50% chance event will typically be priced slightly below 2.0 at most bookmakers.</p>

<h2>Near-Evens: Odds-On vs Odds-Against</h2>
<p>Anything below evens (e.g., 4/5, 1.80, -125) is &ldquo;odds-on&rdquo; &mdash; you must stake more than you will profit. Anything above evens (e.g., 11/10, 2.10, +110) is &ldquo;odds-against&rdquo; &mdash; you will profit more than you stake. Evens is the crossover point.</p>

<h2>Free Bets and the Evens Requirement</h2>
<p>Many free bet and welcome offers require minimum odds of evens (2.0 decimal / 1/1 fractional) for qualifying bets. This is because odds-on bets return less profit and reduce the amount the operator effectively pays out in bonus value. Always check the minimum odds stated in any bonus T&amp;Cs.</p>

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px 20px;margin:24px 0">
  <strong>Related guides:</strong> <a href="how-to-read-betting-odds-ireland">Reading betting odds</a> &middot; <a href="implied-probability-guide">Implied probability</a> &middot; <a href="odds-converter-guide">Odds converter guide</a>
</div>
""",
    faqs=[
        ("What does evens mean in betting?", "Evens (1/1 fractional, 2.0 decimal, +100 American) means you profit exactly the same as your stake on a winning bet. A €20 bet at evens returns €40 total — €20 profit plus your €20 stake."),
        ("What is the implied probability of evens?", "50% — a true evens bet implies equal chances of either outcome. In practice, bookmaker margins mean an event needs a slightly higher than 50% chance to represent value at evens."),
        ("Is evens the same as 2.0 in decimal odds?", "Yes — 1/1 fractional, 2.0 decimal, and +100 American all mean the same thing: equal profit to stake."),
        ("What does odds-on mean compared to evens?", "Odds-on means your potential profit is less than your stake (e.g., 4/5 = 1.80 decimal). Odds-against means your profit exceeds your stake. Evens is the crossover point between the two."),
        ("Why do free bets require minimum odds of evens?", "Because odds-on bets return less profit. Free bet minimum odds requirements ensure customers use the bonus in a way that generates meaningful value and prevents it being used to back near-certainties."),
    ]
)

build(
    slug="what-does-sp-mean-in-horse-racing",
    title="What Does SP Mean in Horse Racing? Starting Price Explained",
    desc="SP (Starting Price) is the official odds of a horse at the moment the race starts. CSP, early price vs SP, and when to take SP vs early price in Ireland.",
    h1="What Does SP Mean in Horse Racing? Starting Price Explained",
    page_title="SP Starting Price Horse Racing",
    body=f"""<p class="article-intro">SP stands for Starting Price &mdash; the officially recorded odds of a horse at the moment a race starts. If you place a bet &ldquo;at SP&rdquo;, your bet is settled at the odds the horse is returned at the start, not the odds when you placed the bet. Here is everything Irish punters need to know about SP in 2026.</p>

<h2>How Starting Price Is Calculated</h2>
<p>In Irish horse racing, the SP is calculated by the Racing Post&rsquo;s SP reporters at the course, based on the state of the on-course betting market in the final minutes before the off. It reflects the best available price with on-course bookmakers (not the exchanges). The SP is the official price used to settle SP bets at all bookmakers.</p>

{cta_box()}

<h2>CSP: Computerised Starting Price</h2>
<p>Some bookmakers (particularly in the UK) use a Computerised Starting Price (CSP), derived from exchange prices rather than on-course reporters. CSP is generally considered a more accurate reflection of the true market price. The SP you receive may be the traditional course SP or CSP depending on your bookmaker &mdash; check the Horse Racing section of their House Rules.</p>

<h2>Early Price vs SP: Which Is Better?</h2>
<p>Early prices are often available from the previous evening or early morning for major races. If you back a horse early and it shortens to SP favourite, you have got the better of the bookmaker. If it drifts in price, SP would have been better. As a rule:</p>
<ul>
  <li>Take early price: if you believe the horse will shorten (popular, well-backed, improving form)</li>
  <li>Take SP: if you think the horse may drift or if you are following the market consensus</li>
  <li>Best Odds Guaranteed (BOG): many GRAI-licensed bookmakers offer BOG on UK and Irish racing &mdash; you get the higher of your early price or SP automatically</li>
</ul>

<h2>SP Bets and Handicap Races</h2>
<p>SP bets are placed before the market closes and do not carry odds. The final settlement price depends on market activity you cannot predict. For races where late market moves are significant (big-field handicaps, ante-post futures), SP betting carries more uncertainty.</p>

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px 20px;margin:24px 0">
  <strong>Related guides:</strong> <a href="what-does-each-way-mean-horse-racing">Each-way betting guide</a> &middot; <a href="how-to-read-betting-odds-ireland">Reading odds</a> &middot; <a href="horse-racing-betting-ireland">Horse racing betting Ireland</a>
</div>
""",
    faqs=[
        ("What does SP mean in horse racing?", "Starting Price — the official odds of a horse at the moment a race starts, based on on-course bookmaker prices. SP bets are settled at this price regardless of when you placed the bet."),
        ("Is SP different from the price when I placed my bet?", "Yes — your early price is locked in when you place it. SP is determined at the start of the race. With Best Odds Guaranteed (BOG), you get whichever is higher."),
        ("What is Best Odds Guaranteed in horse racing?", "BOG means you receive the higher of your early price or SP. If you took 10/1 and the horse starts at 12/1 SP, you receive 12/1. Many GRAI-licensed bookmakers offer BOG on UK and Irish racing."),
        ("What is CSP vs SP in horse racing?", "CSP (Computerised Starting Price) uses exchange data to calculate the starting price. Traditional SP uses on-course reporters. CSP is often considered a more accurate market price."),
        ("When should I take early price vs SP in horse racing?", "Take early price if you think the horse will shorten (or if BOG is available). Take SP if you think the horse may drift in price. BOG makes early prices risk-free on the downside."),
    ]
)

build(
    slug="what-does-each-way-mean-horse-racing",
    title="What Does Each-Way Mean in Horse Racing? Beginner's Guide with Examples",
    desc="Each-way betting splits your stake into a win bet and a place bet. How place terms work, what you win if your horse places but doesn't win, with worked examples.",
    h1="What Does Each-Way Mean in Horse Racing? A Complete Beginner's Guide",
    page_title="Each-Way Horse Racing Explained",
    body=f"""<p class="article-intro">An each-way bet is two bets in one: a win bet and a place bet. If your horse wins, both bets pay. If it places (finishes in the top 2, 3, or 4 depending on the race), you receive the place portion. If it neither wins nor places, both parts of your bet lose. Here is a plain-English explanation with worked examples.</p>

<h2>How Each-Way Betting Works</h2>
<p>When you place an each-way bet, your stake is doubled &mdash; half goes on the win, half on the place. Example: a &euro;10 each-way bet actually costs &euro;20 (&euro;10 win + &euro;10 place).</p>
<p>Place terms are set by the bookmaker before each race and determine: (1) how many places pay, and (2) the fraction of the win odds paid for a placed horse.</p>

{cta_box()}

<h2>Standard Each-Way Place Terms</h2>
<div class="comparison-table" style="overflow-x:auto;margin:20px 0">
  <table>
    <thead><tr><th>Race type</th><th>Places paid</th><th>Place fraction</th></tr></thead>
    <tbody>
      <tr><td>2–4 runners</td><td>Win only (no place)</td><td>N/A</td></tr>
      <tr><td>5–7 runners</td><td>1st and 2nd</td><td>1/4 odds</td></tr>
      <tr><td>8+ runners</td><td>1st, 2nd, 3rd</td><td>1/4 odds</td></tr>
      <tr><td>Handicap 12–15 runners</td><td>1st, 2nd, 3rd</td><td>1/4 odds</td></tr>
      <tr><td>Handicap 16+ runners</td><td>1st, 2nd, 3rd, 4th</td><td>1/4 odds</td></tr>
    </tbody>
  </table>
</div>

<h2>Worked Example</h2>
<p>&euro;10 each-way on a horse at 10/1 in a 10-runner race (1/4 odds, 3 places). Total stake: &euro;20.</p>
<p><strong>Horse wins:</strong> Win part: &euro;10 &times; 10/1 = &euro;100 profit + &euro;10 stake = &euro;110. Place part: &euro;10 &times; (10/1 &times; 1/4) = &euro;10 &times; 2.5/1 = &euro;25 profit + &euro;10 stake = &euro;35. <strong>Total return: &euro;145</strong> (&euro;125 profit on a &euro;20 stake).</p>
<p><strong>Horse places (2nd or 3rd but not 1st):</strong> Win part: loses (&euro;10 gone). Place part: &euro;25 profit + &euro;10 stake = &euro;35. Total return: &euro;35 on a &euro;20 stake (&euro;15 profit).</p>
<p><strong>Horse unplaced:</strong> Both parts lose. Total loss: &euro;20.</p>

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px 20px;margin:24px 0">
  <strong>Related guides:</strong> <a href="what-does-sp-mean-in-horse-racing">Starting Price guide</a> &middot; <a href="horse-racing-betting-ireland">Horse racing Ireland</a> &middot; <a href="each-way-betting-guide">Each-way full guide</a>
</div>
""",
    faqs=[
        ("What does each-way mean in betting?", "An each-way bet is two bets — a win bet and a place bet. If the horse wins, both pay. If it places (but doesn't win), only the place part pays. If it's unplaced, both bets lose."),
        ("How much does an each-way bet cost?", "Double your stated stake. A €10 each-way bet costs €20 — €10 on the win and €10 on the place."),
        ("What are place terms in each-way betting?", "Place terms define how many places pay and at what fraction of the win odds. Common: top 3 at 1/4 odds for 8+ runner races. Bookmakers set terms before each race."),
        ("Is each-way betting good value?", "It depends on the race type and odds. Each-way value is best for outsiders in big-field handicaps (16+ runners, 4 places). For short-priced favourites in small fields, an each-way bet is poor value because the place fraction adds little."),
        ("What happens if a race is void after I've placed an each-way bet?", "If the race is void, both the win and place parts of your each-way bet are voided and stakes returned. If your selected horse is a non-runner, the same applies — stakes returned."),
    ]
)

build(
    slug="how-to-read-betting-odds-ireland",
    title="How to Read Betting Odds in Ireland: Fractional, Decimal, American Explained",
    desc="Irish betting sites show odds as fractional (2/1), decimal (3.0), or American (+200). How to convert between formats, calculate returns, and find value.",
    h1="How to Read Betting Odds: Fractional, Decimal and American Explained",
    page_title="Reading Betting Odds Ireland",
    body=f"""<p class="article-intro">Odds are the language of betting, and Irish bookmakers offer three formats: fractional (the traditional Irish and UK format), decimal (increasingly default on most sites), and American (less common, used mainly for US sports). This guide explains all three, with conversion formulas and practical examples.</p>

<h2>Fractional Odds (Traditional Irish/UK Format)</h2>
<p>Fractional odds show profit relative to stake. The numerator is the profit; the denominator is the stake. So 5/2 means: stake &euro;2, profit &euro;5. Total return: &euro;7 (&euro;5 profit + &euro;2 stake back).</p>
<p><strong>Key examples:</strong> 1/2 (odds-on, profit half the stake), 1/1 (evens), 2/1 (double your stake), 5/1 (five times your stake as profit).</p>

{cta_box()}

<h2>Decimal Odds (European Format)</h2>
<p>Decimal odds show total return per unit staked, including your stake back. <strong>Total return = Stake &times; Decimal odds.</strong></p>
<p>Decimal odds of 3.0 on a &euro;10 bet: &euro;10 &times; 3.0 = &euro;30 total return (&euro;20 profit + &euro;10 stake). Note: fractional 2/1 and decimal 3.0 are identical.</p>
<p>Converting fractional to decimal: (Numerator &divide; Denominator) + 1. So 5/2 = (5 &divide; 2) + 1 = 3.5 decimal.</p>

<h2>American (Moneyline) Odds</h2>
<p>Positive (+) means profit on a $100 stake. Negative (&minus;) means how much you must stake to profit $100.</p>
<ul>
  <li>+200: stake $100, profit $200 (same as 2/1 or 3.0)</li>
  <li>&minus;200: stake $200 to profit $100 (same as 1/2 or 1.5)</li>
</ul>

<h2>Implied Probability: The Most Useful Conversion</h2>
<p>Implied probability = 1 &divide; Decimal odds &times; 100. This tells you what percentage chance the bookmaker is pricing in.</p>
<ul>
  <li>2.0 (evens): 50% implied</li>
  <li>3.0 (2/1): 33.3% implied</li>
  <li>5.0 (4/1): 20% implied</li>
  <li>10.0 (9/1): 10% implied</li>
</ul>
<p>Compare implied probability with your own assessment of likelihood. If you think there is a 40% chance of an event but it is priced at 25% (3.0), that is a value bet.</p>

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px 20px;margin:24px 0">
  <strong>Related guides:</strong> <a href="implied-probability-guide">Implied probability guide</a> &middot; <a href="odds-converter-guide">Odds converter</a> &middot; <a href="bookmaker-margin-explained">Bookmaker margin</a>
</div>
""",
    faqs=[
        ("What is the difference between fractional and decimal odds?", "Fractional odds (5/2) show profit relative to stake. Decimal odds (3.5) show total return per unit staked, including stake. They convey the same information in different formats."),
        ("How do I convert fractional odds to decimal?", "Divide the top number by the bottom, then add 1. Example: 5/2 = (5÷2) + 1 = 3.5. Or: 7/4 = (7÷4) + 1 = 2.75."),
        ("How do I calculate my return from decimal odds?", "Stake × Decimal odds = Total return (including stake). €25 × 3.5 = €87.50 total (€62.50 profit + €25 stake)."),
        ("What is implied probability in betting?", "1 ÷ Decimal odds × 100. Tells you what chance the bookmaker is pricing in. If the implied probability is lower than your own estimate, it may be a value bet."),
        ("Which odds format do Irish betting sites use by default?", "Many Irish sites default to fractional for horse racing and decimal for football, but most allow you to change the display format in account settings."),
    ]
)

build(
    slug="what-is-a-push-in-sports-betting",
    title="What Is a Push in Sports Betting? Void Bets and Handicap Pushes Explained",
    desc="A push means your bet is a tie — stake is returned. When pushes happen in spread betting, Asian handicap 0, and totals markets at GRAI-licensed Irish bookmakers.",
    h1="What Is a Push in Sports Betting?",
    page_title="Push in Sports Betting Explained",
    body=f"""<p class="article-intro">A push in sports betting occurs when the outcome exactly matches the line set by the bookmaker, resulting in neither a win nor a loss &mdash; your stake is returned. Pushes are most common in points spread betting, Asian handicap markets, and over/under totals. Here is a complete guide.</p>

<h2>When Does a Push Occur?</h2>
<p><strong>Points spread (American football, basketball):</strong> If you bet Team A &minus;3.5 and they win by exactly 3.5 (not possible with a half-point spread), it is a push. With whole-number spreads (Team A &minus;3), if they win by exactly 3, the bet pushes.</p>
<p><strong>Asian Handicap 0 (Draw No Bet):</strong> If the match ends in a draw, the bet pushes and stakes are returned. This is equivalent to Draw No Bet in European markets.</p>
<p><strong>Over/Under totals:</strong> If you bet Over 2.5 goals and the game ends 1-1 (2 goals), you lose. But with a whole-number line (Over 2 goals), a game ending 1-1 is a push &mdash; stake returned.</p>

{cta_box()}

<h2>Half-Points Eliminate Pushes</h2>
<p>Bookmakers often set lines with half-points (&minus;3.5, Over 2.5) specifically to eliminate the possibility of a push. When a half-point is included, one side must win. If you see a whole-number line, be aware that a push is possible.</p>

<h2>Pushes in Accumulators</h2>
<p>If one leg of an accumulator pushes, that leg is treated as a void/no-bet and removed from the accumulator. The remaining legs continue at adjusted odds. For example, a 4-fold acca where one leg pushes becomes a 3-fold. If all legs push, the entire stake is returned.</p>

<h2>Irish Bookmaker Rules on Pushes</h2>
<p>Under GRAI transparency requirements, operators must clearly state their rules on pushes and voids in their House Rules. Check the specific rules for each market at your operator &mdash; practices can differ between American-style and European-style markets. The standard industry practice is stake return, but always verify.</p>

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px 20px;margin:24px 0">
  <strong>Related guides:</strong> <a href="what-does-dnb-mean-betting">Draw No Bet guide</a> &middot; <a href="what-is-asian-handicap-ireland">Asian handicap guide</a> &middot; <a href="void-bets-settlement">Void bets explained</a>
</div>
""",
    faqs=[
        ("What is a push in sports betting?", "A push is when your bet ties — the result exactly matches the line. Your stake is returned and you neither win nor lose. Common in points spread and Asian handicap markets."),
        ("What happens to my bet if it pushes?", "Your stake is returned in full. No profit, no loss. If it was a leg of an accumulator, that leg is removed and the acca recalculates at adjusted odds."),
        ("Can a push happen in football betting?", "Yes — with whole-number Asian handicap lines (AH 0 = Draw No Bet, AH 1, AH 2) or whole-number over/under lines. Half-point lines (AH 0.5, Over 2.5) eliminate pushes."),
        ("Is a push the same as a void bet?", "Similar but not identical. A push is caused by the result tying the line. A void bet is usually caused by external factors (match abandoned, non-runner). Both result in stake return."),
        ("Do pushes affect accumulator odds?", "Yes — a pushed leg is removed from the acca, and odds are recalculated. A 4-fold acca with one push becomes a 3-fold at adjusted odds."),
    ]
)

build(
    slug="what-does-dnb-mean-betting",
    title="What Does DNB Mean in Betting? Draw No Bet Explained",
    desc="DNB (Draw No Bet) means if the match draws, your stake is returned. How it differs from 1X2, the implied probability maths, and when to use it.",
    h1="What Does DNB Mean in Betting? Draw No Bet Explained",
    page_title="DNB Draw No Bet Explained",
    body=f"""<p class="article-intro">DNB stands for Draw No Bet. It is a market where you back a team to win, and if the match ends in a draw, your stake is returned. Only a loss ends with you losing your money. DNB effectively removes the draw as an outcome, giving you a binary win/return scenario.</p>

<h2>How Draw No Bet Works</h2>
<p>Standard 1X2 market: back Team A, if they draw or lose you lose your stake. DNB: back Team A, if they win you win, if they draw your stake is returned, only if they lose do you lose.</p>
<p>This safety net comes at a cost: DNB odds are lower than the standard win odds, because you are buying protection against the draw.</p>

{cta_box()}

<h2>DNB vs Asian Handicap 0</h2>
<p>Draw No Bet and Asian Handicap 0 (AH 0) are mathematically identical. If a bookmaker offers AH 0 on a match, it is the same as DNB. The notation differs between European and Asian market styles, but the settlement rules are the same: draw = stake returned.</p>

<h2>Calculating the Real Value of DNB</h2>
<p>In a typical Premier League match, the draw probability is roughly 25&ndash;30%. By buying DNB odds instead of outright win odds, you are sacrificing roughly 25&ndash;30% of potential value in exchange for draw insurance.</p>
<p>Example: Team A wins at 2.0 (evens). Team A DNB at 1.60. The difference (2.0 &minus; 1.60) represents the value of the draw insurance. Whether it is worth it depends on how likely you think a draw is for this specific match.</p>

<h2>When to Use DNB</h2>
<p>DNB makes most sense when: you are confident in one team&rsquo;s quality but worried about defensive opposition that might hold for a draw; or when the win price is very short and a small extra safety net is worth the reduced return. DNB is less useful when draw probability is low (e.g., a heavy favourite against weak opposition).</p>

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px 20px;margin:24px 0">
  <strong>Related guides:</strong> <a href="what-is-asian-handicap-ireland">Asian handicap guide</a> &middot; <a href="what-does-double-chance-mean">Double chance explained</a> &middot; <a href="draw-no-bet-explained">DNB full guide</a>
</div>
""",
    faqs=[
        ("What does DNB mean in betting?", "Draw No Bet — if you back a team and the match draws, your stake is returned. Only a loss results in losing your bet. The draw is removed as a result that costs you money."),
        ("Is DNB the same as Asian Handicap 0?", "Yes — mathematically identical. AH 0 and Draw No Bet have the same settlement rules: draw = stake returned, win = win, loss = lose. The notation differs by market style."),
        ("Are DNB odds lower than outright win odds?", "Yes — because DNB includes draw insurance. The odds are lower to reflect the fact that you can't lose your stake in the event of a draw."),
        ("When should I use Draw No Bet?", "When you're confident in a team but worried about a draw. DNB reduces profit on a win but provides a safety net. Worth using when draw probability is high and the team's win margin is uncertain."),
        ("What happens to a DNB bet in an accumulator if one game draws?", "The DNB leg is treated as a void — stake for that leg is returned and it's removed from the acca. The remaining legs continue at adjusted odds."),
    ]
)

build(
    slug="what-is-asian-handicap-ireland",
    title="What Is Asian Handicap Betting? Quarter and Half Goal Lines Explained",
    desc="Asian handicap betting eliminates the draw and allows quarter-goal handicaps. How AH 0, AH 0.5, AH 0.25 and AH 0.75 work, with Irish bookmaker examples.",
    h1="What Is Asian Handicap Betting? A Complete Guide for Irish Punters",
    page_title="Asian Handicap Explained Ireland",
    body=f"""<p class="article-intro">Asian handicap (AH) betting removes the draw outcome and uses fractional goal lines to create two-way markets with better value than standard 1X2. Used heavily in football, AH is available at most GRAI-licensed Irish bookmakers. Here is how every common line works.</p>

<h2>The Four Main Asian Handicap Lines</h2>
<p><strong>AH 0 (Draw No Bet):</strong> Draw = stake returned. Only two outcomes: win or lose.</p>
<p><strong>AH 0.5 (Half-goal handicap):</strong> No push possible. If you back Team A &minus;0.5, they must win by at least 1 goal. If they draw, you lose.</p>
<p><strong>AH 0.25 (Quarter-goal handicap):</strong> Your stake is split across AH 0 and AH 0.5. If Team A draws, half stake is returned (the AH 0 portion) and half loses (the AH 0.5 portion). Result: half your stake back on a draw.</p>
<p><strong>AH 0.75 (Three-quarter goal handicap):</strong> Stake split across AH 0.5 and AH 1. If Team A wins by exactly 1 goal, half wins and half pushes (returned). Win by 2+: full win.</p>

{cta_box()}

<h2>Why Use Asian Handicap Over 1X2?</h2>
<p>Bookmaker margins on 1X2 markets are typically 5&ndash;8% because there are three outcomes. AH markets have only two outcomes, so margins are typically 2&ndash;4%. Lower margin = better odds for punters. For regular football bettors, switching to AH on suitable matches can meaningfully improve long-term returns.</p>

<h2>Reading AH Odds at Irish Bookmakers</h2>
<p>AH odds are shown in decimal format. If Manchester City are &minus;1.0 AH at 1.95, and Arsenal are +1.0 at 1.95: City must win by 2+ for the City AH bet to win. City winning by exactly 1 goal = push (stake returned). Arsenal holding to a loss of 1 or less = Arsenal AH wins.</p>

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px 20px;margin:24px 0">
  <strong>Related guides:</strong> <a href="what-does-dnb-mean-betting">DNB guide</a> &middot; <a href="what-does-double-chance-mean">Double chance</a> &middot; <a href="asian-handicap-explained">Full Asian handicap guide</a>
</div>
""",
    faqs=[
        ("What is Asian handicap betting?", "A form of football betting that removes the draw and uses fractional goal lines. Asian handicap creates two-way markets with lower bookmaker margins than standard 1X2."),
        ("What does AH 0 mean?", "Asian Handicap 0 = Draw No Bet. If the match draws, your stake is returned. Only a win or loss ends the bet in profit or loss."),
        ("What is a quarter-goal Asian handicap?", "Your stake is split between two half-goal lines. AH 0.25 splits between AH 0 and AH 0.5. On a draw, the AH 0 portion returns and the AH 0.5 portion loses — net result: half stake returned."),
        ("Are Asian handicap margins lower than standard football markets?", "Yes — AH has two outcomes vs three for 1X2. This typically means margins of 2–4% vs 5–8% for 1X2. Lower margin means better value for the punter over time."),
        ("Do all GRAI-licensed bookmakers offer Asian handicap?", "Most do, particularly on major football leagues. Coverage of Asian handicap on smaller markets (League of Ireland, lower divisions) is more variable."),
    ]
)

build(
    slug="what-does-double-chance-mean",
    title="What Does Double Chance Mean in Betting? 1X, X2, 12 Explained",
    desc="Double chance covers two of three possible results in one bet. How 1X, X2, and 12 work, implied probability maths, and when double chance makes sense.",
    h1="What Does Double Chance Mean in Betting?",
    page_title="Double Chance Betting Explained",
    body=f"""<p class="article-intro">Double chance allows you to cover two of the three possible football outcomes (home win, draw, away win) in a single bet. The trade-off for this safety is lower odds. Here is exactly how the three double-chance options work, with the implied probability maths.</p>

<h2>The Three Double Chance Options</h2>
<ul>
  <li><strong>1X (Home Win or Draw):</strong> Your bet wins if the home team wins or the match draws. Loses only if the away team wins.</li>
  <li><strong>X2 (Draw or Away Win):</strong> Your bet wins if the away team wins or the match draws. Loses only if the home team wins.</li>
  <li><strong>12 (Home Win or Away Win):</strong> Your bet wins if either team wins. Loses only on a draw.</li>
</ul>

{cta_box()}

<h2>Implied Probability of Double Chance Outcomes</h2>
<p>Double chance implied probability = sum of the two covered outcomes&rsquo; individual implied probabilities. If home win = 50%, draw = 25%, away win = 25%:</p>
<ul>
  <li>1X implied: 50% + 25% = 75%</li>
  <li>X2 implied: 25% + 25% = 50%</li>
  <li>12 implied: 50% + 25% = 75%</li>
</ul>
<p>At these probabilities, 1X and X2 at 75% would be priced around 1.33 decimal. 12 at 75% around 1.33. The bookmaker&rsquo;s margin means actual prices are slightly lower.</p>

<h2>When Does Double Chance Make Sense?</h2>
<p>Double chance is most useful when you are confident a certain outcome will not happen, but are less sure between the other two. It is a popular market for:</p>
<ul>
  <li>Away underdogs where you want draw or away win (X2 on a solid travelling side)</li>
  <li>Eliminating the draw risk when backing a heavy favourite (1X provides more insurance than DNB at lower odds)</li>
  <li>Both teams competitive, one clear winner expected but draw remains possible (12)</li>
</ul>

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px 20px;margin:24px 0">
  <strong>Related guides:</strong> <a href="what-does-dnb-mean-betting">Draw No Bet vs Double Chance</a> &middot; <a href="what-is-asian-handicap-ireland">Asian handicap guide</a> &middot; <a href="how-to-read-betting-odds-ireland">Reading odds</a>
</div>
""",
    faqs=[
        ("What does double chance mean in betting?", "Double chance covers two of the three football outcomes (home win/draw/away win) in one bet. 1X = home or draw, X2 = draw or away, 12 = home or away win."),
        ("What is the difference between double chance and Draw No Bet?", "Draw No Bet (DNB) covers only the win outcome and returns stake on a draw. Double chance 1X covers win AND draw — it doesn't return stake on draw, it wins. 1X double chance odds are slightly lower than DNB odds."),
        ("Is double chance good value?", "It can be — particularly X2 on a strong away team where you want to cover both win and draw. But double chance by definition has lower odds than a single outcome, so you need to be confident the excluded result won't happen."),
        ("Can I use double chance in an accumulator?", "Yes — double chance legs can be added to accas. Each leg must win for the acca to pay out. If a double chance leg pushes or ties (not applicable — DC always has a winner or loser), it is treated normally."),
        ("What does 1X mean in betting?", "Home win or draw — the 1X double chance option wins if the home team wins or the match ends in a draw. It loses only if the away team wins."),
    ]
)

build(
    slug="what-is-a-nap-in-horse-racing",
    title="What Is a NAP in Horse Racing? Tipster Terms Nap, NB and E/W Explained",
    desc="A NAP is a tipster's best bet of the day. How nap, nb, e/w and each-way selections work in Irish racing tips, and how to use tipster terms.",
    h1="What Is a NAP in Horse Racing Tipping?",
    page_title="NAP Horse Racing Explained",
    body=f"""<p class="article-intro">NAP is a tipster&rsquo;s best bet of the day &mdash; their single most confident selection. The term comes from the card game Napoleon, where &ldquo;going nap&rdquo; means staking everything on one hand. Understanding tipster terminology helps you interpret any form guide or racing column you read.</p>

<h2>NAP: The Banker Selection</h2>
<p>A tipster&rsquo;s NAP is their highest-confidence pick for the day &mdash; not necessarily an odds-on favourite, just the selection they are most confident about. In a column listing four or five selections, the NAP is the one they consider most likely to win at fair value.</p>

{cta_box()}

<h2>NB: Next Best</h2>
<p>NB stands for Next Best &mdash; the tipster&rsquo;s second most confident selection. If you are following a tipster, the NB is the first choice after the NAP. Some tipsters provide NAP + NB daily; others provide more context in their write-up.</p>

<h2>E/W: Each-Way</h2>
<p>When a tipster marks a selection as E/W (each-way), they are recommending the selection specifically as an each-way bet rather than a straight win bet. This typically applies to longer-priced horses in big-field handicaps where a place finish is a realistic target. The tipster believes the horse has each-way value: a decent chance of placing at odds that make the place portion worthwhile.</p>

<h2>How to Use Tipster Columns</h2>
<p>Reading Irish racing columns (Racing Post, Irish Racing, national newspapers): the NAP and NB are the most reliable signals of the tipster&rsquo;s confidence. E/W marks suggest the horse is worth the each-way bet but should not be backed to win at the stated odds. Following any tipster blindly is not recommended &mdash; use their selections as one input alongside your own form analysis.</p>

<h2>NAP Competition Tables</h2>
<p>Some publications run NAP competition tables throughout the season, tracking which tipster&rsquo;s NAPs have the best win record and profit/loss. These tables are a useful guide to consistent performance &mdash; though past form does not guarantee future results.</p>

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px 20px;margin:24px 0">
  <strong>Related guides:</strong> <a href="what-does-each-way-mean-horse-racing">Each-way guide</a> &middot; <a href="horse-racing-betting-ireland">Horse racing betting Ireland</a> &middot; <a href="horse-racing-form-guide">Reading racing form</a>
</div>
""",
    faqs=[
        ("What does NAP mean in horse racing?", "NAP is a tipster's best bet of the day — their most confident selection. The term comes from the card game Napoleon. It indicates the tipster's highest-confidence pick, not necessarily the shortest-priced horse."),
        ("What is the difference between NAP and NB in racing tips?", "NAP is the tipster's top selection (best bet). NB (Next Best) is their second-strongest pick. Both are worth noting if you follow a specific tipster's column."),
        ("What does E/W mean next to a racing selection?", "Each-way — the tipster recommends backing this horse each-way (win and place) rather than on the win only. Usually signals a longer-priced horse with realistic place chances in a big-field race."),
        ("Should I always follow a tipster's NAP?", "Not blindly — use NAP selections as one input alongside your own form reading. Even the best tipsters have win rates of 30–40% on their NAPs. Always check the horse's form, ground, and trainer/jockey record yourself."),
        ("What is a NAP competition in horse racing?", "A competition where multiple tipsters submit their daily NAP, and performance is tracked over a season. Tables show win rates, strike rates, and profit/loss to level stakes. Useful for identifying consistently accurate tipsters."),
    ]
)

print("Groups D and E done (20 pages)")
