---
title: "Aragon: create a DAO and pass a proposal"
module: 11
order: 4
kind: "lab-gui"
minutes: "60 min"
legacy: "G4"
problem: "A student cooperative wants its members to decide on spending together, with every decision on public record."
---

## Problem

<div class="cc-callout cc-callout--problem"><div><b>The question.</b> A student cooperative wants its members to decide on spending together, with every decision on public record.</div></div>

## Concept

<div class="ov">
      <div><b>You will</b>Create a decentralised autonomous organisation (DAO) with three members, fund its treasury and pass a payment proposal.</div>
      <div><b>Tool</b><a href="https://app.aragon.org" target="_blank" rel="noopener">Aragon App</a>, a no-code DAO builder. It supports Ethereum, Polygon, Arbitrum and Base, and their testnets including Sepolia.</div>
      <div><b>You need</b>MetaMask with three accounts on Sepolia, about 0.03 SepoliaETH in account 1.</div>
    </div>
    <p>A DAO is a group whose rules (who is a member, how decisions are made, who controls the money) are written in smart contracts. A <b>proposal</b> bundles actions, for example “pay 0.002 ETH to X”. The actions run only if the vote passes. Compared with the Safe in <a href="/lessons/lab-safe/">11.3 Safe</a>, the DAO adds proposals, voting periods and a public record of decisions.</p>

## Build

<div class="checked"><b>Checked on 20 November 2026</b> against the tool’s official documentation. Tools change their screens often. If a button has a different name, look for the closest one and note the difference in your lab log.</div>

<h4>A. Create the DAO</h4>
    <ol class="steps">
      <li>Open <a href="https://app.aragon.org" target="_blank" rel="noopener">app.aragon.org</a>. Connect MetaMask (account 1). Click <span class="ui">Create a DAO</span>.<span class="exp">The DAO creation wizard opens.</span></li>
      <li>Blockchain: choose the <b>Sepolia</b> testnet.<span class="why">The blockchain is the only setting that cannot be changed later by a vote.</span><span class="exp">Sepolia is selected. If the app does not list Ethereum Sepolia, choose another testnet it offers, such as Hoodi or Base Sepolia, and get test ETH for that network first.</span></li>
      <li>Name: “Lab Cooperative”, a short description. No logo needed.<span class="exp">The name and description appear in the summary on the right or at the last step.</span></li>
      <li>Membership: choose <b>multisig members</b>. Add account 1, account 2 and account 3. Allow only members to create proposals.<span class="exp">Three member addresses; proposal creation limited to members; threshold set in the next step.</span></li>
      <li>Approval threshold: <b>2</b>. Review all settings, deploy and confirm in MetaMask.<span class="exp">After a short wait, the DAO homepage opens with its address, members, treasury and proposals.</span></li>
    </ol>
    <h4>B. Fund the treasury and propose</h4>
    <ol class="steps">
      <li>Copy the DAO address. From MetaMask (account 1), send 0.01 SepoliaETH to it.<span class="exp">The treasury shows 0.01 ETH.</span></li>
      <li>Create a new proposal: title “Pay workshop speaker”, a one-paragraph reason. Add the action <b>transfer</b> (or “withdraw assets”): recipient = a classmate’s course address, amount = 0.002 ETH. Publish and confirm.<span class="exp">A proposal page with status “active” and 0 of 2 approvals.</span></li>
    </ol>
    <h4>C. Approve and execute</h4>
    <ol class="steps">
      <li>As account 1, approve the proposal. Switch to account 2 and approve it too.<span class="exp">2 of 2 approvals. Status changes to “approved” or “executable”.</span></li>
      <li>Click <span class="ui">Execute</span> and confirm.<span class="exp">Status “executed”. The recipient receives 0.002 ETH. Anyone can see the decision and its reason forever.</span></li>
      <li>Optional: create a second proposal that adds a fourth member, and let it fail with only one approval.<span class="exp">The proposal stays open or expires without execution; the member list is unchanged.</span></li>
    </ol>

## Apply

<div class="aud">
      <div class="cs"><h5>Technology lens</h5><ul><li>The DAO is made of several contracts (plugins). Find them on Etherscan. Which contract actually holds the money?</li></ul></div>
      <div class="bi"><h5>Business lens</h5><ul><li>Token voting versus multisig: which fits a club, a cooperative, an investment group?</li></ul></div>
      <div class="lw"><h5>Law lens</h5><ul><li>Under German law, a DAO without a legal wrapper may be treated as a civil-law partnership (GbR), with members personally liable. What does this mean for the three of you?</li><li>Compare with DAO laws such as Wyoming’s DAO LLC. Is a legal wrapper needed in the EU?</li></ul></div>
    </div>

## Ship

<ul class="outc">
      <li>You created an on-chain organisation with members, a treasury and a decision rule.</li>
      <li>You passed and executed a proposal, and know what happens when it fails.</li>
      <li>You can compare a DAO with a Safe and with a legal entity.</li>
    </ul>
    <div class="callout lab"><h5>Lab log</h5><p>DAO address, proposal link, Etherscan link of the execution, and a table comparing <a href="/lessons/lab-safe/">11.3 Safe</a> and <a href="/lessons/lab-aragon/">11.4 Aragon DAO</a>.</p></div>
