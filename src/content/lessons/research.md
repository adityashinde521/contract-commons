---
title: "Current research and open problems"
module: 13
order: 3
kind: "lesson"
minutes: "60 min"
legacy: "F7"
problem: "You are choosing a seminar paper or thesis topic. Where is the research frontier, and what is still open?"
---

## Problem

<div class="cc-callout cc-callout--problem"><div><b>The question.</b> You are choosing a seminar paper or thesis topic. Where is the research frontier, and what is still open?</div></div>

## Concept

<div class="goal"><b>Goal:</b> you know the active research areas, one recent work in each, and the open questions.</div>
    <div class="tw"><table>
      <tr><th>Research area</th><th>Main question</th><th>Recent work and finding</th></tr>
      <tr><td><b>AI for smart-contract security</b></td><td>Can language models find and fix vulnerabilities reliably?</td><td>Ince et al. (2025), systematic review: LLM-based tools are not yet ready to replace classic analysers such as Slither and Mythril; hybrids work best, and small fine-tuned models can beat large general models. SCONE-bench (Dec 2025) measures exploitation in dollars (<a href="/lessons/security-in-practice/">7.2 Security in practice</a>).</td></tr>
      <tr><td><b>MEV and transaction ordering</b></td><td>Who profits from the order of transactions, and how do we make ordering fair?</td><td>Mancino and Sevim (Mar 2026), SoK: MEV research moved through three eras; the current frontier is <b>cross-chain MEV</b>. Glamsterdam’s ePBS (<a href="/lessons/ethereum-today/">10.1 Ethereum today</a>) comes from this line of research.</td></tr>
      <tr><td><b>Computable and smart legal contracts</b></td><td>How do we write contracts that lawyers can read and machines can execute?</td><td>Laneve, Parenti and Sartor (Computer Law &amp; Security Review, Dec 2025): the <b>Stipula</b> language can import statutory rules, such as consumer protection, into a computable contract. Related: Catala, Lexon, Accord Project (<a href="/lessons/lab-accord/">12.4</a>).</td></tr>
      <tr><td><b>Privacy for agreements</b></td><td>Can parties prove a confidential contract was performed correctly?</td><td>zk-Agreements (arXiv, Oct 2025) combines Accord Project contracts, zero-knowledge proofs and trusted execution environments.</td></tr>
      <tr><td><b>Scaling and data availability</b></td><td>How far can rollups scale without losing decentralisation?</td><td>PeerDAS in production since Fusaka (Dec 2025). Next: stateless clients, ZK-EVMs, real-time proving.</td></tr>
      <tr><td><b>Post-quantum blockchains</b></td><td>How do we migrate keys and signatures without loss of funds?</td><td>Ethereum Foundation Post-Quantum team (since Jan 2026): hash-based signatures, aggregation, account migration (<a href="/lessons/quantum/">13.2 Quantum</a>).</td></tr>
      <tr><td><b>Agent economies</b></td><td>How do autonomous agents find, trust and pay each other, and who is accountable?</td><td>ERC-8004 and x402 are the first standards. Open: reputation manipulation, validation of agent work, legal attribution (<a href="/lessons/ai-agents/">13.1 AI agents</a>).</td></tr>
      <tr><td><b>Formal verification</b></td><td>Can we prove that a contract always behaves as intended?</td><td>Solidity SMTChecker, Certora Prover, the K framework. Open: specifications that non-experts, including lawyers, can write and check.</td></tr>
    </table></div>
    <div class="callout law"><h5>The common thread</h5><p>Most open problems sit between disciplines: a technical fix (fair ordering, a pause switch) needs an economic reason and a legal basis. That is why every student in this course learns technology, business and law.</p></div>

<!-- deep:start -->
### Worked example

<div class="worked">
<p><b>Case:</b> summarise one paper in the course format.</p>
<ol>
  <li><b>Problem:</b> Can language models find vulnerabilities in smart contracts reliably? (Ince et al., 2025)</li>
  <li><b>Method:</b> a systematic review of studies that test LLM-based tools on labelled contract datasets.</li>
  <li><b>Result:</b> LLMs are not yet reliable enough to replace analysers such as Slither; combined approaches work best.</li>
  <li><b>Technology lens:</b> how were false positives counted? Would results hold on new contracts?</li>
  <li><b>Business lens:</b> could a hybrid tool reduce audit cost for small teams?</li>
  <li><b>Law lens:</b> if an AI audit misses a bug, who is liable: the tool provider, the auditor, or the developer?</li>
</ol>
</div>

### Common mistakes

<ul>
  <li>Citing a preprint as settled fact. Check whether it was peer reviewed.</li>
  <li>Reading only the abstract. The limitations section often changes the meaning.</li>
</ul>
<!-- deep:end -->

### Watch and read

<p>For each paper, read the abstract, introduction and conclusion. Write three lines: problem, method, result. Then one line each for the technology, business and law lenses.</p>
    <div class="vids">
      <a class="vid read" href="https://arxiv.org/abs/2504.04685" target="_blank" rel="noopener"><span class="play"></span><span><b>Generative LLM usage in smart contract vulnerability detection</b><small>Ince, Yu, Liu, Du. arXiv, April 2025</small></span></a>
      <a class="vid read" href="https://red.anthropic.com/2025/smart-contracts/" target="_blank" rel="noopener"><span class="play"></span><span><b>AI agents find $4.6M in blockchain smart contract exploits (SCONE-bench)</b><small>Anthropic and MATS, December 2025</small></span></a>
      <a class="vid read" href="https://arxiv.org/abs/2603.07716" target="_blank" rel="noopener"><span class="play"></span><span><b>SoK: The evolution of Maximal Extractable Value</b><small>Mancino and Sevim. arXiv, March 2026</small></span></a>
      <a class="vid read" href="https://doi.org/10.1016/j.clsr.2025.106223" target="_blank" rel="noopener"><span class="play"></span><span><b>Integration of statutory norms in computable contracts (Stipula)</b><small>Laneve, Parenti, Sartor. CLSR, December 2025. Best entry paper for the law lens.</small></span></a>
      <a class="vid read" href="https://arxiv.org/pdf/2510.20007" target="_blank" rel="noopener"><span class="play"></span><span><b>zk-Agreements: privacy-preserving trust in confidential agreements</b><small>arXiv, October 2025</small></span></a>
      <a class="vid read" href="https://arxiv.org/pdf/2407.19572" target="_blank" rel="noopener"><span class="play"></span><span><b>MEV mitigation approaches in Ethereum and Layer-2 chains: a survey</b><small>arXiv, July 2024</small></span></a>
    </div>
    <p class="note">Preprints (arXiv) are not peer-reviewed yet. Read them with care.</p>
<div class="tw"><table>
      <tr><th>Type</th><th>Where</th><th>Best for</th></tr>
      <tr><td>Security conferences</td><td>IEEE S&amp;P, ACM CCS, USENIX Security, NDSS</td><td>Attacks, analysis tools, formal methods</td></tr>
      <tr><td>Blockchain conferences</td><td>Financial Cryptography (FC), ACM AFT, IEEE ICBC</td><td>Protocols, DeFi, MEV, economics</td></tr>
      <tr><td>Preprints</td><td>arXiv (cs.CR), IACR ePrint</td><td>The newest work, before review</td></tr>
      <tr><td>Ethereum research</td><td>ethresear.ch, pq.ethereum.org, EIPs</td><td>Protocol design, upgrade proposals</td></tr>
      <tr><td>Law and technology</td><td>Computer Law &amp; Security Review, SSRN, Stanford CodeX</td><td>Smart legal contracts, regulation</td></tr>
    </table></div>

## Try it

<p>Pick one paper from the reading list. Write the three-line summary (problem, method, result) and one line each for the technology, business and law lenses.</p>

## Apply

<div class="aud"><div class="cs"><h5>Technology lens</h5><ul><li>Which open problem could you test with the course labs?</li></ul></div><div class="bi"><h5>Business lens</h5><ul><li>Which research result changes a business decision?</li></ul></div><div class="lw"><h5>Law lens</h5><ul><li>Which result needs a legal answer before it can be used?</li></ul></div></div>

## Ship

<p>Write three sentences in your lab log: the main idea, one example for each lens (technology, business, law), and one open question. Then take the quiz below.</p>
