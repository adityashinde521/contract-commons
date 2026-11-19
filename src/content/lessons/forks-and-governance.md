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
<p>Upgrades now come about twice a year: Dencun (2024), Pectra (May 2025), Fusaka (December 2025), and Glamsterdam, which went live on Sepolia on 6 October 2026. Its next testnet step was then paused on 22 October because a proposed change to gas costs could break assumptions inside contracts that are already deployed and cannot be changed. As of 20 November 2026 there is no mainnet date. This is governance in action: a technical change meets the interests of people who rely on old code.</p>
<div class="cc-callout cc-callout--law"><div><b>Law lens.</b> Protocol governance is informal: no legal entity owns Ethereum. If a hard fork changes who owns funds, who is responsible? Courts and regulators look for a “sufficiently decentralised” network, a term without a fixed legal test.</div></div>

<!-- deep:start -->
### In depth

<p>A blockchain’s rules live in the software that nodes run. To change the rules, enough people must run new software. A <b>soft fork</b> makes the rules stricter: old nodes still accept new blocks, so upgrades can be gradual. A <b>hard fork</b> changes the rules in a way old nodes reject. Everyone must upgrade by a set time, or the network splits in two.</p>
<!-- diagram:forks -->
<figure class="dg"><div class="sv"><svg viewBox="0 0 720 250" role="img" aria-label="Soft fork and hard fork" xmlns="http://www.w3.org/2000/svg"><defs><marker id="ah-softforkandhardfork-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="m-a" d="M0 0L10 5L0 10z"/></marker><marker id="ah-softforkandhardfork-ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="m-ar" d="M0 0L10 5L0 10z"/></marker><marker id="ah-softforkandhardfork-ag" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="m-ag" d="M0 0L10 5L0 10z"/></marker><marker id="ah-softforkandhardfork-am" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="m-am" d="M0 0L10 5L0 10z"/></marker></defs><text class="th" x="20" y="24" text-anchor="start" font-size="14">Soft fork: stricter rules, one chain</text><rect class="k-n" x="20" y="36" width="90" height="40" rx="12"/><text class="t" x="65.0" y="60.7" text-anchor="middle" font-size="13.5">old</text><rect class="k-n" x="135" y="36" width="90" height="40" rx="12"/><text class="t" x="180.0" y="60.7" text-anchor="middle" font-size="13.5">old</text><line class="k-a" x1="110" y1="56" x2="133" y2="56" marker-end="url(#ah-softforkandhardfork-a)"/><rect class="k-n" x="250" y="36" width="90" height="40" rx="12"/><text class="t" x="295.0" y="60.7" text-anchor="middle" font-size="13.5">old</text><line class="k-a" x1="225" y1="56" x2="248" y2="56" marker-end="url(#ah-softforkandhardfork-a)"/><rect class="k-brand" x="365" y="36" width="90" height="40" rx="12"/><text class="t" x="410.0" y="60.7" text-anchor="middle" font-size="13.5">new rules</text><line class="k-a" x1="340" y1="56" x2="363" y2="56" marker-end="url(#ah-softforkandhardfork-a)"/><rect class="k-brand" x="480" y="36" width="90" height="40" rx="12"/><text class="t" x="525.0" y="60.7" text-anchor="middle" font-size="13.5">new rules</text><line class="k-a" x1="455" y1="56" x2="478" y2="56" marker-end="url(#ah-softforkandhardfork-a)"/><rect class="k-brand" x="595" y="36" width="90" height="40" rx="12"/><text class="t" x="640.0" y="60.7" text-anchor="middle" font-size="13.5">new rules</text><line class="k-a" x1="570" y1="56" x2="593" y2="56" marker-end="url(#ah-softforkandhardfork-a)"/><text class="tl" x="20" y="104" text-anchor="start" font-size="12.5">Old nodes still accept the new blocks.</text><text class="th" x="20" y="140" text-anchor="start" font-size="14">Hard fork: changed rules; nodes that do not upgrade split off</text><rect class="k-n" x="20" y="172" width="90" height="40" rx="12"/><text class="t" x="65.0" y="196.7" text-anchor="middle" font-size="13.5">old</text><rect class="k-n" x="135" y="172" width="90" height="40" rx="12"/><text class="t" x="180.0" y="196.7" text-anchor="middle" font-size="13.5">old</text><line class="k-a" x1="110" y1="192" x2="133" y2="192" marker-end="url(#ah-softforkandhardfork-a)"/><rect class="k-n" x="250" y="172" width="90" height="40" rx="12"/><text class="t" x="295.0" y="196.7" text-anchor="middle" font-size="13.5">old</text><line class="k-a" x1="225" y1="192" x2="248" y2="192" marker-end="url(#ah-softforkandhardfork-a)"/><rect class="k-brand" x="365" y="152" width="90" height="36" rx="12"/><text class="t" x="410.0" y="174.7" text-anchor="middle" font-size="13.5">new rules</text><rect class="k-warn" x="365" y="204" width="90" height="36" rx="12"/><text class="t" x="410.0" y="226.7" text-anchor="middle" font-size="13.5">old rules</text><rect class="k-brand" x="480" y="152" width="90" height="36" rx="12"/><text class="t" x="525.0" y="174.7" text-anchor="middle" font-size="13.5">new rules</text><rect class="k-warn" x="480" y="204" width="90" height="36" rx="12"/><text class="t" x="525.0" y="226.7" text-anchor="middle" font-size="13.5">old rules</text><line class="k-a" x1="455" y1="170" x2="478" y2="170" marker-end="url(#ah-softforkandhardfork-a)"/><line class="k-am" x1="455" y1="222" x2="478" y2="222" marker-end="url(#ah-softforkandhardfork-am)"/><rect class="k-brand" x="595" y="152" width="90" height="36" rx="12"/><text class="t" x="640.0" y="174.7" text-anchor="middle" font-size="13.5">new rules</text><rect class="k-warn" x="595" y="204" width="90" height="36" rx="12"/><text class="t" x="640.0" y="226.7" text-anchor="middle" font-size="13.5">old rules</text><line class="k-a" x1="570" y1="170" x2="593" y2="170" marker-end="url(#ah-softforkandhardfork-a)"/><line class="k-am" x1="570" y1="222" x2="593" y2="222" marker-end="url(#ah-softforkandhardfork-am)"/><path class="k-a" d="M 340 192 C 352 192 350 170 363 170" fill="none" marker-end="url(#ah-softforkandhardfork-a)"/><path class="k-am" d="M 340 192 C 352 192 350 222 363 222" fill="none" marker-end="url(#ah-softforkandhardfork-am)"/></svg></div><figcaption><b>Upgrades and splits.</b> A soft fork narrows the rules, so old software keeps working. A hard fork changes them; if a group keeps the old rules, two chains continue, as Ethereum and Ethereum Classic did in 2016.</figcaption></figure>
<p>On Ethereum, changes start as an <b>EIP</b> (Ethereum Improvement Proposal) on GitHub. Researchers and client teams discuss them in the public All Core Devs calls. An upgrade bundles several EIPs and gets a name (Pectra, Fusaka, Glamsterdam). Client teams implement it, test it on devnets, then on the public testnets (Sepolia, then Hoodi), and finally choose a mainnet date. Node operators, staking providers and exchanges then decide to run the new version. Nobody can force them, but a node on the old rules is left on a chain that the economy has abandoned.</p>
<p>So who holds power? Client developers write the code, validators and node operators choose to run it, and users, exchanges and application developers decide which chain has value. When they disagree, the chain can split: after the DAO hack in 2016, most of the community accepted a hard fork that returned the stolen ETH, and a minority continued the original chain as Ethereum Classic.</p>

### Worked example

<div class="worked">
<p><b>Case:</b> Glamsterdam, autumn 2026 (as of 20 November 2026).</p>
<ol>
  <li>Glamsterdam bundles block building inside the protocol (ePBS), block-level access lists and gas repricing (EIP-8037, EIP-8038).</li>
  <li>It went live on the Sepolia testnet on 6 October 2026.</li>
  <li>Auditors found that the new gas rules could break assumptions inside some contracts that are already deployed and cannot be changed.</li>
  <li>On 22 October the next testnet step (Hoodi) was postponed. Audit reports were presented in November and discussed on 19 November without a decision. A delay to 2027 is possible.</li>
</ol>
<p><b>What it shows:</b> a technical improvement (cheaper, fairer gas) collides with the interests of people who rely on old code. Nobody voted; the decision is made by rough consensus among client teams, under public pressure from application developers.</p>
</div>

### Common mistakes

<ul>
  <li>“Vitalik decides upgrades.” He is one influential voice; client teams implement and node operators adopt.</li>
  <li>“A fork is always a split.” Most hard forks are planned upgrades that everyone runs; a split happens only when a large group refuses.</li>
</ul>
<!-- deep:end -->

### Watch and read

<div class="vids">
<a class="vid" href="https://ethereum.org/videos/dao-hack-ethereum-classic/" target="_blank" rel="noopener"><span class="play"></span><span><b>The DAO hack: story of Ethereum Classic</b><small>10 min</small></span></a>
<a class="vid read" href="https://ethereum.org/governance/" target="_blank" rel="noopener"><span class="play"></span><span><b>Ethereum governance</b><small>ethereum.org</small></span></a>
<a class="vid read" href="https://eips.ethereum.org" target="_blank" rel="noopener"><span class="play"></span><span><b>Ethereum Improvement Proposals</b><small>eips.ethereum.org</small></span></a>
</div>

## Try it

<p>Open <a href="https://eips.ethereum.org/EIPS/eip-7702" target="_blank" rel="noopener">EIP-7702</a> (part of Pectra). Find the authors, the status and the motivation section. Write two sentences: what problem it solves and who had to agree before it went live.</p>

## Apply

<div class="aud"><div class="cs"><h5>Technology lens</h5><ul><li>Why is a soft fork backwards compatible and a hard fork not?</li></ul></div><div class="bi"><h5>Business lens</h5><ul><li>An exchange must decide which side of a contentious fork to list. What does it consider?</li></ul></div><div class="lw"><h5>Law lens</h5><ul><li>After a fork, a token exists on both chains. Who owns the copy, and is it taxable?</li></ul></div></div>

## Ship

<ul class="outc"><li>You can tell a soft fork from a hard fork.</li><li>You can describe the EIP process.</li><li>You can explain why “immutability” is social and economic, not absolute.</li></ul>
