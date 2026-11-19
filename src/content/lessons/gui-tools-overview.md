---
title: "GUI tools: overview and safety"
module: 0
order: 0
kind: "reading"
minutes: "20 min"
legacy: "G0"
problem: "Law and business students need to use blockchains, not only read about them. Which professional tools work without code?"
---

## Problem

<div class="cc-callout cc-callout--problem"><div><b>The question.</b> Law and business students need to use blockchains, not only read about them. Which professional tools work without code?</div></div>

## Concept

<h3>Tool map</h3>
<div class="goal"><b>Goal:</b> know which real, market-standard tools let you create and inspect smart contracts through a graphical interface, and which lab uses each one.</div>
    <p>All tools below are used by professional teams. None of them needs programming for the parts you do in this course. Every lab runs on the <b>Sepolia testnet</b> or reads public data. <b>No real money is used anywhere.</b></p>
    <h4>A. Build: create and deploy contracts without code</h4>
    <div class="tw"><table>
      <tr><th>Lab</th><th>Tool</th><th>What you create</th><th>Account</th><th>Best for</th></tr>
      <tr><td>G1</td><td><a href="https://wizard.openzeppelin.com" target="_blank" rel="noopener">OpenZeppelin Contracts Wizard</a> + Remix</td><td>An audited ERC-721 certificate contract, configured with checkboxes and deployed with buttons</td><td>None (MetaMask for Sepolia)</td><td>All</td></tr>
      <tr><td>G2</td><td><a href="https://thirdweb.com/explore" target="_blank" rel="noopener">thirdweb</a> dashboard</td><td>A ready-made NFT “Edition Drop” (tickets or certificates) with claim rules and an airdrop, managed from a dashboard</td><td>thirdweb sign-in + MetaMask</td><td>BI, Law</td></tr>
      <tr><td>G3</td><td><a href="https://app.safe.global/welcome?chain=sep" target="_blank" rel="noopener">Safe{Wallet}</a></td><td>A 2-of-3 company wallet: no payment without two signatures</td><td>MetaMask (3 accounts)</td><td>Law, BI</td></tr>
      <tr><td>G4</td><td><a href="https://app.aragon.org" target="_blank" rel="noopener">Aragon App</a></td><td>A DAO with members, a treasury and proposals that execute on chain</td><td>MetaMask (3 accounts)</td><td>Law, BI</td></tr>
      <tr><td>G5</td><td><a href="https://sepolia.easscan.org" target="_blank" rel="noopener">Ethereum Attestation Service</a></td><td>Your own record format and a signed on-chain statement about a document</td><td>MetaMask</td><td>Law</td></tr>
      <tr><td>G6</td><td><a href="https://playground.accordproject.org" target="_blank" rel="noopener">Accord Project Template Playground</a></td><td>A smart legal contract template: legal text, data model and data</td><td>None</td><td>Law</td></tr>
      <tr><td>G7</td><td>Remix QuickDApp</td><td>A clickable web app for your team’s Escrow, generated with AI</td><td>MetaMask</td><td>Team</td></tr>
    </table></div>
    <h4>B. Inspect and visualise: see what a contract really does</h4>
    <div class="tw"><table>
      <tr><th>Lab</th><th>Tool</th><th>What you see</th><th>Account</th></tr>
      <tr><td>G8</td><td><a href="https://dashboard.tenderly.co" target="_blank" rel="noopener">Tenderly</a></td><td>Visual debugger with the call trace next to the source code; a simulator that runs a transaction as any address without signing or paying</td><td>Free Tenderly account</td></tr>
      <tr><td>G9</td><td><a href="https://blocksec.com/explorer" target="_blank" rel="noopener">Phalcon Explorer</a> (BlockSec)</td><td>Invocation flow, fund flow and balance changes of any transaction, including real hacks</td><td>None for basic use</td></tr>
      <tr><td>G10</td><td>Remix debugger, <a href="https://github.com/naddison36/sol2uml" target="_blank" rel="noopener">sol2uml</a>, <a href="https://eth.build" target="_blank" rel="noopener">ETH.BUILD</a></td><td>Step-by-step execution, UML class diagrams of contracts, a drag-and-drop sandbox for hashes, keys and transactions</td><td>None</td></tr>
    </table></div>
    <h4>C. Research: on-chain data dashboards</h4>
    <div class="tw"><table>
      <tr><th>Lab</th><th>Tool</th><th>What you research</th><th>Account</th></tr>
      <tr><td>G11</td><td><a href="https://dune.com" target="_blank" rel="noopener">Dune</a>, <a href="https://l2beat.com" target="_blank" rel="noopener">L2BEAT</a>, <a href="https://defillama.com" target="_blank" rel="noopener">DefiLlama</a></td><td>Network activity, rollup risk and governance, value locked and hacks over time</td><td>None (Dune free account to edit)</td></tr>
    </table></div>
    <p>G12 lists newer visual builders that are not yet part of the course and gives a checklist to evaluate them.</p>
<h3>Safety</h3>
<div class="callout warn"><h5>Rules for every GUI lab</h5><ol>
      <li>Use only the course MetaMask wallet (S2). It must never hold real money.</li>
      <li>Before every signature, check the network in MetaMask: it must say <b>Sepolia</b>. If it says Ethereum Mainnet, Arbitrum One or any other main network, click <span class="ui">Reject</span>.</li>
      <li>Never enter your recovery phrase on any website. No tool in this course asks for it.</li>
      <li>When a tool offers a paid plan, a card form or a mainnet option, skip it. Every lab works on the free tier.</li>
      <li>Read-only labs (G9, G11) may show mainnet data. You look at it; you never sign anything there.</li>
    </ol></div>
    <div class="callout tip"><h5>Signing in to tools</h5><p>thirdweb (G2) and Tenderly (G8) need a free account. Use your university e-mail or the course wallet. You can delete the account after the course.</p></div>
<h3>Limits</h3>
<ul>
      <li>No-code builders offer fixed templates. A new rule (for example “partial refund after an expert opinion”) still needs code.</li>
      <li>A graphical interface can hide what you sign. Always read the MetaMask screen: network, contract, amount.</li>
      <li>Hosted tools change their labels and plans often. If a button has another name, look for the closest match and note it in your lab log.</li>
      <li>Contracts and attestations stay on the chain even if a website closes. Your Etherscan links remain valid.</li>
    </ul>
    <div class="callout law"><h5>Why this matters for lawyers</h5><p>You do not need to write Solidity to ask the right questions: Who can call this function? Who can upgrade the contract? What happens if the signer is tricked? These tools let you check the answers yourself.</p></div>

## Ship

<p>Write three sentences in your lab log: the main idea, one example from your discipline, and one open question. Then take the quiz below.</p>
