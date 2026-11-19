---
title: "Forks and protocol governance"
module: 2
order: 2
kind: "lesson"
minutes: "35 min"
problem: "In 2016 the Ethereum community reversed a theft by changing its own history. Who has the power to change a blockchain’s rules?"
---

## Problem

<div class="cc-callout cc-callout--problem"><div><b>The question.</b> In 2016 the Ethereum community reversed a theft by changing its own history. Who has the power to change a blockchain’s rules?</div></div>

## Concept

<ul>
<li>A <b>fork</b> happens when nodes follow different rules or different histories.</li>
<li>A <b>soft fork</b> tightens the rules: old nodes still accept new blocks. A <b>hard fork</b> changes the rules so that old nodes reject new blocks: everyone must upgrade.</li>
<li>A <b>contentious hard fork</b> splits the network when part of the community refuses. After the DAO hack, the majority forked to return the funds; the minority kept the original chain as <b>Ethereum Classic</b>.</li>
<li>Short <b>reorganisations</b> (reorgs) happen when two blocks compete briefly; finality (Module 2, lesson 1) ends them.</li>
</ul>
<h3>Who decides on Ethereum</h3>
<ol>
<li>Anyone can write an <b>Ethereum Improvement Proposal</b> (EIP).</li>
<li>Client teams and researchers discuss it in public <b>All Core Devs</b> calls.</li>
<li>Client teams implement agreed EIPs; an upgrade is scheduled first on testnets (Sepolia, Hoodi) and then on mainnet.</li>
<li>Node operators, validators, exchanges and users decide whether to run the new software. No vote is binding; adoption is.</li>
</ol>
<p>Upgrades now come about twice a year: Dencun (2024), Pectra (May 2025), Fusaka (December 2025), and Glamsterdam, which was live on Sepolia in October 2026 with no mainnet date yet.</p>
<div class="cc-callout cc-callout--law"><div><b>Law lens.</b> Protocol governance is informal: no legal entity owns Ethereum. If a hard fork changes who owns funds, who is responsible? Courts and regulators look for a “sufficiently decentralised” network, a term without a fixed legal test.</div></div>

### Watch and read

<div class="vids">
<a class="vid" href="https://ethereum.org/videos/dao-hack-ethereum-classic/" target="_blank" rel="noopener"><span class="play"></span><span><b>The DAO hack: story of Ethereum Classic</b><small>10 min</small></span></a>
<a class="vid read" href="https://ethereum.org/governance/" target="_blank" rel="noopener"><span class="play"></span><span><b>Ethereum governance</b><small>ethereum.org</small></span></a>
<a class="vid read" href="https://eips.ethereum.org" target="_blank" rel="noopener"><span class="play"></span><span><b>Ethereum Improvement Proposals</b><small>eips.ethereum.org</small></span></a>
</div>

## Try it

<p>Open <a href="https://eips.ethereum.org/EIPS/eip-7702" target="_blank" rel="noopener">EIP-7702</a> (part of Pectra). Find the authors, the status and the motivation section. Write two sentences: what problem it solves and who had to agree before it went live.</p>

## Apply

<div class="aud"><div class="cs"><h5>Computer science</h5><ul><li>Why is a soft fork backwards compatible and a hard fork not?</li></ul></div><div class="bi"><h5>Business informatics</h5><ul><li>An exchange must decide which side of a contentious fork to list. What does it consider?</li></ul></div><div class="lw"><h5>Law</h5><ul><li>After a fork, a token exists on both chains. Who owns the copy, and is it taxable?</li></ul></div></div>

## Ship

<ul class="outc"><li>You can tell a soft fork from a hard fork.</li><li>You can describe the EIP process.</li><li>You can explain why “immutability” is social and economic, not absolute.</li></ul>
