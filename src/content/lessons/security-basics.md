---
title: "Security basics"
module: 7
order: 1
kind: "lesson"
minutes: "40 min"
legacy: "T8"
problem: "In 2016 an attacker took about a third of the funds in The DAO using the contract exactly as written. Which four mistakes cause most such losses?"
---

## Problem

<div class="cc-callout cc-callout--problem"><div><b>The question.</b> In 2016 an attacker took about a third of the funds in The DAO using the contract exactly as written. Which four mistakes cause most such losses?</div></div>

## Concept

<div class="goal"><b>Goal:</b> you can name four common bugs and the defence for each.</div>
    <div class="tw"><table>
      <tr><th>Bug</th><th>What happens</th><th>Defence</th></tr>
      <tr><td>Reentrancy</td><td>The contract sends ETH before it updates state. The receiver calls back and withdraws again.</td><td>Checks-effects-interactions, or OpenZeppelin <code>ReentrancyGuard</code>. Lab L6.</td></tr>
      <tr><td>Missing access control</td><td>Anyone can call an admin function, for example <code>withdraw</code> or <code>mint</code>.</td><td>Check <code>msg.sender</code> or use <code>Ownable</code>. Lab L5.</td></tr>
      <tr><td><code>tx.origin</code> authentication</td><td>A malicious contract tricks the user into calling it, then acts with the user’s authority.</td><td>Use <code>msg.sender</code>.</td></tr>
      <tr><td>Oracle manipulation</td><td>The contract trusts one bad price or data source.</td><td>Use several sources or a trusted oracle network.</td></tr>
    </table></div>
    <p>Bugs cost real money because code is public and immutable. Audits, tests and bug bounties are standard practice. In 2025, most large losses came from operations (stolen keys, tricked signers) rather than code bugs: see F5.</p>
    <div class="callout law"><h5>Law lens</h5><p>The DAO attacker in 2016 used the code exactly as written. Was it theft? Prosecutors have since charged people for similar “code exploits”, for example in the US Mango Markets case, with mixed results in court. The idea “code is law” is a good topic for debate, not a legal defence.</p></div>

### Watch and read

<div class="vids">
      <a class="vid" href="https://www.youtube.com/watch?v=4Mm3BCyHtDY" target="_blank" rel="noopener"><span class="play"></span><span><b>Reentrancy (Hack Solidity)</b><small>Smart Contract Programmer</small></span></a>
      <a class="vid" href="https://ethereum.org/videos/dao-hack-ethereum-classic/" target="_blank" rel="noopener"><span class="play"></span><span><b>The DAO hack: story of Ethereum Classic</b><small>10 min</small></span></a>
      <a class="vid read" href="https://consensys.github.io/smart-contract-best-practices/attacks/reentrancy/" target="_blank" rel="noopener"><span class="play"></span><span><b>Best practices: reentrancy</b><small>ConsenSys article</small></span></a>
    </div>

## Try it

<p>Read the vulnerable <code>withdraw</code> function in <a href="../lab-reentrancy/">lab L6</a> and write, in one sentence, the order in which it should do its three steps. Then run the lab.</p>

## Apply

<div class="aud"><div class="cs"><h5>Technology lens</h5><ul><li>Which defence would you add first to a new contract, and why?</li></ul></div><div class="bi"><h5>Business lens</h5><ul><li>Compare the cost of an audit with the funds at risk.</li></ul></div><div class="lw"><h5>Law lens</h5><ul><li>Was the DAO attacker a thief or a user of the code as written?</li></ul></div></div>

## Ship

<p>Write three sentences in your lab log: the main idea, one example for each lens (technology, business, law), and one open question. Then take the quiz below.</p>
