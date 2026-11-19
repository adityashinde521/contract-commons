---
title: "To evaluate: new visual builders"
module: 13
order: 4
kind: "reading"
minutes: "20 min"
legacy: "G12"
problem: "A new tool promises to build contracts visually with AI. Should your course or your company use it?"
---

## Problem

<div class="cc-callout cc-callout--problem"><div><b>The question.</b> A new tool promises to build contracts visually with AI. Should your course or your company use it?</div></div>

## Concept

<div class="goal"><b>Goal:</b> judge a new no-code or visual builder before it is used in teaching or in a business.</div>
    <p>New visual tools for smart contracts appear every few months, often with AI features. They are not part of the course labs yet. Students or instructors can evaluate them with the checklist below and propose them for a future semester.</p>
    <div class="tw"><table>
      <tr><th>Tool</th><th>What it claims</th><th>Status (Nov 2026)</th></tr>
      <tr><td><a href="https://peerpush.com/p/doodledapp" target="_blank" rel="noopener">DoodleDapp</a></td><td>Build, test and deploy Solidity contracts visually, without code</td><td>Listed as newly launched in April 2026 after a beta. Chains, pricing and code export not confirmed.</td></tr>
      <tr><td>AI contract generators</td><td>Write a contract from a text prompt</td><td>Many tools, quality varies. Compare the output with OpenZeppelin (G1) and test it (G8).</td></tr>
    </table></div>

## Try it

<div class="tw"><table>
      <tr><th>Question</th><th>Why it matters</th></tr>
      <tr><td>Does it work on a testnet (Sepolia) for free?</td><td>Course rule: no real money.</td></tr>
      <tr><td>Can you see and export the generated Solidity code?</td><td>Without the code, nobody can audit or verify the contract.</td></tr>
      <tr><td>Is the code based on audited libraries (for example OpenZeppelin)?</td><td>Reduces the risk of bugs.</td></tr>
      <tr><td>Can the contract be verified on Etherscan?</td><td>Others must be able to read the terms.</td></tr>
      <tr><td>Who holds the admin keys after deployment?</td><td>The vendor must not keep control over your contract.</td></tr>
      <tr><td>What data does the tool collect, and where is it stored?</td><td>GDPR and university data-protection rules.</td></tr>
      <tr><td>What happens if the vendor closes?</td><td>The contract stays on chain; the dashboard may not.</td></tr>
    </table></div>
    <div class="callout warn"><h5>Safety</h5><p>Evaluate only with the course wallet on a testnet. Never connect a wallet that holds real funds to an unknown tool.</p></div>

## Ship

<p>Write three sentences in your lab log: the main idea, one example from your discipline, and one open question. Then take the quiz below.</p>
