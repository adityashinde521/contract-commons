---
title: "Ethereum: accounts, transactions, EVM, gas"
module: 3
order: 1
kind: "lesson"
minutes: "45 min"
legacy: "T5"
problem: "You click transact in Remix and a fee appears. What exactly did you just pay for, and who runs your code?"
---

## Problem

<div class="cc-callout cc-callout--problem"><div><b>The question.</b> You click transact in Remix and a fee appears. What exactly did you just pay for, and who runs your code?</div></div>

## Concept

<div class="goal"><b>Goal:</b> you can explain what happens when you click “transact” in Remix.</div>
    <ul>
      <li>Ethereum is a shared computer. Its state is the balance and storage of all accounts.</li>
      <li><b>EOA</b> (externally owned account): a person with a private key. Only an EOA can start a transaction.</li>
      <li><b>Contract account</b>: has code and storage, no private key. It runs only when called.</li>
      <li>A <b>transaction</b> is a signed message from an EOA: send ETH, deploy a contract, or call a function.</li>
      <li>A call to a <code>view</code> function only reads. It is free and makes no transaction.</li>
      <li>The <b>EVM</b> (Ethereum Virtual Machine) runs contract bytecode. All nodes must get the same result, so code must be deterministic: no random numbers, no internet calls.</li>
      <li><b>Gas</b> measures computation. You pay gas used × gas price in ETH. Storage writes are the most expensive operations.</li>
      <li>If a transaction <b>reverts</b>, all its state changes are undone. You still pay for the gas used.</li>
      <li>1 ether = 10<sup>18</sup> wei. Solidity stores all amounts in wei. 1 gwei = 10<sup>9</sup> wei, used for gas prices.</li>
    </ul>
    <h4>What happens when you click “transact”</h4>
    <ol>
      <li>The wallet builds a transaction: to, value, data (function and arguments), gas limit.</li>
      <li>You sign it with your private key.</li>
      <li>Nodes check the signature and your balance, then a validator puts it in a block.</li>
      <li>Every node runs the code in the EVM and gets the same new state.</li>
      <li>You get a <b>receipt</b>: status (success or revert), gas used, events (logs).</li>
    </ol>
    <h4>Remix VM versus Sepolia</h4>
    <div class="tw"><table>
      <tr><th></th><th>Remix VM</th><th>Sepolia testnet</th><th>Mainnet</th></tr>
      <tr><td>Where</td><td>Your browser</td><td>Public network</td><td>Public network</td></tr>
      <tr><td>Speed</td><td>Instant</td><td>About 12 s per block</td><td>About 12 s per block</td></tr>
      <tr><td>Money</td><td>Fake, 100 ETH per account</td><td>Free test ETH from a faucet</td><td>Real money</td></tr>
      <tr><td>Used in</td><td>Most code labs (Remix VM)</td><td>Sepolia deployment and most tool labs</td><td>Never in this course</td></tr>
    </table></div>

<!-- deep:start -->
### In depth

<p>Ethereum is a single, shared computer. Its state is a table of accounts. <b>Externally owned accounts</b> (EOAs) are controlled by private keys and can start transactions. <b>Contract accounts</b> hold code and storage and run only when called. A transaction is a signed message from an EOA that either moves ETH, deploys a contract, or calls a contract function with some input data.</p>
<p>Every node runs the same transactions in the same order in the <b>Ethereum Virtual Machine</b> (EVM). The EVM executes bytecode, simple instructions such as ADD, SSTORE (write storage) or CALL (call another contract). Because every node must get exactly the same result, the EVM cannot use random numbers, the internet or the clock of the computer it runs on. That is why contracts need oracles for outside data.</p>
<p>Each instruction costs <b>gas</b>. Gas stops endless loops (a transaction must say how much gas it may use, the gas limit) and prices scarce resources. Writing a new value to storage costs about 20,000 gas; an addition costs 3. Since EIP-1559, each block has a <b>base fee</b> per gas that rises when blocks are full and falls when they are empty; the base fee is burned. Users add a <b>priority fee</b> (tip) for the validator.</p>
<!-- diagram:tx-lifecycle -->
<figure class="dg"><div class="sv"><svg viewBox="0 0 720 190" role="img" aria-label="Life of an Ethereum transaction" xmlns="http://www.w3.org/2000/svg"><defs><marker id="ah-lifeofanethereumtran-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="m-a" d="M0 0L10 5L0 10z"/></marker><marker id="ah-lifeofanethereumtran-ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="m-ar" d="M0 0L10 5L0 10z"/></marker><marker id="ah-lifeofanethereumtran-ag" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="m-ag" d="M0 0L10 5L0 10z"/></marker><marker id="ah-lifeofanethereumtran-am" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="m-am" d="M0 0L10 5L0 10z"/></marker></defs><rect class="k-law" x="10" y="40" width="100" height="66" rx="12"/><text class="tb" x="60.0" y="68.5" text-anchor="middle" font-size="13.5">Wallet</text><text class="t" x="60.0" y="87.0" text-anchor="middle" font-size="13.5">signs</text><rect class="k-n" x="128" y="40" width="100" height="66" rx="12"/><text class="tb" x="178.0" y="68.5" text-anchor="middle" font-size="13.5">Mempool</text><text class="t" x="178.0" y="87.0" text-anchor="middle" font-size="13.5">waits</text><line class="k-a" x1="110" y1="73" x2="126" y2="73" marker-end="url(#ah-lifeofanethereumtran-a)"/><rect class="k-bi" x="246" y="40" width="100" height="66" rx="12"/><text class="tb" x="296.0" y="68.5" text-anchor="middle" font-size="13.5">Proposer</text><text class="t" x="296.0" y="87.0" text-anchor="middle" font-size="13.5">orders</text><line class="k-a" x1="228" y1="73" x2="244" y2="73" marker-end="url(#ah-lifeofanethereumtran-a)"/><rect class="k-cs" x="364" y="40" width="100" height="66" rx="12"/><text class="tb" x="414.0" y="68.5" text-anchor="middle" font-size="13.5">EVM</text><text class="t" x="414.0" y="87.0" text-anchor="middle" font-size="13.5">runs, gas</text><line class="k-a" x1="346" y1="73" x2="362" y2="73" marker-end="url(#ah-lifeofanethereumtran-a)"/><rect class="k-brand" x="482" y="40" width="100" height="66" rx="12"/><text class="tb" x="532.0" y="68.5" text-anchor="middle" font-size="13.5">Included</text><text class="t" x="532.0" y="87.0" text-anchor="middle" font-size="13.5">≈ 12 s</text><line class="k-a" x1="464" y1="73" x2="480" y2="73" marker-end="url(#ah-lifeofanethereumtran-a)"/><rect class="k-brand" x="600" y="40" width="100" height="66" rx="12"/><text class="tb" x="650.0" y="68.5" text-anchor="middle" font-size="13.5">Final</text><text class="t" x="650.0" y="87.0" text-anchor="middle" font-size="13.5">≈ 13 min</text><line class="k-a" x1="582" y1="73" x2="598" y2="73" marker-end="url(#ah-lifeofanethereumtran-a)"/><text class="tl" x="360" y="140" text-anchor="middle" font-size="13">Revert in the EVM: state changes are undone, gas used is still paid.</text><text class="tl" x="360" y="165" text-anchor="middle" font-size="13">Fee = gas used × (base fee, burned + priority fee, to validator)</text></svg></div><figcaption><b>From click to finality.</b> The wallet signs locally, the transaction waits in the mempool, a validator includes it, every node runs it in the EVM, and after about 13 minutes it is final.</figcaption></figure>

### Worked example

<div class="worked">
<p><b>Case:</b> what does calling <code>deposit()</code> on the Escrow cost?</p>
<ol>
  <li>The transaction uses 50,000 gas (one storage write for the state, one event, checks).</li>
  <li>The base fee is 8 gwei, and the user offers a priority fee of 1 gwei. 1 gwei = 0.000000001 ETH.</li>
  <li>Fee = 50,000 × (8 + 1) gwei = 450,000 gwei = 0.00045 ETH.</li>
  <li>At an ETH price of 3,000 EUR, that is 1.35 EUR. Of this, 0.0004 ETH is burned and 0.00005 ETH goes to the validator.</li>
  <li>If the transaction reverts halfway (wrong sender), the user still pays for the gas used up to the revert, but the state does not change.</li>
</ol>
<p>On a rollup the same call often costs a few cents, because the expensive part (posting data to Ethereum) is shared by many users.</p>
</div>

### Common mistakes

<ul>
  <li>“Gas is a token.” Gas is a unit of work. You pay for it in ETH.</li>
  <li>“A higher gas limit costs more.” You pay for gas <i>used</i>; unused gas is not charged.</li>
  <li>“Reading a contract costs gas.” Calling a view function from outside is free; only transactions cost gas.</li>
</ul>
<!-- deep:end -->

### Watch and read

<div class="vids">
      <a class="vid" href="https://ethereum.org/videos/ethereum-basics-intro/" target="_blank" rel="noopener"><span class="play"></span><span><b>Ethereum basics: intro</b><small>11 min</small></span></a>
      <a class="vid" href="https://ethereum.org/videos/transactions-eth-build/" target="_blank" rel="noopener"><span class="play"></span><span><b>Transactions</b><small>ETH.BUILD, 6 min</small></span></a>
      <a class="vid read" href="https://ethereum.org/gas/" target="_blank" rel="noopener"><span class="play"></span><span><b>Gas fees</b><small>ethereum.org article</small></span></a>
    </div>

## Try it

<p>Do labs <a href="../lab-remix-tour/">3.4 Remix tour</a> and <a href="../lab-simple-storage/">3.5 SimpleStorage</a> right after this lesson. Watch the gas field of every transaction.</p>

## Apply

<div class="aud"><div class="cs"><h5>Technology lens</h5><ul><li>Why must contract code be deterministic?</li></ul></div><div class="bi"><h5>Business lens</h5><ul><li>Estimate the cost of 1,000 transactions at 30 gwei and 50,000 gas each.</li></ul></div><div class="lw"><h5>Law lens</h5><ul><li>A transaction reverts but the fee is still paid. Is that fair to a consumer?</li></ul></div></div>

## Ship

<p>Write three sentences in your lab log: the main idea, one example for each lens (technology, business, law), and one open question. Then take the quiz below.</p>
