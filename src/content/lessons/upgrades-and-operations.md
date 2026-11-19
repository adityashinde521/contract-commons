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
<li>Admin held by a <b>multisig</b> (lab <a href="/lessons/lab-safe/">11.3 Safe</a>), not one key.</li>
<li>A <b>timelock</b>: every upgrade is announced and waits, for example 48 hours, so users can leave.</li>
<li>A <b>pause</b> function for emergencies, with clear limits on who can use it and for how long.</li>
<li>Rollup risk sites such as L2BEAT grade exactly these powers (lab <a href="/lessons/lab-dashboards/">10.4 Dashboards</a>).</li>
</ul>
<h3>Operating a contract</h3>
<ul>
<li><b>Monitoring:</b> alerts on large transfers, admin calls and failed transactions (for example Tenderly Alerts or open-source monitors).</li>
<li><b>Incident plan:</b> who can pause, who decides, how users are informed.</li>
<li><b>Maintenance:</b> dependency updates (OpenZeppelin releases), compiler versions, and documenting every deployment address.</li>
</ul>

<!-- deep:start -->
### In depth

<p>Immutability protects users from sudden rule changes, but it also means bugs cannot be fixed. Many protocols therefore use a <b>proxy</b>. Users always talk to one fixed proxy address. The proxy holds the data and forwards every call with <code>delegatecall</code> to an <b>implementation</b> contract that holds the logic. To upgrade, an admin points the proxy at a new implementation; the address and data stay, the logic changes.</p>
<!-- diagram:proxy -->
<figure class="dg"><div class="sv"><svg viewBox="0 0 720 260" role="img" aria-label="Upgradeable proxy pattern" xmlns="http://www.w3.org/2000/svg"><defs><marker id="ah-upgradeableproxypatt-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="m-a" d="M0 0L10 5L0 10z"/></marker><marker id="ah-upgradeableproxypatt-ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="m-ar" d="M0 0L10 5L0 10z"/></marker><marker id="ah-upgradeableproxypatt-ag" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="m-ag" d="M0 0L10 5L0 10z"/></marker><marker id="ah-upgradeableproxypatt-am" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="m-am" d="M0 0L10 5L0 10z"/></marker></defs><rect class="k-law" x="20" y="100" width="120" height="56" rx="12"/><text class="tb" x="80.0" y="132.7" text-anchor="middle" font-size="13.5">User</text><rect class="k-cs" x="200" y="86" width="180" height="84" rx="12"/><text class="tb" x="290.0" y="114.2" text-anchor="middle" font-size="13.5">Proxy</text><text class="t" x="290.0" y="132.7" text-anchor="middle" font-size="13.5">fixed address</text><text class="t" x="290.0" y="151.2" text-anchor="middle" font-size="13.5">holds storage &amp; ETH</text><rect class="k-n" x="470" y="20" width="220" height="70" rx="12"/><text class="tb" x="580.0" y="50.5" text-anchor="middle" font-size="13.5">Implementation v1</text><text class="t" x="580.0" y="69.0" text-anchor="middle" font-size="13.5">logic only</text><rect class="k-brand" x="470" y="166" width="220" height="70" rx="12"/><text class="tb" x="580.0" y="196.5" text-anchor="middle" font-size="13.5">Implementation v2</text><text class="t" x="580.0" y="215.0" text-anchor="middle" font-size="13.5">fixed logic</text><line class="k-a" x1="140" y1="128" x2="198" y2="128" marker-end="url(#ah-upgradeableproxypatt-a)"/><text class="tl" x="169.0" y="121.0" text-anchor="middle" font-size="12.5">call</text><line class="k-a" x1="380" y1="110" x2="468" y2="60" marker-end="url(#ah-upgradeableproxypatt-a)"/><text class="tl" x="470" y="112" text-anchor="start" font-size="12.5">delegatecall</text><line class="k-ag" x1="380" y1="150" x2="468" y2="196" marker-end="url(#ah-upgradeableproxypatt-ag)" stroke-dasharray="5 4"/><text class="tlg" x="470" y="150" text-anchor="start" font-size="12.5">after upgrade</text><rect class="k-warn" x="200" y="200" width="180" height="50" rx="12"/><text class="tb" x="290.0" y="220.6" text-anchor="middle" font-size="13">Admin</text><text class="t" x="290.0" y="238.6" text-anchor="middle" font-size="13">multisig + timelock</text><line class="k-am" x1="290" y1="200" x2="290" y2="172" marker-end="url(#ah-upgradeableproxypatt-am)"/></svg></div><figcaption><b>Same address, new logic.</b> The proxy keeps the data and borrows the code of the current implementation. An upgrade only changes which implementation it points to, so whoever controls the admin controls the contract.</figcaption></figure>
<p>Upgradeability moves trust from code to people: whoever controls the upgrade key can change everything, including taking the funds. Good practice limits that power. Put the admin role in a <b>multisig</b>, add a <b>timelock</b> (for example 48 hours) so users can see an upgrade coming and exit, and publish who the signers are. Rating sites such as L2BEAT grade protocols on exactly these points. Proxies also have technical traps: the storage layout of a new implementation must match the old one, and implementations must not be initialisable by strangers.</p>
<p>Operating a live contract also means <b>monitoring</b> (alerts on large transfers or admin calls), an <b>incident plan</b> (who can pause, how fast, who informs users), and key management for every privileged role. Many losses happen not at launch but months later, when an admin key is stolen.</p>

### Worked example

<div class="worked">
<p><b>Case:</b> a bug is found in a live, upgradeable Escrow platform.</p>
<ol>
  <li><b>Hour 0:</b> a researcher reports a bug through the bounty programme. The team confirms it with a test on a mainnet fork.</li>
  <li><b>Hour 1:</b> two of three multisig signers call <code>pause()</code>. Deposits stop; funds stay safe.</li>
  <li><b>Day 1–3:</b> the fix is written, tested and reviewed. The storage layout is checked with a tool.</li>
  <li><b>Day 3:</b> the upgrade is proposed in the multisig and enters a 48-hour timelock, announced publicly.</li>
  <li><b>Day 5:</b> the upgrade executes; the source of the new implementation is verified; the contract is unpaused.</li>
</ol>
<p><b>Trade-off:</b> the timelock slows the fix but stops a stolen key from upgrading instantly.</p>
</div>

### Common mistakes

<ul>
  <li>“Upgradeable contracts are unsafe.” They are a trust choice; with a multisig and a timelock they can be safer than unfixable code.</li>
  <li>Adding a new variable at the top of the storage layout in an upgrade, which overwrites existing data.</li>
</ul>
<!-- deep:end -->

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
