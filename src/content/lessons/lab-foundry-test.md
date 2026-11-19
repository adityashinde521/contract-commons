---
title: "Lab: test the Escrow with Foundry"
module: 6
order: 3
kind: "lab-remix"
minutes: "60 min"
problem: "You will prove, with code, that the Escrow pays the seller, refuses the seller’s refund and rejects any wrong deposit, for hundreds of random amounts."
---

## Problem

<div class="cc-callout cc-callout--problem"><div><b>The question.</b> You will prove, with code, that the Escrow pays the seller, refuses the seller’s refund and rejects any wrong deposit, for hundreds of random amounts.</div></div>

## Concept

<div class="ov"><div><b>You will</b>Create a Foundry project, add the Escrow from L2 and write three tests: a unit test, a revert test and a fuzz test.</div><div><b>Before</b>Lab L2 and lesson “Testing smart contracts”. Code track.</div><div><b>You need</b>macOS, Linux or Windows with WSL; a terminal; Git.</div></div>

## Build

<ol class="steps">
<li>Install Foundry: <code>curl -L https://foundry.paradigm.xyz | bash</code>, open a new terminal, then run <code>foundryup</code>.<span class="exp"><code>forge --version</code> prints a version.</span></li>
<li>Create a project: <code>forge init escrow-tests</code> and <code>cd escrow-tests</code>.<span class="exp">Folders <code>src</code>, <code>test</code>, <code>script</code>, <code>lib/forge-std</code>.</span></li>
<li>Delete the sample <code>src/Counter.sol</code>, <code>test/Counter.t.sol</code> and <code>script/Counter.s.sol</code>. Copy the Escrow from lab L2 into <code>src/Escrow.sol</code>.</li>
<li>Run <code>forge build</code>.<span class="exp">“Compiler run successful”.</span></li>
<li>Create <code>test/Escrow.t.sol</code> with the code below.</li>
</ol>
<div class="pre-wrap"><pre><code>// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import "forge-std/Test.sol";
import "../src/Escrow.sol";

contract EscrowTest is Test {
    Escrow escrow;
    address buyer = address(0xB0B);
    address payable seller = payable(address(0x5E11));
    address arbiter = address(0xA4B);

    function setUp() public {
        vm.deal(buyer, 10 ether);
        vm.prank(buyer);                       // the buyer deploys
        escrow = new Escrow(seller, arbiter, 1 ether);
    }

    function test_ReleasePaysSeller() public {
        vm.prank(buyer);
        escrow.deposit{value: 1 ether}();
        vm.prank(buyer);
        escrow.confirmDelivery();
        assertEq(seller.balance, 1 ether);
        assertEq(uint256(escrow.state()), 2); // Complete
    }

    function test_SellerCannotRefund() public {
        vm.prank(buyer);
        escrow.deposit{value: 1 ether}();
        vm.prank(seller);
        vm.expectRevert(bytes("Only arbiter"));
        escrow.refund();
    }

    function testFuzz_DepositNeedsExactPrice(uint256 amount) public {
        vm.assume(amount != 1 ether &amp;&amp; amount &lt;= 10 ether);
        vm.prank(buyer);
        vm.expectRevert(bytes("Send exact price"));
        escrow.deposit{value: amount}();
    }
}</code></pre><button class="copy" type="button">Copy</button></div>
<ol class="steps" start="6">
<li>Run <code>forge test -vv</code>.<span class="exp">3 tests passed. The fuzz test reports 256 runs.</span></li>
<li>Break the contract on purpose: in <code>refund</code>, change <code>msg.sender == arbiter</code> to <code>msg.sender == arbiter || msg.sender == seller</code>. Run the tests again.<span class="exp"><code>test_SellerCannotRefund</code> fails. The test caught a change to the agreement.</span></li>
<li>Undo the change. Run <code>forge coverage</code>.<span class="exp">A table of line and branch coverage per file.</span></li>
</ol>

### If something goes wrong

<div class="tw"><table><tr><th>Message</th><th>Fix</th></tr>
<tr><td><code>forge: command not found</code></td><td>Open a new terminal after installing, then run <code>foundryup</code>.</td></tr>
<tr><td>Source not found: forge-std</td><td>Run <code>forge install foundry-rs/forge-std</code> inside the project.</td></tr>
<tr><td>Compiler version error</td><td>Set <code>solc = "0.8.24"</code> in <code>foundry.toml</code>.</td></tr>
</table></div>

## Apply

<div class="aud"><div class="cs"><h5>Computer science</h5><ul><li>Add an invariant: the contract’s balance is never more than the price.</li></ul></div><div class="bi"><h5>Business informatics</h5><ul><li>Which test would you show a client to prove the money is safe?</li></ul></div><div class="lw"><h5>Law</h5><ul><li>Write the test name for “the arbiter may release payment”. Is it in the agreement or only in the code?</li></ul></div></div>

## Ship

<ul class="outc"><li>A Foundry project with three passing tests.</li><li>A screenshot of a failing test after the deliberate change.</li><li>A coverage table.</li></ul>
