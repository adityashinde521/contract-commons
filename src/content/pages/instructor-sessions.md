---
title: "Running a lab session"
minutes: "15 min"
---

## 90-minute plan

<ol>
      <li><b>0–10 min.</b> Show the business or legal problem first (for example: “How do strangers buy safely online?”).</li>
      <li><b>10–25 min.</b> Live demo in Remix or in G1. Students watch and predict each result before you click.</li>
      <li><b>25–60 min.</b> Teams do the lab. The builder reads each step aloud; the analysts explain it in their words.</li>
      <li><b>60–80 min.</b> Teams change one rule (an extension task) and present the effect in two minutes.</li>
      <li><b>80–90 min.</b> Three-question check: one per lens: technology, business, law. Quiz as homework.</li>
    </ol>

## Preparation checklist

<ul>
      <li><b>Test ETH:</b> faucets often need a login or a small Mainnet balance. Fund a course wallet a week before L7 and the GUI labs, and send each team about 0.1 SepoliaETH.</li>
      <li><b>Tool accounts:</b> students need free accounts for thirdweb (G2) and Tenderly (G8), and an Etherscan API key for sol2uml (G10). Ask them to sign up before the session. No tool needs a payment method.</li>
      <li><b>Compiler:</b> open every lab file in Remix the day before. Remix updates often.</li>
      <li><b>Accounts:</b> Remix VM addresses are the same for everyone. Put account 1–4 addresses on a slide.</li>
      <li><b>Hosted tools:</b> check easscan, Safe and the Wizard the day before. Labels change.</li>
      <li><b>Testnet:</b> a proposal from May 2026 would replace Sepolia and sunset it in Q2/Q3 2027. Check the status each semester.</li>
      <li><b>Safety:</b> repeat the five rules (S2) at the start of every Sepolia session.</li>
    </ul>

## Common errors

<div class="tw"><table>
      <tr><th>Symptom</th><th>Cause</th><th>Fix</th></tr>
      <tr><td>Deploy reverts, “should be payable”</td><td>Value still set from an earlier payment.</td><td>Value 0 for every non-payable call.</td></tr>
      <tr><td><code>BigNumberish … empty string</code></td><td>Empty constructor field.</td><td>Fill all fields.</td></tr>
      <tr><td>“Wrong state”</td><td>Wrong step order or an old instance.</td><td>Click <code>state</code> first; delete old instances.</td></tr>
      <tr><td>“Send exact price”</td><td>Unit Wei instead of Ether.</td><td>Value unit Ether.</td></tr>
      <tr><td>“Only …”</td><td>Wrong account selected.</td><td>Check the Account field.</td></tr>
      <tr><td>Compiler error at <code>pragma</code></td><td>Compiler too old.</td><td>0.8.24 or newer.</td></tr>
      <tr><td>Contracts gone</td><td>Remix VM resets on reload.</td><td>Deploy again.</td></tr>
      <tr><td>No balance in MetaMask</td><td>Wrong network.</td><td>Select Sepolia.</td></tr>
      <tr><td>Safe transaction stuck at “1 of 2”</td><td>Second owner not connected.</td><td>Switch MetaMask account and reload.</td></tr>
    </table></div>
