# Deeper explanations, worked examples and common mistakes: modules 1-3.
# Inserted before "### Watch and read" by tools/deepen.py. <!-- diagram:x --> marks where a figure goes.

D = {}

D["trust-and-ledgers"] = """
### In depth

<p>Every agreement between strangers needs someone to keep the record. When you pay a seller by bank transfer, the bank keeps one ledger, checks that you have the money, and makes sure the same euro is not spent twice. You trust the bank because it is regulated, insured and liable when it makes mistakes. That trust is useful, but it has costs: fees, opening hours, borders, and the power to freeze or reverse a payment.</p>
<p>A blockchain replaces the single record keeper with many copies of the same ledger that check each other. Three problems have to be solved for this to work. First, <b>integrity</b>: nobody may change an old entry without everyone noticing. Second, <b>authorisation</b>: only the owner of money may spend it. Third, <b>agreement</b>: when two payments conflict, all copies must pick the same one. Hashes solve the first, digital signatures the second, and consensus the third. The rest of Modules 1 and 2 explains each one.</p>
<p>The famous case is <b>double spending</b>. With digital files, copying is free: if money were just a file, Alice could send the same coin to Bob and to Carol. A central ledger stops this by refusing the second payment. A blockchain stops it because all nodes follow one agreed order of transactions; the second payment arrives later and finds the coin already spent.</p>
<p>A blockchain is not automatically better. It is slower and more expensive than a database, every entry is public on most chains, and mistakes are hard to undo. It is worth it only when several parties must share a record, do not want to trust one of them to keep it, and need anyone to be able to check it later.</p>

### Worked example

<div class="worked">
<p><b>Case:</b> a second-hand laptop sale between two students who have never met. The price is 1 ETH.</p>
<ol>
  <li><b>With a bank:</b> the buyer transfers 300 EUR, the bank updates two accounts. If the seller never ships, the buyer must ask the bank or a court to help. The bank is the record keeper and, in practice, the judge of who paid.</li>
  <li><b>With a shared ledger:</b> the buyer signs a payment of 1 ETH. Thousands of nodes check the signature and the balance and include it in the next block. Anyone can verify the payment forever.</li>
  <li><b>What is still missing:</b> the ledger proves that 1 ETH moved. It cannot prove that the laptop arrived. That needs a smart contract with rules (Module 4) and someone or something that reports delivery (an arbiter or an oracle).</li>
</ol>
<p><b>Conclusion:</b> the ledger removes the need to trust a record keeper, but not the need to trust facts from the outside world.</p>
</div>

### Common mistakes

<ul>
  <li>“A blockchain means nobody has to trust anyone.” You still trust the code, the majority of validators, and whoever reports outside facts.</li>
  <li>“A blockchain is a better database.” For one organisation it is usually a worse one: slower, public and harder to correct.</li>
  <li>“Blockchain data is anonymous.” Addresses are pseudonyms. Once one is linked to a person, its whole history is visible.</li>
</ul>
"""

D["hash-functions"] = """
### In depth

<p>A hash function is like a very strict fingerprint machine. Feed it the text of a lease and it returns 64 hexadecimal characters. Feed it the same text tomorrow and it returns exactly the same 64 characters. Change one letter, even a space, and the result looks completely unrelated. This is what makes a hash useful as evidence: it is cheap to check and impossible to fake in practice.</p>
<p>Why can nobody fake it? A 256-bit hash has 2<sup>256</sup> possible values, roughly the number of atoms in the observable universe. To find a different document with the same hash (a <b>collision</b>), an attacker would have to try an astronomical number of inputs. To recover the document from its hash (a <b>preimage</b>), there is no shortcut either: the function is designed to scramble every input bit into every output bit.</p>
<p>Blockchains use hashes in three places. (1) <b>Linking blocks</b>: each block header contains the hash of the previous header, so the chain is <i>tamper-evident</i>. (2) <b>Summarising data</b>: all transactions in a block are combined into one Merkle root (lesson 1.4). (3) <b>Identifiers</b>: an Ethereum address is the last 20 bytes of the Keccak-256 hash of a public key, and a transaction is known by its hash.</p>
<p>Ethereum uses Keccak-256, the original winner of the SHA-3 competition. It is not identical to the later standard SHA3-256 because NIST changed the padding. That is why Solidity calls it <code>keccak256</code> and not <code>sha3</code>.</p>
<!-- diagram:hash-chain -->

### Worked example

<div class="worked">
<p><b>Case:</b> the landlord from the question claims the lease said 990 EUR.</p>
<ol>
  <li>On the signing day, the tenant computed the hash of the PDF and registered it in the Document registry (lab 4.5). The block timestamp shows the date.</li>
  <li>In the dispute, the tenant hands the court the PDF that says 900 EUR. Anyone can hash it again: the result matches the hash on chain.</li>
  <li>The landlord’s version with 990 EUR produces a completely different hash, which was never registered.</li>
  <li>Result: the 900 EUR text existed unchanged on the signing day. What the hash does <i>not</i> show is that the landlord agreed to it. That needs a signature, which is the next lesson.</li>
</ol>
</div>

### Common mistakes

<ul>
  <li>“A hash encrypts the document.” Encryption can be reversed with a key. A hash cannot be reversed at all.</li>
  <li>“Short or predictable data is safe once hashed.” A date of birth has few possible values; an attacker can hash them all and compare. Add a random salt before hashing personal data.</li>
  <li>“Similar documents have similar hashes.” They do not. That is the avalanche effect.</li>
</ul>
"""

D["keys-and-signatures"] = """
### In depth

<p>Ethereum accounts are controlled by a key pair. The <b>private key</b> is a random 256-bit number. From it, elliptic-curve multiplication on the curve secp256k1 gives the <b>public key</b>. This direction is easy; the reverse is practically impossible. The <b>address</b> is the last 20 bytes of the Keccak-256 hash of the public key, which is why addresses are shorter than keys.</p>
<p>To spend from an account, the wallet <b>signs</b> the transaction: it combines the transaction hash with the private key using ECDSA and produces a signature (the values r, s and v). Nodes never see the private key. They run the verification math on the transaction and the signature and recover the public key, hash it, and check that the resulting address is the sender. If one byte of the transaction was changed after signing, the recovered address is different and the transaction is rejected.</p>
<p>A signature therefore proves two things: <b>authenticity</b> (only the holder of the private key could have produced it) and <b>integrity</b> (the message was not changed). It does not prove <i>who</i> the holder is in the real world. That is the gap between cryptography and law: a qualified electronic signature under eIDAS links a key to an identified person through a trust service; a blockchain address does not.</p>
<p>A <b>recovery phrase</b> (12 or 24 words, BIP-39) is just a human-readable form of the seed from which the wallet derives all its private keys. Whoever has the phrase has every account in that wallet. There is no “forgot password”: if it is lost, the funds are gone; if it is stolen, they are gone too.</p>
<!-- diagram:sign-verify -->

### Worked example

<div class="worked">
<p><b>Case:</b> Alice sends 0.1 SepoliaETH to Bob.</p>
<ol>
  <li>MetaMask builds the transaction: to = Bob, value = 0.1 ETH, nonce = 7, gas settings, chain ID 11155111 (Sepolia).</li>
  <li>It hashes this data and signs the hash with Alice’s private key. The output is a signature of 65 bytes.</li>
  <li>A node receives transaction + signature, recovers a public key from them, hashes it, and gets <code>0x5B38…eddC4</code>: Alice’s address. It also checks the nonce (7 is next) and the balance.</li>
  <li>An attacker who intercepts the transaction and changes the receiver to their own address breaks the signature: the recovered address is now a random one with no funds, so the node rejects it.</li>
  <li>The chain ID inside the signed data stops the same transaction from being replayed on mainnet.</li>
</ol>
</div>

### Common mistakes

<ul>
  <li>“The public key and the address are the same.” The address is derived from the public key by hashing.</li>
  <li>“A signature encrypts the transaction.” Transactions are public. The signature only proves who authorised them.</li>
  <li>“Support can restore my wallet.” Nobody can. Anyone who asks for your recovery phrase is attacking you.</li>
</ul>
"""

D["blocks-and-state-models"] = """
### In depth

<p>A block has two parts: a small <b>header</b> and a list of <b>transactions</b>. The header contains the hash of the previous header (the link), a timestamp, and several roots: one hash that summarises all transactions, one for the receipts (results and logs), and one for the whole <b>state</b> after the block. Light clients can download only headers and still check that a transaction is included.</p>
<p>The summary works with a <b>Merkle tree</b>. Hash each transaction. Then hash the hashes in pairs, then the results in pairs, until one hash remains: the root. To prove that transaction C is in a block of 1,000 transactions, you need only about 10 hashes (the “Merkle proof”), not all 1,000 transactions. Change any transaction and the root changes. Ethereum uses a variant called a Merkle Patricia trie, which also works as a key-value store for account balances.</p>
<!-- diagram:merkle -->
<p>Blockchains also differ in how they keep <b>state</b>. Bitcoin uses the <b>UTXO</b> model: there are no balances, only unspent outputs, like banknotes in a wallet. A payment consumes whole outputs and creates new ones, including change back to the sender. Ethereum uses the <b>account</b> model: a global table of accounts with balances, nonces and, for contracts, code and storage, like bank accounts. Smart contracts are much easier to write in the account model, because a contract can simply update a balance in its storage.</p>

### Worked example

<div class="worked">
<p><b>Case:</b> Alice owns 0.7 BTC as two outputs (0.5 and 0.2) and pays Bob 0.6. Then the same payment on Ethereum.</p>
<div class="tw"><table>
  <tr><th></th><th>UTXO (Bitcoin)</th><th>Account (Ethereum)</th></tr>
  <tr><td>Before</td><td>Outputs: 0.5 (Alice), 0.2 (Alice)</td><td>balance[Alice] = 0.7</td></tr>
  <tr><td>Transaction</td><td>Inputs: both outputs. Outputs: 0.6 to Bob, 0.099 change to Alice. Fee: 0.001</td><td>to = Bob, value = 0.6, nonce = 3</td></tr>
  <tr><td>After</td><td>Outputs: 0.6 (Bob), 0.099 (Alice). Old outputs are spent forever.</td><td>balance[Alice] = 0.7 − 0.6 − fee; balance[Bob] += 0.6; nonce[Alice] = 4</td></tr>
  <tr><td>Double-spend protection</td><td>An output can be spent once</td><td>The nonce must be the next number</td></tr>
</table></div>
</div>

### Common mistakes

<ul>
  <li>“The block stores all balances.” It stores the transactions and a state root; nodes keep the state itself.</li>
  <li>“A Merkle proof shows the transaction is valid.” It shows only that the transaction is included in that block.</li>
  <li>“The block timestamp is exact.” Validators set it within narrow rules; use it for days, not seconds.</li>
</ul>
"""

D["types-of-blockchains"] = """
### In depth

<p>“Blockchain” covers very different systems. The main question is <b>who may write and who may validate</b>. On a <b>public, permissionless</b> chain such as Ethereum, anyone can send transactions, read all data and, with enough stake, become a validator. On a <b>permissioned</b> chain, an operator or a group decides who joins. When one organisation controls it, it is a <b>private</b> chain; when several known organisations share control, it is a <b>consortium</b> chain (for example Hyperledger Fabric networks in trade finance).</p>
<p>Each choice moves the trade-off between openness and control. Public chains give strong neutrality and censorship resistance, but data is visible to everyone and fees vary. Permissioned chains are faster and can keep data confidential, but users must trust the operators, who can change the rules or the history if they agree. A private chain run by one company gives few advantages over a normal database with audit logs.</p>
<p>Today many projects mix models. Rollups (Module 10) run their own fast chain but post data and proofs to Ethereum for security. Banks issue tokenised bonds on public chains but restrict who may hold them with allow-lists in the token contract. The useful question is not “which chain is best?” but “who must be able to do what, and whom are users willing to trust?”.</p>

### Worked example

<div class="worked">
<p><b>Case:</b> three scenarios, three answers.</p>
<div class="tw"><table>
  <tr><th>Scenario</th><th>Analysis</th><th>Choice</th></tr>
  <tr><td>A university issues diplomas that employers worldwide must verify.</td><td>One writer (the university), many readers who should not need an account.</td><td>Public chain with only hashes or attestations; the data stays at the university.</td></tr>
  <tr><td>Five shipping companies share container status updates.</td><td>Several known writers who compete and do not want one of them in control; data is commercially sensitive.</td><td>Consortium chain, or a public chain with encrypted data.</td></tr>
  <tr><td>A shop wants an internal log of price changes.</td><td>One writer, one organisation, no outside verifier.</td><td>Normal database with an audit log. No blockchain.</td></tr>
</table></div>
</div>

### Common mistakes

<ul>
  <li>“Private chains are blockchains with privacy.” They are blockchains with an owner. Privacy can also be built on public chains.</li>
  <li>“Permissioned means more secure.” It means fewer, known validators: more trust in them, not more security by default.</li>
</ul>
"""

D["consensus"] = """
### In depth

<p>Consensus answers one question: when thousands of nodes receive transactions in different orders, how do they all end up with the same history? A protocol must pick who proposes the next block and make cheating more expensive than honesty.</p>
<p><b>Proof of Work</b> (Bitcoin) lets anyone propose a block if they find a number (nonce) that makes the block hash smaller than a target. Finding it costs electricity; checking it is instant. Nodes follow the chain with the most accumulated work. To rewrite history, an attacker would need more computing power than the rest of the network together (a “51% attack”).</p>
<p><b>Proof of Stake</b> (Ethereum since September 2022) replaces electricity with deposited ETH. Validators lock 32 ETH (or more since Pectra). Time is divided into <b>slots</b> of 12 seconds and <b>epochs</b> of 32 slots. In each slot one validator is chosen at random to propose a block; committees of other validators <b>attest</b> that it is correct. When two thirds of the stake has attested to a checkpoint over two epochs, the block is <b>finalised</b>, after about 13 minutes. Reversing a finalised block would require validators with at least one third of all stake to break the rules, and they would lose that stake through <b>slashing</b>.</p>
<!-- diagram:pos-finality -->
<p>This leads to two levels of “done”. A transaction in a new block is <i>included</i> after about 12 seconds; it is <i>final</i> after about 13 minutes. Exchanges and bridges wait for finality before they treat large deposits as safe.</p>

### Worked example

<div class="worked">
<p><b>Case:</b> how expensive is it to attack Ethereum’s finality?</p>
<ol>
  <li>Assume about 34 million ETH is staked (check the current number on beaconcha.in).</li>
  <li>To finalise two conflicting blocks, attackers must control at least one third: more than 11 million ETH.</li>
  <li>When they do, the protocol detects the double votes and slashes them. The attack costs the attackers a large part of that stake.</li>
  <li>Compare with Proof of Work: an attacker who rents enough computing power can stop after the attack and keep the hardware. Proof of Stake punishes the attacker’s capital directly.</li>
</ol>
<p><b>Takeaway for law and business:</b> “final” on Ethereum is economic finality. It is extremely expensive, not mathematically impossible, to reverse.</p>
</div>

### Common mistakes

<ul>
  <li>“Miners still create Ethereum blocks.” Since the Merge there is no mining on Ethereum; validators propose and attest.</li>
  <li>“51% of nodes decide.” Votes are weighted by stake, not by number of computers.</li>
  <li>“A transaction in a block is final.” It is final only after the checkpoint is finalised.</li>
</ul>
"""

D["forks-and-governance"] = """
### In depth

<p>A blockchain’s rules live in the software that nodes run. To change the rules, enough people must run new software. A <b>soft fork</b> makes the rules stricter: old nodes still accept new blocks, so upgrades can be gradual. A <b>hard fork</b> changes the rules in a way old nodes reject. Everyone must upgrade by a set time, or the network splits in two.</p>
<!-- diagram:forks -->
<p>On Ethereum, changes start as an <b>EIP</b> (Ethereum Improvement Proposal) on GitHub. Researchers and client teams discuss them in the public All Core Devs calls. An upgrade bundles several EIPs and gets a name (Pectra, Fusaka, Glamsterdam). Client teams implement it, test it on devnets, then on the public testnets (Sepolia, then Hoodi), and finally choose a mainnet date. Node operators, staking providers and exchanges then decide to run the new version. Nobody can force them, but a node on the old rules is left on a chain that the economy has abandoned.</p>
<p>So who holds power? Client developers write the code, validators and node operators choose to run it, and users, exchanges and application developers decide which chain has value. When they disagree, the chain can split: after the DAO hack in 2016, most of the community accepted a hard fork that returned the stolen ETH, and a minority continued the original chain as Ethereum Classic.</p>

### Worked example

<div class="worked">
<p><b>Case:</b> Glamsterdam, autumn 2026 (as of 20 November 2026).</p>
<ol>
  <li>Glamsterdam bundles block building inside the protocol (ePBS), block-level access lists and gas repricing (EIP-8037, EIP-8038).</li>
  <li>It went live on the Sepolia testnet on 6 October 2026.</li>
  <li>Auditors found that the new gas rules could break assumptions inside some contracts that are already deployed and cannot be changed.</li>
  <li>On 22 October the next testnet step (Hoodi) was postponed. Audit reports were presented in November and discussed on 19 November without a decision. A delay to 2027 is possible.</li>
</ol>
<p><b>What it shows:</b> a technical improvement (cheaper, fairer gas) collides with the interests of people who rely on old code. Nobody voted; the decision is made by rough consensus among client teams, under public pressure from application developers.</p>
</div>

### Common mistakes

<ul>
  <li>“Vitalik decides upgrades.” He is one influential voice; client teams implement and node operators adopt.</li>
  <li>“A fork is always a split.” Most hard forks are planned upgrades that everyone runs; a split happens only when a large group refuses.</li>
</ul>
"""

D["ethereum-evm-gas"] = """
### In depth

<p>Ethereum is a single, shared computer. Its state is a table of accounts. <b>Externally owned accounts</b> (EOAs) are controlled by private keys and can start transactions. <b>Contract accounts</b> hold code and storage and run only when called. A transaction is a signed message from an EOA that either moves ETH, deploys a contract, or calls a contract function with some input data.</p>
<p>Every node runs the same transactions in the same order in the <b>Ethereum Virtual Machine</b> (EVM). The EVM executes bytecode, simple instructions such as ADD, SSTORE (write storage) or CALL (call another contract). Because every node must get exactly the same result, the EVM cannot use random numbers, the internet or the clock of the computer it runs on. That is why contracts need oracles for outside data.</p>
<p>Each instruction costs <b>gas</b>. Gas stops endless loops (a transaction must say how much gas it may use, the gas limit) and prices scarce resources. Writing a new value to storage costs about 20,000 gas; an addition costs 3. Since EIP-1559, each block has a <b>base fee</b> per gas that rises when blocks are full and falls when they are empty; the base fee is burned. Users add a <b>priority fee</b> (tip) for the validator.</p>
<!-- diagram:tx-lifecycle -->

### Worked example

<div class="worked">
<p><b>Case:</b> what does calling <code>deposit()</code> on the Escrow cost?</p>
<ol>
  <li>The transaction uses 50,000 gas (one storage write for the state, one event, checks).</li>
  <li>The base fee is 8 gwei, and the user offers a priority fee of 1 gwei. 1 gwei = 0.000000001 ETH.</li>
  <li>Fee = 50,000 × (8 + 1) gwei = 450,000 gwei = 0.00045 ETH.</li>
  <li>At an ETH price of 3,000 EUR, that is 1.35 EUR. Of this, 0.0004 ETH is burned and 0.00005 ETH goes to the validator.</li>
  <li>If the transaction reverts halfway (wrong sender), the user still pays for the gas used up to the revert, but the state does not change.</li>
</ol>
<p>On a rollup the same call often costs a few cents, because the expensive part (posting data to Ethereum) is shared by many users.</p>
</div>

### Common mistakes

<ul>
  <li>“Gas is a token.” Gas is a unit of work. You pay for it in ETH.</li>
  <li>“A higher gas limit costs more.” You pay for gas <i>used</i>; unused gas is not charged.</li>
  <li>“Reading a contract costs gas.” Calling a view function from outside is free; only transactions cost gas.</li>
</ul>
"""

D["wallets-and-testnets"] = """
### In depth

<p>A wallet does not hold coins. Coins are entries on the chain. A wallet holds <b>keys</b> and offers three functions: show balances (by asking a node), build transactions, and sign them. Wallets differ in where the keys live. A <b>browser wallet</b> such as MetaMask stores encrypted keys on your computer: convenient, but exposed to malware. A <b>hardware wallet</b> keeps keys on a separate device and signs inside it. A <b>custodial wallet</b> on an exchange means the exchange holds the keys; you hold a claim against the exchange.</p>
<p><b>Smart accounts</b> put the rules into a contract: several signers, daily limits, recovery through friends or a company. ERC-4337 introduced them without changing the protocol; EIP-7702 (Pectra, May 2025) lets a normal account temporarily act as a smart account, for example to batch an approval and a swap in one click or let a company pay the gas.</p>
<p>A <b>testnet</b> is a copy of Ethereum where coins have no value. Sepolia is the standard testnet for applications; Hoodi is used by validators and staking providers. Faucets give out test ETH for free, usually with limits to stop abuse. Testnets are sometimes reset or replaced, so never build anything permanent on them.</p>

### Worked example

<div class="worked">
<p><b>Case:</b> set up a safe course wallet and check it.</p>
<ol>
  <li>Install MetaMask from metamask.io only. Create a <i>new</i> wallet just for this course.</li>
  <li>Write the 12 words on paper. Never type them anywhere else, never photograph them.</li>
  <li>Turn on “Show test networks” and select Sepolia. Your address is the same on every network; only the balance differs.</li>
  <li>Get 0.05 SepoliaETH from a faucet. Open sepolia.etherscan.io and search your address: one incoming transaction.</li>
  <li>Send 0.001 to a classmate. Etherscan shows <i>From</i> (you), <i>To</i>, <i>Value</i> and the fee.</li>
</ol>
</div>

### Common mistakes

<ul>
  <li>“Test ETH can be sold.” It has no value. Anyone offering to buy or sell it is running a scam.</li>
  <li>“Each network needs a new wallet.” One key gives the same address on all EVM networks.</li>
  <li>“A browser extension is as safe as a hardware wallet.” Not for real money.</li>
</ul>
"""

D["nodes-and-providers"] = """
### In depth

<p>When your wallet shows a balance, it asked a <b>node</b>. A node is software that downloads every block, runs every transaction in the EVM and keeps the current state. Since the Merge an Ethereum node runs two programs. The <b>execution client</b> (Geth, Nethermind, Besu, Erigon, Reth) runs transactions and keeps the state. The <b>consensus client</b> (Lighthouse, Prysm, Teku, Nimbus, Lodestar, Grandine) follows Proof of Stake. A full node needs a fast SSD of about 2 TB and a good internet connection; an <b>archive node</b>, which keeps every historical state, needs much more.</p>
<p>Most applications do not run their own node. They send JSON-RPC requests (<code>eth_getBalance</code>, <code>eth_call</code>, <code>eth_sendRawTransaction</code>) to an <b>RPC provider</b> such as Infura, Alchemy or QuickNode. This is convenient but brings back a trusted middleman: the provider sees your IP address and every address you look up, can be down, can refuse service in some regions, and could in theory return wrong data. <b>Light clients</b> reduce that trust: they follow block headers and verify the answers they get with Merkle proofs.</p>
<p><b>Client diversity</b> protects the network. If one client with more than two thirds of validators had a bug, it could finalise a wrong chain; with more than one third, a bug could stop finality. That is why staking providers are asked to spread across clients.</p>

### Worked example

<div class="worked">
<p><b>Case:</b> follow one balance request.</p>
<ol>
  <li>MetaMask sends <code>{"method":"eth_getBalance","params":["0x5B38…","latest"]}</code> to its default provider.</li>
  <li>The provider’s node looks up the account in its state and returns <code>"0x2386f26fc10000"</code>: 10<sup>16</sup> wei, which is 0.01 ETH.</li>
  <li>You change the RPC URL in MetaMask to another provider and get the same answer. Two independent sources agree.</li>
  <li>When you send a transaction, the wallet signs it locally and only sends the signed bytes. The provider cannot change it without breaking the signature, but it could delay it or not forward it.</li>
</ol>
</div>

### Common mistakes

<ul>
  <li>“MetaMask is a node.” It is a wallet that talks to someone else’s node.</li>
  <li>“The provider can steal my funds.” It never has your key; it can mislead or censor you, not spend for you.</li>
</ul>
"""
