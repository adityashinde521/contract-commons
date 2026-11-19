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

<!-- deep:start -->
### In depth

<p>A deployed contract usually cannot be fixed, and it holds money. Testing is therefore the main way to gain confidence before launch. Good tests check three kinds of behaviour. <b>Happy paths</b>: the normal flow works (deposit, confirm, seller paid). <b>Failure paths</b>: every forbidden action reverts with the right message (seller confirms, wrong amount, wrong state). <b>Properties</b>: rules that must hold whatever happens, such as “the contract never pays out more than it received”.</p>
<p>Four techniques build on each other. <b>Unit tests</b> call one function with chosen inputs. <b>Fuzz tests</b> let the framework try hundreds of random inputs for a parameter; they find edge cases you did not think of, such as zero or the maximum value. <b>Invariant tests</b> call random sequences of functions and check a property after each one. <b>Fork tests</b> run against a copy of mainnet to see how your contract behaves with real tokens.</p>
<p>A useful habit for this course: derive tests directly from the legal clauses. Every “only”, “must”, “after” and “at most” in the text becomes at least one failure test. This is where the three lenses meet: the lawyer writes the rule, the business analyst names the edge cases, the developer turns both into code.</p>

### Worked example

<div class="worked">
<p><b>Case:</b> clause §4 of the Escrow, “The buyer or the arbiter may release the payment once it is held”.</p>
<div class="tw"><table>
  <tr><th>Test</th><th>Type</th><th>Expectation</th></tr>
  <tr><td>Buyer confirms after deposit</td><td>Unit, happy path</td><td>Seller balance + price; state Complete</td></tr>
  <tr><td>Arbiter confirms after deposit</td><td>Unit, happy path</td><td>Same result</td></tr>
  <tr><td>Seller confirms</td><td>Failure</td><td>Revert “Only buyer or arbiter”</td></tr>
  <tr><td>Buyer confirms before deposit</td><td>Failure</td><td>Revert “Wrong state”</td></tr>
  <tr><td>Any random caller address</td><td>Fuzz</td><td>Reverts unless caller is buyer or arbiter</td></tr>
  <tr><td>After any sequence of calls</td><td>Invariant</td><td>Contract balance is either 0 or exactly price</td></tr>
</table></div>
</div>

### Common mistakes

<ul>
  <li>Testing only the happy path. Most real bugs are actions that should have failed but did not.</li>
  <li>“100% line coverage means no bugs.” Coverage shows which lines ran, not whether the rules are right.</li>
</ul>
<!-- deep:end -->

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
