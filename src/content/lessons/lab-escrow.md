---
title: "Escrow: three parties and a state machine"
module: 4
order: 3
kind: "lab-remix"
minutes: "60 min"
legacy: "L2"
problem: "Lena sells a used laptop to Marco in another city for 1 ETH. If Marco pays first, Lena could keep the money; if Lena ships first, Marco could keep the laptop. Can a contract hold the money instead, and what can it not decide on its own?"
---

## Problem

<div class="cc-callout cc-callout--problem"><div><b>The question.</b> Lena sells a used laptop to Marco in another city for 1 ETH. If Marco pays first, Lena could keep the money; if Lena ships first, Marco could keep the laptop. Can a contract hold the money instead, and what can it not decide on its own?</div></div>

## Concept

<div class="ov">
      <div><b>You will</b>Run a purchase where a contract holds the payment until delivery, with an arbiter for disputes.</div>
      <div><b>Concepts</b><ul><li>State machine (<code>enum</code>)</li><li>Access control</li><li><code>payable</code> and wei</li><li>Reverts as protection</li></ul></div>
      <div><b>You produce</b>Two runs: release to the seller, refund to the buyer.</div>
    </div>
    <h4>The process</h4>
    <p>The buyer deploys the contract and names the seller, the arbiter and the price. The contract moves through four states:</p>
    <div class="tw"><table>
      <tr><th>Value</th><th>State</th><th>What can happen next</th></tr>
      <tr><td>0</td><td>AwaitingPayment</td><td>Buyer calls <code>deposit</code> with exactly the price.</td></tr>
      <tr><td>1</td><td>AwaitingDelivery</td><td>Buyer or arbiter calls <code>confirmDelivery</code> (seller is paid), or arbiter calls <code>refund</code> (buyer is repaid).</td></tr>
      <tr><td>2</td><td>Complete</td><td>Nothing. The deal is closed.</td></tr>
      <tr><td>3</td><td>Refunded</td><td>Nothing. The deal is closed.</td></tr>
    </table></div>
    <div class="pre-wrap"><pre><code>// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

/// @title Escrow: the buyer pays into the contract.
/// The buyer or arbiter releases the funds; only the arbiter refunds.
contract Escrow {
    enum State { AwaitingPayment, AwaitingDelivery, Complete, Refunded }

    address public immutable buyer;
    address payable public immutable seller;
    address public immutable arbiter;
    uint256 public immutable price;
    State public state;

    event Deposited(address indexed buyer, uint256 amount);
    event Released(address indexed seller, uint256 amount);
    event Refunded(address indexed buyer, uint256 amount);

    modifier inState(State expected) {
        require(state == expected, "Wrong state");
        _;
    }

    constructor(address payable _seller, address _arbiter, uint256 _price) {
        require(_seller != address(0) &amp;&amp; _arbiter != address(0), "Zero address");
        require(_price &gt; 0, "Price must be &gt; 0");
        buyer = msg.sender;
        seller = _seller;
        arbiter = _arbiter;
        price = _price;
        state = State.AwaitingPayment;
    }

    function deposit() external payable inState(State.AwaitingPayment) {
        require(msg.sender == buyer, "Only buyer");
        require(msg.value == price, "Send exact price");
        state = State.AwaitingDelivery;
        emit Deposited(msg.sender, msg.value);
    }

    function confirmDelivery() external inState(State.AwaitingDelivery) {
        require(msg.sender == buyer || msg.sender == arbiter, "Only buyer or arbiter");
        state = State.Complete;                        // effect first
        uint256 amount = address(this).balance;
        (bool ok, ) = seller.call{value: amount}("");  // interaction last
        require(ok, "Transfer failed");
        emit Released(seller, amount);
    }

    function refund() external inState(State.AwaitingDelivery) {
        require(msg.sender == arbiter, "Only arbiter");
        state = State.Refunded;
        uint256 amount = address(this).balance;
        (bool ok, ) = payable(buyer).call{value: amount}("");
        require(ok, "Transfer failed");
        emit Refunded(buyer, amount);
    }
}</code></pre><button class="copy" type="button">Copy</button></div>
    <div class="callout gui"><h5>See it in a real tool</h5><p>After L7, open your Escrow transactions in <a href="../lab-tenderly/">Tenderly (G8)</a>: every step of this lab becomes visible in the debugger, and the simulator lets you test each role without signing.</p></div>

## Build

<div class="callout warn"><h5>The Value rule</h5><p>Value must be <b>0</b> for Deploy and for every function except <code>deposit</code>. Remix keeps the last Value you typed. Check it before every click.</p></div>
    <h4>A. Prepare</h4>
    <ol class="steps">
      <li>Create <code>Escrow.sol</code>, paste the code and compile.<span class="exp">Green check on the compiler icon.</span></li>
      <li>Under Deployed Contracts, click the trash icon to remove old instances.</li>
      <li>Open the Account list. Copy the address of <b>account 2</b> (seller, ends in <code>35cb2</code>) and <b>account 3</b> (arbiter, ends in <code>C02db</code>) with the copy icons. Paste them in a text file.<span class="why">Remix VM addresses are the same for everyone, which helps in class.</span></li>
    </ol>
    <h4>B. Deploy</h4>
    <ol class="steps">
      <li>Select <b>account 1</b>. It becomes the buyer, because the constructor sets <code>buyer = msg.sender</code>.</li>
      <li>Set Value to <b>0</b>. Choose Contract <code>Escrow</code>.</li>
      <li>Click the small arrow next to <span class="ui">Deploy</span> to open three fields: <code>_seller</code>, <code>_arbiter</code>, <code>_price</code>.</li>
      <li>Paste the seller and arbiter addresses. Type the price <code>1000000000000000000</code> (1 ether in wei: a 1 and 18 zeros, no spaces or quotes). Click <span class="ui">transact</span>.<span class="exp">Terminal: green line, <code>value: 0 wei</code>. A new “ESCROW AT 0x…” entry.</span></li>
      <li>Expand it and click <span class="ui">state</span>.<span class="exp"><code>0</code> (AwaitingPayment).</span></li>
    </ol>
    <h4>C. Release path</h4>
    <ol class="steps">
      <li>Still account 1: set Value to <code>1</code> and the unit to <b>Ether</b>. Click <span class="ui">deposit</span>.<span class="exp">Logs show <code>Deposited</code>. <span class="ui">state</span> = 1. Account 1 has about 99 ETH.</span></li>
      <li>Set Value back to <b>0</b>. Click <span class="ui">confirmDelivery</span>.<span class="exp">Logs show <code>Released</code>. <span class="ui">state</span> = 2. Account 2 (seller) has about 101 ETH.</span></li>
      <li>Click <span class="ui">deposit</span> again (Value 1 Ether).<span class="exp">Revert: “Wrong state”. The contract protects the closed deal.</span></li>
    </ol>
    <h4>D. Refund path and a revert on purpose</h4>
    <ol class="steps">
      <li>Account 1, Value 0: deploy a second Escrow with the same three fields. Work only on this new instance.</li>
      <li>Value 1 Ether, click <span class="ui">deposit</span>. Then Value back to 0.<span class="exp"><span class="ui">state</span> = 1.</span></li>
      <li>Select account 2 (seller). Click <span class="ui">refund</span>.<span class="exp">Revert: “Only arbiter”. Take a screenshot: this is the most important picture of the lab.</span></li>
      <li>Select account 3 (arbiter). Click <span class="ui">refund</span>.<span class="exp">Logs show <code>Refunded</code>. <span class="ui">state</span> = 3. Account 1 has about 100 ETH again, minus gas.</span></li>
    </ol>

### If something goes wrong

<div class="tw"><table>
      <tr><th>Message</th><th>Cause</th><th>Fix</th></tr>
      <tr><td><code>invalid BigNumberish string: empty string</code></td><td>A constructor field is empty.</td><td>Fill all three fields. No trailing comma.</td></tr>
      <tr><td>Deploy reverts; note says “should be payable”</td><td>Value is not 0 during Deploy. The constructor is not payable.</td><td>Set Value to 0.</td></tr>
      <tr><td>“Wrong state”</td><td>Deposit not done yet, already closed, or you clicked an older instance.</td><td>Click <span class="ui">state</span> first. Delete old instances.</td></tr>
      <tr><td>“Send exact price”</td><td>Value unit is Wei, or the amount differs from <code>_price</code>.</td><td>Value 1, unit <b>Ether</b>.</td></tr>
      <tr><td>“Only buyer”</td><td>Wrong account for <code>deposit</code>.</td><td>Select account 1.</td></tr>
      <tr><td>“Only arbiter”</td><td>Wrong account for <code>refund</code>.</td><td>Select the account you entered as <code>_arbiter</code>.</td></tr>
      <tr><td>“Zero address” or “Price must be &gt; 0”</td><td>Empty or zero values in the constructor.</td><td>Paste real addresses; price in wei.</td></tr>
    </table></div>

## Apply

<div class="aud">
      <div class="cs"><h5>Technology lens</h5><ul><li>What happens if the arbiter loses its key? Add a deadline: after 30 days, the buyer can refund without the arbiter.</li><li>Why is <code>price</code> <code>immutable</code>?</li></ul></div>
      <div class="bi"><h5>Business lens</h5><ul><li>Compare cost and time with a bank escrow or a payment service with buyer protection.</li><li>Who would pay the arbiter, and how?</li></ul></div>
      <div class="lw"><h5>Law lens</h5><ul><li>The arbiter acts like a judge or an arbitral tribunal. Who chooses it? Is its decision enforceable?</li><li>Goods are only partly defective. The code knows only “all” or “nothing”. What does the law say (price reduction, §441 BGB)?</li></ul></div>
    </div>

### Go further

<ol>
      <li><b>Deadline:</b> add <code>uint256 public deadline</code> and a function <code>refundAfterDeadline()</code> for the buyer.</li>
      <li><b>Partial release:</b> let the arbiter split the amount between buyer and seller.</li>
      <li><b>Arbiter fee:</b> pay the arbiter 1% on release or refund.</li>
    </ol>

## Ship

<ul class="outc">
      <li>You can run both paths and read the state after each step.</li>
      <li>You can explain each revert message and which rule it enforces.</li>
      <li>You can explain why <code>confirmDelivery</code> changes the state before it sends ETH.</li>
      <li>You can explain the Escrow in one sentence each through the technology, business and law lenses.</li>
    </ul>
    <div class="card"><h4>One contract, three sentences</h4>
      <p><b>Technology:</b> “A state machine with three roles. Access control and checks-effects-interactions protect the funds.”</p>
      <p><b>Business:</b> “It automates a three-party payment process, removes the bank as intermediary and leaves an audit trail of events.”</p>
      <p><b>Law:</b> “It performs part of a purchase agreement. The code cannot judge if goods are defective, so the arbiter still needs a legal mandate.”</p>
    </div>
    <div class="callout lab"><h5>Lab log</h5><p>Screenshots: state after each step, the “Only arbiter” revert, account balances after release. The state diagram drawn by the process analyst.</p></div>
