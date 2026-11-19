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
