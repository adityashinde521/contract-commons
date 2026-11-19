---
title: "Upgrades, monitoring and maintenance"
module: 8
order: 1
kind: "lesson"
minutes: "35 min"
problem: "Code on a blockchain cannot be changed, yet many large protocols ship new versions every few months. How, and who holds that power?"
---

## Problem

<div class="cc-callout cc-callout--problem"><div><b>The question.</b> Code on a blockchain cannot be changed, yet many large protocols ship new versions every few months. How, and who holds that power?</div></div>

## Concept

<h3>Upgrade patterns</h3>
<ul>
<li><b>Redeploy and migrate:</b> deploy a new contract and ask users to move. Simple and honest, but slow.</li>
<li><b>Proxy pattern:</b> users talk to a fixed <b>proxy</b> address that forwards every call to an <b>implementation</b> contract. An admin can point the proxy to a new implementation. Variants: Transparent proxy, UUPS (ERC-1822 style), Beacon proxy.</li>
<li><b>Parameters and modules:</b> keep the code fixed, but let governance change limits or add modules.</li>
</ul>
<div class="cc-callout cc-callout--warn"><div><b>The trade-off.</b> Whoever controls the upgrade can change every rule, including who owns the funds. An upgradeable contract is only as trustworthy as its admin key.</div></div>
<h3>Making the power safe</h3>
<ul>
<li>Admin held by a <b>multisig</b> (lab G3), not one key.</li>
<li>A <b>timelock</b>: every upgrade is announced and waits, for example 48 hours, so users can leave.</li>
<li>A <b>pause</b> function for emergencies, with clear limits on who can use it and for how long.</li>
<li>Rollup risk sites such as L2BEAT grade exactly these powers (lab G11).</li>
</ul>
<h3>Operating a contract</h3>
<ul>
<li><b>Monitoring:</b> alerts on large transfers, admin calls and failed transactions (for example Tenderly Alerts or open-source monitors).</li>
<li><b>Incident plan:</b> who can pause, who decides, how users are informed.</li>
<li><b>Maintenance:</b> dependency updates (OpenZeppelin releases), compiler versions, and documenting every deployment address.</li>
</ul>

### Watch and read

<div class="vids">
<a class="vid read" href="https://docs.openzeppelin.com/upgrades-plugins/proxies" target="_blank" rel="noopener"><span class="play"></span><span><b>Proxy upgrade pattern</b><small>OpenZeppelin documentation</small></span></a>
<a class="vid read" href="https://ethereum.org/developers/docs/smart-contracts/upgrading/" target="_blank" rel="noopener"><span class="play"></span><span><b>Upgrading smart contracts</b><small>ethereum.org</small></span></a>
</div>

## Try it

<p>On Etherscan, open a large stablecoin or lending contract. If it is a proxy, Etherscan shows “Read as Proxy” and the implementation address. Find who the admin is: a single address, a multisig or a timelock?</p>

## Apply

<div class="aud"><div class="cs"><h5>Technology lens</h5><ul><li>Why must a proxy and its implementation agree on the storage layout?</li></ul></div><div class="bi"><h5>Business lens</h5><ul><li>Write a short incident plan for the course Escrow: who pauses, who tells users?</li></ul></div><div class="lw"><h5>Law lens</h5><ul><li>Users accepted the terms of version 1. An upgrade changes them. Is that a unilateral change of contract terms?</li></ul></div></div>

## Ship

<ul class="outc"><li>You can explain the proxy pattern and its main risk.</li><li>You can name three controls on upgrade power.</li><li>You can find a contract’s admin on Etherscan.</li></ul>
