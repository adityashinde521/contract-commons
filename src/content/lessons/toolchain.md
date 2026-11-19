---
title: "From Remix to a professional toolchain"
module: 6
order: 1
kind: "lesson"
minutes: "30 min"
problem: "Remix is great for learning, but a real project has many files, a team, tests and reviews. What do professionals use instead?"
---

## Problem

<div class="cc-callout cc-callout--problem"><div><b>The question.</b> Remix is great for learning, but a real project has many files, a team, tests and reviews. What do professionals use instead?</div></div>

## Concept

<div class="tw"><table>
<tr><th>Tool</th><th>What it is</th><th>When to use it</th></tr>
<tr><td><b>Remix</b></td><td>Browser IDE with compiler, deployer and debugger</td><td>Learning, quick experiments, demos (the code labs)</td></tr>
<tr><td><b>Foundry</b></td><td>Command-line toolkit: <code>forge</code> (build, test), <code>cast</code> (call chains), <code>anvil</code> (local chain). Tests in Solidity.</td><td>Most new professional projects; fast tests and fuzzing</td></tr>
<tr><td><b>Hardhat</b></td><td>JavaScript and TypeScript toolkit with plugins and a local network</td><td>Teams with a web or TypeScript background</td></tr>
<tr><td><b>Git and GitHub</b></td><td>Version control and code review</td><td>Always: every change reviewed, every release tagged</td></tr>
<tr><td><b>VS Code</b> + Solidity extension</td><td>Editor with syntax checks</td><td>Daily work</td></tr>
<tr><td>Truffle, Brownie</td><td>Earlier frameworks, no longer maintained</td><td>Reading old projects only</td></tr>
</table></div>
<ul>
<li><b>Vyper</b> is a second EVM language with Python-like syntax and fewer features by design. Solidity remains the most used.</li>
<li>Typical project layout (Foundry): <code>src/</code> contracts, <code>test/</code> tests, <code>script/</code> deployment scripts, <code>foundry.toml</code> settings.</li>
</ul>

<!-- deep:start -->
### In depth

<p>Remix is ideal for learning: everything runs in the browser, deployment is a button, and the debugger shows each step. Professional teams work differently, because they need version control, repeatable builds, automated tests and scripted deployments. The usual toolchain has four parts. A <b>framework</b> (Foundry or Hardhat) compiles contracts, runs tests and executes deployment scripts. <b>Git</b> keeps every version and makes code review possible. <b>Libraries</b> such as OpenZeppelin Contracts provide audited building blocks. <b>Explorers and services</b> (Etherscan, Tenderly) verify and monitor what is deployed.</p>
<p><b>Foundry</b> writes tests in Solidity itself and is very fast; it includes <code>forge</code> (build and test), <code>cast</code> (talk to a chain from the command line) and <code>anvil</code> (a local chain). <b>Hardhat</b> writes tests and scripts in JavaScript or TypeScript, which suits teams that also build the web front end. Both can <b>fork</b> mainnet: run a local copy of the real chain state, so you can test your contract against real tokens and protocols without spending anything.</p>
<p>A deployment is not finished until the source is <b>verified</b>: the explorer recompiles your source with the same compiler settings and checks that the bytecode matches. Only then can users read what they interact with.</p>

### Worked example

<div class="worked">
<p><b>Case:</b> the life of one change in a team.</p>
<ol>
  <li>A developer creates a Git branch and adds a fee to the Escrow.</li>
  <li><code>forge test</code> runs 30 tests locally in two seconds; one old test fails because the seller now receives price minus fee. She updates the test on purpose.</li>
  <li>She opens a pull request. A colleague reviews the diff; CI runs the tests and a static analyser (Slither) automatically.</li>
  <li>After approval, <code>forge script</code> deploys to Sepolia and verifies the source on Etherscan in one command.</li>
  <li>Only after a testnet trial and, for real funds, an audit does the same script run against mainnet.</li>
</ol>
</div>

### Common mistakes

<ul>
  <li>“Remix is not professional.” It is excellent for exploring and debugging; it is just not enough for a team process.</li>
  <li>Deploying with a private key pasted into a script file that ends up on GitHub. Use encrypted keystores or hardware wallets.</li>
</ul>
<!-- deep:end -->

### Watch and read

<div class="vids">
<a class="vid read" href="https://book.getfoundry.sh" target="_blank" rel="noopener"><span class="play"></span><span><b>The Foundry Book</b><small>Official documentation</small></span></a>
<a class="vid read" href="https://hardhat.org/docs" target="_blank" rel="noopener"><span class="play"></span><span><b>Hardhat documentation</b><small>Official documentation</small></span></a>
<a class="vid read" href="https://docs.vyperlang.org" target="_blank" rel="noopener"><span class="play"></span><span><b>Vyper documentation</b><small>Official documentation</small></span></a>
</div>

## Try it

<p>Read the Foundry Book chapter “Getting started”. Install Foundry (the <a href="../lab-foundry-test/">Foundry lab</a> needs it). Run <code>forge --version</code>.</p>

## Apply

<div class="aud"><div class="cs"><h5>Technology lens</h5><ul><li>Why are tests written in Solidity (Foundry) faster to run than tests in JavaScript?</li></ul></div><div class="bi"><h5>Business lens</h5><ul><li>Which tool choices reduce the risk of a project depending on one developer?</li></ul></div><div class="lw"><h5>Law lens</h5><ul><li>Git history shows who changed what and when. Could it serve as evidence in a dispute about a bug?</li></ul></div></div>

## Ship

<ul class="outc"><li>You can choose between Remix, Foundry and Hardhat for a task.</li><li>You know which old tools not to start with.</li></ul>
