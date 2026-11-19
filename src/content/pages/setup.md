---
title: "Setup and safety rules"
minutes: "30 min"
---

## Setup

<div class="goal"><b>Goal:</b> your browser, Remix and a test wallet are ready before the first lab.</div>
    <h4>For everyone</h4>
    <ol class="steps">
      <li>Use a desktop browser: Chrome, Brave, Edge or Firefox. Phones are not suitable for the labs.<span class="exp">You can open <a href="https://remix.ethereum.org" target="_blank" rel="noopener">remix.ethereum.org</a> and see the file explorer on the left.</span></li>
      <li>Install the <a href="https://metamask.io" target="_blank" rel="noopener">MetaMask</a> browser extension from the official site only. Create a <b>new wallet just for this course</b>.<span class="exp">A fox icon in the browser toolbar and a 12-word recovery phrase that you wrote on paper.</span><span class="why">Labs L7, G1–G5 and G7–G8 sign transactions on a public test network.</span></li>
      <li>In MetaMask, turn on <span class="ui">Show test networks</span> and select <b>Sepolia</b>.<span class="exp">The network name at the top shows “Sepolia”. Balance 0 SepoliaETH.</span></li>
      <li>Get test ETH from a faucet, for example the <a href="https://www.alchemy.com/faucets/ethereum-sepolia" target="_blank" rel="noopener">Alchemy Sepolia faucet</a>, the Google Cloud Web3 faucet or the pk910 PoW faucet. Some ask for a login or a small Mainnet balance. If that is a problem, ask the instructor: test ETH is shared in class.<span class="exp">0.05 SepoliaETH or more after a few minutes.</span></li>
      <li>Create two more accounts in MetaMask (<span class="ui">Add account</span>). Name them “Account 2” and “Account 3”.<span class="exp">Three addresses. G3 (Safe) and G4 (Aragon) need them.</span></li>
    </ol>
    <h4>For the code labs</h4>
    <ul>
      <li>A free GitHub account to back up your lab files. Remix stores files only in the browser.</li>
      <li>Optional: Visual Studio Code with the Solidity extension, for work after the course.</li>
    </ul>

## Safety rules

<div class="callout warn"><h5>Five rules for the whole course</h5><ol>
      <li><b>Never</b> type, paste or photograph your recovery phrase anywhere: not in a website, not in a chat, not in a file. Nobody from the course will ever ask for it.</li>
      <li>Use the course wallet for testnets only. Never send real money to it.</li>
      <li>Never deploy to Ethereum Mainnet in this course.</li>
      <li>Check the network before every signature: it must say Sepolia or Remix VM.</li>
      <li>Read what MetaMask asks you to sign. If you do not understand it, click <span class="ui">Reject</span>.</li>
    </ol></div>
    <div class="callout tip"><h5>Remix VM, Sepolia and Mainnet</h5><p>The Remix VM is a simulated chain inside your browser: instant, free, reset on reload. Sepolia is a real public test network with worthless test ETH and blocks every 12 seconds. Mainnet is real money. Most code labs use the Remix VM; L7 and most GUI labs use Sepolia. G9 and G11 only read public data.</p></div>
    <div class="callout warn"><h5>Testnet status (November 2026)</h5><p>Sepolia is the standard Ethereum test network for applications. A public proposal from May 2026 on the Ethereum Magicians forum suggests replacing Sepolia with a new testnet and sunsetting it in Q2 or Q3 2027. It is a proposal, not a decision. If it happens, only the network name in L7 and the GUI labs changes; the steps stay the same.</p></div>
