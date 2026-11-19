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

<!-- deep:start -->
### In depth

<p>Ethereum accounts are controlled by a key pair. The <b>private key</b> is a random 256-bit number. From it, elliptic-curve multiplication on the curve secp256k1 gives the <b>public key</b>. This direction is easy; the reverse is practically impossible. The <b>address</b> is the last 20 bytes of the Keccak-256 hash of the public key, which is why addresses are shorter than keys.</p>
<p>To spend from an account, the wallet <b>signs</b> the transaction: it combines the transaction hash with the private key using ECDSA and produces a signature (the values r, s and v). Nodes never see the private key. They run the verification math on the transaction and the signature and recover the public key, hash it, and check that the resulting address is the sender. If one byte of the transaction was changed after signing, the recovered address is different and the transaction is rejected.</p>
<p>A signature therefore proves two things: <b>authenticity</b> (only the holder of the private key could have produced it) and <b>integrity</b> (the message was not changed). It does not prove <i>who</i> the holder is in the real world. That is the gap between cryptography and law: a qualified electronic signature under eIDAS links a key to an identified person through a trust service; a blockchain address does not.</p>
<p>A <b>recovery phrase</b> (12 or 24 words, BIP-39) is just a human-readable form of the seed from which the wallet derives all its private keys. Whoever has the phrase has every account in that wallet. There is no “forgot password”: if it is lost, the funds are gone; if it is stolen, they are gone too.</p>
<!-- diagram:sign-verify -->
<figure class="dg"><div class="sv"><svg viewBox="0 0 720 250" role="img" aria-label="Signing in the wallet and verifying on a node" xmlns="http://www.w3.org/2000/svg"><defs><marker id="ah-signinginthewalletan-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="m-a" d="M0 0L10 5L0 10z"/></marker><marker id="ah-signinginthewalletan-ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="m-ar" d="M0 0L10 5L0 10z"/></marker><marker id="ah-signinginthewalletan-ag" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="m-ag" d="M0 0L10 5L0 10z"/></marker><marker id="ah-signinginthewalletan-am" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="m-am" d="M0 0L10 5L0 10z"/></marker></defs><rect class="k-zone" x="10" y="10" width="330" height="230" rx="16"/><rect class="k-zone" x="380" y="10" width="330" height="230" rx="16"/><text class="th" x="175" y="34" text-anchor="middle" font-size="14">In the wallet (private)</text><text class="th" x="545" y="34" text-anchor="middle" font-size="14">On every node (public)</text><rect class="k-n" x="30" y="52" width="130" height="56" rx="12"/><text class="tb" x="95.0" y="75.5" text-anchor="middle" font-size="13.5">Transaction</text><text class="t" x="95.0" y="94.0" text-anchor="middle" font-size="13.5">to, value, nonce</text><rect class="k-law" x="30" y="160" width="130" height="56" rx="12"/><text class="tb" x="95.0" y="183.5" text-anchor="middle" font-size="13.5">Private key</text><text class="t" x="95.0" y="202.0" text-anchor="middle" font-size="13.5">never leaves</text><rect class="k-brand" x="200" y="106" width="120" height="56" rx="12"/><text class="tb" x="260.0" y="129.5" text-anchor="middle" font-size="13.5">Sign</text><text class="t" x="260.0" y="148.0" text-anchor="middle" font-size="13.5">ECDSA</text><line class="k-a" x1="160" y1="80" x2="198" y2="120" marker-end="url(#ah-signinginthewalletan-a)"/><line class="k-a" x1="160" y1="188" x2="198" y2="150" marker-end="url(#ah-signinginthewalletan-a)"/><rect class="k-n" x="400" y="52" width="140" height="56" rx="12"/><text class="tb" x="470.0" y="75.5" text-anchor="middle" font-size="13.5">Tx + signature</text><text class="t" x="470.0" y="94.0" text-anchor="middle" font-size="13.5">r, s, v</text><rect class="k-cs" x="400" y="160" width="140" height="56" rx="12"/><text class="tb" x="470.0" y="183.5" text-anchor="middle" font-size="13.5">Recover</text><text class="t" x="470.0" y="202.0" text-anchor="middle" font-size="13.5">public key → address</text><rect class="k-brand" x="570" y="106" width="125" height="56" rx="12"/><text class="tb" x="632.5" y="129.5" text-anchor="middle" font-size="13.5">Matches sender?</text><text class="t" x="632.5" y="148.0" text-anchor="middle" font-size="13.5">yes: valid</text><line class="k-a" x1="320" y1="134" x2="398" y2="84" marker-end="url(#ah-signinginthewalletan-a)"/><text class="tl" x="359.0" y="99.0" text-anchor="middle" font-size="12.5">broadcast</text><line class="k-a" x1="470" y1="108" x2="470" y2="158" marker-end="url(#ah-signinginthewalletan-a)"/><line class="k-a" x1="540" y1="188" x2="568" y2="150" marker-end="url(#ah-signinginthewalletan-a)"/></svg></div><figcaption><b>The key signs; the network only checks.</b> Nodes recover the signer’s address from the signature. Change one byte of the transaction and a different, random address comes out, so the transaction is rejected.</figcaption></figure>

### Worked example

<div class="worked">
<p><b>Case:</b> Alice sends 0.1 SepoliaETH to Bob.</p>
<ol>
  <li>MetaMask builds the transaction: to = Bob, value = 0.1 ETH, nonce = 7, gas settings, chain ID 11155111 (Sepolia).</li>
  <li>It hashes this data and signs the hash with Alice’s private key. The output is a signature of 65 bytes.</li>
  <li>A node receives transaction + signature, recovers a public key from them, hashes it, and gets <code>0x5B38…eddC4</code>: Alice’s address. It also checks the nonce (7 is next) and the balance.</li>
  <li>An attacker who intercepts the transaction and changes the receiver to their own address breaks the signature: the recovered address is now a random one with no funds, so the node rejects it.</li>
  <li>The chain ID inside the signed data stops the same transaction from being replayed on mainnet.</li>
</ol>
</div>

### Common mistakes

<ul>
  <li>“The public key and the address are the same.” The address is derived from the public key by hashing.</li>
  <li>“A signature encrypts the transaction.” Transactions are public. The signature only proves who authorised them.</li>
  <li>“Support can restore my wallet.” Nobody can. Anyone who asks for your recovery phrase is attacking you.</li>
</ul>
<!-- deep:end -->

### Watch and read

<div class="vids">
      <a class="vid" href="https://ethereum.org/videos/key-pair-eth-build/" target="_blank" rel="noopener"><span class="play"></span><span><b>Key pair</b><small>ETH.BUILD, 4 min</small></span></a>
      <a class="vid" href="https://youtu.be/xIDL_akeras" target="_blank" rel="noopener"><span class="play"></span><span><b>Blockchain 101, part 2: public and private keys</b><small>Anders Brownworth</small></span></a>
    </div>

## Try it

<ol class="steps"><li>Open the <a href="https://andersbrownworth.com/blockchain/public-private-keys/keys" target="_blank" rel="noopener">public and private key demo</a>. Generate a key pair.</li><li>On the Signatures tab, sign a message, then verify it with the public key.<span class="exp">Verification succeeds.</span></li><li>Change one word of the message and verify again.<span class="exp">Verification fails: the signature belongs to the exact message.</span></li></ol>

## Apply

<div class="aud"><div class="cs"><h5>Technology lens</h5><ul><li>Why can’t a signature be copied to a different transaction?</li></ul></div><div class="bi"><h5>Business lens</h5><ul><li>Who should hold the keys in a company: each employee, IT, or a custody provider?</li></ul></div><div class="lw"><h5>Law lens</h5><ul><li>A key is stolen and funds are moved. Is the owner bound by the transaction?</li></ul></div></div>

## Ship

<p>Write three sentences in your lab log: the main idea, one example for each lens (technology, business, law), and one open question. Then take the quiz below.</p>
