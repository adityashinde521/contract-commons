---
title: "Deploy to Ethereum (Sepolia) and verify"
module: 8
order: 2
kind: "lab-remix"
minutes: "90 min"
legacy: "L7"
problem: "So far everything ran in your browser. Now your contract goes on a public network that anyone in the world can read and use."
---

## Problem

<div class="cc-callout cc-callout--problem"><div><b>The question.</b> So far everything ran in your browser. Now your contract goes on a public network that anyone in the world can read and use.</div></div>

## Concept

<div class="ov">
      <div><b>You will</b>Deploy two contracts to the public Sepolia testnet, verify the source and use them from Etherscan.</div>
      <div><b>Before</b>S2 done. At least 0.05 SepoliaETH in MetaMask account 1, a little in account 2.</div>
      <div><b>You produce</b>Two verified contracts with Etherscan links in your lab log.</div>
    </div>
    <div class="callout warn"><h5>Safety</h5><ul>
      <li>Course wallet only. No real money. Never Mainnet.</li>
      <li>Never type your recovery phrase into a website, chat or file.</li>
      <li>Before each MetaMask confirmation, check: network = Sepolia.</li>
    </ul></div>

## Build

<h4>A. Connect Remix to Sepolia</h4>
    <ol class="steps">
      <li>In MetaMask, select Sepolia and account 1.</li>
      <li>In Remix Deploy &amp; run, set Environment to <span class="ui">Injected Provider – MetaMask</span>. Approve the connection in MetaMask.<span class="exp">Remix shows “Sepolia (11155111) network” and your MetaMask address with its SepoliaETH balance.</span></li>
    </ol>
    <h4>B. Deploy DocumentRegistry</h4>
    <ol class="steps">
      <li>Select <code>DocumentRegistry</code>, Value 0, click <span class="ui">Deploy</span>. MetaMask opens: check network and fee, click <span class="ui">Confirm</span>.<span class="exp">After about 12 seconds the terminal shows the receipt and a link to Etherscan.</span></li>
      <li>Copy the contract address. Open <a href="https://sepolia.etherscan.io" target="_blank" rel="noopener">sepolia.etherscan.io</a> and search for it.<span class="exp">The contract page with one transaction: “Contract Creation”. Note block number and gas used.</span></li>
      <li>In Remix, call <span class="ui">hashText</span> (free) and then <span class="ui">register</span> with the result (MetaMask confirms).<span class="exp">On Etherscan, a new transaction and, under <span class="ui">Events</span>, <code>DocumentRegistered</code>.</span></li>
    </ol>
    <h4>C. Verify the source code</h4>
    <ol class="steps">
      <li>In Remix, open the <span class="ui">Plugin manager</span> (plug icon, bottom left). Activate <span class="ui">Contract Verification</span>.</li>
      <li>Choose the network Sepolia, paste the contract address, select the contract, and verify with <b>Sourcify</b> (no API key) or Etherscan (free API key).<span class="exp">Status “verified” or “perfect match”.</span></li>
      <li>Reload the contract on Etherscan. Open the <span class="ui">Contract</span> tab.<span class="exp">Green check, readable source, and the tabs <span class="ui">Read Contract</span> and <span class="ui">Write Contract</span>.</span></li>
      <li>In <span class="ui">Write Contract</span>, click <span class="ui">Connect to Web3</span>, then call <code>register</code> with a new hash.<span class="exp">A transaction from Etherscan itself. This is a no-code interface to your contract that law students can use (see G1).</span></li>
    </ol>
    <h4>D. Escrow on a real network</h4>
    <ol class="steps">
      <li>In MetaMask, copy the address of account 2 (seller). Use account 1’s address or a classmate’s address as arbiter.</li>
      <li>Account 1, Value 0. Deploy <code>Escrow</code> with price <code>1000000000000000</code> (0.001 ether).</li>
      <li>Value 0.001 Ether, call <span class="ui">deposit</span>. Then Value 0, call <span class="ui">confirmDelivery</span>.<span class="exp">On Etherscan: three transactions and an internal transaction that pays account 2.</span></li>
      <li>Verify the Escrow as in C.</li>
    </ol>

### If something goes wrong

<div class="tw"><table>
      <tr><th>Symptom</th><th>Fix</th></tr>
      <tr><td>Remix shows no account after choosing Injected Provider</td><td>Unlock MetaMask, approve the connection, reload Remix.</td></tr>
      <tr><td>“Insufficient funds”</td><td>Faucet again, or ask the instructor for test ETH.</td></tr>
      <tr><td>Transaction pending for minutes</td><td>Wait. If stuck, speed it up in MetaMask.</td></tr>
      <tr><td>Verification fails</td><td>Same compiler version and settings as in Remix. Try Sourcify.</td></tr>
      <tr><td>MetaMask shows Ethereum Mainnet</td><td>Stop. Switch to Sepolia before confirming anything.</td></tr>
    </table></div>

## Apply

<div class="aud">
      <div class="cs"><h5>CS</h5><ul><li>Compare gas used on Sepolia with the Remix VM. Why are they almost the same?</li></ul></div>
      <div class="bi"><h5>BI</h5><ul><li>Convert the gas used to euros at today’s Mainnet gas price and ETH price. Then compare with a Layer 2 (F1).</li></ul></div>
      <div class="lw"><h5>Law</h5><ul><li>Verified code is public. Can a party claim “I did not know the terms”? Does publishing code satisfy transparency rules for standard terms?</li></ul></div>
    </div>

## Ship

<ul class="outc">
      <li>Two verified contracts on Sepolia, with links in the lab log.</li>
      <li>You can read a transaction on Etherscan: from, to, value, gas, status, events.</li>
      <li>You can explain why Sepolia takes seconds and the Remix VM is instant.</li>
    </ul>
