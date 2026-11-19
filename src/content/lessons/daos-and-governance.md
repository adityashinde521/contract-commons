---
title: "DAOs and on-chain governance"
module: 11
order: 2
kind: "lesson"
minutes: "35 min"
problem: "A group wants to manage shared money without a company. Can a smart contract replace articles of association?"
---

## Problem

<div class="cc-callout cc-callout--problem"><div><b>The question.</b> A group wants to manage shared money without a company. Can a smart contract replace articles of association?</div></div>

## Concept

<ul>
<li>A <b>DAO</b> (decentralised autonomous organisation) is a group whose membership, decision rules and treasury are governed by smart contracts.</li>
<li><b>Who votes:</b> token holders (one token, one vote), members of a multisig, or holders of non-transferable membership tokens.</li>
<li><b>How:</b> a proposal bundles on-chain actions. It passes if it meets a <b>quorum</b> and a <b>threshold</b> within a voting period, then often waits in a <b>timelock</b> before execution.</li>
<li><b>Off-chain voting</b> (for example Snapshot) uses signed messages, costs no gas, and needs a trusted executor or multisig to carry out the result.</li>
<li><b>Delegation</b> lets token holders give their votes to active delegates; most token holders never vote.</li>
</ul>
<h3>Known problems</h3>
<ul>
<li>Concentration: a few large holders decide.</li>
<li>Governance attacks: borrowing tokens to pass a proposal (Beanstalk, 2022, about $180 million drained in one transaction).</li>
<li>Low participation and voter fatigue.</li>
</ul>
<h3>Legal wrappers</h3>
<p>Without a legal entity, members may be treated as an unincorporated partnership with personal liability. US courts have treated DAOs as unincorporated associations or partnerships whose members can be liable (CFTC v. Ooki DAO and Sarcuni v. bZx, both 2023). Some jurisdictions offer wrappers (Wyoming DAO LLC, Marshall Islands DAO LLC); in Germany, a DAO without a wrapper may be treated as a civil-law partnership (GbR).</p>

<!-- deep:start -->
### In depth

<p>A DAO (decentralised autonomous organisation) is a group whose membership, decision rules and treasury are managed by contracts. Members usually hold governance tokens or membership NFTs. A <b>proposal</b> bundles concrete on-chain actions, for example “transfer 10,000 USDC to the audit firm”. Members vote during a voting period. If the proposal reaches the <b>quorum</b> and the required majority, it is queued in a <b>timelock</b> and then executed by the contract itself; no person has to press a button at the bank.</p>
<!-- diagram:dao-lifecycle -->
<figure class="dg"><div class="sv"><svg viewBox="0 0 720 220" role="img" aria-label="DAO proposal lifecycle" xmlns="http://www.w3.org/2000/svg"><defs><marker id="ah-daoproposallifecycle-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="m-a" d="M0 0L10 5L0 10z"/></marker><marker id="ah-daoproposallifecycle-ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="m-ar" d="M0 0L10 5L0 10z"/></marker><marker id="ah-daoproposallifecycle-ag" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="m-ag" d="M0 0L10 5L0 10z"/></marker><marker id="ah-daoproposallifecycle-am" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="m-am" d="M0 0L10 5L0 10z"/></marker></defs><rect class="k-n" x="15" y="40" width="150" height="66" rx="12"/><text class="tb" x="90.0" y="68.5" text-anchor="middle" font-size="13">Propose</text><text class="t" x="90.0" y="86.5" text-anchor="middle" font-size="13">actions + snapshot</text><rect class="k-bi" x="193" y="40" width="150" height="66" rx="12"/><text class="tb" x="268.0" y="68.5" text-anchor="middle" font-size="13">Vote</text><text class="t" x="268.0" y="86.5" text-anchor="middle" font-size="13">3 days</text><line class="k-a" x1="167" y1="73" x2="191" y2="73" marker-end="url(#ah-daoproposallifecycle-a)"/><rect class="k-warn" x="371" y="40" width="150" height="66" rx="12"/><text class="tb" x="446.0" y="68.5" text-anchor="middle" font-size="13">Timelock</text><text class="t" x="446.0" y="86.5" text-anchor="middle" font-size="13">2 days, can exit</text><line class="k-a" x1="345" y1="73" x2="369" y2="73" marker-end="url(#ah-daoproposallifecycle-a)"/><rect class="k-brand" x="549" y="40" width="150" height="66" rx="12"/><text class="tb" x="624.0" y="68.5" text-anchor="middle" font-size="13">Execute</text><text class="t" x="624.0" y="86.5" text-anchor="middle" font-size="13">contract acts</text><line class="k-a" x1="523" y1="73" x2="547" y2="73" marker-end="url(#ah-daoproposallifecycle-a)"/><text class="tl" x="270" y="30" text-anchor="middle" font-size="12.5">quorum + majority?</text><rect class="k-danger" x="193" y="150" width="150" height="50" rx="12"/><text class="tb" x="268.0" y="170.6" text-anchor="middle" font-size="13">Defeated</text><text class="t" x="268.0" y="188.6" text-anchor="middle" font-size="13">nothing happens</text><line class="k-ar" x1="268" y1="106" x2="268" y2="148" marker-end="url(#ah-daoproposallifecycle-ar)"/><text class="tl" x="282.0" y="131.0" text-anchor="middle" font-size="12.5">no</text></svg></div><figcaption><b>Code executes what members decide.</b> The snapshot fixes voting power before the vote, so borrowed tokens do not count. The timelock gives members time to react before money moves.</figcaption></figure>
<p>Design choices shape power. <b>Token voting</b> (one token, one vote) is simple but concentrates power in large holders. <b>Delegation</b> lets members give their votes to active representatives. <b>Snapshots</b> fix voting power at a past block, so tokens borrowed for the vote do not count. The Beanstalk attack in 2022 used a flash loan to gain a majority and pass a malicious proposal in one transaction. Many DAOs combine <b>off-chain signalling</b> (free votes on Snapshot) with on-chain execution for money.</p>
<p>Legally, a DAO without a registered entity is risky for its members. US courts treated DAOs as unincorporated associations or partnerships in 2023 (CFTC v. Ooki DAO, Sarcuni v. bZx), which can make members personally liable. Many DAOs therefore use a legal wrapper such as a foundation, an association or a special DAO law (for example in Wyoming or the Marshall Islands).</p>

### Worked example

<div class="worked">
<p><b>Case:</b> a student-club DAO with 100 tokens decides to fund a hackathon.</p>
<ol>
  <li>Rules: quorum 30 tokens, simple majority, 3-day vote, 2-day timelock. Snapshot at proposal creation.</li>
  <li>Member A proposes “send 500 USDC to the event venue”. 40 tokens vote: 28 yes, 12 no. Quorum (30) and majority are reached.</li>
  <li>The proposal enters the 2-day timelock. Members who disagree can exit (for example sell or redeem their tokens).</li>
  <li>After the timelock anyone calls <code>execute()</code>; the treasury contract sends 500 USDC.</li>
  <li>If someone had bought 50 tokens after the snapshot, those tokens would have had no vote.</li>
</ol>
</div>

### Common mistakes

<ul>
  <li>“A DAO has no leaders.” Core teams, delegates and multisigs often hold real power.</li>
  <li>“On-chain votes are binding in law.” Only if a legal structure or contract says so.</li>
</ul>
<!-- deep:end -->

### Watch and read

<div class="vids">
<a class="vid read" href="https://ethereum.org/dao/" target="_blank" rel="noopener"><span class="play"></span><span><b>Decentralised autonomous organisations</b><small>ethereum.org</small></span></a>
<a class="vid read" href="https://law.stanford.edu/courses/blockchain-governance/" target="_blank" rel="noopener"><span class="play"></span><span><b>Blockchain Governance (LAW 1078)</b><small>Stanford Law course description</small></span></a>
</div>

## Try it

<p>On <a href="https://www.tally.xyz" target="_blank" rel="noopener">Tally</a> or <a href="https://snapshot.box" target="_blank" rel="noopener">Snapshot</a> (read only), open one large DAO. Find its quorum, its voting period and the turnout of its last three proposals. Then build your own in lab <a href="../lab-aragon/">Aragon</a>.</p>

## Apply

<div class="aud"><div class="cs"><h5>Technology lens</h5><ul><li>How does a timelock protect against a governance attack?</li></ul></div><div class="bi"><h5>Business lens</h5><ul><li>Design voting rules for a 50-member student cooperative.</li></ul></div><div class="lw"><h5>Law lens</h5><ul><li>Which German legal form fits a DAO best: GbR, e.V., GmbH or eG? Why?</li></ul></div></div>

## Ship

<ul class="outc"><li>You can explain quorum, threshold, timelock and delegation.</li><li>You can name three governance risks.</li><li>You can discuss legal wrappers for DAOs.</li></ul>
