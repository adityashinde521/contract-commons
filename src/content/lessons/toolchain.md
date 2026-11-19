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
