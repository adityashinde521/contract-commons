---
title: "Rental deposit: time and mandatory law"
module: 4
order: 4
kind: "lab-remix"
minutes: "45 min"
legacy: "L3"
problem: "A landlord holds a tenant’s deposit and decides alone how much to keep for damage. Code can enforce deadlines, but German tenancy law sets limits the code does not know."
---

## Problem

<div class="cc-callout cc-callout--problem"><div><b>The question.</b> A landlord holds a tenant’s deposit and decides alone how much to keep for damage. Code can enforce deadlines, but German tenancy law sets limits the code does not know.</div></div>

## Concept

<div class="ov">
      <div><b>You will</b>Run a residential rental deposit with a lease end and a damage deduction.</div>
      <div><b>Concepts</b><ul><li><code>block.timestamp</code></li><li>Splitting a payment</li><li>A safety net for the weaker party</li></ul></div>
      <div><b>You produce</b>One settled deposit and a list of conflicts between the code and tenancy law.</div>
    </div>
    <div class="pre-wrap"><pre><code>// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

/// @title RentalDeposit: the tenant pays a deposit.
/// After the lease ends, the landlord keeps a damage amount and returns the rest.
contract RentalDeposit {
    address public immutable landlord;
    address public immutable tenant;
    uint256 public immutable depositAmount;
    uint256 public immutable leaseEnd;
    bool public paid;
    bool public settled;

    event DepositPaid(uint256 amount);
    event Settled(uint256 toLandlord, uint256 toTenant);

    constructor(address _tenant, uint256 _depositAmount, uint256 _leaseDays) {
        require(_tenant != address(0), "Zero address");
        landlord = msg.sender;
        tenant = _tenant;
        depositAmount = _depositAmount;
        leaseEnd = block.timestamp + (_leaseDays * 1 days);
    }

    function payDeposit() external payable {
        require(msg.sender == tenant, "Only tenant");
        require(!paid, "Already paid");
        require(msg.value == depositAmount, "Wrong amount");
        paid = true;
        emit DepositPaid(msg.value);
    }

    function settle(uint256 damageAmount) external {
        require(msg.sender == landlord, "Only landlord");
        require(paid &amp;&amp; !settled, "Nothing to settle");
        require(block.timestamp &gt;= leaseEnd, "Lease not ended");
        require(damageAmount &lt;= depositAmount, "Damage too high");
        settled = true;
        _payOut(damageAmount);
    }

    /// Safety net: if the landlord does nothing for 30 days after the lease,
    /// the tenant can take back the full deposit.
    function claimAfterTimeout() external {
        require(msg.sender == tenant, "Only tenant");
        require(paid &amp;&amp; !settled, "Nothing to settle");
        require(block.timestamp &gt;= leaseEnd + 30 days, "Too early");
        settled = true;
        _payOut(0);
    }

    function _payOut(uint256 damageAmount) private {
        uint256 toTenant = depositAmount - damageAmount;
        if (damageAmount &gt; 0) {
            (bool ok1, ) = payable(landlord).call{value: damageAmount}("");
            require(ok1, "Transfer to landlord failed");
        }
        if (toTenant &gt; 0) {
            (bool ok2, ) = payable(tenant).call{value: toTenant}("");
            require(ok2, "Transfer to tenant failed");
        }
        emit Settled(damageAmount, toTenant);
    }
}</code></pre><button class="copy" type="button">Copy</button></div>

## Build

<div class="checked"><b>Checked on 20 November 2026.</b> The contract code in this lab compiles with Solidity 0.8.24 to 0.8.30. Remix screens change between releases: if a label differs, look for the closest one and note it in your lab log.</div>

<h4>A. Settle a deposit</h4>
    <ol class="steps">
      <li>Create <code>RentalDeposit.sol</code>, paste, compile. Copy account 2’s address (tenant).<span class="exp">A green compiler check and one address in your clipboard (ends in 35cb2 in the Remix VM).</span></li>
      <li>Account 1 (landlord), Value 0. Deploy with: <code>_tenant</code> = account 2, <code>_depositAmount</code> = <code>2000000000000000000</code> (2 ether), <code>_leaseDays</code> = <code>0</code>.<span class="why">0 days makes the lease end at once, so you can test settlement without waiting.</span><span class="exp">A RentalDeposit instance. depositAmount() returns 2000000000000000000; leaseEnd() equals the block time (lease already ended).</span></li>
      <li>Select account 2. Value 2 Ether. Click <span class="ui">payDeposit</span>. Then Value back to 0.<span class="exp"><span class="ui">paid</span> = true. Logs: <code>DepositPaid</code>.</span></li>
      <li>Select account 1. Call <span class="ui">settle</span> with <code>500000000000000000</code> (0.5 ether damage).<span class="exp">Logs: <code>Settled</code> with toLandlord 0.5 and toTenant 1.5 ether (in wei). Balances change accordingly.</span></li>
    </ol>
    <h4>B. Time protects the tenant</h4>
    <ol class="steps">
      <li>Deploy again with <code>_leaseDays</code> = <code>30</code>. Tenant pays 2 Ether.<span class="exp">A new instance; leaseEnd() is about 30 × 86,400 seconds later than now. paid() returns true after the tenant’s payment.</span></li>
      <li>Landlord calls <span class="ui">settle</span> with any amount.<span class="exp">Revert: “Lease not ended”.</span></li>
      <li>On the same contract, the tenant calls <span class="ui">claimAfterTimeout</span>.<span class="exp">Revert: “Too early”. In real use it works 30 days after the lease ends if the landlord does nothing.</span></li>
      <li>Deploy a third contract with <code>_leaseDays</code> = <code>0</code>. Tenant pays 2 Ether. Landlord calls <span class="ui">settle</span> with <code>3000000000000000000</code> (3 ether).<span class="exp">Revert: “Damage too high”. The landlord cannot keep more than the deposit.</span></li>
    </ol>

### If something goes wrong

<div class="tw"><table>
      <tr><th>Message</th><th>Fix</th></tr>
      <tr><td>“Wrong amount”</td><td>Value must equal the deposit exactly: 2 Ether.</td></tr>
      <tr><td>“Only tenant” / “Only landlord”</td><td>Check the Account field.</td></tr>
      <tr><td>“Nothing to settle”</td><td>Deposit not paid, or already settled. Deploy a new instance.</td></tr>
    </table></div>

## Apply

<div class="aud">
      <div class="cs"><h5>Technology lens</h5><ul><li>Add an arbiter for disputed damage, as in <a href="/lessons/lab-escrow/">4.3 Escrow</a>.</li><li>Validators can shift <code>block.timestamp</code> a little. Does it matter here?</li></ul></div>
      <div class="bi"><h5>Business lens</h5><ul><li>The deposit earns no interest in the contract. What would a tenant lose over three years?</li></ul></div>
      <div class="lw"><h5>Law lens (German tenancy law)</h5><ul><li>§551 BGB limits a residential deposit to three months’ net rent and requires the landlord to keep it separate from its own assets, with interest. Does a contract-held deposit meet this?</li><li>The landlord alone decides the damage. Who must prove it? Is this clause valid in a standard-form contract (§307 BGB)?</li></ul></div>
    </div>

### Go further

<ol>
      <li>Add a deposit cap: the constructor takes <code>monthlyRent</code> and rejects a deposit above 3 × rent.</li>
      <li>Require the landlord to submit a damage hash (photo report) before settling.</li>
    </ol>

## Ship

<ul class="outc">
      <li>You can explain how a contract uses time and why time comes from the block, not from a clock.</li>
      <li>You can name the safety net in the code and why it exists.</li>
      <li>You can list at least three rules of tenancy law that the code does not enforce.</li>
    </ul>
