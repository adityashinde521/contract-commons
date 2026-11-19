---
title: "Certificate contract with the OpenZeppelin Wizard"
module: 5
order: 3
kind: "lab-gui"
minutes: "45 min"
legacy: "G1"
problem: "A university wants a certificate contract but has no Solidity developer."
---

## Problem

<div class="cc-callout cc-callout--problem"><div><b>The question.</b> A university wants a certificate contract but has no Solidity developer.</div></div>

## Concept

<div class="ov">
      <div><b>You will</b>Configure an NFT certificate contract with checkboxes, deploy it with buttons and issue a certificate.</div>
      <div><b>Tools</b><a href="https://wizard.openzeppelin.com" target="_blank" rel="noopener">wizard.openzeppelin.com</a>, Remix, Etherscan.</div>
      <div><b>You need</b>A browser. For Sepolia: MetaMask and test ETH.</div>
    </div>
    <p>The OpenZeppelin Wizard writes audited contract code from your choices. OpenZeppelin is the most widely used library of contract building blocks. You do not type code; you decide what the contract should allow, and that decision is the legal and business work.</p>

## Build

<div class="checked"><b>Checked on 20 November 2026</b> against the tool’s official documentation. Tools change their screens often. If a button has a different name, look for the closest one and note the difference in your lab log.</div>

<h4>A. Configure</h4>
    <ol class="steps">
      <li>Open <a href="https://wizard.openzeppelin.com" target="_blank" rel="noopener">wizard.openzeppelin.com</a>. Select <span class="ui">ERC721</span>.<span class="exp">The Wizard shows ERC721 settings on the left and Solidity code on the right.</span></li>
      <li>Name: <code>Course Certificate</code>. Symbol: <code>CERT</code>.<span class="exp">The code updates live: contract CourseCertificate is ERC721, with “Course Certificate”, “CERT” in the constructor.</span></li>
      <li>Features: tick <span class="ui">Mintable</span>, <span class="ui">Auto Increment Ids</span> and <span class="ui">URI Storage</span>. Access control: <span class="ui">Ownable</span>.<span class="exp">The code on the right updates with every click. Find the <code>safeMint</code> function and <code>onlyOwner</code>.</span></li>
      <li>Do not tick <span class="ui">Burnable</span> yet. Discuss first: should a holder be able to destroy a certificate?<span class="exp">No ERC721Burnable import in the code. Your team’s one-sentence answer is in the lab log.</span></li>
    </ol>
    <h4>B. Deploy</h4>
    <ol class="steps">
      <li>Click <span class="ui">Open in Remix</span>.<span class="exp">Remix opens with the contract file.</span></li>
      <li>Compile. In Deploy &amp; run, select the certificate contract. The constructor asks for <code>initialOwner</code>: paste your own account address.<span class="exp">A deployed CourseCertificate with orange buttons safeMint and transferFrom and blue buttons such as owner and name.</span></li>
      <li>Deploy on Remix VM, or on Sepolia with Injected Provider – MetaMask.<span class="exp">A deployed contract with many buttons: these are the ERC-721 functions.</span></li>
    </ol>
    <h4>C. Issue and check a certificate</h4>
    <ol class="steps">
      <li>Call <span class="ui">safeMint</span>: <code>to</code> = a teammate’s address, <code>uri</code> = a short text such as <code>Smart Contracts Lab 2026 – passed</code>.<span class="exp">Logs: <code>Transfer</code> from the zero address. Token ID 0.</span></li>
      <li>Call <span class="ui">ownerOf</span>(0) and <span class="ui">tokenURI</span>(0).<span class="exp">The teammate’s address and your text.</span></li>
      <li>Switch to the teammate’s account and try <span class="ui">safeMint</span>.<span class="exp">Revert: only the owner (issuer) can mint.</span></li>
      <li>On Sepolia: verify the contract (<a href="/lessons/lab-sepolia/">8.2 Sepolia deployment</a>, step C) and issue a second certificate from Etherscan’s <span class="ui">Write Contract</span> tab.<span class="exp">A form-based interface for your own contract, with no Remix needed.</span></li>
    </ol>

## Apply

<div class="aud">
      <div class="cs"><h5>Technology lens</h5><ul><li>Make the certificate non-transferable (“soulbound”). Which function do you need to override?</li></ul></div>
      <div class="bi"><h5>Business lens</h5><ul><li>Who pays gas when a university issues 5,000 certificates? Compare with a PDF and a verification portal.</li></ul></div>
      <div class="lw"><h5>Law lens</h5><ul><li>A transferable degree certificate can be sold. Is that a problem? Which features must a legally useful credential have?</li><li>A student wants a certificate deleted under the GDPR. What can the issuer do?</li></ul></div>
    </div>

## Ship

<ul class="outc">
      <li>You configured and deployed a standard contract without writing code.</li>
      <li>You can explain each option you ticked as a business or legal decision.</li>
      <li>You can check who issued and who holds a certificate.</li>
    </ul>
    <div class="callout lab"><h5>Lab log</h5><p>Screenshot of your Wizard settings, contract address, Etherscan link, and one sentence per option explaining why you chose it.</p></div>
