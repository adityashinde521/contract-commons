---
title: "Hash functions"
module: 1
order: 2
kind: "lesson"
minutes: "30 min"
legacy: "T2"
problem: "A landlord says the lease you signed said 990 EUR, not 900. How could anyone prove which text existed, without trusting either of you?"
---

## Problem

<div class="cc-callout cc-callout--problem"><div><b>The question.</b> A landlord says the lease you signed said 990 EUR, not 900. How could anyone prove which text existed, without trusting either of you?</div></div>

## Concept

<div class="goal"><b>Goal:</b> you can list the properties of a hash and say why each is important for a blockchain.</div>
    <ul>
      <li>A <b>hash function</b> turns any input (a word, a contract, a film) into a fixed-length output, a “fingerprint” of the input.</li>
      <li>Bitcoin uses SHA-256. Ethereum uses <b>Keccak-256</b>. In Solidity, call <code>keccak256(...)</code>. Both give 256 bits, written as 64 hexadecimal characters.</li>
    </ul>
    <div class="tw"><table>
      <tr><th>Property</th><th>Meaning</th><th>Why it matters</th></tr>
      <tr><td>Deterministic</td><td>Same input, same hash, every time.</td><td>Anyone can recompute and check.</td></tr>
      <tr><td>Avalanche effect</td><td>One changed character gives a completely different hash.</td><td>Small edits cannot hide.</td></tr>
      <tr><td>One-way</td><td>You cannot calculate the input from the hash.</td><td>You can publish the hash of a confidential document.</td></tr>
      <tr><td>Collision-resistant</td><td>It is not practical to find two inputs with the same hash.</td><td>A hash identifies one document.</td></tr>
    </table></div>
    <ul>
      <li>Each block contains the hash of the previous block. If someone changes an old block, its hash changes and all later links break. ETH.BUILD (<a href="/lessons/lab-eth-build/">1.6</a>) shows this visually.</li>
      <li>Law use: store only the hash of a document on chain to prove it existed at a time (labs <a href="/lessons/lab-document-registry/">4.5 Document registry</a> and <a href="/lessons/lab-attestations/">9.4 Attestations</a>).</li>
    </ul>
    <div class="callout law"><h5>Law lens</h5><p>A hash proves integrity (“this exact text”) and, with a block timestamp, existence at a time. It does not prove who wrote the text or that anyone agreed to it. A hash of personal data may still be personal data under the GDPR if the data can be guessed and re-hashed.</p></div>

<!-- deep:start -->
### In depth

<p>A hash function is like a very strict fingerprint machine. Feed it the text of a lease and it returns 64 hexadecimal characters. Feed it the same text tomorrow and it returns exactly the same 64 characters. Change one letter, even a space, and the result looks completely unrelated. This is what makes a hash useful as evidence: it is cheap to check and impossible to fake in practice.</p>
<p>Why can nobody fake it? A 256-bit hash has 2<sup>256</sup> possible values, roughly the number of atoms in the observable universe. To find a different document with the same hash (a <b>collision</b>), an attacker would have to try an astronomical number of inputs. To recover the document from its hash (a <b>preimage</b>), there is no shortcut either: the function is designed to scramble every input bit into every output bit.</p>
<p>Blockchains use hashes in three places. (1) <b>Linking blocks</b>: each block header contains the hash of the previous header, so the chain is <i>tamper-evident</i>. (2) <b>Summarising data</b>: all transactions in a block are combined into one Merkle root (lesson 1.4). (3) <b>Identifiers</b>: an Ethereum address is the last 20 bytes of the Keccak-256 hash of a public key, and a transaction is known by its hash.</p>
<p>Ethereum uses Keccak-256, the original winner of the SHA-3 competition. It is not identical to the later standard SHA3-256 because NIST changed the padding. That is why Solidity calls it <code>keccak256</code> and not <code>sha3</code>.</p>
<!-- diagram:hash-chain -->
<figure class="dg"><div class="sv"><svg viewBox="0 0 720 300" role="img" aria-label="Hash-linked blocks and what tampering does" xmlns="http://www.w3.org/2000/svg"><defs><marker id="ah-hashlinkedblocksandw-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="m-a" d="M0 0L10 5L0 10z"/></marker><marker id="ah-hashlinkedblocksandw-ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="m-ar" d="M0 0L10 5L0 10z"/></marker><marker id="ah-hashlinkedblocksandw-ag" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="m-ag" d="M0 0L10 5L0 10z"/></marker><marker id="ah-hashlinkedblocksandw-am" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="m-am" d="M0 0L10 5L0 10z"/></marker></defs><text class="th" x="20" y="24" text-anchor="start" font-size="14">Honest chain</text><rect class="k-cs" x="20" y="36" width="200" height="92" rx="12"/><text class="tb" x="120.0" y="59.5" text-anchor="middle" font-size="13">Block 1</text><text class="t" x="120.0" y="77.5" text-anchor="middle" font-size="13">prev: 0000…</text><text class="t" x="120.0" y="95.5" text-anchor="middle" font-size="13">data: Rent 900 EUR</text><text class="t" x="120.0" y="113.5" text-anchor="middle" font-size="13">hash: 3f9a…</text><rect class="k-cs" x="260" y="36" width="200" height="92" rx="12"/><text class="tb" x="360.0" y="59.5" text-anchor="middle" font-size="13">Block 2</text><text class="t" x="360.0" y="77.5" text-anchor="middle" font-size="13">prev: 3f9a…</text><text class="t" x="360.0" y="95.5" text-anchor="middle" font-size="13">data: Alice → Bob 1</text><text class="t" x="360.0" y="113.5" text-anchor="middle" font-size="13">hash: b21c…</text><line class="k-a" x1="220" y1="82" x2="258" y2="82" marker-end="url(#ah-hashlinkedblocksandw-a)"/><rect class="k-cs" x="500" y="36" width="200" height="92" rx="12"/><text class="tb" x="600.0" y="59.5" text-anchor="middle" font-size="13">Block 3</text><text class="t" x="600.0" y="77.5" text-anchor="middle" font-size="13">prev: b21c…</text><text class="t" x="600.0" y="95.5" text-anchor="middle" font-size="13">data: Bob → Eve 0.5</text><text class="t" x="600.0" y="113.5" text-anchor="middle" font-size="13">hash: 7d04…</text><line class="k-a" x1="460" y1="82" x2="498" y2="82" marker-end="url(#ah-hashlinkedblocksandw-a)"/><text class="th" x="20" y="168" text-anchor="start" font-size="14">Someone edits block 1</text><rect class="k-danger" x="20" y="180" width="200" height="92" rx="12"/><text class="tb" x="120.0" y="203.6" text-anchor="middle" font-size="13">Block 1</text><text class="t" x="120.0" y="221.6" text-anchor="middle" font-size="13">prev: 0000…</text><text class="t" x="120.0" y="239.6" text-anchor="middle" font-size="13">data: Rent 990 EUR</text><text class="t" x="120.0" y="257.6" text-anchor="middle" font-size="13">hash: c8e1…</text><rect class="k-danger" x="260" y="180" width="200" height="92" rx="12"/><text class="tb" x="360.0" y="203.6" text-anchor="middle" font-size="13">Block 2</text><text class="t" x="360.0" y="221.6" text-anchor="middle" font-size="13">prev: 3f9a… ≠ c8e1…</text><text class="t" x="360.0" y="239.6" text-anchor="middle" font-size="13">data: Alice → Bob 1</text><text class="t" x="360.0" y="257.6" text-anchor="middle" font-size="13">hash: b21c…</text><line class="k-ar" x1="220" y1="226" x2="258" y2="226" marker-end="url(#ah-hashlinkedblocksandw-ar)"/><rect class="k-warn" x="500" y="180" width="200" height="92" rx="12"/><text class="tb" x="600.0" y="203.6" text-anchor="middle" font-size="13">Block 3</text><text class="t" x="600.0" y="221.6" text-anchor="middle" font-size="13">prev: b21c…</text><text class="t" x="600.0" y="239.6" text-anchor="middle" font-size="13">data: Bob → Eve 0.5</text><text class="t" x="600.0" y="257.6" text-anchor="middle" font-size="13">hash: 7d04…</text><line class="k-ar" x1="460" y1="226" x2="498" y2="226" marker-end="url(#ah-hashlinkedblocksandw-ar)"/></svg></div><figcaption><b>Tamper-evident, not tamper-proof.</b> Changing block 1 changes its hash, so block 2’s “prev” no longer matches. To hide the edit, every later block would have to be rebuilt and accepted by the network again.</figcaption></figure>

### Worked example

<div class="worked">
<p><b>Case:</b> the landlord from the question claims the lease said 990 EUR.</p>
<ol>
  <li>On the signing day, the tenant computed the hash of the PDF and registered it in the Document registry (lab 4.5). The block timestamp shows the date.</li>
  <li>In the dispute, the tenant hands the court the PDF that says 900 EUR. Anyone can hash it again: the result matches the hash on chain.</li>
  <li>The landlord’s version with 990 EUR produces a completely different hash, which was never registered.</li>
  <li>Result: the 900 EUR text existed unchanged on the signing day. What the hash does <i>not</i> show is that the landlord agreed to it. That needs a signature, which is the next lesson.</li>
</ol>
</div>

### Common mistakes

<ul>
  <li>“A hash encrypts the document.” Encryption can be reversed with a key. A hash cannot be reversed at all.</li>
  <li>“Short or predictable data is safe once hashed.” A date of birth has few possible values; an attacker can hash them all and compare. Add a random salt before hashing personal data.</li>
  <li>“Similar documents have similar hashes.” They do not. That is the avalanche effect.</li>
</ul>
<!-- deep:end -->

### Watch and read

<div class="vids">
      <a class="vid" href="https://ethereum.org/videos/hash-function-eth-build/" target="_blank" rel="noopener"><span class="play"></span><span><b>Hash function</b><small>ETH.BUILD, 5 min</small></span></a>
      <a class="vid tool" href="https://andersbrownworth.com/blockchain/hash" target="_blank" rel="noopener"><span class="play"></span><span><b>Try it: live hash and blockchain demo</b><small>Anders Brownworth. Type text, watch the hash, tamper with a block</small></span></a>
    </div>

## Try it

<ol class="steps"><li>Open the <a href="https://andersbrownworth.com/blockchain/hash" target="_blank" rel="noopener">live hash demo</a>. Type <code>Lease Kiel: rent 900 EUR</code>.<span class="exp">A 64-character SHA-256 hash.</span></li><li>Change 900 to 990.<span class="exp">A completely different hash (avalanche effect).</span></li><li>Type the first text again exactly.<span class="exp">The original hash returns (deterministic).</span></li></ol>

## Apply

<div class="aud"><div class="cs"><h5>Technology lens</h5><ul><li>Why is a 256-bit hash still safe if computers get much faster?</li></ul></div><div class="bi"><h5>Business lens</h5><ul><li>Which business documents need proof that they were not changed?</li></ul></div><div class="lw"><h5>Law lens</h5><ul><li>Is a hash of personal data still personal data under the GDPR?</li></ul></div></div>

## Ship

<p>Write three sentences in your lab log: the main idea, one example for each lens (technology, business, law), and one open question. Then take the quiz below.</p>
