---
title: "Course token with OpenZeppelin"
module: 5
order: 2
kind: "lab-remix"
minutes: "30 min"
legacy: "L5"
problem: "Writing your own token is how money gets lost. Professionals build on audited code instead."
---

## Problem

<div class="cc-callout cc-callout--problem"><div><b>The question.</b> Writing your own token is how money gets lost. Professionals build on audited code instead.</div></div>

## Concept

<div class="ov">
      <div><b>You will</b>Create an ERC-20 token with an audited library, then use allowances.</div>
      <div><b>Concepts</b><ul><li>Imports and inheritance</li><li><code>Ownable</code></li><li>18 decimals</li><li><code>approve</code> / <code>transferFrom</code></li></ul></div>
      <div><b>You produce</b>A token with balances on three accounts.</div>
    </div>
    <div class="pre-wrap"><pre><code>// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/// @title CourseToken: a simple ERC-20 token. Only the owner can mint.
contract CourseToken is ERC20, Ownable {
    constructor() ERC20("Course Token", "CRS") Ownable(msg.sender) {
        _mint(msg.sender, 1000 * 10 ** decimals());
    }

    function mint(address to, uint256 amount) external onlyOwner {
        _mint(to, amount);
    }
}</code></pre><button class="copy" type="button">Copy</button></div>

## Build

<ol class="steps">
      <li>Create <code>CourseToken.sol</code>, paste, compile.<span class="exp">Remix downloads OpenZeppelin automatically. A <code>.deps</code> folder appears.</span></li>
      <li>Deploy as account 1 (Value 0). Call <span class="ui">balanceOf</span> with account 1’s address.<span class="exp"><code>1000000000000000000000</code> = 1000 tokens × 10<sup>18</sup>.</span></li>
      <li>Call <span class="ui">transfer</span>: to = account 2, amount = <code>10000000000000000000</code> (10 tokens).<span class="exp">Logs: <code>Transfer</code>. Account 2’s balance = 10 tokens.</span></li>
      <li>Select account 2. Call <span class="ui">mint</span> to itself with any amount.<span class="exp">Revert with <code>OwnableUnauthorizedAccount</code>. Only the owner can mint.</span></li>
      <li>Select account 1. Call <span class="ui">approve</span>: spender = account 3, amount = <code>5000000000000000000</code> (5 tokens).<span class="exp">Logs: <code>Approval</code>. <span class="ui">allowance</span>(account 1, account 3) = 5 tokens.</span></li>
      <li>Select account 3. Call <span class="ui">transferFrom</span>: from = account 1, to = account 3, amount = 5 tokens.<span class="exp">Account 3 has 5 tokens. Allowance is now 0.</span></li>
    </ol>

## Apply

<div class="aud">
      <div class="cs"><h5>Technology lens</h5><ul><li>Add an allow-list so only “verified investors” can receive tokens (programmable compliance, F6).</li></ul></div>
      <div class="bi"><h5>Business lens</h5><ul><li>The token could be a course credit, a voucher or a loyalty point. Which business model fits, and who sets the supply?</li></ul></div>
      <div class="lw"><h5>Law lens</h5><ul><li>When is a token a financial instrument (MiFID II), an e-money token, or another crypto-asset under MiCA? Does a voucher fall under an exemption?</li></ul></div>
    </div>

## Ship

<ul class="outc">
      <li>You can explain why token amounts carry 18 zeros.</li>
      <li>You can explain how an allowance lets a contract or person spend your tokens.</li>
      <li>You can explain why audited libraries are standard practice.</li>
    </ul>
