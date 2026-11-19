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

<!-- deep:start -->
### In depth

<p>Decentralised finance (DeFi) rebuilds financial services as open contracts. Four building blocks matter most. <b>Stablecoins</b> keep a stable value: fiat-backed ones (USDC, USDT) hold reserves at an issuer; crypto-backed ones (DAI/USDS) are over-collateralised by other tokens; algorithmic ones rely on incentives and failed badly with TerraUSD in 2022. <b>Decentralised exchanges</b> (DEXs) such as Uniswap replace order books with liquidity pools and a pricing formula. <b>Lending protocols</b> such as Aave let users deposit collateral and borrow against it; positions that fall below a safety level are liquidated automatically. <b>MEV</b> (maximal extractable value) is the profit that block builders and bots make by ordering, inserting or front-running transactions.</p>
<p>An automated market maker (AMM) keeps two token reserves, x and y, and enforces <b>x × y = k</b>. A buyer adds one token and removes the other so that the product stays constant. Large trades move the price a lot (<b>slippage</b>); small pools are easy to move, which is why they are dangerous as price oracles.</p>
<!-- diagram:amm -->
<figure class="dg"><div class="sv"><svg viewBox="0 0 720 300" role="img" aria-label="Constant-product AMM curve" xmlns="http://www.w3.org/2000/svg"><defs><marker id="ah-constantproductammcu-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="m-a" d="M0 0L10 5L0 10z"/></marker><marker id="ah-constantproductammcu-ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="m-ar" d="M0 0L10 5L0 10z"/></marker><marker id="ah-constantproductammcu-ag" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="m-ag" d="M0 0L10 5L0 10z"/></marker><marker id="ah-constantproductammcu-am" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="m-am" d="M0 0L10 5L0 10z"/></marker></defs><line class="k-axis" x1="70" y1="260" x2="690" y2="260"/><line class="k-axis" x1="70" y1="260" x2="70" y2="20"/><polyline class="k-curve" points="78.4,76.4 86.8,84.7 95.2,92.5 103.6,99.9 112.0,106.8 120.4,113.3 128.8,119.5 137.2,125.4 145.6,131.0 154.0,136.2 162.4,141.3 170.8,146.1 179.2,150.6 187.6,155.0 196.0,159.2 204.4,163.2 212.8,167.0 221.2,170.6 229.6,174.1 238.0,177.5 246.4,180.7 254.8,183.8 263.2,186.8 271.6,189.7 280.0,192.5 288.4,195.2 296.8,197.8 305.2,200.3 313.6,202.7 322.0,205.0 330.4,207.3 338.8,209.4 347.2,211.5 355.6,213.6 364.0,215.6 372.4,217.5 380.8,219.4 389.2,221.2 397.6,222.9 406.0,224.6 414.4,226.3 422.8,227.9 431.2,229.5 439.6,231.0 448.0,232.5 456.4,233.9 464.8,235.4 473.2,236.7 481.6,238.1 490.0,239.4 498.4,240.6 506.8,241.9 515.2,243.1 523.6,244.3 532.0,245.4 540.4,246.6 548.8,247.7 557.2,248.8 565.6,249.8 574.0,250.8 582.4,251.8 590.8,252.8 599.2,253.8 607.6,254.7 616.0,255.7 624.4,256.6 632.8,257.4 641.2,258.3 649.6,259.2"/><circle class="k-dot" cx="238.0" cy="177.5" r="6"/><circle class="k-dot2" cx="280.0" cy="192.5" r="6"/><text class="tl" x="250.0" y="167.5" text-anchor="start" font-size="12.5">A: 100 ETH · 300,000 USDC</text><text class="tl" x="294.0" y="226.5" text-anchor="start" font-size="12.5">B: 110 ETH · 272,727 USDC</text><text class="tl" x="690" y="286" text-anchor="end" font-size="12.5">ETH in pool →</text><text class="tl" x="62" y="34" text-anchor="end" font-size="12.5">USDC</text><text class="th" x="500" y="70" text-anchor="middle" font-size="14">x × y = k = 30,000,000</text><text class="tl" x="500" y="94" text-anchor="middle" font-size="12.5">Sell 10 ETH → get 27,273 USDC</text></svg></div><figcaption><b>Price is the slope of the curve.</b> A trade moves the pool from A to B along x × y = k. The bigger the trade compared with the pool, the worse the average price (slippage).</figcaption></figure>
<p>Because every DeFi contract can call every other one (“money legos”), new products are built quickly, but risks also spread: a broken oracle or a depegged stablecoin can trigger liquidations across many protocols at once.</p>

### Worked example

<div class="worked">
<p><b>Case:</b> swap in a pool with 100 ETH and 300,000 USDC (k = 30,000,000). Price ≈ 3,000 USDC per ETH. Fees ignored.</p>
<ol>
  <li>A trader sells 10 ETH. New ETH reserve: 110.</li>
  <li>The USDC reserve must become 30,000,000 / 110 = 272,727.</li>
  <li>The trader receives 300,000 − 272,727 = 27,273 USDC, an average of 2,727 per ETH, about 9% below the starting price. That is slippage.</li>
  <li>The new pool price is 272,727 / 110 ≈ 2,479 USDC per ETH. Arbitrageurs will buy cheap ETH here and sell it elsewhere until the price matches other markets.</li>
</ol>
</div>

### Common mistakes

<ul>
  <li>“DeFi has no counterparty risk.” You rely on code, oracles, governance and stablecoin issuers.</li>
  <li>“A stablecoin always equals one dollar.” Only as long as its reserves or mechanism hold.</li>
</ul>
<!-- deep:end -->

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

<div class="aud"><div class="cs"><h5>Technology lens</h5><ul><li>Why can a flash loan be repaid in the same transaction, and what happens if it is not?</li></ul></div><div class="bi"><h5>Business lens</h5><ul><li>A company holds treasury in a stablecoin. List the risks: issuer, freeze, peg, smart contract.</li></ul></div><div class="lw"><h5>Law lens</h5><ul><li>Is providing liquidity to a pool a regulated activity? Who is the counterparty?</li></ul></div></div>

## Ship

<ul class="outc"><li>You can compare three kinds of stablecoins.</li><li>You can calculate a constant-product swap.</li><li>You can explain liquidation, flash loans and a sandwich attack.</li></ul>
