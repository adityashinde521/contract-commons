---
title: "Tokenisation, stablecoins and regulation"
module: 12
order: 3
kind: "lesson"
minutes: "45 min"
legacy: "F6"
problem: "A bank wants to issue a tokenised bond to EU clients. Which rules apply, and what does the token actually give the holder?"
---

## Problem

<div class="cc-callout cc-callout--problem"><div><b>The question.</b> A bank wants to issue a tokenised bond to EU clients. Which rules apply, and what does the token actually give the holder?</div></div>

## Concept

<div class="goal"><b>Goal:</b> you can explain where real money now moves on chain, and which rules apply.</div>
    <h4>Tokenised real-world assets (RWA)</h4>
    <ul>
      <li>Bonds, fund shares and treasuries are issued as tokens. Tokenised real-world assets (excluding stablecoins) were worth about <b>$46 billion</b> in November 2026. Tokenised US treasuries (about $13 billion) are still the largest single category, but no longer the majority: private credit and funds are growing fast.</li>
      <li>Benefits: settlement in minutes, 24/7 trading, fractional ownership, programmable compliance (only verified investors can hold the token).</li>
    </ul>
    <h4>Stablecoins and rules</h4>
    <div class="tw"><table>
      <tr><th>Rule</th><th>Status</th><th>Effect</th></tr>
      <tr><td>EU MiCA</td><td>Fully applies since 30 Dec 2024. Transitional period ended 1 July 2026.</td><td>Crypto service providers need a MiCA licence to serve EU clients. Non-compliant stablecoins were delisted on EU exchanges.</td></tr>
      <tr><td>US GENIUS Act</td><td>Signed July 2025. The OCC issued the first final implementing rule on 21 Oct 2026; the Act takes effect on 18 Jan 2027 at the latest.</td><td>First US federal framework for payment stablecoins, with anti-money-laundering duties.</td></tr>
      <tr><td>EU DLT Pilot Regime</td><td>Since 2023</td><td>Test environment for trading and settling tokenised securities.</td></tr>
      <tr><td>EU AML package</td><td>Applies from July 2027</td><td>Stricter anti-money-laundering rules and a new EU AML authority.</td></tr>
    </table></div>
    <div class="callout law"><h5>Questions to answer</h5><ul>
      <li>Is a token a financial instrument (MiFID II) or a crypto-asset (MiCA)? The Commission is reviewing gaps between the two.</li>
      <li>Does a token give legal ownership of the bond, or only a claim against the issuer?</li>
      <li>Can MiCA apply to a fully decentralised protocol with no intermediary?</li>
    </ul></div>
    <div class="callout lab"><h5>Connect to the labs</h5><p><a href="/lessons/lab-course-token/">5.2 Course token</a> CourseToken is a starting point. Add an allow-list so only “verified investors” can receive tokens: programmable compliance in about ten lines of code.</p></div>

<!-- deep:start -->
### In depth

<p>Regulation looks at what a token <i>does</i>, not what it is called. The first test in the EU is whether a token is a <b>financial instrument</b> under MiFID II, for example because it gives a share of profits or a claim like a bond. Then securities law applies, including prospectus rules; the DLT Pilot Regime allows special market infrastructure for such tokens. If it is not a financial instrument, <b>MiCA</b> (Markets in Crypto-Assets Regulation) applies to most other crypto-assets. MiCA distinguishes <b>e-money tokens</b> (EMT, referencing one official currency, such as a euro stablecoin), <b>asset-referenced tokens</b> (ART, referencing a basket or other assets), and other crypto-assets, such as utility tokens. Truly unique NFTs and fully decentralised services are largely outside MiCA.</p>
<p>MiCA places duties on two groups. <b>Issuers</b> must publish a white paper, and stablecoin issuers need authorisation and reserves. <b>Crypto-asset service providers</b> (CASPs) such as exchanges and custodians need a licence; the transition period ended on 1 July 2026. Anti-money-laundering rules add the travel rule for transfers and, from July 2027, the new EU AML Regulation. The GDPR applies to any personal data on or off chain. In the US, the GENIUS Act (July 2025) created a federal framework for payment stablecoins.</p>
<p>Code can help with compliance (<b>programmable compliance</b>): allow-lists of verified holders, transfer limits, pause functions for court orders. But each such feature also gives someone power over users, which must be disclosed and controlled.</p>

### Worked example

<div class="worked">
<p><b>Case:</b> classify three tokens step by step (simplified; not legal advice).</p>
<div class="tw"><table>
  <tr><th>Token</th><th>Financial instrument?</th><th>Under MiCA</th><th>Main duty</th></tr>
  <tr><td>A token that pays holders 5% of a company’s profits</td><td>Likely yes (transferable security)</td><td>Not MiCA</td><td>Prospectus, securities law</td></tr>
  <tr><td>A euro stablecoin redeemable 1:1</td><td>No</td><td>E-money token</td><td>Issuer must be a credit or e-money institution; white paper</td></tr>
  <tr><td>CourseToken that gives access to workshops</td><td>No</td><td>Other crypto-asset (utility)</td><td>White paper if offered to the public above thresholds</td></tr>
</table></div>
</div>

### Common mistakes

<ul>
  <li>“Calling it a utility token avoids securities law.” The economic rights decide, not the label.</li>
  <li>“MiCA regulates all of DeFi.” Fully decentralised services are largely outside it; the question of who is a service provider is still debated.</li>
</ul>
<!-- deep:end -->

### Watch and read

<div class="vids">
      <a class="vid read" href="https://www.esma.europa.eu/esmas-activities/digital-finance-and-innovation/markets-crypto-assets-regulation-mica" target="_blank" rel="noopener"><span class="play"></span><span><b>MiCA official page</b><small>ESMA</small></span></a>
      <a class="vid read" href="https://stablecoininsider.org/stablecoin-regulations-in-2026/" target="_blank" rel="noopener"><span class="play"></span><span><b>Stablecoin regulations in 2026: GENIUS Act and MiCA</b><small>Overview article</small></span></a>
    </div>

## Try it

<p>On <a href="https://defillama.com" target="_blank" rel="noopener">DefiLlama</a>, find the real-world assets (RWA) category and the stablecoins page. Note the three largest of each and who issues them.</p>

## Apply

<div class="aud"><div class="cs"><h5>Technology lens</h5><ul><li>Add an investor allow-list to the <a href="/lessons/lab-course-token/">5.2 Course token</a>.</li></ul></div><div class="bi"><h5>Business lens</h5><ul><li>Write the business case for a tokenised bond.</li></ul></div><div class="lw"><h5>Law lens</h5><ul><li>Is the token a financial instrument or a crypto-asset under MiCA?</li></ul></div></div>

## Ship

<p>Write three sentences in your lab log: the main idea, one example for each lens (technology, business, law), and one open question. Then take the quiz below.</p>
