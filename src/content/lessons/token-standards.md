---
title: "Tokens: ERC-20 and ERC-721"
module: 5
order: 1
kind: "lesson"
minutes: "30 min"
legacy: "T9"
problem: "A university wants to issue course credits and degree certificates on chain. Why do almost all tokens follow a handful of standards?"
---

## Problem

<div class="cc-callout cc-callout--problem"><div><b>The question.</b> A university wants to issue course credits and degree certificates on chain. Why do almost all tokens follow a handful of standards?</div></div>

## Concept

<div class="goal"><b>Goal:</b> you can explain what a token standard is and why it is useful.</div>
    <ul>
      <li>A <b>token</b> is a contract that keeps a balance list (<code>mapping(address =&gt; uint256)</code>). Tokens are not stored “in” wallets; the token contract records who owns what.</li>
      <li>An <b>ERC</b> is a standard interface. Wallets and exchanges support every token that uses it.</li>
      <li><b>ERC-20</b>: fungible tokens, each unit equal. Functions: <code>totalSupply</code>, <code>balanceOf</code>, <code>transfer</code>, <code>approve</code>, <code>allowance</code>, <code>transferFrom</code>.</li>
      <li><code>approve</code> + <code>transferFrom</code> let another address move your tokens, up to a limit. Example: a shop contract collects a payment.</li>
      <li><b>ERC-721</b>: non-fungible tokens (NFTs). Each has a unique ID. Uses: certificates, tickets, ownership records.</li>
      <li>Do not write token code from scratch. Use audited <b>OpenZeppelin</b> contracts (<a href="/lessons/lab-course-token/">5.2 Course token</a>) or the OpenZeppelin Wizard (<a href="/lessons/lab-openzeppelin-wizard/">5.3</a>).</li>
    </ul>
    <div class="callout law"><h5>Law lens</h5><p>A token is a record in a contract. Whether it gives a legal right (ownership of a bond, a claim against an issuer, nothing at all) depends on the legal terms around it. Under MiCA and MiFID II, the rights the token gives decide its classification (<a href="/lessons/regulation/">12.3 Regulation</a>).</p></div>

<!-- deep:start -->
### In depth

<p>A token is not a coin that moves; it is a row in a contract’s table. An ERC-20 contract keeps <code>balanceOf[address]</code>. A “transfer” lowers one row and raises another. What makes tokens powerful is the <b>standard interface</b>: because every ERC-20 has the same functions and events, any wallet, exchange or explorer can show and move any token without custom code.</p>
<p>ERC-20 has a second way to move tokens: <b>approve and transferFrom</b>. You first approve a spender (for example an exchange contract) to move up to a certain amount; later the spender pulls the tokens in its own transaction. This lets contracts take payment in tokens, but it is also a risk: many people give unlimited approvals, and a hacked spender can drain them. Newer designs (permit signatures, EIP-7702 batching) reduce the number of steps.</p>
<!-- diagram:approve-flow -->
<figure class="dg"><div class="sv"><svg viewBox="0 0 720 280" role="img" aria-label="ERC-20 approve and transferFrom" xmlns="http://www.w3.org/2000/svg"><defs><marker id="ah-erc20approveandtrans-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="m-a" d="M0 0L10 5L0 10z"/></marker><marker id="ah-erc20approveandtrans-ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="m-ar" d="M0 0L10 5L0 10z"/></marker><marker id="ah-erc20approveandtrans-ag" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="m-ag" d="M0 0L10 5L0 10z"/></marker><marker id="ah-erc20approveandtrans-am" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="m-am" d="M0 0L10 5L0 10z"/></marker></defs><rect class="k-law" x="10" y="12" width="160" height="40" rx="12"/><text class="tb" x="90.0" y="36.7" text-anchor="middle" font-size="13.5">Alice</text><line class="k-life" x1="90" y1="52" x2="90" y2="270"/><rect class="k-cs" x="280" y="12" width="160" height="40" rx="12"/><text class="tb" x="360.0" y="36.7" text-anchor="middle" font-size="13.5">Token contract</text><line class="k-life" x1="360" y1="52" x2="360" y2="270"/><rect class="k-bi" x="550" y="12" width="160" height="40" rx="12"/><text class="tb" x="630.0" y="36.7" text-anchor="middle" font-size="13.5">Shop contract</text><line class="k-life" x1="630" y1="52" x2="630" y2="270"/><line class="k-a" x1="90" y1="90" x2="358" y2="90" marker-end="url(#ah-erc20approveandtrans-a)"/><text class="tl" x="224.0" y="83.0" text-anchor="middle" font-size="12.5">1  approve(Shop, 50)</text><text class="tl" x="372" y="108" text-anchor="start" font-size="12">allowance[Alice][Shop] = 50</text><line class="k-a" x1="90" y1="150" x2="628" y2="150" marker-end="url(#ah-erc20approveandtrans-a)"/><text class="tl" x="509.0" y="143.0" text-anchor="middle" font-size="12.5">2  buy(item)</text><line class="k-a" x1="630" y1="200" x2="362" y2="200" marker-end="url(#ah-erc20approveandtrans-a)"/><text class="tl" x="496.0" y="192.0" text-anchor="middle" font-size="12.5">3  transferFrom(Alice, Shop, 50)</text><text class="tl" x="372" y="230" text-anchor="start" font-size="12">balance Alice −50 · Shop +50</text><text class="tl" x="372" y="250" text-anchor="start" font-size="12">allowance back to 0</text></svg></div><figcaption><b>Two transactions, one pull.</b> Alice first allows the shop to take up to 50 tokens. The shop then pulls them itself. If step 1 is missing, step 3 reverts.</figcaption></figure>
<p><b>ERC-721</b> tokens are unique: each token ID has one owner and a <code>tokenURI</code> pointing to metadata (name, image). <b>ERC-1155</b> manages many token types in one contract, some unique and some with copies, which saves gas for games and tickets. Tokens can also add rules: pausing, allow-lists of verified holders, or a maximum supply. Those rules are where regulation meets code (lesson 12.3).</p>

### Worked example

<div class="worked">
<p><b>Case:</b> Alice pays 50 CRS course tokens to a shop contract.</p>
<div class="tw"><table>
  <tr><th>Step</th><th>Call</th><th>State after</th></tr>
  <tr><td>Start</td><td></td><td>balanceOf[Alice] = 100, balanceOf[Shop] = 0, allowance[Alice][Shop] = 0</td></tr>
  <tr><td>1</td><td>Alice: <code>approve(Shop, 50)</code></td><td>allowance[Alice][Shop] = 50. Event Approval</td></tr>
  <tr><td>2</td><td>Alice: <code>Shop.buy(itemId)</code>, which calls <code>transferFrom(Alice, Shop, 50)</code></td><td>balanceOf[Alice] = 50, balanceOf[Shop] = 50, allowance = 0. Event Transfer</td></tr>
  <tr><td>Wrong order</td><td>Alice calls <code>buy</code> first</td><td>Revert: insufficient allowance. Nothing changes.</td></tr>
</table></div>
<p>Note the units: with 18 decimals, “50 CRS” is stored as 50 × 10<sup>18</sup>.</p>
</div>

### Common mistakes

<ul>
  <li>“The NFT contains the image.” Usually it contains a link; the image lives elsewhere (lesson 9.3).</li>
  <li>“Owning a token means owning the asset.” Only the legal terms around the token can give that right.</li>
  <li>“Approvals expire.” They do not, until you set them to zero.</li>
</ul>
<!-- deep:end -->

### Watch and read

<div class="vids">
      <a class="vid" href="https://simplyexplained.com/videos/erc20-tokens/" target="_blank" rel="noopener"><span class="play"></span><span><b>ERC20 tokens</b><small>Simply Explained</small></span></a>
      <a class="vid" href="https://ethereum.org/videos/learn-nfts-and-defi/" target="_blank" rel="noopener"><span class="play"></span><span><b>What are NFTs?</b><small>11 min</small></span></a>
      <a class="vid read" href="https://ethereum.org/en/developers/docs/standards/tokens/erc-20/" target="_blank" rel="noopener"><span class="play"></span><span><b>ERC-20 standard</b><small>ethereum.org docs</small></span></a>
    </div>

## Try it

<p>On <a href="https://etherscan.io/tokens" target="_blank" rel="noopener">Etherscan’s token list</a> (read only), open one ERC-20 token and one ERC-721 collection. Compare the “Read Contract” functions of each.<span class="exp" style="display:block">Both show <code>balanceOf</code>; only the NFT shows <code>ownerOf</code> and <code>tokenURI</code>.</span></p>

## Apply

<div class="aud"><div class="cs"><h5>Technology lens</h5><ul><li>Why does ERC-20 use approve and transferFrom instead of one call?</li></ul></div><div class="bi"><h5>Business lens</h5><ul><li>Which business models fit a fungible token, which a non-fungible one?</li></ul></div><div class="lw"><h5>Law lens</h5><ul><li>Does owning a token give a legal right? Which one?</li></ul></div></div>

## Ship

<p>Write three sentences in your lab log: the main idea, one example for each lens (technology, business, law), and one open question. Then take the quiz below.</p>
