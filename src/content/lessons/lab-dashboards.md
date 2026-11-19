---
title: "Research with on-chain dashboards"
module: 10
order: 4
kind: "lab-gui"
minutes: "60 min"
legacy: "G11"
problem: "A claim in a paper or a pitch says “most losses come from key theft” or “this rollup is decentralised”. How do you check it with data?"
---

## Problem

<div class="cc-callout cc-callout--problem"><div><b>The question.</b> A claim in a paper or a pitch says “most losses come from key theft” or “this rollup is decentralised”. How do you check it with data?</div></div>

## Concept

<div class="ov">
      <div><b>You will</b>Use public dashboards to answer research questions with data, and judge the quality of that data.</div>
      <div><b>Tools</b><a href="https://dune.com" target="_blank" rel="noopener">Dune</a> (SQL dashboards on blockchain data), <a href="https://l2beat.com" target="_blank" rel="noopener">L2BEAT</a> (risk analysis of rollups), <a href="https://defillama.com" target="_blank" rel="noopener">DefiLlama</a> (value locked, fees, hacks).</div>
      <div><b>You need</b>A browser. A free Dune account if you want to edit queries.</div>
    </div>

## Build

<h4>A. L2BEAT: who controls a rollup? (<a href="/lessons/ethereum-today/">10.1 Ethereum today</a>)</h4>
    <ol class="steps">
      <li>Open <a href="https://l2beat.com" target="_blank" rel="noopener">l2beat.com</a>. Sort the scaling list by value secured.</li>
      <li>Open two rollups with different <b>stages</b> (0, 1 or 2).<span class="exp">A risk summary and sections on upgrades, permissions and exit windows.</span></li>
      <li>For each, note: who can upgrade the contracts, how fast, and whether users can leave before an upgrade.</li>
    </ol>
    <h4>B. DefiLlama: losses over time (<a href="/lessons/security-in-practice/">7.2 Security in practice</a>)</h4>
    <ol class="steps">
      <li>Open <a href="https://defillama.com" target="_blank" rel="noopener">defillama.com</a> and find its hacks section.</li>
      <li>Filter by 2025. Find Bybit and GMX.<span class="exp">Amount, date, chain, technique.</span></li>
      <li>Compare totals by technique. Does the data support the claim in <a href="/lessons/security-in-practice/">7.2 Security in practice</a> that operations cause more losses than code bugs?</li>
    </ol>
    <h4>C. Dune: build one chart</h4>
    <ol class="steps">
      <li>Open <a href="https://dune.com" target="_blank" rel="noopener">dune.com</a> and search the dashboards for a topic: for example stablecoin supply, Ethereum gas or a rollup’s activity.</li>
      <li>Open one chart and click through to its query.<span class="exp">The SQL behind the chart. Every number has a visible source.</span></li>
      <li>With a free account, fork the query, change one parameter (for example the date range), and add the chart to your own dashboard.</li>
    </ol>

## Apply

<div class="aud">
      <div class="cs"><h5>Technology lens</h5><ul><li>Dashboards depend on how raw data is decoded. How can a chart be wrong even if the chain is correct?</li></ul></div>
      <div class="bi"><h5>Business lens</h5><ul><li>Is “total value locked” a good measure of business success? What would you measure instead?</li></ul></div>
      <div class="lw"><h5>Law lens</h5><ul><li>A rollup at stage 0 can be upgraded by a small group at any time. Who is the “operator” for MiCA or liability purposes?</li></ul></div>
    </div>

## Ship

<ul class="outc">
      <li>You can find, read and question public blockchain data.</li>
      <li>You can explain rollup risk in terms of upgrade powers and exit windows.</li>
      <li>You have one chart for your capstone or seminar paper.</li>
    </ul>
    <div class="callout lab"><h5>Lab log</h5><p>One research question, the chart or table that answers it, its source link, and one limitation of the data.</p></div>
