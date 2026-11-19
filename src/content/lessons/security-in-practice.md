---
title: "Security in practice: hacks and AI"
module: 7
order: 2
kind: "lesson"
minutes: "40 min"
legacy: "F5"
problem: "About $3.4 billion was stolen in crypto in 2025, but most of it not through code bugs. How do attacks really happen today?"
---

## Problem

<div class="cc-callout cc-callout--problem"><div><b>The question.</b> About $3.4 billion was stolen in crypto in 2025, but most of it not through code bugs. How do attacks really happen today?</div></div>

## Concept

<div class="goal"><b>Goal:</b> you can describe how attacks really happen today, beyond code bugs.</div>
    <h4>The numbers (Chainalysis, December 2025)</h4>
    <ul>
      <li>About <b>$3.4 billion</b> in crypto was stolen in 2025.</li>
      <li>The <b>Bybit</b> hack (February 2025, about $1.5 billion) was the largest single theft in crypto history, about 44% of the year’s total. Signers of a multisig approved a manipulated transaction.</li>
      <li>Hackers linked to <b>North Korea</b> stole at least $2.02 billion in 2025. One method: fake IT workers inside crypto companies.</li>
      <li>Attacks on personal wallets increased. Losses from DeFi code exploits stayed relatively low.</li>
    </ul>
    <h4>The weakest point is often not the contract</h4>
    <ul>
      <li>Large losses now often come from <b>operations</b>: compromised developer machines, manipulated signing interfaces, stolen keys, insiders.</li>
      <li>“Blind signing”: a signer approves a transaction that the wallet cannot show clearly. The contract works correctly but does the attacker’s will (compare <a href="/lessons/lab-safe/">11.3 Safe</a>).</li>
    </ul>
    <h4>AI changes both attack and defence</h4>
    <ul>
      <li>In December 2025, Anthropic and MATS researchers published <b>SCONE-bench</b>: 405 smart contracts that were really exploited from 2020 to 2025.</li>
      <li>On contracts exploited after March 2025, AI agents succeeded in about 56% of cases, worth $4.6 million in simulated funds. A year earlier the rate was about 2%.</li>
      <li>Agents also found two new bugs in freshly deployed contracts, at about $1.22 of compute per contract scanned.</li>
      <li>Conclusion: defenders must use AI too, together with human audits, formal verification and tests.</li>
    </ul>
    <h4>Defence checklist</h4>
    <ul>
      <li>Code: checks-effects-interactions, OpenZeppelin, tests, audits, AI-assisted review, bug bounties.</li>
      <li>Keys: multisig with hardware wallets, clear signing, separate devices.</li>
      <li>Operations: timelocks on admin actions, a pause function, monitoring, an incident plan.</li>
    </ul>
    <div class="callout law"><h5>Law lens</h5><ul>
      <li>Is an exchange liable to customers after a hack? What does DORA (EU digital operational resilience for financial firms) require?</li>
      <li>Stolen funds that go to a sanctioned state raise sanctions-law questions for anyone who touches them.</li>
      <li>If an AI tool finds a bug, may a researcher use it to “rescue” funds? Where is the line to unauthorised access?</li>
    </ul></div>

<!-- deep:start -->
### In depth

<p>The numbers for 2025 changed the security picture. About $3.4 billion was stolen, and almost half of it in a single incident: the Bybit hack of February 2025, about $1.5 billion. The contracts worked perfectly. The attackers compromised a computer used by the wallet provider’s developers and injected code into the signing website, so the exchange’s signers saw a normal transfer while they actually approved a change that gave the attackers control of the cold wallet.</p>
<p>This is the main lesson: <b>operational security</b> now matters as much as code. Typical attack paths are stolen or phished private keys, compromised front ends and software supply chains, social engineering of staff (including fake job applicants), and governance or admin keys with too much power. Hackers linked to North Korea were responsible for at least $2.02 billion in 2025, often through such human routes.</p>
<p>Defences follow from the attack paths. Use multisig with independent signers and hardware wallets. Verify transactions on a second device, by reading the raw data or a simulation, not only the website. Limit what admin keys can do, add timelocks, and monitor contracts so you can pause quickly. At the same time, attackers use AI too: in December 2025, AI agents in the SCONE-bench study exploited more than half of recent real-world vulnerable contracts in simulation.</p>

### Worked example

<div class="worked">
<p><b>Case:</b> review a company’s payment process against the Bybit pattern.</p>
<div class="tw"><table>
  <tr><th>Step today</th><th>Risk</th><th>Better</th></tr>
  <tr><td>Three signers approve in the same web app</td><td>One compromised app fools all three</td><td>Each signer checks the decoded transaction on a hardware wallet or an independent tool</td></tr>
  <tr><td>Signers check the receiver address only</td><td>The attack changed the call type, not the address</td><td>Check the function, the value and whether it is a delegatecall</td></tr>
  <tr><td>Admin key on one laptop</td><td>Malware takes full control</td><td>Admin in a multisig with a 48-hour timelock</td></tr>
  <tr><td>No monitoring</td><td>Loss found hours later</td><td>Alerts on large transfers and admin calls; a pause switch</td></tr>
</table></div>
</div>

### Common mistakes

<ul>
  <li>“A multisig is safe by design.” It is only as safe as the way its signers check what they sign.</li>
  <li>“Hacks are mostly clever code exploits.” The largest losses are increasingly human and operational.</li>
</ul>
<!-- deep:end -->

### Watch and read

<div class="vids">
      <a class="vid read" href="https://red.anthropic.com/2025/smart-contracts/" target="_blank" rel="noopener"><span class="play"></span><span><b>AI agents find $4.6M in blockchain smart contract exploits</b><small>Anthropic red team, Dec 2025</small></span></a>
      <a class="vid read" href="https://www.theblock.co/post/382477" target="_blank" rel="noopener"><span class="play"></span><span><b>Crypto hacks hit $3.4 billion in 2025</b><small>The Block, on the Chainalysis report</small></span></a>
    </div>

## Try it

<p>Do <a href="../lab-phalcon/">lab 7.5 Phalcon</a> after this lesson: you will trace one of the 2025 incidents call by call.</p>

## Apply

<div class="aud"><div class="cs"><h5>Technology lens</h5><ul><li>Which defences protect against operations failures rather than code bugs?</li></ul></div><div class="bi"><h5>Business lens</h5><ul><li>What should an incident plan contain?</li></ul></div><div class="lw"><h5>Law lens</h5><ul><li>Is an exchange liable to customers after a hack?</li></ul></div></div>

## Ship

<p>Write three sentences in your lab log: the main idea, one example for each lens (technology, business, law), and one open question. Then take the quiz below.</p>
