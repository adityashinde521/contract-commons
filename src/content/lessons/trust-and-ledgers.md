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
      <li>Three tools solve it together: hashes (<a href="/lessons/hash-functions/">1.2 Hash functions</a>) make history tamper-evident, signatures (<a href="/lessons/keys-and-signatures/">1.3</a>) prove who sent a transaction, consensus (<a href="/lessons/consensus/">2.1</a>) makes everyone agree on one order.</li>
      <li>Result: the ledger is <b>tamper-evident</b> and <b>append-only</b>. You can add data. You cannot change old data without everyone noticing.</li>
    </ul>
    <h4>Worked example</h4>
    <p>Alice has 10 coins. She sends a payment of 10 to Bob and, one second later, a payment of 10 to Carol. With a bank, the bank sees both and rejects the second. Without a bank, the network needs a rule to decide which payment came first and must make every computer apply the same order. That rule is consensus.</p>
    <h4>When a blockchain does not help</h4>
    <ul>
      <li>One trusted party already exists and all parties accept it. A normal database is cheaper, faster and private.</li>
      <li>The data must be secret. Public chains show all data to everyone.</li>
      <li>The data comes from the real world. The chain cannot check if “the goods arrived” is true (the oracle problem, <a href="/lessons/what-smart-contracts-are/">4.1 What smart contracts are</a>).</li>
      <li>Decisions need human judgment or must be reversible.</li>
    </ul>
    <div class="aud">
      <div class="cs"><h5>Technology lens</h5><ul><li>A replicated, append-only log with Byzantine fault tolerance.</li></ul></div>
      <div class="bi"><h5>Business lens</h5><ul><li>Removes or reduces an intermediary, at the cost of fees and slower changes.</li></ul></div>
      <div class="lw"><h5>Law lens</h5><ul><li>A register without a registrar. Who is responsible for errors?</li></ul></div>
    </div>

<!-- deep:start -->
### In depth

<p>Every agreement between strangers needs someone to keep the record. When you pay a seller by bank transfer, the bank keeps one ledger, checks that you have the money, and makes sure the same euro is not spent twice. You trust the bank because it is regulated, insured and liable when it makes mistakes. That trust is useful, but it has costs: fees, opening hours, borders, and the power to freeze or reverse a payment.</p>
<p>A blockchain replaces the single record keeper with many copies of the same ledger that check each other. Three problems have to be solved for this to work. First, <b>integrity</b>: nobody may change an old entry without everyone noticing. Second, <b>authorisation</b>: only the owner of money may spend it. Third, <b>agreement</b>: when two payments conflict, all copies must pick the same one. Hashes solve the first, digital signatures the second, and consensus the third. The rest of Modules 1 and 2 explains each one.</p>
<p>The famous case is <b>double spending</b>. With digital files, copying is free: if money were just a file, Alice could send the same coin to Bob and to Carol. A central ledger stops this by refusing the second payment. A blockchain stops it because all nodes follow one agreed order of transactions; the second payment arrives later and finds the coin already spent.</p>
<p>A blockchain is not automatically better. It is slower and more expensive than a database, every entry is public on most chains, and mistakes are hard to undo. It is worth it only when several parties must share a record, do not want to trust one of them to keep it, and need anyone to be able to check it later.</p>

### Worked example

<div class="worked">
<p><b>Case:</b> a second-hand laptop sale between two students who have never met. The price is 1 ETH.</p>
<ol>
  <li><b>With a bank:</b> the buyer transfers 300 EUR, the bank updates two accounts. If the seller never ships, the buyer must ask the bank or a court to help. The bank is the record keeper and, in practice, the judge of who paid.</li>
  <li><b>With a shared ledger:</b> the buyer signs a payment of 1 ETH. Thousands of nodes check the signature and the balance and include it in the next block. Anyone can verify the payment forever.</li>
  <li><b>What is still missing:</b> the ledger proves that 1 ETH moved. It cannot prove that the laptop arrived. That needs a smart contract with rules (Module 4) and someone or something that reports delivery (an arbiter or an oracle).</li>
</ol>
<p><b>Conclusion:</b> the ledger removes the need to trust a record keeper, but not the need to trust facts from the outside world.</p>
</div>

### Common mistakes

<ul>
  <li>“A blockchain means nobody has to trust anyone.” You still trust the code, the majority of validators, and whoever reports outside facts.</li>
  <li>“A blockchain is a better database.” For one organisation it is usually a worse one: slower, public and harder to correct.</li>
  <li>“Blockchain data is anonymous.” Addresses are pseudonyms. Once one is linked to a person, its whole history is visible.</li>
</ul>
<!-- deep:end -->

### Watch and read

<div class="vids">
      <a class="vid" href="https://www.youtube.com/watch?v=bBC-nXj3Ng4" target="_blank" rel="noopener"><span class="play"></span><span><b>But how does bitcoin actually work?</b><small>3Blue1Brown, 25 min. Best single video for lessons 1.1 to 2.1.</small></span></a>
      <a class="vid" href="https://www.youtube.com/watch?v=_160oMzblY8" target="_blank" rel="noopener"><span class="play"></span><span><b>Blockchain 101: a visual demo</b><small>Anders Brownworth, 18 min</small></span></a>
    </div>

## Try it

<ol class="steps"><li>Open <a href="https://andersbrownworth.com/blockchain/blockchain" target="_blank" rel="noopener">Anders Brownworth’s blockchain demo</a>. Mine the blocks in order.<span class="exp">Every block turns green.</span></li><li>Change one character in block 2.<span class="exp">Block 2 and every later block turn red.</span></li><li>Open the “Distributed” tab and change the same block on one peer only.<span class="exp">That peer disagrees with the others; the majority copy wins.</span></li></ol>

## Apply

<div class="aud"><div class="cs"><h5>Technology lens</h5><ul><li>Which failure does a blockchain tolerate that a replicated database does not?</li></ul></div><div class="bi"><h5>Business lens</h5><ul><li>Name a process in your field with many parties and low trust. Is a blockchain worth it there?</li></ul></div><div class="lw"><h5>Law lens</h5><ul><li>A land registry already exists. What would a blockchain register add, and what would it remove?</li></ul></div></div>

## Ship

<p>Write three sentences in your lab log: the main idea, one example for each lens (technology, business, law), and one open question. Then take the quiz below.</p>
