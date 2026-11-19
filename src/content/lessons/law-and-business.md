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
