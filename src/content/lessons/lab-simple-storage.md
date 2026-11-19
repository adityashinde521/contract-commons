---
title: "SimpleStorage: transaction versus call"
module: 3
order: 5
kind: "lab-remix"
minutes: "30 min"
legacy: "L1"
problem: "Some clicks in Remix cost gas and some are free. You will see exactly why."
---

## Problem

<div class="cc-callout cc-callout--problem"><div><b>The question.</b> Some clicks in Remix cost gas and some are free. You will see exactly why.</div></div>

## Concept

<div class="ov">
      <div><b>You will</b>Write, compile, deploy and call your first contract, and read its event.</div>
      <div><b>Concepts</b><ul><li>Transaction vs. call</li><li><code>msg.sender</code></li><li>Events</li></ul></div>
      <div><b>You produce</b>A deployed SimpleStorage with two writes from different accounts.</div>
    </div>
    <h4>The contract</h4>
    <div class="pre-wrap"><pre><code>// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

/// @title SimpleStorage: store and read one number
contract SimpleStorage {
    uint256 private storedValue;
    address public lastWriter;

    event ValueChanged(address indexed writer, uint256 newValue);

    function set(uint256 newValue) external {
        storedValue = newValue;
        lastWriter = msg.sender;
        emit ValueChanged(msg.sender, newValue);
    }

    function get() external view returns (uint256) {
        return storedValue;
    }
}</code></pre><button class="copy" type="button">Copy</button></div>
    <p class="note">Read it before you start: one private number, the address of the last writer, an event, a write function <code>set</code> and a read function <code>get</code>.</p>

## Build

<ol class="steps">
      <li>In the file explorer, create <code>SimpleStorage.sol</code>. Paste the code. Compile (or wait for auto compile).<span class="exp">A green check on the compiler icon. No red errors.</span></li>
      <li>In Deploy &amp; run: Environment = Remix VM, Account = account 1, Value = 0, Contract = SimpleStorage. Click <span class="ui">Deploy</span>.<span class="exp">A green line in the terminal. Under <span class="ui">Deployed Contracts</span>: “SIMPLESTORAGE AT 0x…”.</span></li>
      <li>Expand the deployed contract. Type <code>42</code> next to the orange <span class="ui">set</span> button. Click it.<span class="exp">A new transaction in the terminal. Account 1’s balance drops a tiny amount (gas).</span><span class="why">Orange buttons change state and cost gas. Blue buttons only read.</span></li>
      <li>Click the blue <span class="ui">get</span> button.<span class="exp">Output <code>0: uint256: 42</code>. No new transaction line.</span></li>
      <li>Click the <code>set</code> transaction in the terminal. Find the <span class="ui">logs</span> field.<span class="exp"><code>ValueChanged</code> with <code>writer</code> = account 1 and <code>newValue</code> = 42.</span></li>
      <li>Switch Account to account 2. Call <code>set</code> with <code>7</code>. Click <span class="ui">lastWriter</span>.<span class="exp">The address of account 2. <code>get</code> now returns 7.</span></li>
    </ol>

### If something goes wrong

<div class="tw"><table>
      <tr><th>Symptom</th><th>Cause and fix</th></tr>
      <tr><td>Red error at <code>pragma</code></td><td>Compiler too old. Select 0.8.24 or newer.</td></tr>
      <tr><td>No <span class="ui">Deploy</span> button, only <span class="ui">At Address</span></td><td>Contract not compiled, or wrong Contract selected. Compile again.</td></tr>
      <tr><td>Deployed contract disappeared</td><td>Page reload resets the Remix VM. Deploy again.</td></tr>
    </table></div>

## Apply

<div class="aud">
      <div class="cs"><h5>Technology lens</h5><ul><li>Why is <code>storedValue</code> private but still readable on chain? Find it with the debugger or <code>eth_getStorageAt</code>.</li></ul></div>
      <div class="bi"><h5>Business lens</h5><ul><li>Each write costs money. Which business data would you write on chain, and which not?</li></ul></div>
      <div class="lw"><h5>Law lens</h5><ul><li>All chain data is public. What does this mean for personal data and trade secrets?</li></ul></div>
    </div>

## Ship

<ul class="outc">
      <li>You can explain why <code>set</code> costs gas and <code>get</code> does not.</li>
      <li>You can find an event in a transaction receipt.</li>
      <li>You can show that <code>msg.sender</code> changes with the selected account.</li>
    </ul>
    <div class="callout lab"><h5>Lab log</h5><p>Screenshot of the <code>ValueChanged</code> log and of <code>lastWriter</code> after step 6. One sentence: what is the difference between a transaction and a call?</p></div>
