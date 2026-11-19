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

### Watch and read

<div class="vids">
<a class="vid read" href="https://github.com/crytic/slither" target="_blank" rel="noopener"><span class="play"></span><span><b>Slither</b><small>Trail of Bits, static analyser</small></span></a>
<a class="vid read" href="https://github.com/crytic/echidna" target="_blank" rel="noopener"><span class="play"></span><span><b>Echidna</b><small>Trail of Bits, fuzzer</small></span></a>
<a class="vid read" href="https://docs.soliditylang.org/en/latest/smtchecker.html" target="_blank" rel="noopener"><span class="play"></span><span><b>SMTChecker</b><small>Solidity documentation</small></span></a>
</div>

## Try it

<p>Code track: in your Foundry project from the Foundry lab, add <code>VulnerableBank</code> from lab L6 to <code>src/</code>, install Slither (<code>pip install slither-analyzer</code>) and run <code>slither .</code>.<span class="exp" style="display:block">A finding named <code>reentrancy-eth</code> pointing to <code>withdraw</code>.</span> Everyone: open a public audit report from an audit firm’s website and find its scope and its highest-severity finding.</p>

## Apply

<div class="aud"><div class="cs"><h5>Computer science</h5><ul><li>Which property of the Escrow would you give to a formal verifier?</li></ul></div><div class="bi"><h5>Business informatics</h5><ul><li>Budget for security: audit, contest, bounty. What would you spend for €2 million at risk?</li></ul></div><div class="lw"><h5>Law</h5><ul><li>Draft the scope and limitation-of-liability clause of an audit contract.</li></ul></div></div>

## Ship

<ul class="outc"><li>You can name six ways to find bugs and their limits.</li><li>You can read the scope and severity sections of an audit report.</li></ul>
