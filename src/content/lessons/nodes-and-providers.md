---
title: "Nodes, clients and providers"
module: 3
order: 3
kind: "lesson"
minutes: "25 min"
problem: "Your wallet shows a balance. But which computer told it that number, and should you trust it?"
---

## Problem

<div class="cc-callout cc-callout--problem"><div><b>The question.</b> Your wallet shows a balance. But which computer told it that number, and should you trust it?</div></div>

## Concept

<ul>
<li>A <b>node</b> is a computer that keeps a copy of the chain and checks every block. Since the Merge, an Ethereum node runs two programs together:</li>
</ul>
<div class="tw"><table>
<tr><th>Layer</th><th>Job</th><th>Clients</th></tr>
<tr><td>Execution client</td><td>Runs transactions in the EVM, keeps the state</td><td>Geth, Nethermind, Besu, Erigon, Reth</td></tr>
<tr><td>Consensus client</td><td>Follows Proof of Stake, proposes and attests blocks</td><td>Lighthouse, Prysm, Teku, Nimbus, Lodestar, Grandine</td></tr>
</table></div>
<ul>
<li><b>Client diversity</b> matters: if one client with a majority share has a bug, the network can split or stop finalising. No client should run more than a third of the network.</li>
<li>Most apps do not run their own node. They use an <b>RPC provider</b> (for example Alchemy, Infura, QuickNode) or a public endpoint. MetaMask uses Infura by default.</li>
<li>Trust trade-off: a provider can see your requests and could, in theory, show wrong data. Running your own node, or a light client, removes that trust.</li>
</ul>

<!-- deep:start -->
### In depth

<p>When your wallet shows a balance, it asked a <b>node</b>. A node is software that downloads every block, runs every transaction in the EVM and keeps the current state. Since the Merge an Ethereum node runs two programs. The <b>execution client</b> (Geth, Nethermind, Besu, Erigon, Reth) runs transactions and keeps the state. The <b>consensus client</b> (Lighthouse, Prysm, Teku, Nimbus, Lodestar, Grandine) follows Proof of Stake. A full node needs a fast SSD of about 2 TB and a good internet connection; an <b>archive node</b>, which keeps every historical state, needs much more.</p>
<p>Most applications do not run their own node. They send JSON-RPC requests (<code>eth_getBalance</code>, <code>eth_call</code>, <code>eth_sendRawTransaction</code>) to an <b>RPC provider</b> such as Infura, Alchemy or QuickNode. This is convenient but brings back a trusted middleman: the provider sees your IP address and every address you look up, can be down, can refuse service in some regions, and could in theory return wrong data. <b>Light clients</b> reduce that trust: they follow block headers and verify the answers they get with Merkle proofs.</p>
<p><b>Client diversity</b> protects the network. If one client with more than two thirds of validators had a bug, it could finalise a wrong chain; with more than one third, a bug could stop finality. That is why staking providers are asked to spread across clients.</p>

### Worked example

<div class="worked">
<p><b>Case:</b> follow one balance request.</p>
<ol>
  <li>MetaMask sends <code>{"method":"eth_getBalance","params":["0x5B38…","latest"]}</code> to its default provider.</li>
  <li>The provider’s node looks up the account in its state and returns <code>"0x2386f26fc10000"</code>: 10<sup>16</sup> wei, which is 0.01 ETH.</li>
  <li>You change the RPC URL in MetaMask to another provider and get the same answer. Two independent sources agree.</li>
  <li>When you send a transaction, the wallet signs it locally and only sends the signed bytes. The provider cannot change it without breaking the signature, but it could delay it or not forward it.</li>
</ol>
</div>

### Common mistakes

<ul>
  <li>“MetaMask is a node.” It is a wallet that talks to someone else’s node.</li>
  <li>“The provider can steal my funds.” It never has your key; it can mislead or censor you, not spend for you.</li>
</ul>
<!-- deep:end -->

### Watch and read

<div class="vids">
<a class="vid read" href="https://ethereum.org/developers/docs/nodes-and-clients/" target="_blank" rel="noopener"><span class="play"></span><span><b>Nodes and clients</b><small>ethereum.org developer docs</small></span></a>
<a class="vid read" href="https://clientdiversity.org" target="_blank" rel="noopener"><span class="play"></span><span><b>Client diversity</b><small>clientdiversity.org: current shares</small></span></a>
<a class="vid read" href="https://ethereum.org/developers/docs/nodes-and-clients/nodes-as-a-service/" target="_blank" rel="noopener"><span class="play"></span><span><b>Nodes as a service</b><small>ethereum.org</small></span></a>
</div>

## Try it

<p>Open <a href="https://clientdiversity.org" target="_blank" rel="noopener">clientdiversity.org</a>. Note the largest execution client and its share. Is it above one third? Then open MetaMask’s network settings and find the RPC URL for Sepolia.</p>

## Apply

<div class="aud"><div class="cs"><h5>Technology lens</h5><ul><li>What would happen if a client with 70% share had a consensus bug?</li></ul></div><div class="bi"><h5>Business lens</h5><ul><li>Run your own node or pay a provider? List costs and risks.</li></ul></div><div class="lw"><h5>Law lens</h5><ul><li>An RPC provider blocks requests from a sanctioned region. Is the network still neutral?</li></ul></div></div>

## Ship

<ul class="outc"><li>You can name the two clients of an Ethereum node.</li><li>You can explain client diversity.</li><li>You know which provider your wallet trusts.</li></ul>
