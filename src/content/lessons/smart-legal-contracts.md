---
title: "Smart legal contracts"
module: 12
order: 2
kind: "lesson"
minutes: "40 min"
problem: "A law firm wants contracts that a court can read and a computer can perform. How do you write one, and which version wins if they disagree?"
---

## Problem

<div class="cc-callout cc-callout--problem"><div><b>The question.</b> A law firm wants contracts that a court can read and a computer can perform. How do you write one, and which version wins if they disagree?</div></div>

## Concept

<h3>Three forms (UK Law Commission, 2021)</h3>
<div class="tw"><table>
<tr><th>Form</th><th>Where the terms are</th><th>Example</th></tr>
<tr><td>Natural language, performed by code</td><td>In the text; code only performs some obligations</td><td>A lease whose deposit is held by the <a href="/lessons/lab-rental-deposit/">4.4 Rental deposit</a> contract</td></tr>
<tr><td>Hybrid</td><td>Some terms in text, some only in code</td><td>Escrow terms plus the contract address and its rules</td></tr>
<tr><td>Code only</td><td>Entirely in code</td><td>Trading on a DEX by calling its contract</td></tr>
</table></div>
<h3>Design patterns</h3>
<ul>
<li><b>Ricardian contract:</b> the legal text and the code are linked by a hash, so each points to the exact other.</li>
<li><b>Template languages:</b> the Accord Project (lab <a href="/lessons/lab-accord/">12.4 Accord Project</a>) separates the data model, the text and the logic. Catala writes statutes as code; Lexon reads like plain English; Stipula (research, 2025) imports mandatory rules such as consumer protection.</li>
<li><b>Precedence clause:</b> the text says which version prevails if text and code disagree, and how errors are corrected.</li>
</ul>
<h3>Checklist for a smart legal contract</h3>
<ol>
<li>Who are the parties, beyond their addresses?</li>
<li>Which obligations does the code perform, and which remain human?</li>
<li>What happens if the code has a bug, or an oracle is wrong?</li>
<li>Can the contract be ended, paused or corrected? By whom? (EU Data Act, Article 36, requires safe termination for data-sharing smart contracts.)</li>
<li>Which law and which court apply?</li>
<li>How are consumer rights and mandatory law respected?</li>
</ol>

<!-- deep:start -->
### In depth

<p>A <b>smart legal contract</b> is a legally binding contract in which some or all obligations are expressed or performed by code. The UK Law Commission (2021) described three forms. In the <b>natural-language</b> form, the legal text is the contract and code only performs parts of it. In the <b>hybrid</b> form, some terms are in text and some in code, and both are part of the agreement. In the <b>code-only</b> form, the code itself is the whole agreement, which raises hard questions about how parties can understand and prove what they agreed.</p>
<!-- diagram:slc-spectrum -->
<figure class="dg"><div class="sv"><svg viewBox="0 0 720 210" role="img" aria-label="Three forms of smart legal contracts" xmlns="http://www.w3.org/2000/svg"><defs><marker id="ah-threeformsofsmartleg-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="m-a" d="M0 0L10 5L0 10z"/></marker><marker id="ah-threeformsofsmartleg-ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="m-ar" d="M0 0L10 5L0 10z"/></marker><marker id="ah-threeformsofsmartleg-ag" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="m-ag" d="M0 0L10 5L0 10z"/></marker><marker id="ah-threeformsofsmartleg-am" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="m-am" d="M0 0L10 5L0 10z"/></marker></defs><rect class="k-law" x="20" y="30" width="210" height="90" rx="12"/><text class="tb" x="125.0" y="61.2" text-anchor="middle" font-size="13.5">Natural language</text><text class="t" x="125.0" y="79.7" text-anchor="middle" font-size="13.5">text is the contract</text><text class="t" x="125.0" y="98.2" text-anchor="middle" font-size="13.5">code performs parts</text><rect class="k-bi" x="255" y="30" width="210" height="90" rx="12"/><text class="tb" x="360.0" y="61.2" text-anchor="middle" font-size="13.5">Hybrid</text><text class="t" x="360.0" y="79.7" text-anchor="middle" font-size="13.5">some terms in text,</text><text class="t" x="360.0" y="98.2" text-anchor="middle" font-size="13.5">some in code</text><rect class="k-cs" x="490" y="30" width="210" height="90" rx="12"/><text class="tb" x="595.0" y="61.2" text-anchor="middle" font-size="13.5">Code only</text><text class="t" x="595.0" y="79.7" text-anchor="middle" font-size="13.5">the code is</text><text class="t" x="595.0" y="98.2" text-anchor="middle" font-size="13.5">the agreement</text><line class="k-a" x1="40" y1="150" x2="680" y2="150" marker-end="url(#ah-threeformsofsmartleg-a)"/><text class="tl" x="360.0" y="142.0" text-anchor="middle" font-size="12.5">more of the agreement lives in code →</text><text class="tl" x="360" y="190" text-anchor="middle" font-size="13">Always answer in writing: which version prevails, and who can pause or end the code?</text></svg></div><figcaption><b>From text to code.</b> The UK Law Commission (2021) describes three forms. The further right, the harder it is for people to read, prove and challenge what they agreed.</figcaption></figure>
<p>Template systems connect text and code in a disciplined way. The Accord Project separates three parts: the <b>text</b> with variables (“The buyer pays {{price}}”), the <b>model</b> that defines the type of each variable, and the <b>logic</b> that computes results such as late fees. Each deal fills in the <b>data</b>. Because text and logic use the same variables, they cannot drift apart for those values. Research languages such as Catala (statutes as code) and Stipula (contracts that import statutory rules) go further.</p>
<p>Whatever the tool, a good smart legal contract answers in writing what happens when things go wrong: which version prevails if text and code differ, who can pause or end the code, how disputes are resolved, and how outside facts are proved. The EU Data Act (Article 36) already requires that smart contracts used for data-sharing agreements can be safely terminated or interrupted.</p>

### Worked example

<div class="worked">
<p><b>Case:</b> write a clause for the laptop Escrow in the hybrid form.</p>
<blockquote><p>“§4 Release. When the Buyer or the Arbiter confirms delivery by calling <code>confirmDelivery()</code> on the contract at address 0x…, the Price held in escrow is released to the Seller. In case of conflict between this text and the code, this text prevails, and the Arbiter shall correct the outcome.”</p></blockquote>
<ul>
  <li><b>Text:</b> names the parties, the action, the address and a priority rule.</li>
  <li><b>Code:</b> <code>require(msg.sender == buyer || msg.sender == arbiter)</code>.</li>
  <li><b>Gap closed:</b> if the code had a bug and released to the wrong party, the text gives a legal basis to claim it back, and names who acts.</li>
</ul>
</div>

### Common mistakes

<ul>
  <li>“The code always wins.” The parties can agree the opposite, and courts will look at what they really agreed.</li>
  <li>“Templates are only for lawyers.” They are a shared specification for lawyers, analysts and developers.</li>
</ul>
<!-- deep:end -->

### Watch and read

<div class="vids">
<a class="vid read" href="https://www.lawcom.gov.uk/project/smart" target="_blank" rel="noopener"><span class="play"></span><span><b>Smart legal contracts: advice to government</b><small>UK Law Commission, 2021</small></span></a>
<a class="vid read" href="https://accordproject.org" target="_blank" rel="noopener"><span class="play"></span><span><b>Accord Project</b><small>Open-source smart legal contract templates</small></span></a>
<a class="vid read" href="https://catala-lang.org" target="_blank" rel="noopener"><span class="play"></span><span><b>Catala</b><small>A language for law as code</small></span></a>
<a class="vid read" href="https://doi.org/10.1016/j.clsr.2025.106223" target="_blank" rel="noopener"><span class="play"></span><span><b>Integration of statutory norms in computable contracts (Stipula)</b><small>Computer Law &amp; Security Review, 2025</small></span></a>
</div>

## Try it

<p>Write a one-page smart legal contract for the laptop sale in lab <a href="/lessons/lab-escrow/">4.3 Escrow</a>: parties, price, the contract address, which clauses the code performs, a precedence clause and a dispute clause. Mark each clause “in code”, “partly in code” or “not in code”.</p>

## Apply

<div class="aud"><div class="cs"><h5>Technology lens</h5><ul><li>How would you embed the hash of the legal text in the Escrow?</li></ul></div><div class="bi"><h5>Business lens</h5><ul><li>Which contract types in a company are good candidates for templates?</li></ul></div><div class="lw"><h5>Law lens</h5><ul><li>Under German law, can a party contest a declaration made by clicking a contract function (§119 BGB, mistake)?</li></ul></div></div>

## Ship

<ul class="outc"><li>You can name the three forms of smart legal contracts.</li><li>You can apply the six-point checklist.</li><li>You can write a precedence clause.</li></ul>
