---
title: "dApp architecture: from contract to app"
module: 9
order: 1
kind: "lesson"
minutes: "30 min"
problem: "Your buyer will never open Remix. What sits between a smart contract and the person who clicks “Pay”?"
---

## Problem

<div class="cc-callout cc-callout--problem"><div><b>The question.</b> Your buyer will never open Remix. What sits between a smart contract and the person who clicks “Pay”?</div></div>

## Concept

<p>A decentralised application (dApp) is a normal web app whose important rules and money live in smart contracts.</p>
<div class="tw"><table>
<tr><th>Layer</th><th>What it does</th><th>Typical tools</th></tr>
<tr><td>Interface</td><td>Pages, buttons, forms</td><td>React, Vue, Angular, Svelte</td></tr>
<tr><td>Wallet connection</td><td>Asks the user’s wallet for an address and signatures</td><td>Injected wallets (MetaMask), WalletConnect, wagmi</td></tr>
<tr><td>Contract library</td><td>Encodes calls, reads state and events</td><td>ethers.js, viem, web3.js</td></tr>
<tr><td>Node access</td><td>Sends transactions, reads the chain</td><td>RPC providers (Module 3)</td></tr>
<tr><td>Indexing</td><td>Collects past events into a searchable database</td><td>The Graph, custom indexers</td></tr>
<tr><td>Storage</td><td>Files and metadata too large for the chain</td><td>IPFS, Arweave (lesson 9.3)</td></tr>
</table></div>
<p>The flow when a buyer clicks “Pay”: the app builds the call with the contract’s <b>ABI</b> (its interface description), the wallet shows it to the buyer, the buyer signs, the app sends it to a node, and the app waits for the receipt and the <code>Deposited</code> event.</p>
<div class="cc-callout cc-callout--law"><div><b>Law lens.</b> The interface is run by someone, and it is often where consumer-protection, sanctions screening and information duties apply. The contract may be neutral; the website showing it is not.</div></div>

### Watch and read

<div class="vids">
<a class="vid read" href="https://ethereum.org/developers/docs/dapps/" target="_blank" rel="noopener"><span class="play"></span><span><b>Introduction to dApps</b><small>ethereum.org</small></span></a>
<a class="vid read" href="https://docs.ethers.org/v6/" target="_blank" rel="noopener"><span class="play"></span><span><b>ethers.js v6 documentation</b><small>Official documentation</small></span></a>
<a class="vid read" href="https://viem.sh" target="_blank" rel="noopener"><span class="play"></span><span><b>viem</b><small>TypeScript interface for Ethereum</small></span></a>
</div>

## Try it

<p>In Remix, open the compiler tab and copy the Escrow’s <b>ABI</b>. Find the entries for <code>deposit</code> and <code>Deposited</code>. Which one says <code>"stateMutability": "payable"</code>? Then build an interface for it in lab <a href="../lab-quickdapp/">QuickDApp</a>.</p>

## Apply

<div class="aud"><div class="cs"><h5>Computer science</h5><ul><li>Why do apps read past events from an indexer instead of the node directly?</li></ul></div><div class="bi"><h5>Business informatics</h5><ul><li>Which parts of a dApp can a company still switch off?</li></ul></div><div class="lw"><h5>Law</h5><ul><li>Who is the provider of a dApp under consumer law: the contract author or the website operator?</li></ul></div></div>

## Ship

<ul class="outc"><li>You can draw the six layers of a dApp.</li><li>You can explain what an ABI is.</li></ul>
