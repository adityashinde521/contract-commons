# Curriculum and sources

Contract Commons has 13 modules and 56 lessons and labs. The structure follows the
[roadmap.sh blockchain roadmap](https://roadmap.sh/blockchain), narrowed to Ethereum smart
contracts, and was checked against these syllabi (retrieved November 2026):

| Institution | Course | Topics used |
|---|---|---|
| Stanford University | [CS251 Cryptocurrencies, Blockchains and Smart Contracts, Fall 2026](https://cs251.stanford.edu/syllabus.html) | Consensus, Ethereum and Solidity, stablecoins, DEXs, MEV, privacy and zk-SNARKs, channels, rollups, account abstraction, post-quantum |
| Princeton University | [Principles of Blockchains](https://web3.princeton.edu/principles-of-blockchains) | Cryptographic primitives, Nakamoto consensus, PoS, scaling, channels, rollups, ZK, bridges |
| MIT Sloan | [15.S12 Blockchain and Money](https://ocw.mit.edu/courses/15-s12-blockchain-and-money-fall-2018/pages/calendar/) | Money and ledgers, smart contracts, public policy, use-case economics |
| University of Zurich | [Blockchain and Crypto-economics 2024](https://ifi.uzh.ch/dam/jcr:c8b2f22d-b059-4bef-b21d-1782a3a29012/Course%20Syllabus_BCE%2024.pdf) | UTXO and accounts, tokens, DeFi, DAOs, L2, attacks; hands-on sessions |
| Singapore Management University | [LAW 649 Blockchain and Governance](https://law.smu.edu.sg/sites/law.smu.edu.sg/files/2023-05/LAW649.pdf) | Trust foundations, governance, tokenisation and regulation, law and economics of smart contracts |
| Stanford Law School | [LAW 1078 Blockchain Governance](https://law.stanford.edu/courses/blockchain-governance/) | DAOs, voting, delegation, identity, for law, technical and business students |

## Modules

| # | Module | Lessons and labs |
|---|---|---|
| 1 | Blockchain foundations | 1.1 The problem: trust and a shared ledger; 1.2 Hash functions; 1.3 Keys, signatures and addresses; 1.4 Blocks, Merkle trees and state models; 1.5 Types of blockchains; 1.6 ETH.BUILD: hashes, keys and transactions as blocks (lab) |
| 2 | Consensus and decentralisation | 2.1 Blocks, chain and consensus; 2.2 Forks and protocol governance; 2.3 Read the chain with Etherscan (lab) |
| 3 | Ethereum and the EVM | 3.1 Ethereum: accounts, transactions, EVM, gas; 3.2 Wallets, keys and test networks; 3.3 Nodes, clients and providers; 3.4 Remix setup and tour (lab); 3.5 SimpleStorage: transaction versus call (lab) |
| 4 | Solidity smart contracts | 4.1 Smart contracts: what they are and are not; 4.2 Solidity for programmers; 4.3 Escrow: three parties and a state machine (lab); 4.4 Rental deposit: time and mandatory law (lab); 4.5 Document registry: proof of existence (lab) |
| 5 | Tokens and standards | 5.1 Tokens: ERC-20 and ERC-721; 5.2 Course token with OpenZeppelin (lab); 5.3 Certificate contract with the OpenZeppelin Wizard (lab); 5.4 thirdweb: deploy and manage a ready-made contract (lab) |
| 6 | Developer tooling and testing | 6.1 From Remix to a professional toolchain; 6.2 Testing smart contracts; 6.3 Lab: test the Escrow with Foundry (lab) |
| 7 | Smart contract security | 7.1 Security basics; 7.2 Security in practice: hacks and AI; 7.3 Audits, static analysis and fuzzing; 7.4 Reentrancy: attack and fix (lab); 7.5 Phalcon: trace a real hack visually (lab) |
| 8 | Deploy, verify and operate | 8.1 Upgrades, monitoring and maintenance; 8.2 Deploy to Ethereum (Sepolia) and verify (lab); 8.3 Tenderly: debug and simulate your own transactions (lab); 8.4 See inside: Remix debugger, contract diagrams, ETH.BUILD (lab) |
| 9 | dApps, oracles and storage | 9.1 dApp architecture: from contract to app; 9.2 Oracles: getting outside facts on chain; 9.3 Decentralised storage; 9.4 Attestations: notarise a document on Sepolia (lab); 9.5 Team lab: a clickable app for your Escrow (lab) |
| 10 | Scaling, privacy and interoperability | 10.1 Ethereum today: scaling and the roadmap; 10.2 Channels, sidechains and bridges; 10.3 Zero-knowledge proofs and privacy; 10.4 Research with on-chain dashboards (lab) |
| 11 | DeFi, DAOs and governance | 11.1 DeFi: stablecoins, exchanges, lending and MEV; 11.2 DAOs and on-chain governance; 11.3 Safe: a company wallet with two signatures (lab); 11.4 Aragon: create a DAO and pass a proposal (lab) |
| 12 | Law, regulation and business | 12.1 Law and business lens; 12.2 Smart legal contracts; 12.3 Tokenisation, stablecoins and regulation; 12.4 Smart legal contract templates (Accord Project) (lab) |
| 13 | Frontiers and research | 13.1 AI agents with wallets; 13.2 Quantum computing and blockchain security; 13.3 Current research and open problems; 13.4 To evaluate: new visual builders |

The roadmap.sh topics Truffle and Brownie are mentioned as history only, because both are no longer maintained.
