---
title: "Remix setup and tour"
module: 3
order: 4
kind: "lab-remix"
minutes: "20 min"
legacy: "L0"
problem: "Before you write a contract you need a place to run it safely. Remix gives you a complete blockchain in your browser."
---

## Problem

<div class="cc-callout cc-callout--problem"><div><b>The question.</b> Before you write a contract you need a place to run it safely. Remix gives you a complete blockchain in your browser.</div></div>

## Concept

<div class="ov">
      <div><b>You will</b>Open Remix, create a workspace and find the four panels used in every lab.</div>
      <div><b>Before</b>Setup and safety. Lesson 3.1 recommended.</div>
      <div><b>You produce</b>A workspace named <code>course-labs</code>, backed up to GitHub.</div>
    </div>
    <h4>Remix in one paragraph</h4>
    <p>Remix is a complete development environment that runs in the browser. You write Solidity in the editor, compile it, then deploy it to a simulated chain (Remix VM) or, through MetaMask, to a real network. Nothing to install.</p>

## Build

<div class="checked"><b>Checked on 20 November 2026.</b> The contract code in this lab compiles with Solidity 0.8.24 to 0.8.30. Remix screens change between releases: if a label differs, look for the closest one and note it in your lab log.</div>

<ol class="steps">
      <li>Open <a href="https://remix.ethereum.org" target="_blank" rel="noopener">remix.ethereum.org</a>. Close any welcome pop-ups.<span class="exp">Editor in the middle, icon bar on the far left, terminal at the bottom.</span></li>
      <li>Click the <span class="ui">File explorer</span> icon (top of the left bar). Open the workspace menu, choose <span class="ui">Create blank workspace</span>, name it <code>course-labs</code>.<span class="exp">An empty workspace. Remix may add a few default folders.</span></li>
      <li>Click the <span class="ui">Solidity compiler</span> icon. Choose compiler <b>0.8.24 or newer</b>. Tick <span class="ui">Auto compile</span>.<span class="why">All lab contracts start with <code>pragma solidity ^0.8.24;</code>.</span><span class="exp">A green check on the compiler icon after each save. Errors appear in red under the compile button.</span></li>
      <li>Click the <span class="ui">Deploy &amp; run transactions</span> icon (the Ethereum logo). Under <span class="ui">Environment</span> choose a <b>Remix VM</b> option (for example “Remix VM (Prague)”).<span class="exp">The <span class="ui">Account</span> list shows several addresses with 100 ETH each.</span></li>
      <li>Find these fields in the same panel, top to bottom: <span class="ui">Account</span>, <span class="ui">Gas limit</span>, <span class="ui">Value</span> (with a unit selector: Wei, Gwei, Finney, Ether), <span class="ui">Contract</span>, <span class="ui">Deploy</span>.<span class="why">Almost every lab error comes from the Account or the Value field.</span><span class="exp">Account shows 0x5B38… with 100 ether in the Remix VM; Value shows 0 and Wei.</span></li>
      <li>Look at the <b>terminal</b> at the bottom. Later, each transaction appears there. Click a line to see status, gas, input and logs.<span class="exp">An empty terminal with a welcome text. After the next deploy, a line with a green check and “[vm] from: 0x5B3… to: … value: 0 wei”.</span></li>
      <li>Optional: connect the workspace to GitHub (<span class="ui">File explorer → Git</span>) or download it as a ZIP after each lab.<span class="exp">A ZIP file in your downloads, or a Git panel with your first commit.</span></li>
    </ol>

## Ship

<ul class="outc">
      <li>You can name the four panels: file explorer, compiler, deploy &amp; run, terminal.</li>
      <li>You know where Account and Value are, and why they matter.</li>
      <li>You know that the Remix VM resets when you reload the page.</li>
    </ul>
