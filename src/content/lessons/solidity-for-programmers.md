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

<div class="goal"><b>Goal:</b> you can read all lab contracts and know where Solidity differs from languages you know.</div>
    <div class="tw"><table>
      <tr><th>Solidity</th><th>Similar to</th><th>Important difference</th></tr>
      <tr><td><code>contract</code></td><td>class</td><td>One instance per deployment, with its own address and balance.</td></tr>
      <tr><td>state variable</td><td>field</td><td>Stored on chain. Each write costs gas.</td></tr>
      <tr><td><code>mapping(address =&gt; uint)</code></td><td>hash map</td><td>All keys exist with default 0. You cannot iterate.</td></tr>
      <tr><td><code>constructor</code></td><td>constructor</td><td>Runs one time, at deployment. Its arguments are filled in the Deploy fields.</td></tr>
      <tr><td><code>modifier</code></td><td>decorator</td><td><code>_;</code> marks where the function body runs.</td></tr>
      <tr><td><code>require(cond, "msg")</code></td><td>guard + throw</td><td>Reverts all changes of the transaction. The message appears in Remix.</td></tr>
      <tr><td><code>event</code> / <code>emit</code></td><td>log</td><td>Off-chain apps read them. Contracts cannot.</td></tr>
      <tr><td><code>enum</code></td><td>enum</td><td>Use it for a state machine (<a href="/lessons/lab-escrow/">4.3 Escrow</a>). Remix shows values as numbers 0, 1, 2…</td></tr>
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

<!-- deep:start -->
### In depth

<p>Solidity looks like JavaScript or Java, but three ideas make it different. First, <b>state is permanent and expensive</b>. Variables declared at contract level live in storage on every node; writing them costs thousands of gas. Local variables in <code>memory</code> disappear after the call. Second, <b>every call has a sender and maybe a value</b>: <code>msg.sender</code> is the direct caller, <code>msg.value</code> is the ETH sent with the call, and only <code>payable</code> functions may receive ETH. Third, <b>failure is all or nothing</b>: <code>require(condition, "message")</code> reverts the whole transaction and undoes every change if the condition is false.</p>
<p>Visibility decides who can call: <code>external</code> and <code>public</code> functions are part of the contract’s interface; <code>internal</code> and <code>private</code> are helpers. <code>view</code> functions only read; <code>pure</code> functions read nothing at all. <b>Modifiers</b> package repeated checks, such as <code>onlyOwner</code>. <b>Events</b> write cheap logs that apps and explorers read; contracts cannot read them back.</p>
<p>Since Solidity 0.8, arithmetic overflow reverts automatically, which removed a whole class of old bugs. Amounts of ETH are always integers in <b>wei</b> (1 ether = 10<sup>18</sup> wei); there are no decimals. Mixing up units is one of the most common beginner mistakes.</p>

### Worked example

<div class="worked">
<p><b>Case:</b> read a function line by line and predict what happens.</p>
<pre><code>function refund() external inState(State.AwaitingDelivery) {
    require(msg.sender == arbiter, "Only arbiter");
    state = State.Refunded;
    (bool ok, ) = payable(buyer).call{value: price}("");
    require(ok, "Transfer failed");
    emit Refunded(buyer, price);
}</code></pre>
<ol>
  <li><code>inState</code> (a modifier) reverts unless the money is currently held.</li>
  <li>The first <code>require</code> reverts unless the caller is the arbiter.</li>
  <li>The state changes <i>before</i> the money leaves (checks, effects, interactions: lesson 7.1).</li>
  <li>The low-level <code>call</code> sends <code>price</code> wei to the buyer and reports success.</li>
  <li>If sending fails, everything is reverted, including the state change.</li>
</ol>
<p><b>Prediction:</b> the seller calls <code>refund()</code> → revert “Only arbiter”, no state change, the seller pays for the gas used.</p>
</div>

### Common mistakes

<ul>
  <li>Forgetting <code>payable</code>: every call with a value reverts.</li>
  <li>Writing <code>1</code> where <code>1 ether</code> was meant: that is 1 wei.</li>
  <li>Using <code>tx.origin</code> for access control instead of <code>msg.sender</code>.</li>
  <li>Thinking <code>private</code> hides data: anyone can read storage directly from the chain.</li>
</ul>
<!-- deep:end -->

### Watch and read

<div class="vids">
      <a class="vid" href="https://www.youtube.com/watch?v=umepbfKp5rI" target="_blank" rel="noopener"><span class="play"></span><span><b>Learn Solidity full course, part 1</b><small>Patrick Collins. The Remix lessons are enough for this course.</small></span></a>
      <a class="vid" href="https://updraft.cyfrin.io/courses/solidity/simple-storage/introduction" target="_blank" rel="noopener"><span class="play"></span><span><b>Cyfrin Updraft: Solidity course</b><small>Free, same teacher, with text</small></span></a>
      <a class="vid read" href="https://solidity-by-example.org/hello-world/" target="_blank" rel="noopener"><span class="play"></span><span><b>Solidity by Example</b><small>Short reference programs</small></span></a>
    </div>

## Try it

<p>Open <a href="https://solidity-by-example.org/hello-world/" target="_blank" rel="noopener">Solidity by Example</a>. Read “Hello World”, “Mapping”, “Function Modifier” and “Events”. Then predict what <code>require(msg.sender == buyer)</code> does when account 2 calls it, and check your answer in lab <a href="/lessons/lab-escrow/">4.3 Escrow</a>.</p>

## Apply

<div class="aud"><div class="cs"><h5>Technology lens</h5><ul><li>Why is a mapping not iterable, and how do you work around it?</li></ul></div><div class="bi"><h5>Business lens</h5><ul><li>Storage writes cost the most gas. What does that mean for data you keep on chain?</li></ul></div><div class="lw"><h5>Law lens</h5><ul><li>Code comments are not terms. Should the legal text link to the code by hash?</li></ul></div></div>

## Ship

<p>Write three sentences in your lab log: the main idea, one example for each lens (technology, business, law), and one open question. Then take the quiz below.</p>
