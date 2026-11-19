---
title: "Solidity for programmers"
module: 4
order: 2
kind: "lesson"
minutes: "60 min"
legacy: "T7"
problem: "You know Java or Python. Which habits work in Solidity, and which ones will cost real money?"
---

## Problem

<div class="cc-callout cc-callout--problem"><div><b>The question.</b> You know Java or Python. Which habits work in Solidity, and which ones will cost real money?</div></div>

## Concept

<div class="goal"><b>Goal:</b> you can read all lab contracts and know where Solidity differs from languages you know. (Code track.)</div>
    <div class="tw"><table>
      <tr><th>Solidity</th><th>Similar to</th><th>Important difference</th></tr>
      <tr><td><code>contract</code></td><td>class</td><td>One instance per deployment, with its own address and balance.</td></tr>
      <tr><td>state variable</td><td>field</td><td>Stored on chain. Each write costs gas.</td></tr>
      <tr><td><code>mapping(address =&gt; uint)</code></td><td>hash map</td><td>All keys exist with default 0. You cannot iterate.</td></tr>
      <tr><td><code>constructor</code></td><td>constructor</td><td>Runs one time, at deployment. Its arguments are filled in the Deploy fields.</td></tr>
      <tr><td><code>modifier</code></td><td>decorator</td><td><code>_;</code> marks where the function body runs.</td></tr>
      <tr><td><code>require(cond, "msg")</code></td><td>guard + throw</td><td>Reverts all changes of the transaction. The message appears in Remix.</td></tr>
      <tr><td><code>event</code> / <code>emit</code></td><td>log</td><td>Off-chain apps read them. Contracts cannot.</td></tr>
      <tr><td><code>enum</code></td><td>enum</td><td>Use it for a state machine (L2). Remix shows values as numbers 0, 1, 2…</td></tr>
    </table></div>
    <h4>Special words</h4>
    <ul>
      <li><code>msg.sender</code>: the caller. <code>msg.value</code>: wei sent; the function must be <code>payable</code>.</li>
      <li><code>block.timestamp</code>: block time in seconds. <code>1 days</code> = 86400.</li>
      <li><code>view</code> reads state. <code>pure</code> reads no state. <code>immutable</code> is set one time in the constructor.</li>
      <li>Send ETH: <code>(bool ok, ) = to.call{value: amount}("");</code> then check <code>ok</code>.</li>
      <li>Since 0.8, arithmetic overflow reverts automatically.</li>
    </ul>
    <h4>Pattern you will see in every lab</h4>
    <ol>
      <li><b>Checks:</b> <code>require</code> the right caller, state, amount and time.</li>
      <li><b>Effects:</b> update the contract’s state.</li>
      <li><b>Interactions:</b> send ETH or call other contracts last.</li>
    </ol>

### Watch and read

<div class="vids">
      <a class="vid" href="https://www.youtube.com/watch?v=umepbfKp5rI" target="_blank" rel="noopener"><span class="play"></span><span><b>Learn Solidity full course, part 1</b><small>Patrick Collins. The Remix lessons are enough for this course.</small></span></a>
      <a class="vid" href="https://updraft.cyfrin.io/courses/solidity/simple-storage/introduction" target="_blank" rel="noopener"><span class="play"></span><span><b>Cyfrin Updraft: Solidity course</b><small>Free, same teacher, with text</small></span></a>
      <a class="vid read" href="https://solidity-by-example.org/hello-world/" target="_blank" rel="noopener"><span class="play"></span><span><b>Solidity by Example</b><small>Short reference programs</small></span></a>
    </div>

## Try it

<p>Open <a href="https://solidity-by-example.org/hello-world/" target="_blank" rel="noopener">Solidity by Example</a>. Read “Hello World”, “Mapping”, “Function Modifier” and “Events”. Then predict what <code>require(msg.sender == buyer)</code> does when account 2 calls it, and check your answer in lab L2.</p>

## Apply

<div class="aud"><div class="cs"><h5>Computer science</h5><ul><li>Why is a mapping not iterable, and how do you work around it?</li></ul></div><div class="bi"><h5>Business informatics</h5><ul><li>Storage writes cost the most gas. What does that mean for data you keep on chain?</li></ul></div><div class="lw"><h5>Law</h5><ul><li>Code comments are not terms. Should the legal text link to the code by hash?</li></ul></div></div>

## Ship

<p>Write three sentences in your lab log: the main idea, one example from your discipline, and one open question. Then take the quiz below.</p>
