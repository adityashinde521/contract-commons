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
<tr><td>Multisig (Safe)</td><td>Several owners, a threshold</td><td>Company treasuries (lab <a href="/lessons/lab-safe/">11.3 Safe</a>)</td></tr>
</table></div>
<h3>Test networks</h3>
<ul>
<li><b>Sepolia</b> is the test network for applications. Its ETH is free from faucets and worth nothing.</li>
<li><b>Hoodi</b> replaced Holesky in 2025 as the test network for validators and staking.</li>
<li>Upgrades are activated on testnets first. A public proposal from May 2026 suggests replacing Sepolia in 2027; it is not decided.</li>
</ul>
<div class="cc-callout cc-callout--warn"><div><b>Five course rules.</b> Never share or type your recovery phrase. Course wallet for testnets only. Never deploy to Mainnet. Check the network before every signature. If you do not understand a signature request, reject it. <a href="../../setup/">Full setup guide</a>.</div></div>

<!-- deep:start -->
### In depth

<p>A wallet does not hold coins. Coins are entries on the chain. A wallet holds <b>keys</b> and offers three functions: show balances (by asking a node), build transactions, and sign them. Wallets differ in where the keys live. A <b>browser wallet</b> such as MetaMask stores encrypted keys on your computer: convenient, but exposed to malware. A <b>hardware wallet</b> keeps keys on a separate device and signs inside it. A <b>custodial wallet</b> on an exchange means the exchange holds the keys; you hold a claim against the exchange.</p>
<p><b>Smart accounts</b> put the rules into a contract: several signers, daily limits, recovery through friends or a company. ERC-4337 introduced them without changing the protocol; EIP-7702 (Pectra, May 2025) lets a normal account temporarily act as a smart account, for example to batch an approval and a swap in one click or let a company pay the gas.</p>
<p>A <b>testnet</b> is a copy of Ethereum where coins have no value. Sepolia is the standard testnet for applications; Hoodi is used by validators and staking providers. Faucets give out test ETH for free, usually with limits to stop abuse. Testnets are sometimes reset or replaced, so never build anything permanent on them.</p>

### Worked example

<div class="worked">
<p><b>Case:</b> set up a safe course wallet and check it.</p>
<ol>
  <li>Install MetaMask from metamask.io only. Create a <i>new</i> wallet just for this course.</li>
  <li>Write the 12 words on paper. Never type them anywhere else, never photograph them.</li>
  <li>Turn on “Show test networks” and select Sepolia. Your address is the same on every network; only the balance differs.</li>
  <li>Get 0.05 SepoliaETH from a faucet. Open sepolia.etherscan.io and search your address: one incoming transaction.</li>
  <li>Send 0.001 to a classmate. Etherscan shows <i>From</i> (you), <i>To</i>, <i>Value</i> and the fee.</li>
</ol>
</div>

### Common mistakes

<ul>
  <li>“Test ETH can be sold.” It has no value. Anyone offering to buy or sell it is running a scam.</li>
  <li>“Each network needs a new wallet.” One key gives the same address on all EVM networks.</li>
  <li>“A browser extension is as safe as a hardware wallet.” Not for real money.</li>
</ul>
<!-- deep:end -->

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
