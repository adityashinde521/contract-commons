---
title: "Team lab: a clickable app for your Escrow"
module: 9
order: 5
kind: "lab-gui"
minutes: "60 min"
legacy: "G7"
problem: "The team’s Escrow works in Remix, but the buyer and seller will never open Remix. They need buttons."
---

## Problem

<div class="cc-callout cc-callout--problem"><div><b>The question.</b> The team’s Escrow works in Remix, but the buyer and seller will never open Remix. They need buttons.</div></div>

## Concept

<div class="ov">
      <div><b>You will</b>Generate a simple web app for the team’s Escrow, so anyone can use it with buttons.</div>
      <div><b>Tool</b>Remix <b>QuickDApp</b>, which uses RemixAI to create a React front end from a deployed contract.</div>
      <div><b>You need</b>An Escrow deployed on Sepolia (<a href="/lessons/lab-sepolia/">8.2 Sepolia deployment</a>, part D). One team member at the keyboard; rotate for part B.</div>
    </div>
    <div class="callout warn"><h5>AI-generated code</h5><p>QuickDApp writes the interface with AI. Test every button against the expected results from <a href="/lessons/lab-escrow/">4.3 Escrow</a> before you trust it.</p></div>

## Build

<div class="checked"><b>Checked on 20 November 2026</b> against the tool’s official documentation. Tools change their screens often. If a button has a different name, look for the closest one and note the difference in your lab log.</div>

<h4>A. Generate</h4>
    <ol class="steps">
      <li>In Remix, set Environment to Injected Provider – MetaMask (Sepolia). Make sure the Escrow is listed under Deployed Contracts: deploy a new one, or load the one from <a href="/lessons/lab-sepolia/">8.2 Sepolia deployment</a> by pasting its address and clicking <span class="ui">At Address</span>.<span class="exp">The Escrow is under Deployed Contracts with a Sepolia address. QuickDApp is built for public networks; the Remix VM has limited support.</span></li>
      <li>Click the three dots next to the Escrow and choose <span class="ui">Create a DApp</span>.<span class="exp">The QuickDApp panel opens with the Escrow as Primary Contract and options for the front-end location.</span></li>
      <li>Keep the Escrow as primary contract. Add notes written by the law student: “Three role panels: Buyer, Seller, Arbiter. Show the current state in words. Show the price in ether, not wei. Show clear error messages.”<span class="exp">After Generate DApp, RemixAI proposes files; approve them (or Approve All). A live preview opens in the QuickDApp tab.</span></li>
      <li>Click <span class="ui">Generate DApp</span>. Review the proposed files and approve them.<span class="exp">A live preview in the QuickDApp tab.</span></li>
    </ol>
    <h4>B. Test (every team member, one role each)</h4>
    <ol class="steps">
      <li>Connect MetaMask in the preview. Compare the state the app shows with <span class="ui">state</span> in Remix.<span class="exp">The same value. If not, the interface is wrong.</span></li>
      <li>Run the release path with the app only. Deploy a new Escrow and run the refund path, including the “Only arbiter” revert.<span class="exp">The release path ends with the seller paid; the refund path shows a readable “Only arbiter” error when a non-arbiter clicks Refund.</span></li>
      <li>Write a test report: each button, expected result, actual result, pass or fail.<span class="exp">A table in your lab log with one row per button.</span></li>
      <li>Ask the AI for one improvement from your report (<span class="ui">Ask AI to update</span>). Test again.<span class="exp">After Ask AI to Update → Update with AI, a refreshed preview with your change. Use Refresh Preview if it does not update.</span></li>
    </ol>

## Apply

<div class="aud">
      <div class="cs"><h5>Technology lens</h5><ul><li>The contract is the source of truth; the app is only a view. What can a bad interface still do wrong?</li></ul></div>
      <div class="bi"><h5>Business lens</h5><ul><li>Which information must the interface show so a buyer can decide with full knowledge?</li></ul></div>
      <div class="lw"><h5>Law lens</h5><ul><li>Which EU consumer-law information duties apply before a consumer pays? Does the interface meet them?</li><li>Who is responsible for a misleading button: the contract author, the app author or the AI tool provider?</li></ul></div>
    </div>

## Ship

<ul class="outc">
      <li>The team has a working interface for its contract.</li>
      <li>Every team member ran a contract on a public network without Remix.</li>
      <li>You have a test report comparing the app with the contract.</li>
    </ul>
