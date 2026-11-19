---
title: "Read the chain with Etherscan"
module: 2
order: 3
kind: "lab-gui"
minutes: "40 min"
problem: "Everything on Ethereum is public, but only if you can read it. A block explorer is the first tool every analyst, auditor and lawyer needs."
---

## Problem

<div class="cc-callout cc-callout--problem"><div><b>The question.</b> Everything on Ethereum is public, but only if you can read it. A block explorer is the first tool every analyst, auditor and lawyer needs.</div></div>

## Concept

<div class="ov"><div><b>You will</b>Read blocks, transactions, addresses and a token contract on Ethereum mainnet.</div><div><b>Tool</b><a href="https://etherscan.io" target="_blank" rel="noopener">Etherscan</a>, the most used Ethereum block explorer.</div><div><b>You need</b>A browser. Read only: no wallet, nothing to sign.</div></div>

## Build

<div class="checked"><b>Checked on 20 November 2026</b> against the tool’s official documentation. Tools change their screens often. If a button has a different name, look for the closest one and note the difference in your lab log.</div>

<h3>A. A block</h3>
<ol class="steps">
<li>Open <a href="https://etherscan.io/blocks" target="_blank" rel="noopener">etherscan.io/blocks</a> and click the newest block.<span class="exp">Block height, timestamp, number of transactions, fee recipient, gas used and gas limit, base fee.</span></li>
<li>Note the gas used as a percentage of the gas limit.<span class="why">Ethereum adjusts the base fee up when blocks are more than half full and down when less.</span><span class="exp">A number such as 15,000,000 (50%). Ethereum targets about half-full blocks; fuller blocks raise the base fee.</span></li>
</ol>
<h3>B. A transaction</h3>
<ol class="steps">
<li>Open any transaction from that block.<span class="exp">Status, from, to, value, transaction fee, gas price.</span></li>
<li>Find one transaction that calls a contract (the “To” field is a contract). Open <span class="ui">Logs</span>.<span class="exp">Decoded events, for example <code>Transfer</code>.</span></li>
<li>Click <span class="ui">More details</span> and find the input data.<span class="exp">The function called and its arguments, decoded if the contract is verified.</span></li>
</ol>
<h3>C. A token contract</h3>
<ol class="steps">
<li>Search for a large stablecoin (for example USDC). Open its token page.<span class="exp">The token page shows total supply, number of holders, the contract address with a green check (verified) and a list of recent transfers.</span></li>
<li>Open the <span class="ui">Contract</span> tab, then <span class="ui">Read as Proxy</span> if offered.<span class="exp">Functions such as <code>totalSupply</code>, <code>balanceOf</code>, and admin roles.</span></li>
<li>Look for functions such as <code>blacklist</code> or <code>pause</code>.<span class="exp">Some regulated stablecoins can freeze addresses. This is a business and legal choice written into code.</span></li>
</ol>

## Apply

<div class="aud"><div class="cs"><h5>Technology lens</h5><ul><li>Why can Etherscan decode input data only for verified contracts?</li></ul></div><div class="bi"><h5>Business lens</h5><ul><li>Calculate the fee of one transaction in euros at today’s ETH price.</li></ul></div><div class="lw"><h5>Law lens</h5><ul><li>An issuer can freeze tokens. Is that compatible with “ownership”? What does MiCA say about issuer obligations?</li></ul></div></div>

## Ship

<ul class="outc"><li>You can read a block, a transaction and its events.</li><li>You can find a contract’s admin powers.</li></ul>
<div class="callout lab"><h5>Lab log</h5><p>Links to the block and transactions you read, the fee calculation and the admin functions you found.</p></div>
