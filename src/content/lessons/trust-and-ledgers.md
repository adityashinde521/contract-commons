---
title: "The problem: trust and a shared ledger"
module: 1
order: 1
kind: "lesson"
minutes: "40 min"
legacy: "T1"
problem: "Two companies that do not trust each other must keep one shared list of who owes what. Who keeps the list, and what stops someone from changing it?"
---

## Problem

<div class="cc-callout cc-callout--problem"><div><b>The question.</b> Two companies that do not trust each other must keep one shared list of who owes what. Who keeps the list, and what stops someone from changing it?</div></div>

## Concept

<div class="goal"><b>Goal:</b> you can say which problem a blockchain solves and when it does not help.</div>
    <h4>Key ideas</h4>
    <ul>
      <li>A <b>ledger</b> is a list of transactions. Example: “Alice pays Bob 10.”</li>
      <li>Usually one trusted party keeps the ledger: a bank, a land registry, a notary, a stock exchange.</li>
      <li>A <b>blockchain</b> lets many parties keep the same ledger. No single party controls it, and every party can check it.</li>
      <li>The core problem for digital money is <b>double spending</b>: digital data is easy to copy, so a person must not spend the same coin two times.</li>
      <li>Three tools solve it together: hashes (T2) make history tamper-evident, signatures (T3) prove who sent a transaction, consensus (T4) makes everyone agree on one order.</li>
      <li>Result: the ledger is <b>tamper-evident</b> and <b>append-only</b>. You can add data. You cannot change old data without everyone noticing.</li>
    </ul>
    <h4>Worked example</h4>
    <p>Alice has 10 coins. She sends a payment of 10 to Bob and, one second later, a payment of 10 to Carol. With a bank, the bank sees both and rejects the second. Without a bank, the network needs a rule to decide which payment came first and must make every computer apply the same order. That rule is consensus.</p>
    <h4>When a blockchain does not help</h4>
    <ul>
      <li>One trusted party already exists and all parties accept it. A normal database is cheaper, faster and private.</li>
      <li>The data must be secret. Public chains show all data to everyone.</li>
      <li>The data comes from the real world. The chain cannot check if “the goods arrived” is true (the oracle problem, T6).</li>
      <li>Decisions need human judgment or must be reversible.</li>
    </ul>
    <div class="aud">
      <div class="cs"><h5>Technology lens</h5><ul><li>A replicated, append-only log with Byzantine fault tolerance.</li></ul></div>
      <div class="bi"><h5>Business lens</h5><ul><li>Removes or reduces an intermediary, at the cost of fees and slower changes.</li></ul></div>
      <div class="lw"><h5>Law lens</h5><ul><li>A register without a registrar. Who is responsible for errors?</li></ul></div>
    </div>

### Watch and read

<div class="vids">
      <a class="vid" href="https://www.youtube.com/watch?v=bBC-nXj3Ng4" target="_blank" rel="noopener"><span class="play"></span><span><b>But how does bitcoin actually work?</b><small>3Blue1Brown, 25 min. Best single video for T1–T4.</small></span></a>
      <a class="vid" href="https://www.youtube.com/watch?v=_160oMzblY8" target="_blank" rel="noopener"><span class="play"></span><span><b>Blockchain 101: a visual demo</b><small>Anders Brownworth, 18 min</small></span></a>
    </div>

## Try it

<ol class="steps"><li>Open <a href="https://andersbrownworth.com/blockchain/blockchain" target="_blank" rel="noopener">Anders Brownworth’s blockchain demo</a>. Mine the blocks in order.<span class="exp">Every block turns green.</span></li><li>Change one character in block 2.<span class="exp">Block 2 and every later block turn red.</span></li><li>Open the “Distributed” tab and change the same block on one peer only.<span class="exp">That peer disagrees with the others; the majority copy wins.</span></li></ol>

## Apply

<div class="aud"><div class="cs"><h5>Technology lens</h5><ul><li>Which failure does a blockchain tolerate that a replicated database does not?</li></ul></div><div class="bi"><h5>Business lens</h5><ul><li>Name a process in your field with many parties and low trust. Is a blockchain worth it there?</li></ul></div><div class="lw"><h5>Law lens</h5><ul><li>A land registry already exists. What would a blockchain register add, and what would it remove?</li></ul></div></div>

## Ship

<p>Write three sentences in your lab log: the main idea, one example for each lens (technology, business, law), and one open question. Then take the quiz below.</p>
