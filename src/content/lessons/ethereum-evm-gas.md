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
      <tr><td>Used in</td><td>L1–L6</td><td>L7, G1–G8</td><td>Never in this course</td></tr>
    </table></div>

### Watch and read

<div class="vids">
      <a class="vid" href="https://ethereum.org/videos/ethereum-basics-intro/" target="_blank" rel="noopener"><span class="play"></span><span><b>Ethereum basics: intro</b><small>11 min</small></span></a>
      <a class="vid" href="https://ethereum.org/videos/transactions-eth-build/" target="_blank" rel="noopener"><span class="play"></span><span><b>Transactions</b><small>ETH.BUILD, 6 min</small></span></a>
      <a class="vid read" href="https://ethereum.org/gas/" target="_blank" rel="noopener"><span class="play"></span><span><b>Gas fees</b><small>ethereum.org article</small></span></a>
    </div>

## Try it

<p>Do labs <a href="../lab-remix-tour/">L0 Remix tour</a> and <a href="../lab-simple-storage/">L1 SimpleStorage</a> right after this lesson. Watch the gas field of every transaction.</p>

## Apply

<div class="aud"><div class="cs"><h5>Computer science</h5><ul><li>Why must contract code be deterministic?</li></ul></div><div class="bi"><h5>Business informatics</h5><ul><li>Estimate the cost of 1,000 transactions at 30 gwei and 50,000 gas each.</li></ul></div><div class="lw"><h5>Law</h5><ul><li>A transaction reverts but the fee is still paid. Is that fair to a consumer?</li></ul></div></div>

## Ship

<p>Write three sentences in your lab log: the main idea, one example from your discipline, and one open question. Then take the quiz below.</p>
