---
title: "Decentralised storage"
module: 9
order: 3
kind: "lesson"
minutes: "25 min"
problem: "A certificate NFT points to an image on a startup’s server. The startup closes. What does the token now prove?"
---

## Problem

<div class="cc-callout cc-callout--problem"><div><b>The question.</b> A certificate NFT points to an image on a startup’s server. The startup closes. What does the token now prove?</div></div>

## Concept

<ul>
<li>Storing data on Ethereum is expensive (every byte is kept by every node), so files live elsewhere and the chain stores a pointer or a hash.</li>
<li><b>IPFS</b> addresses files by their content hash (a CID). The same file always has the same address, so a link cannot silently point to a changed file. But a file stays available only while someone <b>pins</b> it.</li>
<li><b>Filecoin</b> adds paid storage deals on top of IPFS; <b>Arweave</b> sells one-time payments for long-term storage.</li>
<li>A normal web server (<code>https://…</code>) can change or delete the file at any time.</li>
</ul>
<div class="tw"><table>
<tr><th>Where the file lives</th><th>Can it change?</th><th>Can it disappear?</th></tr>
<tr><td>Company web server</td><td>Yes</td><td>Yes</td></tr>
<tr><td>IPFS (CID)</td><td>No, a change gives a new CID</td><td>Yes, if nobody pins it</td></tr>
<tr><td>Arweave</td><td>No</td><td>Designed not to</td></tr>
<tr><td>On chain</td><td>No</td><td>No, but costly and public</td></tr>
</table></div>
<div class="cc-callout cc-callout--law"><div><b>Law lens.</b> Permanent storage meets the GDPR right to erasure. Never store personal data in permanent storage; store it in a system that can delete, and put only a hash on chain (see labs <a href="/lessons/lab-document-registry/">4.5 Document registry</a> and <a href="/lessons/lab-attestations/">9.4 Attestations</a>).</div></div>

### Watch and read

<div class="vids">
<a class="vid read" href="https://ethereum.org/developers/docs/storage/" target="_blank" rel="noopener"><span class="play"></span><span><b>Decentralised storage</b><small>ethereum.org</small></span></a>
<a class="vid read" href="https://docs.ipfs.tech/concepts/what-is-ipfs/" target="_blank" rel="noopener"><span class="play"></span><span><b>What is IPFS?</b><small>IPFS documentation</small></span></a>
</div>

## Try it

<p>Open an NFT collection on Etherscan, call <code>tokenURI</code> for one token in the Read tab, and look at the address it returns. Is it <code>https://</code>, <code>ipfs://</code> or <code>ar://</code>? What would happen to the token if that host went offline?</p>

## Apply

<div class="aud"><div class="cs"><h5>Technology lens</h5><ul><li>Why is a content hash a better pointer than a URL?</li></ul></div><div class="bi"><h5>Business lens</h5><ul><li>Who pays to keep a university’s certificate images pinned for 50 years?</li></ul></div><div class="lw"><h5>Law lens</h5><ul><li>An image linked from an NFT infringes copyright. Who must take it down, and can they?</li></ul></div></div>

## Ship

<ul class="outc"><li>You can compare web, IPFS, Arweave and on-chain storage.</li><li>You can check where an NFT’s metadata really lives.</li></ul>
