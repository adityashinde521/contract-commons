---
title: "Testing smart contracts"
module: 6
order: 2
kind: "lesson"
minutes: "35 min"
problem: "In the Escrow lab you checked each rule by clicking. A real contract has dozens of rules and changes every week. How do you know every rule still holds?"
---

## Problem

<div class="cc-callout cc-callout--problem"><div><b>The question.</b> In the Escrow lab you checked each rule by clicking. A real contract has dozens of rules and changes every week. How do you know every rule still holds?</div></div>

## Concept

<div class="tw"><table>
<tr><th>Test type</th><th>What it checks</th><th>Example for the Escrow</th></tr>
<tr><td><b>Unit test</b></td><td>One function, one expected result</td><td>After the buyer confirms, the seller has 1 ether more</td></tr>
<tr><td><b>Revert test</b></td><td>A forbidden action fails with the right message</td><td>The seller calling <code>refund</code> reverts with “Only arbiter”</td></tr>
<tr><td><b>Fuzz test</b></td><td>A rule holds for hundreds of random inputs</td><td>Any deposit other than the exact price reverts</td></tr>
<tr><td><b>Invariant test</b></td><td>A property holds after any sequence of calls</td><td>The contract never holds more than the price</td></tr>
<tr><td><b>Integration test</b></td><td>Several contracts together, or a fork of a real network</td><td>The Escrow paying a real token on a mainnet fork</td></tr>
<tr><td><b>Coverage</b></td><td>Which lines the tests ran</td><td><code>forge coverage</code> shows untested branches</td></tr>
</table></div>
<ul>
<li>In Foundry, a <b>cheatcode</b> such as <code>vm.prank(addr)</code> makes the next call come from <code>addr</code>, and <code>vm.expectRevert</code> expects a failure. These replace switching accounts in Remix.</li>
<li>Write the tests from the agreement: every clause that the code enforces should have at least one test. Writing these test cases from the clauses is part of the lab for everyone.</li>
</ul>

### Watch and read

<div class="vids">
<a class="vid read" href="https://book.getfoundry.sh/forge/tests" target="_blank" rel="noopener"><span class="play"></span><span><b>Writing tests</b><small>The Foundry Book</small></span></a>
<a class="vid read" href="https://book.getfoundry.sh/forge/fuzz-testing" target="_blank" rel="noopener"><span class="play"></span><span><b>Fuzz testing</b><small>The Foundry Book</small></span></a>
</div>

## Try it

<p>Take the clause-to-code table from lab <a href="../lab-escrow/">4.3</a>. For each clause, write one test name in plain words, for example “seller cannot refund”. Then do the <a href="../lab-foundry-test/">Foundry lab</a>.</p>

## Apply

<div class="aud"><div class="cs"><h5>Technology lens</h5><ul><li>Which invariant would have caught the reentrancy bug in <a href="/lessons/lab-reentrancy/">7.4 Reentrancy</a>?</li></ul></div><div class="bi"><h5>Business lens</h5><ul><li>Turn a business rule into an acceptance test written in plain language.</li></ul></div><div class="lw"><h5>Law lens</h5><ul><li>Write three test names from a rental agreement. Which clause is impossible to test?</li></ul></div></div>

## Ship

<ul class="outc"><li>You can name five kinds of tests and when to use each.</li><li>You can turn a clause into a test name.</li></ul>
