---
title: "Law and business lens"
module: 12
order: 1
kind: "lesson"
minutes: "60 min"
legacy: "T10"
problem: "A smart contract paid the seller, then a court says the sale was void. Who wins: the code or the law?"
---

## Problem

<div class="cc-callout cc-callout--problem"><div><b>The question.</b> A smart contract paid the seller, then a court says the sale was void. Who wins: the code or the law?</div></div>

## Concept

<div class="goal"><b>Goal:</b> you can discuss smart contracts in legal and business terms.</div>
    <h4>Smart contract versus legal contract</h4>
    <ul>
      <li>A <b>legal contract</b> is a binding agreement: offer, acceptance and intention to be bound (in German law: two matching declarations of intent, §§145 ff. BGB).</li>
      <li>A <b>smart contract</b> is code that performs actions. Code alone does not prove an agreement.</li>
      <li>A <b>smart legal contract</b> is a binding contract where code defines or performs some or all obligations.</li>
      <li>The UK Law Commission (2021) found that existing English law can support smart legal contracts. Three forms: natural-language text performed by code, hybrid, and code only. Open issues: deeds and jurisdiction.</li>
      <li>A <b>Ricardian contract</b> links a human-readable legal text to the code, often through a hash of the text (<a href="/lessons/lab-attestations/">9.4 Attestations</a>, <a href="/lessons/lab-accord/">12.4 Accord Project</a>).</li>
    </ul>
    <h4>Seven legal questions</h4>
    <div class="tw"><table>
      <tr><th>Problem</th><th>Example</th><th>Where in the labs</th></tr>
      <tr><td>Identity and capacity</td><td>An address is a pseudonym. Is the party a company, a person, a minor?</td><td><a href="/lessons/lab-simple-storage/">3.5 SimpleStorage</a>, <a href="/lessons/lab-safe/">11.3 Safe</a>, <a href="/lessons/lab-aragon/">11.4 Aragon DAO</a></td></tr>
      <tr><td>Error, fraud, rescission</td><td>The law cancels a contract, but the on-chain payment cannot be reversed.</td><td><a href="/lessons/lab-escrow/">4.3 Escrow</a>, <a href="/lessons/lab-phalcon/">7.5 Phalcon</a></td></tr>
      <tr><td>Interpretation</td><td>Text and code say different things. Which wins?</td><td><a href="/lessons/lab-accord/">12.4 Accord Project</a></td></tr>
      <tr><td>Oracles</td><td>Who is liable if the oracle reports a wrong delivery date?</td><td><a href="/lessons/lab-escrow/">4.3 Escrow</a></td></tr>
      <tr><td>GDPR</td><td>Right to erasure versus immutable storage. Store hashes, not personal data.</td><td><a href="/lessons/lab-document-registry/">4.5 Document registry</a>, <a href="/lessons/lab-attestations/">9.4 Attestations</a></td></tr>
      <tr><td>Jurisdiction</td><td>Nodes are in many countries. Which court and which law apply?</td><td><a href="/capstone/">Capstone</a></td></tr>
      <tr><td>Mandatory law</td><td>Consumer or tenancy rules override the code.</td><td><a href="/lessons/lab-rental-deposit/">4.4 Rental deposit</a></td></tr>
    </table></div>
    <h4>EU notes</h4>
    <ul>
      <li><b>EU Data Act</b> (Regulation 2023/2854, Article 36): requirements for smart contracts that perform data-sharing agreements, for example access control, safe termination or interruption, and archiving.</li>
      <li><b>MiCA</b> regulates the issue of many crypto-assets and the services around them in the EU (<a href="/lessons/regulation/">12.3 Regulation</a>).</li>
      <li><b>eIDAS 2.0</b>: electronic signatures and the EU Digital Identity Wallet (<a href="/lessons/zero-knowledge/">10.3 Zero knowledge</a>).</li>
    </ul>
    <h4>Business informatics view</h4>
    <ul>
      <li>A smart contract is a <b>process automation</b> tool: a business process written as a state machine.</li>
      <li>Value: fewer intermediaries, fast settlement, audit trail, 24/7 operation. Cost: gas, audits, no easy changes, integration with ERP systems.</li>
      <li>Good fit: many parties with low trust and clear digital rules. Bad fit: one trusted operator, private data, human judgment.</li>
    </ul>

<!-- deep:start -->
### In depth

<p>Lawyers and developers use the word “contract” differently. In law, a contract is a binding agreement formed by offer and acceptance; it creates rights and duties that courts enforce. A smart contract is software that moves assets according to rules. The two can overlap: code can be the way the parties <i>perform</i> their agreement, or, in some designs, part of the agreement itself. But the code does not replace contract law. Questions such as capacity, mistake, fraud, unfair terms and consumer rights are still answered by the law of the country that applies.</p>
<p>Seven problems appear again and again: <b>identity and capacity</b> (an address does not show who or how old the party is), <b>error and rescission</b> (the law may cancel a contract, but the payment on chain cannot be reversed), <b>interpretation</b> (what if text and code differ?), <b>oracles and liability</b>, <b>data protection</b> (immutable storage versus the right to erasure), <b>jurisdiction</b> (which court, which law, when nodes are everywhere), and <b>mandatory law</b> (tenancy or consumer rules override what the code says).</p>
<p>For businesses, the question is economic: does automation reduce the cost of trust enough to justify development, audits and legal review? Good candidates are processes with many parties, clear conditions, digital assets and a need for an independent record: escrow, supply-chain payments, tokenised securities, insurance pay-outs based on data.</p>

### Worked example

<div class="worked">
<p><b>Case:</b> the Escrow buyer is 16 years old.</p>
<ol>
  <li>Under German law (§§ 106 ff. BGB) a contract by a minor without parental consent is pending and may be invalid if the parents refuse.</li>
  <li>The contract code has no idea: the buyer deposited, confirmed, and the seller received 1 ETH.</li>
  <li>If the parents refuse, the seller must give the payment back under unjust enrichment rules (§ 812 BGB). The chain will not do it automatically; it is a claim against the seller as a person.</li>
  <li><b>Design options:</b> verify age off chain before allowing deposits (with privacy, lesson 10.3), add an arbiter refund window, or keep the transaction small enough to fall under pocket-money rules (§ 110 BGB).</li>
</ol>
</div>

### Common mistakes

<ul>
  <li>“Once on chain, the law cannot reach it.” Courts act on people and companies, who must return or pay.</li>
  <li>“Lawyers only need to read the comments.” The code is what runs; the comments can be wrong.</li>
</ul>
<!-- deep:end -->

### Watch and read

<div class="vids">
      <a class="vid" href="https://www.youtube.com/watch?v=pWGLtjG-F5c" target="_blank" rel="noopener"><span class="play"></span><span><b>Code is law? (second half: problems and lawyers)</b><small>Finematics</small></span></a>
      <a class="vid read" href="https://www.lawcom.gov.uk/project/smart" target="_blank" rel="noopener"><span class="play"></span><span><b>Smart legal contracts: advice to government</b><small>UK Law Commission</small></span></a>
    </div>

## Try it

<p>Take the Escrow from <a href="../lab-escrow/">lab 4.3</a>. For each of the seven legal questions in the table above, write one sentence on how it applies to the laptop sale.</p>

## Apply

<div class="aud"><div class="cs"><h5>Technology lens</h5><ul><li>How would you make the code follow a court decision?</li></ul></div><div class="bi"><h5>Business lens</h5><ul><li>Where in a company’s processes would a smart contract save the most?</li></ul></div><div class="lw"><h5>Law lens</h5><ul><li>Which of the seven legal questions is hardest for a German court?</li></ul></div></div>

## Ship

<p>Write three sentences in your lab log: the main idea, one example for each lens (technology, business, law), and one open question. Then take the quiz below.</p>
