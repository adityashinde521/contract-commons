---
title: "Wallets, keys and test networks"
module: 3
order: 2
kind: "lesson"
minutes: "35 min"
problem: "A student loses a laptop with MetaMask on it. Is the money gone? What should a company do differently?"
---

## Problem

<div class="cc-callout cc-callout--problem"><div><b>The question.</b> A student loses a laptop with MetaMask on it. Is the money gone? What should a company do differently?</div></div>

## Concept

<h3>What a wallet really is</h3>
<ul>
<li>A wallet does not hold coins. It holds <b>keys</b> and signs transactions. The balances live on the chain.</li>
<li>A <b>recovery phrase</b> (12 or 24 words, standard BIP-39) recreates every key in the wallet. Whoever has it controls the funds. The lost laptop is not the risk; a phrase written in a file on it would be.</li>
</ul>
<div class="tw"><table>
<tr><th>Kind</th><th>Who holds the key</th><th>Typical use</th></tr>
<tr><td>Custodial (exchange account)</td><td>The provider</td><td>Buying and selling; the provider is regulated as a crypto-asset service provider under MiCA</td></tr>
<tr><td>Software wallet (MetaMask, Rabby)</td><td>You, on your device</td><td>Everyday use, development, this course</td></tr>
<tr><td>Hardware wallet</td><td>You, on a separate device</td><td>Larger amounts, signing for a company</td></tr>
<tr><td>Smart account (ERC-4337, EIP-7702)</td><td>Rules in a contract: several keys, limits, recovery</td><td>Companies, families, AI agents (Module 13)</td></tr>
<tr><td>Multisig (Safe)</td><td>Several owners, a threshold</td><td>Company treasuries (lab G3)</td></tr>
</table></div>
<h3>Test networks</h3>
<ul>
<li><b>Sepolia</b> is the test network for applications. Its ETH is free from faucets and worth nothing.</li>
<li><b>Hoodi</b> replaced Holesky in 2025 as the test network for validators and staking.</li>
<li>Upgrades are activated on testnets first. A public proposal from May 2026 suggests replacing Sepolia in 2027; it is not decided.</li>
</ul>
<div class="cc-callout cc-callout--warn"><div><b>Five course rules.</b> Never share or type your recovery phrase. Course wallet for testnets only. Never deploy to Mainnet. Check the network before every signature. If you do not understand a signature request, reject it. <a href="../../setup/">Full setup guide</a>.</div></div>

### Watch and read

<div class="vids">
<a class="vid read" href="https://ethereum.org/wallets/" target="_blank" rel="noopener"><span class="play"></span><span><b>Ethereum wallets</b><small>ethereum.org</small></span></a>
<a class="vid read" href="https://ethereum.org/developers/docs/networks/" target="_blank" rel="noopener"><span class="play"></span><span><b>Networks and testnets</b><small>ethereum.org developer docs</small></span></a>
<a class="vid read" href="https://ethereum.org/roadmap/account-abstraction/" target="_blank" rel="noopener"><span class="play"></span><span><b>Account abstraction</b><small>ethereum.org roadmap</small></span></a>
</div>

## Try it

<ol class="steps">
<li>Follow the <a href="../../setup/">setup guide</a>: install MetaMask, create a course-only wallet, switch to Sepolia.<span class="exp">Network name “Sepolia”, balance 0.</span></li>
<li>Get test ETH from a faucet, or from your instructor.<span class="exp">0.05 SepoliaETH or more.</span></li>
<li>Paste your address into <a href="https://sepolia.etherscan.io" target="_blank" rel="noopener">sepolia.etherscan.io</a>.<span class="exp">The faucet payment appears as an incoming transaction.</span></li>
</ol>

## Apply

<div class="aud"><div class="cs"><h5>Technology lens</h5><ul><li>How can a smart account let someone recover access without a recovery phrase?</li></ul></div><div class="bi"><h5>Business lens</h5><ul><li>Design key management for a small company: who signs what, and with which device?</li></ul></div><div class="lw"><h5>Law lens</h5><ul><li>Is a recovery phrase part of an estate? How can heirs get access lawfully?</li></ul></div></div>

## Ship

<ul class="outc"><li>A course wallet on Sepolia with test ETH.</li><li>You can explain why the recovery phrase, not the device, is the asset.</li><li>You can compare custodial, software, hardware and smart-account wallets.</li></ul>
