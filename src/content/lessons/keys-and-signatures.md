---
title: "Keys, signatures and addresses"
module: 1
order: 3
kind: "lesson"
minutes: "30 min"
legacy: "T3"
problem: "There is no bank to check your ID. How does the network know that a payment really comes from you?"
---

## Problem

<div class="cc-callout cc-callout--problem"><div><b>The question.</b> There is no bank to check your ID. How does the network know that a payment really comes from you?</div></div>

## Concept

<div class="goal"><b>Goal:</b> you can explain how the network knows that a transaction comes from you.</div>
    <ul>
      <li>Each user has a <b>key pair</b>: a private key and a public key.</li>
      <li>Keep the private key secret. Use it to <b>sign</b> transactions.</li>
      <li>Anyone can use the public key to <b>verify</b> the signature.</li>
      <li>A signature depends on the message. You cannot copy it to a different transaction.</li>
      <li>An Ethereum <b>address</b> comes from the public key (the last 20 bytes of its Keccak-256 hash), for example <code>0x5B38…eddC4</code>.</li>
      <li>A <b>wallet</b> such as MetaMask stores keys and signs for you. The <b>recovery phrase</b> (12 or 24 words) can recreate all keys. Lose it and you lose access; share it and you lose everything.</li>
      <li>In Solidity, <code>msg.sender</code> is the verified address that called the function. Contracts use it for access control: “only the buyer may deposit”.</li>
    </ul>
    <div class="callout law"><h5>Law lens</h5><ul>
      <li>An address is a pseudonym, not a legal identity. Who is the contract party? A company, an employee, a minor?</li>
      <li>A wallet signature is technically strong, but it is not a qualified electronic signature under eIDAS. What legal weight does it have?</li>
      <li>If a key is stolen, who bears the loss? Compare with lost bank cards.</li>
    </ul></div>

### Watch and read

<div class="vids">
      <a class="vid" href="https://ethereum.org/videos/key-pair-eth-build/" target="_blank" rel="noopener"><span class="play"></span><span><b>Key pair</b><small>ETH.BUILD, 4 min</small></span></a>
      <a class="vid" href="https://youtu.be/xIDL_akeras" target="_blank" rel="noopener"><span class="play"></span><span><b>Blockchain 101, part 2: public and private keys</b><small>Anders Brownworth</small></span></a>
    </div>

## Try it

<ol class="steps"><li>Open the <a href="https://andersbrownworth.com/blockchain/public-private-keys/keys" target="_blank" rel="noopener">public and private key demo</a>. Generate a key pair.</li><li>On the Signatures tab, sign a message, then verify it with the public key.<span class="exp">Verification succeeds.</span></li><li>Change one word of the message and verify again.<span class="exp">Verification fails: the signature belongs to the exact message.</span></li></ol>

## Apply

<div class="aud"><div class="cs"><h5>Computer science</h5><ul><li>Why can’t a signature be copied to a different transaction?</li></ul></div><div class="bi"><h5>Business informatics</h5><ul><li>Who should hold the keys in a company: each employee, IT, or a custody provider?</li></ul></div><div class="lw"><h5>Law</h5><ul><li>A key is stolen and funds are moved. Is the owner bound by the transaction?</li></ul></div></div>

## Ship

<p>Write three sentences in your lab log: the main idea, one example from your discipline, and one open question. Then take the quiz below.</p>
