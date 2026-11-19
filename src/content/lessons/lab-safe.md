---
title: "Safe: a company wallet with two signatures"
module: 11
order: 3
kind: "lab-gui"
minutes: "45 min"
legacy: "G3"
problem: "A startup’s founders want no single person to be able to move the company’s money."
---

## Problem

<div class="cc-callout cc-callout--problem"><div><b>The question.</b> A startup’s founders want no single person to be able to move the company’s money.</div></div>

## Concept

<div class="ov">
      <div><b>You will</b>Create a smart-contract wallet that pays only when two of three directors sign.</div>
      <div><b>Tool</b><a href="https://app.safe.global/welcome?chain=sep" target="_blank" rel="noopener">Safe{Wallet}</a> on Sepolia. Safe holds the treasuries of many companies and protocols.</div>
      <div><b>You need</b>MetaMask with three accounts on Sepolia, about 0.03 SepoliaETH in account 1.</div>
    </div>
    <p>A Safe is a smart contract with a list of owners and a threshold. It is the on-chain version of joint signing authority (Gesamtvertretung) in a company. Since October 2025 the web app at app.safe.global is operated by Safe Labs; you may be asked to accept its terms.</p>

## Build

<div class="checked"><b>Checked on 20 November 2026</b> against the tool’s official documentation. Tools change their screens often. If a button has a different name, look for the closest one and note the difference in your lab log.</div>

<h4>A. Create the Safe</h4>
    <ol class="steps">
      <li>Open <a href="https://app.safe.global/welcome?chain=sep" target="_blank" rel="noopener">app.safe.global</a> with network Sepolia. Connect MetaMask with account 1.<span class="exp">The Safe app shows Sepolia and your connected address. You may be asked to accept Safe Labs’ terms first.</span></li>
      <li>Click <span class="ui">Create account</span>. Name it “Team Treasury”. Network: Sepolia.<span class="exp">A setup screen with the name and network.</span></li>
      <li>Add owners: account 1, account 2, account 3. Set the threshold to <b>2 out of 3</b>.<span class="why">One director alone cannot move money. Any two can.</span><span class="exp">Three owner rows and “2 out of 3 owner(s)” for the threshold. After creation and a MetaMask confirmation, your Safe has its own address.</span></li>
      <li>Review and create. Confirm the deployment in MetaMask.<span class="exp">A Safe address (0x…). This is a new contract on Sepolia.</span></li>
    </ol>
    <h4>B. Fund it and propose a payment</h4>
    <ol class="steps">
      <li>In MetaMask (account 1), send 0.01 SepoliaETH to the Safe address.<span class="exp">The Safe dashboard shows 0.01 ETH.</span></li>
      <li>In the Safe, click <span class="ui">New transaction</span> → <span class="ui">Send tokens</span>. Recipient: a classmate’s course address. Amount: 0.002 ETH.<span class="exp">A transaction in the queue with 1 of 2 confirmations.</span></li>
      <li>Sign as account 1. MetaMask shows a signature request, not a transaction.<span class="exp">The transaction is queued: “1 of 2 confirmations”. No money has moved.</span></li>
    </ol>
    <h4>C. Second signature and execution</h4>
    <ol class="steps">
      <li>Switch MetaMask to account 2. Reload the Safe app if needed.<span class="exp">The queued transaction shows a Confirm button for account 2.</span></li>
      <li>Open the queued transaction, click <span class="ui">Confirm</span>, then <span class="ui">Execute</span>. Confirm in MetaMask.<span class="exp">“2 of 2”, then “Success”. The recipient gets 0.002 ETH. Account 2 paid the gas.</span></li>
      <li>Optional: as account 3, propose a payment and reject it as another owner.<span class="exp">The proposal shows as rejected; no ETH moved. On Etherscan the Safe’s nonce still advances.</span></li>
      <li>Open the executed transaction in Tenderly or Phalcon (<a href="/lessons/lab-tenderly/">8.3 Tenderly</a>, <a href="/lessons/lab-phalcon/">7.5 Phalcon</a>) and find the two signatures in the call data.<span class="exp">The input data of execTransaction contains a signatures field with two 65-byte signatures (130 bytes in total).</span></li>
    </ol>

## Apply

<div class="aud">
      <div class="cs"><h5>Technology lens</h5><ul><li>The Bybit hack (2025) drained a Safe: injected code in the signing interface showed the signers a harmless transaction. How can signers check what they sign? (<a href="/lessons/security-in-practice/">7.2 Security in practice</a>)</li></ul></div>
      <div class="bi"><h5>Business lens</h5><ul><li>Design a four-eyes principle for payments above €10,000 and a single signature below it.</li></ul></div>
      <div class="lw"><h5>Law lens</h5><ul><li>Map the Safe to a GmbH: managing directors, joint representation (§35 GmbHG). What happens if a director leaves, dies or loses a key?</li><li>Who is liable if two directors sign a fraudulent payment?</li></ul></div>
    </div>

## Ship

<ul class="outc">
      <li>You created a smart-contract account with three owners and a threshold.</li>
      <li>You can explain the difference between a signature (off-chain, free) and an execution (on-chain, costs gas).</li>
      <li>You can relate a multisig to company law and internal controls.</li>
    </ul>
    <div class="callout lab"><h5>Lab log</h5><p>Safe address, Etherscan link of the executed transaction, a screenshot of the “1 of 2” state.</p></div>
