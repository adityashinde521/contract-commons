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

<!-- deep:start -->
### In depth

<p>A decentralised application (dApp) is usually three layers. The <b>contracts</b> on chain hold the rules and the money. The <b>front end</b> is a normal website, often built with React, that reads data and prepares transactions. The <b>wallet</b> in the browser holds the keys and asks the user to approve each transaction. Between them sit an <b>RPC provider</b> that talks to the chain and often an <b>indexer</b> (for example The Graph or a custom database) that collects events, because reading history directly from a node is slow.</p>
<!-- diagram:dapp-stack -->
<figure class="dg"><div class="sv"><svg viewBox="0 0 720 270" role="img" aria-label="Layers of a dApp" xmlns="http://www.w3.org/2000/svg"><defs><marker id="ah-layersofadapp-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="m-a" d="M0 0L10 5L0 10z"/></marker><marker id="ah-layersofadapp-ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="m-ar" d="M0 0L10 5L0 10z"/></marker><marker id="ah-layersofadapp-ag" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="m-ag" d="M0 0L10 5L0 10z"/></marker><marker id="ah-layersofadapp-am" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="m-am" d="M0 0L10 5L0 10z"/></marker></defs><rect class="k-zone-b" x="470" y="10" width="240" height="250" rx="16"/><text class="th" x="590" y="34" text-anchor="middle" font-size="13.5">On chain (decentralised)</text><rect class="k-n" x="20" y="30" width="180" height="60" rx="12"/><text class="tb" x="110.0" y="55.5" text-anchor="middle" font-size="13.5">Front end</text><text class="t" x="110.0" y="74.0" text-anchor="middle" font-size="13.5">website, can be changed</text><rect class="k-law" x="20" y="180" width="180" height="60" rx="12"/><text class="tb" x="110.0" y="205.5" text-anchor="middle" font-size="13.5">Wallet</text><text class="t" x="110.0" y="224.0" text-anchor="middle" font-size="13.5">holds keys, signs</text><rect class="k-n" x="270" y="30" width="150" height="60" rx="12"/><text class="tb" x="345.0" y="55.5" text-anchor="middle" font-size="13.5">Indexer</text><text class="t" x="345.0" y="74.0" text-anchor="middle" font-size="13.5">collects events</text><rect class="k-bi" x="270" y="180" width="150" height="60" rx="12"/><text class="tb" x="345.0" y="205.5" text-anchor="middle" font-size="13.5">RPC node</text><text class="t" x="345.0" y="224.0" text-anchor="middle" font-size="13.5">provider</text><rect class="k-brand" x="490" y="105" width="200" height="60" rx="12"/><text class="tb" x="590.0" y="130.5" text-anchor="middle" font-size="13.5">Smart contracts</text><text class="t" x="590.0" y="149.0" text-anchor="middle" font-size="13.5">rules and money</text><line class="k-a" x1="110" y1="90" x2="110" y2="178" marker-end="url(#ah-layersofadapp-a)"/><text class="tl" x="122" y="140" text-anchor="start" font-size="12">asks to sign</text><line class="k-a" x1="200" y1="210" x2="268" y2="210" marker-end="url(#ah-layersofadapp-a)"/><text class="tl" x="234" y="200" text-anchor="middle" font-size="12">signed tx</text><line class="k-a" x1="420" y1="200" x2="488" y2="150" marker-end="url(#ah-layersofadapp-a)"/><line class="k-am" x1="488" y1="120" x2="422" y2="70" marker-end="url(#ah-layersofadapp-am)"/><text class="tl" x="470" y="84" text-anchor="end" font-size="12">events</text><line class="k-am" x1="268" y1="60" x2="202" y2="60" marker-end="url(#ah-layersofadapp-am)"/><text class="tl" x="234" y="50" text-anchor="middle" font-size="12">history</text></svg></div><figcaption><b>Only the contracts are decentralised.</b> The website, the RPC provider and the indexer are normal services that can fail or be attacked. The wallet is the last check before anything is signed.</figcaption></figure>
<p>Only the contract layer is decentralised. The website runs on a normal server and domain; it can be hacked, changed, or blocked in a country. If the front end is replaced with a malicious one, it can ask users to sign harmful transactions. That is why wallets decode what you are about to sign, and why some teams publish their front end on IPFS so that anyone can host an identical copy.</p>
<p>Reading and writing are different. Reading (<code>balanceOf</code>, <code>state()</code>) is a free <code>eth_call</code> and returns instantly. Writing is a transaction: the user signs, pays gas, and waits for inclusion. Good dApps show this clearly: a pending state, the transaction hash with an explorer link, and a clear message when a call reverts.</p>

### Worked example

<div class="worked">
<p><b>Case:</b> the buyer clicks “Pay 1 ETH” in an Escrow dApp.</p>
<ol>
  <li>The page reads <code>state()</code> and <code>price()</code> through the RPC provider: AwaitingPayment, 1 ETH. It enables the button.</li>
  <li>On click, the front end encodes a call to <code>deposit()</code> with value 1 ETH and passes it to MetaMask.</li>
  <li>MetaMask shows the contract address, the function and the value. The buyer confirms; the wallet signs and sends.</li>
  <li>The page shows “Pending” and the transaction hash. About 12 seconds later the receipt arrives with a <code>Deposited</code> event.</li>
  <li>The indexer stores the event; the seller’s dashboard now shows “Payment held”.</li>
</ol>
</div>

### Common mistakes

<ul>
  <li>“The dApp is on the blockchain.” Usually only the contracts are.</li>
  <li>“If the website is down, my funds are lost.” The contract still works; anyone can call it through Etherscan or another front end.</li>
</ul>
<!-- deep:end -->

### Watch and read

<div class="vids">
<a class="vid read" href="https://ethereum.org/developers/docs/dapps/" target="_blank" rel="noopener"><span class="play"></span><span><b>Introduction to dApps</b><small>ethereum.org</small></span></a>
<a class="vid read" href="https://docs.ethers.org/v6/" target="_blank" rel="noopener"><span class="play"></span><span><b>ethers.js v6 documentation</b><small>Official documentation</small></span></a>
<a class="vid read" href="https://viem.sh" target="_blank" rel="noopener"><span class="play"></span><span><b>viem</b><small>TypeScript interface for Ethereum</small></span></a>
</div>

## Try it

<p>In Remix, open the compiler tab and copy the Escrow’s <b>ABI</b>. Find the entries for <code>deposit</code> and <code>Deposited</code>. Which one says <code>"stateMutability": "payable"</code>? Then build an interface for it in lab <a href="../lab-quickdapp/">QuickDApp</a>.</p>

## Apply

<div class="aud"><div class="cs"><h5>Technology lens</h5><ul><li>Why do apps read past events from an indexer instead of the node directly?</li></ul></div><div class="bi"><h5>Business lens</h5><ul><li>Which parts of a dApp can a company still switch off?</li></ul></div><div class="lw"><h5>Law lens</h5><ul><li>Who is the provider of a dApp under consumer law: the contract author or the website operator?</li></ul></div></div>

## Ship

<ul class="outc"><li>You can draw the six layers of a dApp.</li><li>You can explain what an ABI is.</li></ul>
