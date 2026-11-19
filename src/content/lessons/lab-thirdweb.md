---
title: "thirdweb: deploy and manage a ready-made contract"
module: 5
order: 4
kind: "lab-gui"
minutes: "60 min"
legacy: "G2"
problem: "An events team wants tickets on chain, with a limit per person, by next week, without hiring a developer."
---

## Problem

<div class="cc-callout cc-callout--problem"><div><b>The question.</b> An events team wants tickets on chain, with a limit per person, by next week, without hiring a developer.</div></div>

## Concept

<div class="ov">
      <div><b>You will</b>Deploy a prebuilt “Edition Drop” contract on Sepolia, create event tickets, set claim rules and airdrop tickets, all from a dashboard.</div>
      <div><b>Tool</b><a href="https://thirdweb.com/explore" target="_blank" rel="noopener">thirdweb Explore</a> and the thirdweb dashboard. thirdweb is a commercial Web3 development platform with a catalogue of audited, ready-made contracts.</div>
      <div><b>You need</b>MetaMask on Sepolia with about 0.02 SepoliaETH, a free thirdweb sign-in.</div>
    </div>
    <p>An <b>Edition Drop</b> is an ERC-1155 contract: each token ID is one item (for example “Workshop ticket”), and many people can hold copies. A <b>claim phase</b> sets who may claim, how many, from when and at what price. The dashboard turns these rules into contract settings.</p>
    <div class="callout warn"><h5>Free and test-only</h5><p>Choose Sepolia as the network. Set the claim price to 0. Skip any offer of a paid plan.</p></div>

## Build

<h4>A. Deploy</h4>
    <ol class="steps">
      <li>Open <a href="https://thirdweb.com/explore" target="_blank" rel="noopener">thirdweb.com/explore</a>. Sign in with MetaMask (account 1) or e-mail. If asked, create a team and a project named “Smart Contracts Lab”.</li>
      <li>In the catalogue, open <span class="ui">Edition Drop</span>. Read the description and the list of functions. Click <span class="ui">Deploy</span>.<span class="exp">A deployment form with name, symbol, description and image.</span></li>
      <li>Name: <code>Lab Workshop Tickets</code>, symbol <code>LWT</code>. Leave the primary sale recipient as your own address.</li>
      <li>Under network or chain, choose <b>Sepolia</b>. Click <span class="ui">Deploy now</span> and confirm in MetaMask.<span class="exp">After about 15 seconds, the contract’s own dashboard opens with tabs such as Overview, NFTs, Claim conditions, Permissions, Explorer and Settings.</span></li>
    </ol>
    <h4>B. Create a ticket and claim rules</h4>
    <ol class="steps">
      <li>In the NFTs tab, click <span class="ui">Create</span> (sometimes “Lazy mint”). Name: “Workshop ticket, 3 Dec 2026”. Add a short description. Save and confirm in MetaMask.<span class="exp">Token ID 0 appears with supply 0. Nothing is owned yet: the item only exists as a template.</span></li>
      <li>Open token 0 and its claim conditions. Click <span class="ui">Add initial claim phase</span> (or similar). Set: start now, price 0, limit 1 per wallet. Save and confirm.<span class="why">This is a rule in the contract, not a setting in a website. Anyone can read it on Etherscan.</span></li>
      <li>Claim one ticket yourself from the token page (button such as <span class="ui">Claim</span>).<span class="exp">Supply 1, owner = account 1.</span></li>
      <li>Switch MetaMask to account 1 again and try to claim a second ticket.<span class="exp">The transaction fails or the dashboard refuses: the limit is 1 per wallet.</span></li>
    </ol>
    <h4>C. Airdrop and inspect</h4>
    <ol class="steps">
      <li>Use <span class="ui">Airdrop</span> on token 0. Upload a CSV with two columns, <code>address,quantity</code>, and the addresses of two teammates with quantity 1. Confirm.<span class="exp">The teammates own one ticket each.</span></li>
      <li>Open the <span class="ui">Permissions</span> tab.<span class="exp">A list of roles (for example admin, minter). Your address holds them.</span></li>
      <li>Open the <span class="ui">Explorer</span> tab and call a read function such as <code>balanceOf</code> for a teammate and token 0. Then open the contract on <a href="https://sepolia.etherscan.io" target="_blank" rel="noopener">sepolia.etherscan.io</a>.<span class="exp">Same result in both places: the dashboard only shows what is on chain.</span></li>
    </ol>

## Apply

<div class="aud">
      <div class="cs"><h5>CS</h5><ul><li>Compare the deployed code with the Wizard contract in G1. Which one is easier to audit? Is the thirdweb contract upgradeable?</li></ul></div>
      <div class="bi"><h5>BI</h5><ul><li>Vendor lock-in: what happens to your tickets if the vendor’s dashboard closes or changes its prices?</li><li>Read the vendor’s fee terms. Who earns what on a paid mint?</li></ul></div>
      <div class="lw"><h5>Law</h5><ul><li>A ticket sold with “limit 1 per wallet” can still be bought many times with many wallets. Is the rule an effective anti-scalping term?</li><li>The admin role can change claim rules later. What must the ticket terms say about this?</li></ul></div>
    </div>

## Ship

<ul class="outc">
      <li>You deployed a contract from a vendor catalogue and configured it without code.</li>
      <li>You can explain lazy minting, claim phases, airdrops and roles.</li>
      <li>You can tell what the dashboard controls (a view and a convenience) and what the contract enforces.</li>
    </ul>
    <div class="callout lab"><h5>Lab log</h5><p>Contract address, Etherscan link, a screenshot of the claim phase and of the Permissions tab, and the failed second claim.</p></div>
