---
title: "DeFi: stablecoins, exchanges, lending and MEV"
module: 11
order: 1
kind: "lesson"
minutes: "50 min"
problem: "Banks take days to settle a trade; a decentralised exchange settles in seconds with no bank at all. Who carries the risk instead?"
---

## Problem

<div class="cc-callout cc-callout--problem"><div><b>The question.</b> Banks take days to settle a trade; a decentralised exchange settles in seconds with no bank at all. Who carries the risk instead?</div></div>

## Concept

<h3>Stablecoins</h3>
<ul>
<li><b>Fiat-backed</b> (USDC, USDT, EURC): an issuer holds reserves and can freeze tokens. Regulated under MiCA as e-money or asset-referenced tokens in the EU, and under the GENIUS Act in the US.</li>
<li><b>Crypto-collateralised</b> (DAI/USDS): over-collateralised loans in smart contracts keep the peg.</li>
<li><b>Algorithmic</b>: pegs held by incentives alone; TerraUSD collapsed in May 2022.</li>
</ul>
<h3>Decentralised exchanges (DEXs)</h3>
<p>An <b>automated market maker</b> (AMM) such as Uniswap holds two tokens in a pool. The price follows a formula: in the classic design, the product of the two reserves stays constant (<code>x × y = k</code>). Liquidity providers deposit both tokens and earn fees, but face <b>impermanent loss</b> when prices move.</p>
<h3>Lending</h3>
<p>Protocols such as Aave let users borrow against collateral worth more than the loan. If the collateral falls in value, anyone can <b>liquidate</b> the position and earn a bonus. A <b>flash loan</b> is borrowed and repaid within one transaction, with no collateral: useful for arbitrage, and for attacks on weak oracles.</p>
<h3>MEV</h3>
<p><b>Maximal extractable value</b> is the profit available from choosing the order of transactions in a block. In a <b>sandwich</b>, a searcher buys just before a large trade and sells just after it, at the trader’s expense. Proposer-builder separation (and ePBS in Glamsterdam) and private order flow aim to limit the harm.</p>
<div class="cc-callout cc-callout--law"><div><b>Law lens.</b> Is front-running a trade on a DEX market abuse? The EU Market Abuse Regulation covers financial instruments; MiCA has its own market-abuse rules for crypto-assets. Who is the intermediary when there is none?</div></div>

### Watch and read

<div class="vids">
<a class="vid read" href="https://ethereum.org/defi/" target="_blank" rel="noopener"><span class="play"></span><span><b>Decentralised finance</b><small>ethereum.org</small></span></a>
<a class="vid read" href="https://ethereum.org/developers/docs/mev/" target="_blank" rel="noopener"><span class="play"></span><span><b>Maximal extractable value</b><small>ethereum.org</small></span></a>
<a class="vid read" href="https://docs.uniswap.org/concepts/overview" target="_blank" rel="noopener"><span class="play"></span><span><b>How Uniswap works</b><small>Uniswap documentation</small></span></a>
</div>

## Try it

<ol class="steps">
<li>A pool holds 100 ETH and 300,000 USDC, so <code>k = 30,000,000</code>. Someone buys 10 ETH. How much USDC must remain in the pool? (300,000 × 100 / 90.)<span class="exp">About 333,333 USDC, so the buyer paid about 33,333 USDC: 3,333 per ETH instead of 3,000. That gap is price impact.</span></li>
<li>On <a href="https://defillama.com" target="_blank" rel="noopener">DefiLlama</a>, find the largest DEX and the largest lending protocol by value locked.</li>
</ol>

## Apply

<div class="aud"><div class="cs"><h5>Computer science</h5><ul><li>Why can a flash loan be repaid in the same transaction, and what happens if it is not?</li></ul></div><div class="bi"><h5>Business informatics</h5><ul><li>A company holds treasury in a stablecoin. List the risks: issuer, freeze, peg, smart contract.</li></ul></div><div class="lw"><h5>Law</h5><ul><li>Is providing liquidity to a pool a regulated activity? Who is the counterparty?</li></ul></div></div>

## Ship

<ul class="outc"><li>You can compare three kinds of stablecoins.</li><li>You can calculate a constant-product swap.</li><li>You can explain liquidation, flash loans and a sandwich attack.</li></ul>
