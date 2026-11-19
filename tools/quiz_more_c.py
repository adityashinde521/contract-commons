# Second and third fill / fix / order items per unit: modules 8-10.
from quiz_types_a import F, X, O

ITEMS = {
"upgrades-and-operations": [
  F("Complete how a proxy runs the implementation's code on its own storage.", """
proxy fallback: ____(implementation, msg.data)""", ["delegatecall", "call", "staticcall", "selfdestruct"], 0,
    "delegatecall runs the other contract's code in the proxy's storage context."),
  F("Complete the rule for a safe upgrade of storage.", """
new implementation: keep old variables in the same order,
add new variables ____""", ["only at the end", "at the top", "anywhere", "in a second proxy"], 0,
    "Changing the order shifts storage slots and corrupts data."),
  X("One line in this storage layout upgrade is wrong.", """
// v1: address owner; uint256 total;
// v2 below
uint256 fee;          // new
address owner;
uint256 total;""", 2, ["move uint256 fee; below uint256 total;", "delete owner", "rename total"], 0,
    "New variables must go after the existing ones."),
  X("One line in this admin setup is risky.", """
the upgrade role sits in a 3-of-5 multisig
upgrades wait 48 hours in a timelock
a pause role can stop deposits quickly
a single developer key can also upgrade instantly""", 3, ["remove the single-key upgrade path", "make every user an admin", "remove the pause role"], 0,
    "One key that can bypass the timelock defeats it."),
  O("Order the parts of a safe upgrade.", ["Write the new implementation", "Test it on a mainnet fork", "Check the storage layout", "Propose in the multisig and wait for the timelock", "Execute and verify the new code"],
    "Test, check, govern, execute, verify."),
  O("Order a user's view of an announced upgrade.", ["See the upgrade proposal on chain", "Read the new code during the timelock", "Decide to stay or withdraw", "The upgrade executes after the timelock"],
    "The timelock gives users time to decide."),
],
"lab-sepolia": [
  F("Complete the price for a cheap Sepolia Escrow test.", """
_price = ____  // 0.001 ether""", ["1000000000000000", "1000", "0.001", "1000000000000000000"], 0,
    "0.001 ether = 10^15 wei."),
  F("Complete what verification needs to match.", """
same source + same compiler version + same ____""", ["optimisation settings", "account", "gas price", "block number"], 0,
    "Different settings produce different bytecode."),
  X("One setting is wrong for deploying to Sepolia from Remix.", """
MetaMask network: Sepolia
Remix environment: Injected Provider - MetaMask
Account: your course account with SepoliaETH
Remix environment: Remix VM""", 3, ["delete it: Remix VM is a local simulation", "Environment: Mainnet fork", "Environment: WalletConnect to mainnet"], 0,
    "Only Injected Provider sends to the real Sepolia network."),
  X("One expectation after verifying the Escrow is wrong.", """
the Contract tab shows a green check
Read Contract lists price, state and the three addresses
Write Contract lets you call deposit with MetaMask
the private key of the contract is shown""", 3, ["contracts have no private key", "the buyer's key is shown", "the arbiter's key is shown"], 0,
    "Contracts are controlled by code, not keys."),
  O("Order part D of the Sepolia lab.", ["Deploy the Escrow on Sepolia", "Verify its source", "Deposit 0.001 ether as the buyer", "Confirm delivery as the buyer", "Check the seller's incoming transaction on Etherscan"],
    "Deploy, verify, pay, release, check."),
  O("Order how to get ready for the Sepolia lab.", ["Select Sepolia in MetaMask", "Check you have at least 0.05 SepoliaETH", "Set Remix to Injected Provider", "Check that Remix shows the same account"],
    "Network, funds, connection, account."),
],
"lab-tenderly": [
  F("Complete what the simulator needs to test refund as the arbiter.", """
network: Sepolia
from: ____
to: your Escrow
function: refund()""", ["the arbiter's address", "the seller's address", "0x0", "the Escrow's address"], 0,
    "Simulations can use any sender without a signature."),
  F("Complete the simulator's answer when the seller calls refund.", """
status: ____
error: "Only arbiter\"""", ["Reverted", "Success", "Pending", "Mined"], 0,
    "The simulation shows the revert without spending anything."),
  X("One claim about Tenderly simulations is wrong.", """
a simulation runs on a copy of the current state
it needs no signature
it costs no gas on the real network
it changes the contract on Sepolia""", 3, ["it changes nothing on Sepolia", "it deploys a new contract", "it sends test ETH"], 0,
    "Simulations are dry runs."),
  X("One debugger step is in the wrong order.", """
open the transaction in Tenderly
find the line with state = State.Complete
evaluate msg.sender at that line
search the transaction hash""", 3, ["search the hash first, then open it", "skip the search", "evaluate before opening"], 0,
    "You must find and open the transaction before stepping through it."),
  O("Order the Tenderly debugging part.", ["Add your Sepolia contract", "Open your confirmDelivery transaction", "Step to state = State.Complete", "Step to the line that sends ETH", "Evaluate msg.sender and price"],
    "Open, step, inspect."),
  O("Order the simulation part.", ["Deploy a fresh Escrow and deposit", "Open the Simulator", "Simulate refund from the seller: reverted", "Simulate refund from the arbiter: success", "Compare the state changes"],
    "Same call, two senders, two outcomes."),
],
"lab-see-inside": [
  F("Complete the sol2uml command for a verified Sepolia contract.", """
$ sol2uml class ____ -n sepolia -k $ETHERSCAN_KEY""", ["<contract address>", "<private key>", "<recovery phrase>", "<transaction hash>"], 0,
    "sol2uml reads verified source by address."),
  F("Complete what the Remix debugger shows during the reentrancy attack.", """
call stack: withdraw <- receive <- withdraw <- ____""", ["attack", "constructor", "deposit only", "mint"], 0,
    "The attack function starts the nested withdraw calls."),
  X("One role annotation on the Escrow class diagram is wrong.", """
buyer: deposit, confirmDelivery
arbiter: confirmDelivery, refund
seller: nothing to call, receives the price
seller: refund""", 3, ["delete it: the seller cannot refund", "seller: deposit", "seller: everything"], 0,
    "The seller only receives."),
  X("One tool is matched to the wrong view.", """
ETH.BUILD: hashes, keys and blocks visually
Remix debugger: each step of a transaction
sol2uml: class diagram of contracts
sol2uml: live price charts""", 3, ["sol2uml: storage layout or class diagrams", "sol2uml: wallet balances", "sol2uml: gas prices"], 0,
    "sol2uml draws contract structure."),
  O("Order the four views of the See inside lab.", ["Build a hash chain in ETH.BUILD", "Debug the reentrancy attack in Remix", "Draw the Escrow with sol2uml", "Annotate who may call each function", "Compare the diagram with the legal text"],
    "Concepts, execution, structure, roles, law."),
  O("Order how to read one debugger step.", ["Move the slider to a step", "Read the highlighted source line", "Read the call stack", "Read local and state variables"],
    "Where, who called, what values."),
],
"dapp-architecture": [
  F("Complete what reads cost in a dApp.", """
reading state() through eth_call: ____""", ["free, no transaction", "gas paid by the user", "gas paid by the provider", "a signature"], 0,
    "Calls are free reads; only transactions cost gas."),
  F("Complete where many teams host the front end to avoid a single server.", """
front end on ____, reachable through any gateway""", ["IPFS", "the smart contract storage", "MetaMask", "the RPC provider"], 0,
    "IPFS hosting lets anyone serve the same files."),
  X("One line about dApp layers is wrong.", """
contracts hold the rules and the money
the front end prepares transactions
the wallet asks the user to sign
the front end can sign for the user without asking""", 3, ["only the wallet can sign, after the user confirms", "the provider signs", "the indexer signs"], 0,
    "Keys stay in the wallet."),
  X("One step in this pay flow is wrong.", """
read price() from the contract
prepare deposit() with value = price
wallet shows the call and the user confirms
the app shows Complete before the transaction is included""", 3, ["show Pending until the receipt arrives", "show Complete before signing", "skip the receipt"], 0,
    "Only a receipt proves inclusion."),
  O("Order a write action in a dApp.", ["Read the current state", "Build the transaction", "The wallet asks for confirmation", "The transaction is sent and included", "The app reads the event and updates"],
    "Read, build, sign, include, update."),
  O("Order what to do if the official website is down.", ["Find the contract address from a trusted source", "Open it on Etherscan", "Check the source is verified", "Use Write Contract to call the function"],
    "The contract still works without the website."),
],
"oracles": [
  F("Complete the stale-price check.", """
(price, updatedAt) = feed.latest()
require(block.timestamp - updatedAt <= ____, "Stale")""", ["the feed's heartbeat, e.g. 1 hours", "0", "1 years", "updatedAt"], 0,
    "Reject prices older than the feed's update interval."),
  F("Complete the optimistic oracle rule.", """
answer accepted unless disputed within ____ (with a bond)""", ["a challenge period", "one block", "one second", "never"], 0,
    "Disputers must post a bond during the window."),
  X("One line in this price logic is unsafe.", """
read price from a decentralised feed
reject prices older than the heartbeat
reject moves above 20% from the last price
fall back to the spot price of one small pool""", 3, ["pause instead of using a manipulable source", "use the highest price seen", "use a price from social media"], 0,
    "The fallback reintroduces the manipulation risk."),
  X("One reading of the oracle problem is wrong.", """
contracts cannot fetch web data themselves
an oracle brings outside facts on chain
wrong input gives wrong results from correct code
a decentralised oracle guarantees the data is true""", 3, ["it makes manipulation hard; sources can still be wrong", "it makes data private", "it removes all fees"], 0,
    "Decentralisation reduces, not removes, trust."),
  O("Order the steps of a flash-loan oracle attack.", ["Borrow a large amount", "Move the price in a small pool", "Use the wrong price in the victim protocol", "Swap back and repay the loan", "Keep the profit"],
    "All in one transaction."),
  O("Order a weather insurance payout.", ["Farmer buys a policy on chain", "The season ends", "The oracle reports rainfall", "The contract compares it with the threshold", "The contract pays if the rule is met"],
    "Data in, rule applied, payment out."),
],
"decentralised-storage": [
  F("Complete what keeps an IPFS file available.", """
someone must ____ the file""", ["pin", "burn", "mint", "hash twice"], 0,
    "Unpinned files can disappear."),
  F("Complete the NFT metadata link.", """
tokenURI = "ipfs://" + ____""", ["the CID of the metadata JSON", "the image file name", "the owner", "the token ID"], 0,
    "The metadata JSON points to the image CID."),
  X("One line about storage options is wrong.", """
IPFS: content-addressed, needs pinning
Filecoin: paid storage with proofs
Arweave: pay once for permanent storage
a normal web server: the file can never change""", 3, ["a normal web server: the owner can change the file behind the URL", "a web server is on chain", "a web server is content-addressed"], 0,
    "Location-based URLs do not fix the content."),
  X("One line in this GDPR design is wrong.", """
names and addresses stay in a database that can delete
only a hash goes on chain
the hash uses a random salt
encrypted personal data on chain is always allowed""", 3, ["avoid personal data on chain, even encrypted", "store names on IPFS", "store data in events"], 0,
    "Encryption can be broken later and the key holder can identify people."),
  O("Order publishing an NFT certificate.", ["Upload the image to IPFS", "Write metadata JSON with the image CID", "Upload the metadata and get its CID", "Mint with tokenURI = ipfs://<metadata CID>", "Pin both files"],
    "Image, metadata, mint, keep available."),
  O("Order from easiest to change to hardest to change.", ["File on a normal web server", "File on IPFS (new version = new CID)", "File on Arweave", "Data in Ethereum contract storage"],
    "Content addressing and permanence reduce what can change."),
],
"lab-attestations": [
  F("Complete the schema field for a document fingerprint.", """
schema: ____ documentHash, string documentType""", ["bytes32", "string", "uint8", "address"], 0,
    "A Keccak-256 hash is 32 bytes."),
  F("Complete what an attestation records.", """
attester, recipient, schema, data, ____""", ["time", "private key", "password", "ETH price"], 0,
    "Each attestation has a timestamp and a unique UID."),
  X("One line about EAS is wrong.", """
a schema defines the fields of an attestation
an attestation is a signed statement by an address
onchain attestations cost gas, offchain ones do not
an attestation proves that its content is true""", 3, ["it proves who claimed it and when", "it proves payment", "it proves identity under eIDAS"], 0,
    "Truth needs other evidence."),
  X("One step of the lab is in the wrong order.", """
create the schema
hash your document
attest with the schema
create a second schema after attesting so the attestation can use it""", 3, ["the schema must exist before attesting", "schemas are optional", "attest twice"], 0,
    "Attestations reference an existing schema."),
  O("Order the attestation lab.", ["Hash your document", "Create a schema", "Attest with the schema", "Copy the UID", "A teammate looks it up"],
    "Hash, schema, attest, share, verify."),
  O("Order how to check a received attestation.", ["Open it by UID", "Check the attester's address", "Check the schema", "Compare the document hash with your file"],
    "Who, what format, which document."),
],
"lab-quickdapp": [
  F("Complete where QuickDApp starts from in Remix.", """
Deployed Contracts -> three dots next to the Escrow -> ____""", ["Create a DApp", "Debug", "Verify", "Publish to IPFS"], 0,
    "Create a DApp opens the QuickDApp panel."),
  F("Complete the button that revises the generated app.", """
QuickDApp -> ____ -> describe the change -> Update with AI""", ["Ask AI to Update", "Delete DApp", "Refresh Preview", "Go to Contract"], 0,
    "Ask AI to Update opens the Update DApp dialog."),
  X("One line about QuickDApp is wrong.", """
it generates a front end with RemixAI
you approve the generated files
it works best on public networks such as Sepolia
the generated app can let the seller release the payment""", 3, ["the contract still rejects the seller", "the app changes the contract rules", "the seller becomes the arbiter"], 0,
    "A front end cannot change contract rules."),
  X("One line in the test report is wrong.", """
Deposit as buyer: expected success, actual success, pass
Confirm as seller: expected revert, actual revert, pass
Refund as arbiter: expected success, actual success, pass
Refund as buyer: expected success, actual revert, fail""", 3, ["Refund as buyer: expected revert, actual revert, pass", "Refund as buyer: skip", "Refund as buyer: expected success, pass"], 0,
    "The expectation was wrong: only the arbiter may refund."),
  O("Order the QuickDApp lab from contract to test report.", ["Have the Escrow on Sepolia in Remix", "Create a DApp with notes for three role panels", "Approve the generated files", "Test each role in the preview", "Write the test report"],
    "Contract, generate, approve, test, report."),
  O("Order one AI improvement cycle.", ["Pick one failed or unclear row in the report", "Ask AI to Update with a precise request", "Review the changed files", "Refresh the preview", "Test the row again"],
    "Small, checked changes."),
],
"ethereum-today": [
  F("Complete the upgrade that introduced blobs.", """
Dencun (March 2024): EIP-____""", ["4844", "1559", "7702", "20"], 0,
    "EIP-4844 added blob-carrying transactions for rollups."),
  F("Complete the optimistic rollup withdrawal.", """
withdraw from L2 to L1 -> wait for the ____""", ["challenge window (about 7 days)", "next block only", "next hard fork", "sequencer's approval forever"], 0,
    "Fraud proofs need time to be submitted."),
  X("One line in this upgrade timeline is wrong.", """
The Merge: September 2022, Proof of Stake
Dencun: March 2024, blobs
Pectra: May 2025, EIP-7702
Fusaka: December 2025, introduced Proof of Work again""", 3, ["Fusaka: December 2025, PeerDAS", "Fusaka: December 2025, The Merge", "Fusaka: cancelled"], 0,
    "Fusaka brought PeerDAS for more blob capacity."),
  X("One line about L2BEAT stages is wrong.", """
Stage 0: operators still have strong control
Stage 1: limited training wheels, a security council
Stage 2: users can exit and challenge without special trust
Stage 0 is the most decentralised""", 3, ["Stage 2 is the most decentralised", "all stages are equal", "Stage 1 has no rules"], 0,
    "Higher stage, fewer training wheels."),
  O("Order Ethereum's upgrades by date.", ["The Merge", "Dencun", "Pectra", "Fusaka", "Glamsterdam (live on Sepolia, mainnet pending as of Nov 2026)"],
    "2022, 2024, 2025, 2025, 2026+."),
  O("Order a ZK rollup batch.", ["Users send transactions to the sequencer", "The sequencer executes a batch", "A prover creates a validity proof", "The batch data and proof go to Ethereum", "Ethereum's contract verifies the proof"],
    "Execute off chain, prove, verify on chain."),
],
"channels-sidechains-bridges": [
  F("Complete how a payment channel closes.", """
submit the ____ signed balance update on chain""", ["latest", "first", "random", "unsigned"], 0,
    "The latest state counts; old states can be challenged."),
  F("Complete the return trip of a lock-and-mint bridge.", """
burn wrapped tokens on chain B -> ____ on chain A""", ["unlock the originals", "mint more", "burn the originals", "nothing"], 0,
    "Burning the copy releases the original."),
  X("One line about sidechains is wrong.", """
a sidechain has its own validators
it is connected to Ethereum by a bridge
it is usually cheap and fast
it inherits Ethereum's security like a rollup""", 3, ["its security depends on its own validators", "it is secured by Bitcoin", "it has no security"], 0,
    "That is the key difference to rollups."),
  X("One line about bridge risk is wrong.", """
the vault holds many users' locked funds
a few signers often control releases
Ronin (2022) lost about $600 million
a bridge hack cannot affect the wrapped tokens' value""", 3, ["unbacked wrapped tokens lose value", "wrapped tokens double", "wrapped tokens convert back automatically"], 0,
    "Wrapped tokens depend on the vault."),
  O("Order a payment channel's life.", ["Both parties lock funds on chain", "They exchange signed updates off chain", "Each new update replaces the previous one", "One party submits the latest update", "The contract pays out the balances"],
    "Open, update, close."),
  O("Order the Ronin-style bridge hack.", ["Attackers obtain enough validator keys", "They sign fake withdrawal messages", "The bridge releases the locked funds", "Wrapped tokens on the other chain lose their backing"],
    "Key compromise drains the vault."),
],
"zero-knowledge": [
  F("Complete the three properties of a proof system.", """
completeness, soundness, ____""", ["zero knowledge", "immutability", "decentralisation", "liquidity"], 0,
    "The verifier learns nothing beyond the truth of the statement."),
  F("Complete what a SNARK on Ethereum costs to verify.", """
verify(proof) -> ____""", ["a small, fixed amount of gas", "re-running every transaction", "nothing", "a trusted bank"], 0,
    "Verification is cheap compared with re-execution."),
  X("One line about SNARKs and STARKs is wrong.", """
SNARK proofs are very small
some SNARKs need a trusted setup
STARKs need no trusted setup
STARK proofs are smaller than SNARK proofs""", 3, ["STARK proofs are larger", "STARKs need a trusted setup", "they are the same"], 0,
    "STARKs trade size for transparency and quantum resistance."),
  X("One line about an age proof is wrong.", """
the issuer signs the date of birth
the user proves age >= 18
the shop checks the proof and the issuer's key
the shop learns the exact date of birth""", 3, ["the shop learns only that the statement is true", "the shop learns the passport number", "the shop learns nothing at all"], 0,
    "Selective disclosure in practice."),
  O("Order a ZK age check.", ["A trusted issuer gives the user a signed credential", "The shop asks: over 18?", "The user's wallet creates a proof", "The shop verifies the proof", "The shop sells without seeing the birth date"],
    "Issue, ask, prove, verify, act."),
  O("Order from most to least data revealed.", ["Showing the full ID card", "Showing the date of birth only", "Showing a signed “over 18: yes” statement", "A zero-knowledge proof of age >= 18 that cannot be linked"],
    "Data minimisation step by step."),
],
"lab-dashboards": [
  F("Complete the Dune query filter for one day.", """
WHERE block_time >= TIMESTAMP '2026-11-01'
  AND block_time <  TIMESTAMP '____'""", ["2026-11-02", "2026-11-01", "2025-11-01", "2026-12-01"], 0,
    "One day: from midnight to the next midnight."),
  F("Complete what L2BEAT's risk view answers.", """
who can upgrade, how fast, and can users ____ first?""", ["exit", "vote", "mine", "stake"], 0,
    "Exit windows protect users from bad upgrades."),
  X("One reading of DefiLlama's hacks page is wrong.", """
each entry has date, amount and chain
entries name the technique
totals can be compared by year
the list shows only code bugs""", 3, ["it includes key compromises and other techniques", "it shows only Bitcoin", "it shows only 2016"], 0,
    "Many entries are operational attacks."),
  X("One conclusion overreaches the data.", """
Bybit is the largest 2025 entry
key compromises make up a large share of losses
the data supports “operations matter as much as code”
the data proves no audited contract was ever hacked""", 3, ["audited contracts also appear in the list", "only audited contracts were hacked", "audits cause hacks"], 0,
    "Draw only conclusions the data supports."),
  O("Order a dashboard research task.", ["Pick a research question", "Find data on L2BEAT, DefiLlama or Dune", "Build or fork a chart", "Check how the numbers are defined", "Write one conclusion with its limits"],
    "Question, data, chart, definitions, conclusion."),
  O("Order the L2BEAT part.", ["Sort rollups by value secured", "Pick three", "Note each stage", "Note who can upgrade and how fast", "Compare whether users can exit first"],
    "From ranking to governance risk."),
],
}
