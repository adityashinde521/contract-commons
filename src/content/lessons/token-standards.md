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
