# Deeper explanations, worked examples and common mistakes: modules 9-13.

D = {}

D["dapp-architecture"] = """
### In depth

<p>A decentralised application (dApp) is usually three layers. The <b>contracts</b> on chain hold the rules and the money. The <b>front end</b> is a normal website, often built with React, that reads data and prepares transactions. The <b>wallet</b> in the browser holds the keys and asks the user to approve each transaction. Between them sit an <b>RPC provider</b> that talks to the chain and often an <b>indexer</b> (for example The Graph or a custom database) that collects events, because reading history directly from a node is slow.</p>
<!-- diagram:dapp-stack -->
<p>Only the contract layer is decentralised. The website runs on a normal server and domain; it can be hacked, changed, or blocked in a country. If the front end is replaced with a malicious one, it can ask users to sign harmful transactions. That is why wallets decode what you are about to sign, and why some teams publish their front end on IPFS so that anyone can host an identical copy.</p>
<p>Reading and writing are different. Reading (<code>balanceOf</code>, <code>state()</code>) is a free <code>eth_call</code> and returns instantly. Writing is a transaction: the user signs, pays gas, and waits for inclusion. Good dApps show this clearly: a pending state, the transaction hash with an explorer link, and a clear message when a call reverts.</p>

### Worked example

<div class="worked">
<p><b>Case:</b> the buyer clicks “Pay 1 ETH” in an Escrow dApp.</p>
<ol>
  <li>The page reads <code>state()</code> and <code>price()</code> through the RPC provider: AwaitingPayment, 1 ETH. It enables the button.</li>
  <li>On click, the front end encodes a call to <code>deposit()</code> with value 1 ETH and passes it to MetaMask.</li>
  <li>MetaMask shows the contract address, the function and the value. The buyer confirms; the wallet signs and sends.</li>
  <li>The page shows “Pending” and the transaction hash. About 12 seconds later the receipt arrives with a <code>Deposited</code> event.</li>
  <li>The indexer stores the event; the seller’s dashboard now shows “Payment held”.</li>
</ol>
</div>

### Common mistakes

<ul>
  <li>“The dApp is on the blockchain.” Usually only the contracts are.</li>
  <li>“If the website is down, my funds are lost.” The contract still works; anyone can call it through Etherscan or another front end.</li>
</ul>
"""

D["oracles"] = """
### In depth

<p>Contracts cannot see the outside world, because every node must compute the same result and the internet gives different answers at different times. An <b>oracle</b> is any mechanism that writes outside facts onto the chain: prices, weather, delivery status, sports results, or the result of a computation. The <b>oracle problem</b> is that the contract is only as reliable as that input: perfect code acting on a wrong fact still produces a wrong result.</p>
<p>Oracles differ in how much trust they need. A <b>single reporter</b> (one company or one person signing a value) is simple but can lie or be hacked. A <b>decentralised oracle network</b> such as Chainlink collects the same value from many independent nodes and sources, takes the median, and publishes it, so a few bad reporters cannot move it. <b>On-chain prices</b> from a DEX pool are free but can be manipulated within one transaction; time-weighted averages (TWAP) make that more expensive. <b>Optimistic oracles</b> (for example UMA) accept an answer unless someone disputes it within a time window and puts up a bond.</p>
<!-- diagram:oracle -->
<p>For contracts with legal meaning, the oracle often is a person or institution: an arbiter, a notary, a logistics company. The legal questions follow: who is liable if the oracle is wrong, and was the party who chose it bound by that choice?</p>

### Worked example

<div class="worked">
<p><b>Case:</b> a lending protocol and a manipulated price.</p>
<ol>
  <li>Protocol A lets users borrow against token X. It reads X’s price from one small DEX pool.</li>
  <li>An attacker takes a flash loan of 5 million USDC and buys X in that pool. The pool price of X triples within the transaction.</li>
  <li>In the same transaction the attacker deposits X into Protocol A, which now values it at three times its real price, and borrows the maximum.</li>
  <li>The attacker sells X back, repays the flash loan and keeps the borrowed funds. Protocol A is left with overvalued collateral.</li>
  <li><b>Defence:</b> use a decentralised price feed, reject prices that move too far or are too old, and cap borrowing per block.</li>
</ol>
</div>

### Common mistakes

<ul>
  <li>“Chainlink makes the data true.” It makes it hard to manipulate; the sources can still be wrong.</li>
  <li>Forgetting to check how old a price is. A feed that stopped updating is a silent risk.</li>
</ul>
"""

D["decentralised-storage"] = """
### In depth

<p>Storing data on Ethereum is very expensive: writing 1 MB to contract storage would cost thousands of euros. So blockchains store small facts and <b>pointers</b>, while files live elsewhere. The question is where, and who can change or delete them.</p>
<p><b>IPFS</b> addresses files by their content: the address (CID) is derived from a hash of the file. If anyone changes the file, the CID changes, so a CID in a contract always refers to exactly one version. But IPFS does not guarantee that anyone keeps the file; it disappears unless someone <b>pins</b> it. <b>Filecoin</b> adds paid storage deals with proofs that providers still hold the data. <b>Arweave</b> charges once for permanent storage. A normal cloud server is cheap and fast, but the owner can change the file behind the same URL.</p>
<p>This is a legal design decision as much as a technical one. Data that may need correction or deletion under the GDPR, such as names, addresses or health data, must stay in a system that can delete it. Only a hash or an encrypted reference should go on chain or into permanent storage. Even then, check whether the hash can be linked back to a person.</p>

### Worked example

<div class="worked">
<p><b>Case:</b> where should each part of a course certificate NFT live?</p>
<div class="tw"><table>
  <tr><th>Data</th><th>Where</th><th>Why</th></tr>
  <tr><td>Token ID and owner address</td><td>On chain (ERC-721)</td><td>Must be verifiable by anyone</td></tr>
  <tr><td>Certificate design image</td><td>IPFS, pinned by the university</td><td>Fixed version; the CID proves it was not swapped</td></tr>
  <tr><td>Metadata JSON (course, grade band, image CID)</td><td>IPFS; its CID is the tokenURI</td><td>Tamper-evident</td></tr>
  <tr><td>Student’s name and matriculation number</td><td>University database only</td><td>Personal data must be correctable and deletable</td></tr>
</table></div>
</div>

### Common mistakes

<ul>
  <li>“IPFS stores files forever.” Only while someone pins them.</li>
  <li>“Encrypted personal data on chain is fine.” Encryption can be broken in future, and the key holder can still identify people.</li>
</ul>
"""

D["ethereum-today"] = """
### In depth

<p>Ethereum chose to scale through <b>rollups</b> instead of making the base layer itself much bigger. A rollup executes transactions on its own fast chain, bundles thousands of them, and posts the data and a summary of the new state to Ethereum. Because the data is on Ethereum, anyone can rebuild the rollup’s state and challenge or check it. Users pay much lower fees because the cost of posting to Ethereum is shared.</p>
<p>There are two kinds. <b>Optimistic rollups</b> (Arbitrum, Optimism, Base) assume batches are correct and allow anyone to submit a fraud proof during a challenge window of about seven days; withdrawals to Ethereum wait for that window. <b>ZK rollups</b> (zkSync, Starknet, Scroll, Linea) post a validity proof with each batch; Ethereum checks the proof, so no challenge window is needed.</p>
<!-- diagram:rollup -->
<p>Upgrades made this cheaper. Dencun (March 2024) added <b>blobs</b>, temporary data space priced separately for rollups. Fusaka (December 2025) added PeerDAS, which lets nodes check blob data by sampling small pieces, so Ethereum can carry many more blobs. Not all rollups are equally decentralised yet. L2BEAT rates them in <b>stages</b>: Stage 0 still relies heavily on its operators, Stage 2 lets users exit and challenge without trusting anyone special.</p>

### Worked example

<div class="worked">
<p><b>Case:</b> the same Escrow deposit on Ethereum and on a rollup.</p>
<div class="tw"><table>
  <tr><th></th><th>Ethereum mainnet</th><th>Optimistic rollup</th></tr>
  <tr><td>Fee for the deposit</td><td>About €1 (lesson 3.1 example)</td><td>A few cents</td></tr>
  <tr><td>Confirmation shown in the app</td><td>About 12 seconds</td><td>Under 1 second (from the sequencer)</td></tr>
  <tr><td>Final on Ethereum</td><td>About 13 minutes</td><td>When the batch is posted and finalised; withdrawal to L1 after about 7 days</td></tr>
  <tr><td>Extra trust</td><td>Ethereum validators</td><td>Plus the rollup’s sequencer and upgrade keys (check its L2BEAT stage)</td></tr>
</table></div>
</div>

### Common mistakes

<ul>
  <li>“L2s are separate blockchains.” Good rollups inherit Ethereum’s security for data and settlement; sidechains do not.</li>
  <li>“All rollups are equally safe.” Read the L2BEAT stage and who can upgrade the contracts.</li>
</ul>
"""

D["channels-sidechains-bridges"] = """
### In depth

<p>Before rollups, two other scaling ideas appeared, and both are still used. A <b>payment channel</b> locks funds in a contract between two parties. They then exchange signed balance updates off chain, as many as they like, for free and instantly. Only the opening and the final balance go on chain. The Bitcoin Lightning Network links channels into a network. Channels work well for repeated payments between the same parties, but funds are locked and both sides must stay online to watch for cheating.</p>
<p>A <b>sidechain</b> is an independent blockchain with its own validators that is connected to Ethereum by a bridge, for example Gnosis Chain or Polygon PoS. It is cheap and fast, but its security is its own: if its validators collude, Ethereum cannot help.</p>
<p>A <b>bridge</b> moves value between chains. The common design is <b>lock and mint</b>: lock the original tokens in a contract on chain A, and mint the same number of wrapped tokens on chain B. To return, burn on B and unlock on A. The bridge contract on A then holds everyone’s locked funds, and whoever controls the minting on B, often a small group of signers, controls their value. That is why bridges have suffered some of the largest hacks: Ronin (2022, about $600 million) and Wormhole (2022, about $320 million).</p>
<!-- diagram:bridge -->

### Worked example

<div class="worked">
<p><b>Case:</b> 100 USDC goes from Ethereum to a sidechain and the bridge is hacked.</p>
<ol>
  <li>Alice locks 100 USDC in the bridge on Ethereum. The bridge mints 100 “bridged USDC” to Alice on the sidechain.</li>
  <li>The bridge is controlled by 5 signers with a 3-of-5 threshold. Attackers steal 3 keys.</li>
  <li>They sign a fake message that releases all locked USDC on Ethereum to themselves.</li>
  <li>Alice still holds 100 bridged USDC on the sidechain, but nothing backs it any more. Its market price collapses.</li>
</ol>
<p><b>Lesson:</b> a wrapped token is a claim on someone else’s vault. Ask who guards the vault and how many keys it takes.</p>
</div>

### Common mistakes

<ul>
  <li>“Bridged tokens are the same asset.” They are IOUs from the bridge.</li>
  <li>“A sidechain is a Layer 2.” It does not inherit Ethereum’s security.</li>
</ul>
"""

D["zero-knowledge"] = """
### In depth

<p>A zero-knowledge proof (ZKP) lets a <b>prover</b> convince a <b>verifier</b> that a statement is true without revealing why. The classic picture is a cave with a magic door: Peggy shows Victor that she knows the password by coming out of whichever side he names, many times in a row, without ever saying the password. Modern ZKPs are mathematical: the statement is written as a circuit, the prover computes a short proof, and anyone can check the proof quickly.</p>
<p>A good proof system has three properties. <b>Completeness</b>: an honest prover with a true statement convinces the verifier. <b>Soundness</b>: a cheating prover with a false statement almost never succeeds. <b>Zero knowledge</b>: the verifier learns nothing except that the statement is true. Two families are common. <b>SNARKs</b> (for example Groth16, PLONK) produce tiny proofs that are cheap to verify on chain; some need a trusted setup. <b>STARKs</b> produce larger proofs but need no trusted setup and are considered safer against quantum computers.</p>
<p>ZKPs have two big uses. <b>Scaling</b>: a ZK rollup proves that thousands of transactions were executed correctly, so Ethereum checks one proof instead of re-running them. <b>Privacy</b>: a person proves “I am over 18”, “I am an EU resident” or “my balance is above X” without disclosing the underlying data. This fits the GDPR principle of data minimisation and the selective disclosure of the EU Digital Identity Wallet.</p>

### Worked example

<div class="worked">
<p><b>Case:</b> a wine shop must check that a buyer is over 18.</p>
<div class="tw"><table>
  <tr><th></th><th>Today (show ID card)</th><th>With a ZK credential</th></tr>
  <tr><td>What the shop sees</td><td>Name, date of birth, address, ID number, photo</td><td>“Age ≥ 18: true”, signed by a trusted issuer</td></tr>
  <tr><td>What the shop could leak</td><td>All of it</td><td>Almost nothing</td></tr>
  <tr><td>What the verifier checks</td><td>The card looks real</td><td>The proof is valid and the issuer’s key is on a trusted list</td></tr>
</table></div>
<p><b>Open question for the law lens:</b> is a proof that cannot be linked to a person still personal data? It depends on whether the shop or someone else can link it.</p>
</div>

### Common mistakes

<ul>
  <li>“ZK means encrypted.” The data is not sent at all; only a proof about it is.</li>
  <li>“ZK rollups are private.” Most publish all transaction data; ZK is used for correctness there, not secrecy.</li>
</ul>
"""

D["defi"] = """
### In depth

<p>Decentralised finance (DeFi) rebuilds financial services as open contracts. Four building blocks matter most. <b>Stablecoins</b> keep a stable value: fiat-backed ones (USDC, USDT) hold reserves at an issuer; crypto-backed ones (DAI/USDS) are over-collateralised by other tokens; algorithmic ones rely on incentives and failed badly with TerraUSD in 2022. <b>Decentralised exchanges</b> (DEXs) such as Uniswap replace order books with liquidity pools and a pricing formula. <b>Lending protocols</b> such as Aave let users deposit collateral and borrow against it; positions that fall below a safety level are liquidated automatically. <b>MEV</b> (maximal extractable value) is the profit that block builders and bots make by ordering, inserting or front-running transactions.</p>
<p>An automated market maker (AMM) keeps two token reserves, x and y, and enforces <b>x × y = k</b>. A buyer adds one token and removes the other so that the product stays constant. Large trades move the price a lot (<b>slippage</b>); small pools are easy to move, which is why they are dangerous as price oracles.</p>
<!-- diagram:amm -->
<p>Because every DeFi contract can call every other one (“money legos”), new products are built quickly, but risks also spread: a broken oracle or a depegged stablecoin can trigger liquidations across many protocols at once.</p>

### Worked example

<div class="worked">
<p><b>Case:</b> swap in a pool with 100 ETH and 300,000 USDC (k = 30,000,000). Price ≈ 3,000 USDC per ETH. Fees ignored.</p>
<ol>
  <li>A trader sells 10 ETH. New ETH reserve: 110.</li>
  <li>The USDC reserve must become 30,000,000 / 110 = 272,727.</li>
  <li>The trader receives 300,000 − 272,727 = 27,273 USDC, an average of 2,727 per ETH, about 9% below the starting price. That is slippage.</li>
  <li>The new pool price is 272,727 / 110 ≈ 2,479 USDC per ETH. Arbitrageurs will buy cheap ETH here and sell it elsewhere until the price matches other markets.</li>
</ol>
</div>

### Common mistakes

<ul>
  <li>“DeFi has no counterparty risk.” You rely on code, oracles, governance and stablecoin issuers.</li>
  <li>“A stablecoin always equals one dollar.” Only as long as its reserves or mechanism hold.</li>
</ul>
"""

D["daos-and-governance"] = """
### In depth

<p>A DAO (decentralised autonomous organisation) is a group whose membership, decision rules and treasury are managed by contracts. Members usually hold governance tokens or membership NFTs. A <b>proposal</b> bundles concrete on-chain actions, for example “transfer 10,000 USDC to the audit firm”. Members vote during a voting period. If the proposal reaches the <b>quorum</b> and the required majority, it is queued in a <b>timelock</b> and then executed by the contract itself; no person has to press a button at the bank.</p>
<!-- diagram:dao-lifecycle -->
<p>Design choices shape power. <b>Token voting</b> (one token, one vote) is simple but concentrates power in large holders. <b>Delegation</b> lets members give their votes to active representatives. <b>Snapshots</b> fix voting power at a past block, so tokens borrowed for the vote do not count. The Beanstalk attack in 2022 used a flash loan to gain a majority and pass a malicious proposal in one transaction. Many DAOs combine <b>off-chain signalling</b> (free votes on Snapshot) with on-chain execution for money.</p>
<p>Legally, a DAO without a registered entity is risky for its members. US courts treated DAOs as unincorporated associations or partnerships in 2023 (CFTC v. Ooki DAO, Sarcuni v. bZx), which can make members personally liable. Many DAOs therefore use a legal wrapper such as a foundation, an association or a special DAO law (for example in Wyoming or the Marshall Islands).</p>

### Worked example

<div class="worked">
<p><b>Case:</b> a student-club DAO with 100 tokens decides to fund a hackathon.</p>
<ol>
  <li>Rules: quorum 30 tokens, simple majority, 3-day vote, 2-day timelock. Snapshot at proposal creation.</li>
  <li>Member A proposes “send 500 USDC to the event venue”. 40 tokens vote: 28 yes, 12 no. Quorum (30) and majority are reached.</li>
  <li>The proposal enters the 2-day timelock. Members who disagree can exit (for example sell or redeem their tokens).</li>
  <li>After the timelock anyone calls <code>execute()</code>; the treasury contract sends 500 USDC.</li>
  <li>If someone had bought 50 tokens after the snapshot, those tokens would have had no vote.</li>
</ol>
</div>

### Common mistakes

<ul>
  <li>“A DAO has no leaders.” Core teams, delegates and multisigs often hold real power.</li>
  <li>“On-chain votes are binding in law.” Only if a legal structure or contract says so.</li>
</ul>
"""

D["law-and-business"] = """
### In depth

<p>Lawyers and developers use the word “contract” differently. In law, a contract is a binding agreement formed by offer and acceptance; it creates rights and duties that courts enforce. A smart contract is software that moves assets according to rules. The two can overlap: code can be the way the parties <i>perform</i> their agreement, or, in some designs, part of the agreement itself. But the code does not replace contract law. Questions such as capacity, mistake, fraud, unfair terms and consumer rights are still answered by the law of the country that applies.</p>
<p>Seven problems appear again and again: <b>identity and capacity</b> (an address does not show who or how old the party is), <b>error and rescission</b> (the law may cancel a contract, but the payment on chain cannot be reversed), <b>interpretation</b> (what if text and code differ?), <b>oracles and liability</b>, <b>data protection</b> (immutable storage versus the right to erasure), <b>jurisdiction</b> (which court, which law, when nodes are everywhere), and <b>mandatory law</b> (tenancy or consumer rules override what the code says).</p>
<p>For businesses, the question is economic: does automation reduce the cost of trust enough to justify development, audits and legal review? Good candidates are processes with many parties, clear conditions, digital assets and a need for an independent record: escrow, supply-chain payments, tokenised securities, insurance pay-outs based on data.</p>

### Worked example

<div class="worked">
<p><b>Case:</b> the Escrow buyer is 16 years old.</p>
<ol>
  <li>Under German law (§§ 106 ff. BGB) a contract by a minor without parental consent is pending and may be invalid if the parents refuse.</li>
  <li>The contract code has no idea: the buyer deposited, confirmed, and the seller received 1 ETH.</li>
  <li>If the parents refuse, the seller must give the payment back under unjust enrichment rules (§ 812 BGB). The chain will not do it automatically; it is a claim against the seller as a person.</li>
  <li><b>Design options:</b> verify age off chain before allowing deposits (with privacy, lesson 10.3), add an arbiter refund window, or keep the transaction small enough to fall under pocket-money rules (§ 110 BGB).</li>
</ol>
</div>

### Common mistakes

<ul>
  <li>“Once on chain, the law cannot reach it.” Courts act on people and companies, who must return or pay.</li>
  <li>“Lawyers only need to read the comments.” The code is what runs; the comments can be wrong.</li>
</ul>
"""

D["smart-legal-contracts"] = """
### In depth

<p>A <b>smart legal contract</b> is a legally binding contract in which some or all obligations are expressed or performed by code. The UK Law Commission (2021) described three forms. In the <b>natural-language</b> form, the legal text is the contract and code only performs parts of it. In the <b>hybrid</b> form, some terms are in text and some in code, and both are part of the agreement. In the <b>code-only</b> form, the code itself is the whole agreement, which raises hard questions about how parties can understand and prove what they agreed.</p>
<!-- diagram:slc-spectrum -->
<p>Template systems connect text and code in a disciplined way. The Accord Project separates three parts: the <b>text</b> with variables (“The buyer pays {{price}}”), the <b>model</b> that defines the type of each variable, and the <b>logic</b> that computes results such as late fees. Each deal fills in the <b>data</b>. Because text and logic use the same variables, they cannot drift apart for those values. Research languages such as Catala (statutes as code) and Stipula (contracts that import statutory rules) go further.</p>
<p>Whatever the tool, a good smart legal contract answers in writing what happens when things go wrong: which version prevails if text and code differ, who can pause or end the code, how disputes are resolved, and how outside facts are proved. The EU Data Act (Article 36) already requires that smart contracts used for data-sharing agreements can be safely terminated or interrupted.</p>

### Worked example

<div class="worked">
<p><b>Case:</b> write a clause for the laptop Escrow in the hybrid form.</p>
<blockquote><p>“§4 Release. When the Buyer or the Arbiter confirms delivery by calling <code>confirmDelivery()</code> on the contract at address 0x…, the Price held in escrow is released to the Seller. In case of conflict between this text and the code, this text prevails, and the Arbiter shall correct the outcome.”</p></blockquote>
<ul>
  <li><b>Text:</b> names the parties, the action, the address and a priority rule.</li>
  <li><b>Code:</b> <code>require(msg.sender == buyer || msg.sender == arbiter)</code>.</li>
  <li><b>Gap closed:</b> if the code had a bug and released to the wrong party, the text gives a legal basis to claim it back, and names who acts.</li>
</ul>
</div>

### Common mistakes

<ul>
  <li>“The code always wins.” The parties can agree the opposite, and courts will look at what they really agreed.</li>
  <li>“Templates are only for lawyers.” They are a shared specification for lawyers, analysts and developers.</li>
</ul>
"""

D["regulation"] = """
### In depth

<p>Regulation looks at what a token <i>does</i>, not what it is called. The first test in the EU is whether a token is a <b>financial instrument</b> under MiFID II, for example because it gives a share of profits or a claim like a bond. Then securities law applies, including prospectus rules; the DLT Pilot Regime allows special market infrastructure for such tokens. If it is not a financial instrument, <b>MiCA</b> (Markets in Crypto-Assets Regulation) applies to most other crypto-assets. MiCA distinguishes <b>e-money tokens</b> (EMT, referencing one official currency, such as a euro stablecoin), <b>asset-referenced tokens</b> (ART, referencing a basket or other assets), and other crypto-assets, such as utility tokens. Truly unique NFTs and fully decentralised services are largely outside MiCA.</p>
<p>MiCA places duties on two groups. <b>Issuers</b> must publish a white paper, and stablecoin issuers need authorisation and reserves. <b>Crypto-asset service providers</b> (CASPs) such as exchanges and custodians need a licence; the transition period ended on 1 July 2026. Anti-money-laundering rules add the travel rule for transfers and, from July 2027, the new EU AML Regulation. The GDPR applies to any personal data on or off chain. In the US, the GENIUS Act (July 2025) created a federal framework for payment stablecoins.</p>
<p>Code can help with compliance (<b>programmable compliance</b>): allow-lists of verified holders, transfer limits, pause functions for court orders. But each such feature also gives someone power over users, which must be disclosed and controlled.</p>

### Worked example

<div class="worked">
<p><b>Case:</b> classify three tokens step by step (simplified; not legal advice).</p>
<div class="tw"><table>
  <tr><th>Token</th><th>Financial instrument?</th><th>Under MiCA</th><th>Main duty</th></tr>
  <tr><td>A token that pays holders 5% of a company’s profits</td><td>Likely yes (transferable security)</td><td>Not MiCA</td><td>Prospectus, securities law</td></tr>
  <tr><td>A euro stablecoin redeemable 1:1</td><td>No</td><td>E-money token</td><td>Issuer must be a credit or e-money institution; white paper</td></tr>
  <tr><td>CourseToken that gives access to workshops</td><td>No</td><td>Other crypto-asset (utility)</td><td>White paper if offered to the public above thresholds</td></tr>
</table></div>
</div>

### Common mistakes

<ul>
  <li>“Calling it a utility token avoids securities law.” The economic rights decide, not the label.</li>
  <li>“MiCA regulates all of DeFi.” Fully decentralised services are largely outside it; the question of who is a service provider is still debated.</li>
</ul>
"""

D["ai-agents"] = """
### Worked example

<div class="worked">
<p><b>Case:</b> an AI research assistant buys data for a student project with a spending limit.</p>
<ol>
  <li>The student deploys <code>AgentWallet</code> with the agent’s address, a daily limit of 0.01 ETH, and one allowed payee: a data API.</li>
  <li>The agent finds the API’s identity and reputation through the ERC-8004 registries and calls it. The API answers “HTTP 402 Payment Required” with a price (the x402 pattern).</li>
  <li>The agent pays 0.002 ETH through <code>pay()</code>. The contract checks the agent, the payee and the limit, then pays. The memo links the payment to the request.</li>
  <li>A prompt-injection attack tells the agent to send 1 ETH to a new address. The contract reverts twice: the payee is not allowed, and the amount exceeds the limit.</li>
  <li>The student sees the attempted call in the events and calls <code>pause()</code>.</li>
</ol>
<p><b>Point:</b> the agent’s intelligence is not trusted; its wallet’s rules are.</p>
</div>

### Common mistakes

<ul>
  <li>Giving an agent a normal private key with full access. Use a contract wallet with limits.</li>
  <li>“The agent is liable.” In law, a person or company behind it is; the open question is which one.</li>
</ul>
"""

D["quantum"] = """
### In depth

<p>Quantum computers threaten two kinds of cryptography differently. <b>Shor’s algorithm</b> can compute a private key from a public key for elliptic-curve and RSA schemes, given a large enough, error-corrected quantum computer. That would break ECDSA account signatures, BLS validator signatures and KZG commitments. <b>Grover’s algorithm</b> only speeds up brute-force search, which roughly halves the security of hash functions: Keccak-256 keeps about 128 bits of security, which is still considered enough.</p>
<p>An important detail: an Ethereum address is a <i>hash</i> of the public key. As long as an account has never sent a transaction, its public key is not visible, and a quantum attacker sees only the hash. Once an account signs, its public key can be recovered from the signature. Accounts that have transacted are therefore exposed first, and any migration plan must move funds before an attacker can act.</p>
<p>The response is <b>crypto-agility</b>: making the signature scheme replaceable. Post-quantum signatures standardised by NIST (ML-DSA, SLH-DSA) are larger and more expensive to verify than ECDSA. Ethereum’s path includes account abstraction (so each account can choose its signature scheme), hash-based signatures for validators, and new proof systems. The practical question for long-lived records, such as land registers or certificates, is whether they will still be trustworthy in 20 years.</p>

### Worked example

<div class="worked">
<p><b>Case:</b> a notary office registers document hashes from one EOA and wants them to stay credible until 2045.</p>
<ol>
  <li>Risk: once quantum attacks are practical, someone could forge new signatures from that EOA and register false documents with a backdated story.</li>
  <li>Existing registrations stay valid as records: the hash and the block timestamp do not depend on ECDSA.</li>
  <li>Mitigation now: move registration to a smart account whose verifier can be replaced (crypto-agility), and publish the policy.</li>
  <li>Later: switch the verifier to a post-quantum scheme by governance, and retire the old key in a public transaction.</li>
</ol>
</div>

### Common mistakes

<ul>
  <li>“Quantum computers break all of blockchain.” Hashes survive; signatures and some proofs need replacing.</li>
  <li>“It is decades away, so ignore it.” Migrations take years; records made today must last.</li>
</ul>
"""

D["research"] = """
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
"""
