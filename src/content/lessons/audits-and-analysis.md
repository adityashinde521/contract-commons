---
title: "Audits, static analysis and fuzzing"
module: 7
order: 3
kind: "lesson"
minutes: "30 min"
problem: "A startup will hold €2 million in a new contract next month. How do professionals find the bugs before attackers do?"
---

## Problem

<div class="cc-callout cc-callout--problem"><div><b>The question.</b> A startup will hold €2 million in a new contract next month. How do professionals find the bugs before attackers do?</div></div>

## Concept

<div class="tw"><table>
<tr><th>Method</th><th>What it does</th><th>Tools</th></tr>
<tr><td><b>Static analysis</b></td><td>Reads the code without running it and flags known bug patterns</td><td>Slither, Aderyn, the Solidity compiler’s warnings</td></tr>
<tr><td><b>Fuzzing and invariants</b></td><td>Runs the contract with many random inputs and call sequences</td><td>Foundry fuzz and invariant tests, Echidna, Medusa</td></tr>
<tr><td><b>Symbolic execution and formal verification</b></td><td>Proves a property for all inputs, or finds a counterexample</td><td>SMTChecker, Halmos, Certora Prover</td></tr>
<tr><td><b>AI-assisted review</b></td><td>Language models suggest likely bugs; every finding must be checked by hand</td><td>Coding assistants, specialised tools</td></tr>
<tr><td><b>Manual audit</b></td><td>Experienced reviewers read the code against the specification</td><td>Audit firms, contests (for example Code4rena, Sherlock)</td></tr>
<tr><td><b>Bug bounty</b></td><td>Rewards outside researchers who report bugs after launch</td><td>Immunefi and similar platforms</td></tr>
</table></div>
<ul>
<li>No single method finds everything. Research in 2025 found that AI tools do not yet replace classic analysers, and hybrids work best (Module 13, research).</li>
<li>An audit report lists findings by severity (critical, high, medium, low, informational) and states what was <b>out of scope</b>. Read that part first.</li>
</ul>
<div class="cc-callout cc-callout--law"><div><b>Law lens.</b> An audit is not a guarantee. Audit contracts usually limit liability to the fee. If a protocol says “audited” in its marketing and is then hacked, can users rely on that statement?</div></div>

<!-- deep:start -->
### In depth

<p>Before a contract holds real money, professionals combine several methods, because each one finds different problems. <b>Manual review</b> by experienced auditors finds logic and design flaws that tools cannot understand, such as an unfair liquidation rule. <b>Static analysis</b> (Slither, Aderyn) scans the source for known patterns, such as reentrancy or unchecked return values, in seconds; it reports many false positives. <b>Symbolic execution and formal verification</b> (Mythril, Certora, Halmos) try to prove that a property holds for all inputs, or produce a counterexample. <b>Fuzzing and invariant testing</b> attack the contract with random sequences.</p>
<p>Audits end in a <b>report</b>: each finding has a title, a severity (critical, high, medium, low, informational), a description of the impact and a recommended fix, and the team’s response. After launch, <b>bug bounties</b> (for example on Immunefi) pay outside researchers to report issues instead of exploiting them, and <b>audit contests</b> let many auditors compete for a fixed prize pool.</p>
<p>AI tools are now part of the toolbox. Research in 2025 found that language models are useful for explaining code and proposing hypotheses, but not yet reliable enough to replace classic analysers; combinations work best. Every AI finding must be confirmed by a test.</p>

### Worked example

<div class="worked">
<p><b>Case:</b> plan the security budget for a contract that will hold €2 million.</p>
<ol>
  <li>Internal: full test suite with fuzz and invariant tests; Slither in CI. Cost: team time.</li>
  <li>One independent audit by a firm, about two to four weeks. Typical prices are tens of thousands of euros for a small codebase.</li>
  <li>Fix findings, then a short re-review of the fixes.</li>
  <li>Launch with limits: a deposit cap of €200,000 for the first month and a pause switch held by a multisig.</li>
  <li>Bug bounty: for example 10% of funds at risk, capped, for critical findings.</li>
</ol>
<p><b>Reasoning:</b> spending 3–5% of the value at risk on security is common; losing it all is the alternative.</p>
</div>

### Common mistakes

<ul>
  <li>“An audit is a guarantee.” It is a time-limited review of one version of the code.</li>
  <li>Changing code after the audit without a new review.</li>
</ul>
<!-- deep:end -->

### Watch and read

<div class="vids">
<a class="vid read" href="https://github.com/crytic/slither" target="_blank" rel="noopener"><span class="play"></span><span><b>Slither</b><small>Trail of Bits, static analyser</small></span></a>
<a class="vid read" href="https://github.com/crytic/echidna" target="_blank" rel="noopener"><span class="play"></span><span><b>Echidna</b><small>Trail of Bits, fuzzer</small></span></a>
<a class="vid read" href="https://docs.soliditylang.org/en/latest/smtchecker.html" target="_blank" rel="noopener"><span class="play"></span><span><b>SMTChecker</b><small>Solidity documentation</small></span></a>
</div>

## Try it

<p>In your Foundry project from the Foundry lab, add <code>VulnerableBank</code> from lab <a href="/lessons/lab-reentrancy/">7.4 Reentrancy</a> to <code>src/</code>, install Slither (<code>pip install slither-analyzer</code>) and run <code>slither .</code>.<span class="exp" style="display:block">A finding named <code>reentrancy-eth</code> pointing to <code>withdraw</code>.</span> Everyone: open a public audit report from an audit firm’s website and find its scope and its highest-severity finding.</p>

## Apply

<div class="aud"><div class="cs"><h5>Technology lens</h5><ul><li>Which property of the Escrow would you give to a formal verifier?</li></ul></div><div class="bi"><h5>Business lens</h5><ul><li>Budget for security: audit, contest, bounty. What would you spend for €2 million at risk?</li></ul></div><div class="lw"><h5>Law lens</h5><ul><li>Draft the scope and limitation-of-liability clause of an audit contract.</li></ul></div></div>

## Ship

<ul class="outc"><li>You can name six ways to find bugs and their limits.</li><li>You can read the scope and severity sections of an audit report.</li></ul>
