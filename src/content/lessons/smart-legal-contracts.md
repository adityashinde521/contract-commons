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
<tr><td>Natural language, performed by code</td><td>In the text; code only performs some obligations</td><td>A lease whose deposit is held by the L3 contract</td></tr>
<tr><td>Hybrid</td><td>Some terms in text, some only in code</td><td>Escrow terms plus the contract address and its rules</td></tr>
<tr><td>Code only</td><td>Entirely in code</td><td>Trading on a DEX by calling its contract</td></tr>
</table></div>
<h3>Design patterns</h3>
<ul>
<li><b>Ricardian contract:</b> the legal text and the code are linked by a hash, so each points to the exact other.</li>
<li><b>Template languages:</b> the Accord Project (lab G6) separates the data model, the text and the logic. Catala writes statutes as code; Lexon reads like plain English; Stipula (research, 2025) imports mandatory rules such as consumer protection.</li>
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

### Watch and read

<div class="vids">
<a class="vid read" href="https://www.lawcom.gov.uk/project/smart" target="_blank" rel="noopener"><span class="play"></span><span><b>Smart legal contracts: advice to government</b><small>UK Law Commission, 2021</small></span></a>
<a class="vid read" href="https://accordproject.org" target="_blank" rel="noopener"><span class="play"></span><span><b>Accord Project</b><small>Open-source smart legal contract templates</small></span></a>
<a class="vid read" href="https://catala-lang.org" target="_blank" rel="noopener"><span class="play"></span><span><b>Catala</b><small>A language for law as code</small></span></a>
<a class="vid read" href="https://doi.org/10.1016/j.clsr.2025.106223" target="_blank" rel="noopener"><span class="play"></span><span><b>Integration of statutory norms in computable contracts (Stipula)</b><small>Computer Law &amp; Security Review, 2025</small></span></a>
</div>

## Try it

<p>Write a one-page smart legal contract for the laptop sale in lab L2: parties, price, the contract address, which clauses the code performs, a precedence clause and a dispute clause. Mark each clause “in code”, “partly in code” or “not in code”.</p>

## Apply

<div class="aud"><div class="cs"><h5>Computer science</h5><ul><li>How would you embed the hash of the legal text in the Escrow?</li></ul></div><div class="bi"><h5>Business informatics</h5><ul><li>Which contract types in a company are good candidates for templates?</li></ul></div><div class="lw"><h5>Law</h5><ul><li>Under German law, can a party contest a declaration made by clicking a contract function (§119 BGB, mistake)?</li></ul></div></div>

## Ship

<ul class="outc"><li>You can name the three forms of smart legal contracts.</li><li>You can apply the six-point checklist.</li><li>You can write a precedence clause.</li></ul>
