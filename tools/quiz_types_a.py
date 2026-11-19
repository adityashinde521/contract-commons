# New question types for modules 1-4. Merged into src/data/quizzes.json by tools/quiz_types.py.
# F = fill the missing logic, X = fix the wrong line, O = put steps in order.
def F(q, code, o, a, e): return {"t": "fill", "q": q, "code": code.strip("\n"), "o": o, "a": a, "e": e}
def X(q, code, bad, o, a, e): return {"t": "fix", "q": q, "code": code.strip("\n").split("\n"), "bad": bad, "o": o, "a": a, "e": e}
def O(q, steps, e): return {"t": "order", "q": q, "steps": steps, "e": e}

ITEMS = {
# ---------- Module 1 ----------
"trust-and-ledgers": [
  F("A shared ledger accepts a new entry only if it links to the last one. Complete the pseudo code.", """
function append(ledger, entry):
    entry.prev = ____
    entry.hash = hash(entry.prev + entry.data)
    ledger.add(entry)""", ["hash of the last entry in the ledger", "the current time", "the name of the person adding it", "a random number"], 0,
    "Each entry stores the hash of the one before it. Changing an old entry changes its hash and breaks every link after it, so tampering becomes visible."),
  X("This pseudo code is meant to decide when a blockchain is worth using. One line has the logic reversed. Find it.", """
if only one party writes the data:
    use a normal database
if all writers trust one operator:
    use a blockchain
if writers do not trust each other and no one should control the record:
    consider a blockchain""", 3, ["use a normal database (the trusted operator can run it)", "use two blockchains", "delete the data"], 0,
    "If everyone already trusts one operator, that operator can run a database. A blockchain earns its cost only when no single party should control the record."),
  O("Put the steps of adding a payment to a shared ledger in order.", ["Alice signs a payment message with her key", "The message is broadcast to the network", "Nodes check the signature and the balance", "The payment is put into a new block", "The block is linked to the previous block by its hash"],
    "Sign, broadcast, validate, include in a block, then link the block into the chain."),
],
"hash-functions": [
  F("A notary service proves that a document existed. Complete the line that stores the proof.", """
fingerprint = ____(document_bytes)
store(fingerprint, current_time)""", ["keccak256", "encrypt", "compress", "base64"], 0,
    "A hash such as keccak256 gives a fixed-size fingerprint. Anyone can recompute it from the document, but nobody can get the document back from it."),
  X("This pseudo code checks whether a received file is the original. One line is wrong.", """
expected = stored_hash
actual = hash(received_file)
if actual != expected:
    print("File is unchanged")""", 3, ['print("File was changed")', 'print("Hash is secret")', 'actual = expected'], 0,
    "If the hashes differ, the file was changed. Even one changed bit gives a completely different hash (the avalanche effect)."),
  O("Order the steps to prove later that a contract PDF existed today.", ["Compute the hash of the PDF", "Register the hash on chain with a timestamp", "Keep the original PDF safely off chain", "Later, hash the PDF again", "Compare the new hash with the registered one"],
    "Only the hash goes on chain. To prove existence later, you hash the same file again and compare."),
],
"keys-and-signatures": [
  F("Complete the pseudo code of how a node checks a signed transaction.", """
signer = recover(message, signature)
if signer == ____:
    accept(message)""", ["the account that the message claims to come from", "the miner of the last block", "the receiver of the payment", "any address with a balance"], 0,
    "The signature lets anyone recover the signing address. It must match the account that the transaction claims to come from."),
  X("These safety rules for a course wallet contain one dangerous line. Find it.", """
create a new wallet only for this course
write the recovery phrase on paper
type the recovery phrase into a website when asked
use only Sepolia test ETH""", 2, ["never type or share the recovery phrase anywhere", "email the phrase to yourself", "store the phrase in a screenshot"], 0,
    "No real wallet, tool or support person needs your recovery phrase. Whoever has it controls the account."),
  O("Order what happens from creating a key to a payment being accepted.", ["Generate a private key", "Derive the public key and the address", "Sign a transaction with the private key", "A node recovers the address from the signature", "The node accepts the transaction because the address matches"],
    "The private key creates the address and the signatures. Nodes never see the private key; they only check that the signature fits the address."),
],
"blocks-and-state-models": [
  F("In the account model, a transfer updates balances. Complete the check.", """
function transfer(from, to, amount):
    require(____)
    balance[from] -= amount
    balance[to] += amount""", ["balance[from] >= amount", "balance[to] >= amount", "amount > balance[from]", "to != from"], 0,
    "The sender must have enough balance before anything changes. Ethereum uses this account model; Bitcoin uses unspent outputs (UTXO) instead."),
  X("This pseudo code spends Bitcoin-style outputs (UTXO). One line is wrong.", """
inputs = select_unspent_outputs(owner)
outputs = [payment_to_receiver, change_back_to_owner]
require(sum(inputs) >= sum(outputs))
mark inputs as still unspent""", 3, ["mark inputs as spent", "delete the outputs", "add the inputs to the receiver"], 0,
    "In the UTXO model each output can be spent only once. After use, the inputs are marked as spent; the change goes back to the owner as a new output."),
  O("Order the parts of building a new block.", ["Collect valid transactions from the mempool", "Execute them to get the new state", "Compute the Merkle root of the transactions", "Write the header with the previous block hash", "Propose the block to the network"],
    "Transactions first, then the resulting state and the Merkle root, then the header that links to the previous block."),
],
"types-of-blockchains": [
  F("Complete the decision rule for choosing a chain type.", """
if anyone may read and validate:
    choose a public chain
else if a known group of companies validates:
    choose ____""", ["a consortium (permissioned) chain", "a public chain", "no database at all", "a sidechain of Bitcoin"], 0,
    "When a fixed group of known organisations runs the validators, the chain is a consortium or permissioned chain."),
  X("One line in this comparison is wrong. Find it.", """
public chain: anyone can join as a validator
private chain: one organisation controls who writes
consortium chain: several known organisations validate
private chain: no single party can change the rules""", 3, ["private chain: the operator can change the rules", "private chain: miners compete with proof of work", "private chain: tokens are always required"], 0,
    "A private chain is controlled by one organisation, so that organisation can change the rules. That is the trade-off for speed and privacy."),
  O("Order the questions to decide which type of chain a project needs.", ["Who needs to write data?", "Do the writers trust each other or one operator?", "Must the public be able to read and verify?", "Choose public, consortium, private or a normal database"],
    "Start with who writes and who is trusted. Public readability comes next. The choice of chain type follows from the answers."),
],
"lab-eth-build": [
  F("In ETH.BUILD you connect blocks to show proof of existence. Complete the chain of blocks.", """
[Text input] --> [ ____ ] --> [Display: 0x3f...]""", ["Hash", "Key pair", "Transaction", "Block explorer"], 0,
    "The text goes into a Hash block, and the display shows its fingerprint. Change one letter and the whole output changes."),
  X("A student wires a signature check in ETH.BUILD. One connection is wrong.", """
[Message] --> [Sign] (private key in)
[Sign] --> [Recover]
[Message] --> [Recover]
[Recover] --> compare with the private key""", 3, ["[Recover] --> compare with the address", "[Recover] --> [Hash]", "[Sign] --> [Display] only"], 0,
    "Recovery returns an address. You compare it with the expected address, never with the private key, which stays secret."),
  O("Order the ETH.BUILD demo of a tamper-evident chain.", ["Hash block 1 data", "Feed block 1 hash into block 2", "Hash block 2 data with that previous hash", "Change one letter in block 1", "See that both hashes change"],
    "The demo shows that a change in an old block breaks every hash after it."),
],
# ---------- Module 2 ----------
"consensus": [
  F("Complete the proof-of-stake rule for a validator who signs two different blocks at the same height.", """
if validator signed two blocks for the same slot:
    ____""", ["slash part of the validator's stake", "give the validator a bonus", "ignore it", "make the validator a proposer next time"], 0,
    "Signing two conflicting blocks is an attack. In proof of stake the validator loses part of the stake (slashing)."),
  X("This summary of proof of work has one wrong line.", """
miners collect transactions into a block
miners search for a nonce so the block hash is below a target
the first valid block is broadcast
the longest chain with the most work loses""", 3, ["the chain with the most work wins", "the chain with the fewest blocks wins", "the oldest miner decides"], 0,
    "Nodes follow the chain with the most accumulated work. Rewriting history would need more work than the honest network."),
  O("Order one Ethereum proof-of-stake slot.", ["A validator is chosen as proposer for the slot", "The proposer builds and broadcasts a block", "A committee of validators attests to the block", "After enough epochs, the block becomes final"],
    "Proposer, block, attestations, then finality after two epochs."),
],
"forks-and-governance": [
  F("Complete the rule that tells a soft fork from a hard fork.", """
if old nodes still accept the new blocks:
    type = "soft fork"
else:
    type = ____""", ['"hard fork"', '"soft fork"', '"no fork"', '"sidechain"'], 0,
    "A soft fork tightens the rules, so old nodes still accept the blocks. A hard fork changes them, so old nodes reject the new blocks and must upgrade."),
  X("One line in this timeline of The DAO case (2016) is wrong.", """
The DAO raised about 150 million dollars in ETH
an attacker drained about a third using reentrancy
the community chose a hard fork that returned the funds
everyone accepted the fork, so only one chain exists""", 3, ["a minority kept the old chain, now Ethereum Classic", "the attacker reversed the fork", "Bitcoin absorbed the old chain"], 0,
    "Not everyone accepted the fork. The old chain continued as Ethereum Classic: governance is social, not only technical."),
  O("Order how a change to Ethereum is adopted.", ["Someone writes an EIP", "Researchers and client teams discuss it in All Core Devs calls", "Clients implement it and test it on testnets", "Node operators upgrade their software", "The fork activates at a set block or time"],
    "Proposal, discussion, implementation and testing, upgrade, then activation."),
],
"lab-read-the-chain": [
  F("On Etherscan you want to check that a transaction worked. Complete the check.", """
open the transaction page
look at the field ____
expect: Success""", ["Status", "Nonce", "Gas price", "Input data"], 0,
    "The Status field says Success or Fail. A failed transaction still costs gas but changes nothing."),
  X("A student reads a transaction. One reading is wrong.", """
From: the account that signed and paid gas
To: the receiver or the contract called
Value: the ETH sent with the transaction
Transaction fee: the amount the receiver paid""", 3, ["Transaction fee: the amount the sender paid for gas", "Transaction fee: always zero on Sepolia", "Transaction fee: the price of the block"], 0,
    "The sender pays the fee, calculated from gas used times gas price."),
  O("Order the steps to trace a token transfer on Etherscan.", ["Paste the transaction hash into the search box", "Check Status and Block", "Read From and To", "Open the token transfers section", "Follow the receiver address to see its balance"],
    "Find the transaction, confirm it succeeded, read the parties, then follow the tokens."),
],
# ---------- Module 3 ----------
"ethereum-evm-gas": [
  F("Complete the formula for the fee of a transaction after EIP-1559.", """
fee = gas_used * (____ + priority_fee)""", ["base_fee", "gas_limit", "block_number", "nonce"], 0,
    "Each unit of gas costs the base fee (burned) plus the priority fee (tip to the validator)."),
  X("One statement about gas in this list is wrong.", """
writing to storage costs much more gas than reading
a loop over a growing array can run out of gas
unused gas from the gas limit is refunded
a failed transaction costs no gas""", 3, ["a failed transaction still pays for the gas it used", "a failed transaction refunds double", "a failed transaction is free on mainnet only"], 0,
    "When a transaction reverts, its changes are undone, but the gas used until then is still paid."),
  O("Order how the EVM runs a call to a contract.", ["The transaction arrives with data for a function", "The EVM loads the contract bytecode", "It runs the opcodes and charges gas for each", "It writes the changed storage if no revert happened", "It returns the result and the receipt with logs"],
    "Load code, run with gas metering, commit state only if successful, then produce the receipt."),
],
"wallets-and-testnets": [
  F("Complete the setup rule for this course.", """
network = ____
real_money = 0""", ["Sepolia testnet", "Ethereum mainnet", "any network with low fees", "Bitcoin"], 0,
    "All labs use the Sepolia testnet. Test ETH from a faucet has no value."),
  X("One step in this wallet setup is wrong.", """
install MetaMask from the official site
create a new wallet only for the course
add the Sepolia network
send real ETH from an exchange to test the labs""", 3, ["get free Sepolia ETH from a faucet", "buy a hardware wallet first", "import a friend's wallet"], 0,
    "No real money is ever needed. Use a faucet for free test ETH."),
  O("Order the steps to make your first testnet transaction.", ["Create a course wallet in MetaMask", "Switch to the Sepolia network", "Get test ETH from a faucet", "Send a small amount to a classmate", "Check the transaction on Sepolia Etherscan"],
    "Wallet, network, test ETH, transaction, then verify on the explorer."),
],
"nodes-and-providers": [
  F("A web app reads the chain through a provider. Complete the line.", """
balance = provider.____(address)""", ["getBalance", "signTransaction", "createWallet", "mine"], 0,
    "Reading the chain needs no key: a provider such as an RPC endpoint answers getBalance and similar read calls."),
  X("One line about node types is wrong.", """
a full node checks every block and keeps the recent state
an archive node also keeps all historical states
a light client checks block headers and asks others for data
an RPC provider such as Infura must hold your private key""", 3, ["an RPC provider only forwards signed transactions; your wallet signs", "an RPC provider mines your blocks", "an RPC provider stores your recovery phrase"], 0,
    "The provider never needs your key. Your wallet signs; the provider passes the signed transaction to the network."),
  O("Order how a dApp sends a transaction.", ["The user clicks a button in the dApp", "The dApp builds the transaction", "The wallet shows it and the user signs", "The signed transaction goes to an RPC node", "The node broadcasts it to the network"],
    "The dApp prepares, the wallet signs, the node broadcasts."),
],
"lab-remix-tour": [
  F("Complete the Remix workflow for running a contract.", """
1. write the contract in the File explorer
2. ____ it in the Solidity compiler tab
3. deploy it in the Deploy & run tab""", ["compile", "verify", "audit", "mine"], 0,
    "Remix compiles the Solidity source to bytecode first, then deploys it."),
  X("One setting in this Remix tour is wrong for a first test.", """
Environment: Remix VM (Cancun)
Account: the first test account with 100 ETH
Value: 0 for a normal deploy
Environment: Injected Provider on Ethereum mainnet""", 3, ["keep Remix VM for the first tests", "Environment: any public RPC", "Environment: a private key typed in"], 0,
    "The first labs run in the Remix VM in your browser: no network, no real money."),
  O("Order your first Remix session.", ["Open remix.ethereum.org", "Create a new .sol file", "Compile it", "Deploy it to the Remix VM", "Call a function and read the terminal output"],
    "Open, write, compile, deploy, interact."),
],
"lab-simple-storage": [
  F("Complete SimpleStorage so that every change can be followed off chain.", """
function set(uint256 newValue) external {
    storedValue = newValue;
    lastWriter = msg.sender;
    ____
}""", ["emit ValueChanged(msg.sender, newValue);", "return storedValue;", "selfdestruct(msg.sender);", "require(newValue == 0);"], 0,
    "Events write a log entry that apps and explorers can read cheaply. Storage keeps the value; the event keeps the history."),
  X("One line in this SimpleStorage is wrong: get() should only read.", """
function get() external view returns (uint256) {
    storedValue = storedValue + 1;
    return storedValue;
}""", 1, ["delete this line: a view function only reads", "storedValue = 0;", "lastWriter = msg.sender;"], 0,
    "A view function promises not to change state, and the compiler rejects writes in it. get() must only return the value."),
  O("Order the SimpleStorage lab.", ["Deploy SimpleStorage in the Remix VM", "Call get() and see 0", "Call set(42) and read the event in the terminal", "Call get() again and see 42", "Switch account and see lastWriter change after another set()"],
    "Deploy, read the default, write, read again, then test with another account."),
],
# ---------- Module 4 ----------
"what-smart-contracts-are": [
  F("Complete the pseudo code of what a smart contract can and cannot decide alone.", """
if payment received and deadline passed:
    contract can refund automatically
if goods are "of acceptable quality":
    contract needs ____""", ["an oracle or a human arbiter to decide", "nothing: code knows quality", "a higher gas limit", "a second blockchain"], 0,
    "Code enforces clear, on-chain facts. Vague legal terms such as acceptable quality need outside input: an oracle or an arbiter."),
  X("One claim about smart contracts is wrong.", """
a smart contract is a program on a blockchain
it runs exactly as written once deployed
it can hold and move tokens by itself
it replaces contract law, so courts are not needed""", 3, ["it can be part of a legal contract, but contract law still applies", "it is always a legal contract", "it cannot hold tokens"], 0,
    "A smart contract can perform part of an agreement. Formation, capacity, mandatory law and disputes are still matters of law."),
  O("Order the life of a smart contract.", ["Write the code", "Test it", "Deploy it to a network", "Users call its functions with transactions", "Its state and events record what happened"],
    "Write, test, deploy, use, and the chain keeps the record."),
],
"solidity-for-programmers": [
  F("Complete the modifier so only the owner can call a function.", """
modifier onlyOwner() {
    require(____, "Only owner");
    _;
}""", ["msg.sender == owner", "tx.origin != owner", "owner == address(0)", "msg.value > 0"], 0,
    "msg.sender is the direct caller. Use it, not tx.origin, for access control."),
  X("This function should accept a payment of exactly 1 ether. One line is wrong.", """
function pay() external {
    require(msg.value == 1 ether, "Send 1 ether");
    paid[msg.sender] = true;
}""", 0, ["function pay() external payable {", "function pay() internal {", "function pay() external view {"], 0,
    "A function that receives ETH must be marked payable. Without it, every call with a value reverts."),
  O("Order the parts of a typical Solidity contract file.", ["SPDX license line", "pragma solidity version", "contract declaration", "state variables and events", "constructor", "functions"],
    "License, compiler version, then the contract with state, events, constructor and functions."),
],
"lab-escrow": [
  F("Complete confirmDelivery in the Escrow lab so only the right people can release the money.", """
function confirmDelivery() external inState(State.AwaitingDelivery) {
    require(____, "Only buyer or arbiter");
    state = State.Complete;
    ...
}""", ["msg.sender == buyer || msg.sender == arbiter", "msg.sender == seller", "msg.sender == buyer && msg.sender == arbiter", "msg.value == price"], 0,
    "§4 of the lab contract: the buyer or the arbiter may release. && would need one address to be both."),
  X("This Escrow deposit has one wrong line. Find it.", """
function deposit() external payable inState(State.AwaitingPayment) {
    require(msg.sender == seller, "Only buyer");
    require(msg.value == price, "Send exact price");
    state = State.AwaitingDelivery;
    emit Deposited(msg.sender, msg.value);
}""", 1, ['require(msg.sender == buyer, "Only buyer");', 'require(msg.sender == arbiter, "Only buyer");', 'require(msg.value > 0, "Only buyer");'], 0,
    "A wrong address check: only the buyer pays in. The error message already says so; the condition must match it."),
  O("Order a successful Escrow run in Remix.", ["Deploy as the buyer with the seller, the arbiter and the price", "Call deposit() as the buyer with the exact price", "Check that the state is AwaitingDelivery", "Call confirmDelivery() as the buyer", "Check that the seller's balance went up and the state is Complete"],
    "Deploy, pay in, check state, release, check balances."),
],
"lab-rental-deposit": [
  F("Complete settle() so the landlord cannot settle before the lease ends.", """
function settle(uint256 damageAmount) external {
    require(msg.sender == landlord, "Only landlord");
    require(paid && !settled, "Nothing to settle");
    require(____, "Lease not ended");
    ...
}""", ["block.timestamp >= leaseEnd", "block.timestamp < leaseEnd", "damageAmount == 0", "msg.value == depositAmount"], 0,
    "The time rule: settlement is only possible after leaseEnd. < would allow it only before the end."),
  X("One line in RentalDeposit is wrong. Find it.", """
function settle(uint256 damageAmount) external {
    require(msg.sender == landlord, "Only landlord");
    require(paid && !settled, "Nothing to settle");
    require(block.timestamp >= leaseEnd, "Lease not ended");
    require(damageAmount >= depositAmount, "Damage too high");
    settled = true;
    _payOut(damageAmount);
}""", 4, ['require(damageAmount <= depositAmount, "Damage too high");', 'require(damageAmount == 0, "Damage too high");', 'require(damageAmount > depositAmount, "Damage too high");'], 0,
    "The comparison is reversed. The landlord may keep at most the deposit, so damageAmount must be less than or equal to it."),
  O("Order the RentalDeposit lab when the landlord does nothing.", ["The landlord deploys with the tenant, amount and lease days", "The tenant pays the deposit", "The lease end passes", "30 more days pass with no settlement", "The tenant calls claimAfterTimeout() and gets the full deposit back"],
    "The timeout protects the tenant if the landlord stays silent, close to the idea behind §551 BGB deposit rules."),
],
"lab-document-registry": [
  F("Complete register() so the same document cannot be registered twice.", """
function register(bytes32 docHash) external {
    require(____, "Already registered");
    records[docHash] = Record(msg.sender, block.timestamp);
}""", ["records[docHash].timestamp == 0", "records[docHash].timestamp != 0", "docHash == 0", "msg.sender == owner"], 0,
    "An empty record has timestamp 0. Only then is the hash new."),
  X("One line breaks the privacy promise of the DocumentRegistry.", """
struct Record { address owner; uint256 timestamp; }
mapping(bytes32 => Record) public records;
string public fullDocumentText;
event DocumentRegistered(bytes32 indexed docHash, address indexed owner, uint256 timestamp);""", 2, ["delete it: store only the hash, never the document", "make it private", "store it in an event"], 0,
    "Everything on chain is public, even private variables. The registry stores only the hash, which reveals nothing about the content (GDPR)."),
  O("Order how a court could check a registered contract.", ["Get the original file from the party", "Compute its hash off chain", "Call verify(hash) on the registry", "Read exists, owner and timestamp", "Compare the timestamp with the claimed date"],
    "The proof needs both the file and the on-chain record."),
],
}
