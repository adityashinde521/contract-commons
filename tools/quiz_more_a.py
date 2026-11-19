# Second and third fill / fix / order items per unit: modules 1-3.
from quiz_types_a import F, X, O

ITEMS = {
"trust-and-ledgers": [
  F("Complete the double-spend check of a shared ledger.", """
function accept(payment):
    if ____:
        reject(payment)
    else:
        mark coin as spent""", ["the coin was already spent in an earlier entry", "the payment is larger than 1 coin", "the receiver is new", "the sender is online"], 0,
    "A coin may be spent only once. All nodes follow one order of entries, so the second payment finds the coin already spent."),
  F("Which of the three blockchain tools solves each problem? Complete the line.", """
integrity     -> hashes
authorisation -> signatures
agreement     -> ____""", ["consensus", "encryption", "a central bank", "smart contracts"], 0,
    "Consensus makes all copies of the ledger agree on one order of transactions."),
  X("One line in this description of a bank transfer is wrong.", """
the bank keeps the ledger
the bank checks that the payer has the money
the bank can freeze or reverse a payment
nobody needs to trust the bank""", 3, ["customers trust the bank to keep the record correctly", "the bank never keeps records", "the payer keeps the ledger"], 0,
    "A bank is a trusted record keeper. A blockchain replaces that trust with many checking copies."),
  X("One line overstates what a blockchain proves in the laptop sale.", """
the ledger shows that 1 ETH moved from buyer to escrow
anyone can verify the payment later
the payment cannot be quietly changed
the ledger proves that the laptop arrived""", 3, ["delivery needs an arbiter or an oracle to report it", "the ledger proves the laptop's quality", "the ledger proves the seller's identity"], 0,
    "Outside facts such as delivery are not on chain until someone reports them."),
  O("Order how a double spend is stopped on a blockchain.", ["Alice signs two payments with the same coin", "Both payments reach the network", "Consensus places one payment first in the agreed order", "The second payment finds the coin already spent", "Nodes reject the second payment"],
    "One agreed order decides which payment counts."),
  O("Order the questions that decide whether a blockchain is worth it.", ["Do several parties need to write to the record?", "Do they want to avoid trusting one of them to keep it?", "Must outsiders be able to verify it later?", "Only if all answers are yes, consider a blockchain"],
    "If one party writes or everyone trusts one operator, a database is better."),
],
"hash-functions": [
  F("Complete the rule that protects a hash of personal data.", """
fingerprint = keccak256(____ + date_of_birth)""", ["a secret random salt", "the year", "nothing", "the person's name"], 0,
    "Dates of birth have few possible values. A random salt stops attackers from hashing every date and comparing."),
  F("Complete the line that links a block to the one before it.", """
block.header.prevHash = ____""", ["hash(previous block header)", "hash(next block)", "the block number", "the miner's address"], 0,
    "Each header stores the hash of the previous header, which makes the chain tamper-evident."),
  X("One property in this list is described wrongly.", """
deterministic: same input, same hash
avalanche: one changed letter changes the whole hash
one-way: you cannot get the input back from the hash
collision-resistant: similar texts get similar hashes""", 3, ["collision-resistant: finding two inputs with the same hash is not practical", "collision-resistant: every hash is unique by law", "collision-resistant: hashes can be reversed"], 0,
    "Similar texts give completely different hashes; that is the avalanche effect. Collision resistance means no two inputs share a hash in practice."),
  X("One line about Ethereum's hash function is wrong.", """
Ethereum uses Keccak-256
the output has 256 bits
it is written as 64 hexadecimal characters
it is exactly the same as the NIST SHA3-256 standard""", 3, ["it differs from SHA3-256 because NIST changed the padding", "it uses 128 bits", "it is the same as SHA-1"], 0,
    "Keccak-256 is the original SHA-3 competition winner. The final NIST standard changed the padding, so outputs differ."),
  O("Order how ETH.BUILD shows that tampering breaks a chain.", ["Hash the data of block 1", "Put that hash into block 2 as prev", "Hash block 2 including prev", "Change one letter in block 1", "Block 1's hash changes and block 2's prev no longer matches"],
    "Changing old data breaks every later link."),
  O("Order how a court checks a document against a registered hash.", ["Receive the file from the party", "Compute its hash", "Look up the hash on chain", "Read the block timestamp of the registration", "Conclude whether this exact file existed at that time"],
    "The proof needs both the file and the on-chain record."),
],
"keys-and-signatures": [
  F("Complete how an Ethereum address is derived.", """
publicKey = privateKey * G   (elliptic curve)
address   = last 20 bytes of ____""", ["keccak256(publicKey)", "the private key", "sha1(address)", "the transaction hash"], 0,
    "The address is the last 20 bytes of the Keccak-256 hash of the public key."),
  F("Complete what stops a Sepolia transaction from being replayed on mainnet.", """
signed data includes: to, value, nonce, gas, ____""", ["chainId", "the private key", "the block hash", "the receiver's balance"], 0,
    "The chain ID is part of the signed data (EIP-155). A Sepolia signature is invalid on mainnet."),
  X("One line about signatures is wrong.", """
the wallet signs with the private key
the node recovers an address from the signature
a changed transaction recovers a different address
the node needs the private key to check the signature""", 3, ["the node needs only the transaction and the signature", "the node asks the wallet for the key", "the node uses the recovery phrase"], 0,
    "Verification uses public data only. The private key never leaves the wallet."),
  X("One step in this wallet backup routine is unsafe.", """
write the recovery phrase on paper
store the paper somewhere safe and private
never type the phrase into a website
take a photo of the phrase as a backup""", 3, ["keep a second paper copy in another safe place", "email the phrase to yourself", "upload the photo to the cloud"], 0,
    "Photos sync to clouds and leak. Whoever sees the phrase controls the wallet."),
  O("Order how a key pair and an address come to exist.", ["Generate a random private key", "Multiply it on the elliptic curve to get the public key", "Hash the public key with Keccak-256", "Take the last 20 bytes as the address"],
    "Each step is easy forwards and practically impossible backwards."),
  O("Order what a node checks for an incoming transaction.", ["Recover the signer's address from the signature", "Compare it with the claimed sender", "Check that the nonce is the next one", "Check that the balance covers value and fee", "Accept the transaction into the mempool"],
    "Signature first, then nonce and balance."),
],
"blocks-and-state-models": [
  F("Complete the Merkle tree for four transactions.", """
hAB  = hash(hA + hB)
hCD  = hash(hC + hD)
root = ____""", ["hash(hAB + hCD)", "hash(hA + hD)", "hAB + hCD", "hash(hC)"], 0,
    "Pairs are hashed upwards until one hash, the root, remains."),
  F("Complete the account-model update for a payment of 0.6 ETH.", """
balance[Alice] -= 0.6 + fee
balance[Bob]   += 0.6
nonce[Alice]   = ____""", ["nonce[Alice] + 1", "0", "nonce[Bob]", "the block number"], 0,
    "Each transaction increases the sender's nonce by one, which blocks replays."),
  X("One line about a UTXO payment is wrong.", """
inputs: Alice's outputs of 0.5 and 0.2 BTC
outputs: 0.6 BTC to Bob and 0.099 BTC change to Alice
fee: 0.001 BTC
the 0.5 and 0.2 outputs can be spent again later""", 3, ["the 0.5 and 0.2 outputs are now spent forever", "the change is lost", "Bob receives 0.7 BTC"], 0,
    "In the UTXO model each output is spent exactly once."),
  X("One claim about Merkle proofs is wrong.", """
a Merkle proof shows that a transaction is in a block
it needs only a few hashes, not all transactions
a light client can check it against the header
it proves that the transaction is valid and paid enough""", 3, ["it proves inclusion only, not validity", "it proves the sender's identity", "it proves the block is final"], 0,
    "Inclusion is not validity. Validity comes from full nodes executing the block."),
  O("Order the proof that transaction C is in a block with A, B, C, D.", ["Hash transaction C", "Combine it with the given hash of D", "Combine the result with the given hash of AB", "Compare the final hash with the Merkle root in the header"],
    "Two given hashes are enough for four transactions."),
  O("Order what happens to Ethereum's state in one block.", ["Start from the state after the previous block", "Execute the block's transactions in order", "Write the changed balances and storage", "Compute the new state root", "Put the state root in the block header"],
    "The state root summarises the state after all transactions."),
],
"types-of-blockchains": [
  F("Complete the rule for a single company's internal log.", """
writers = 1 organisation
outside verifiers = none
choose = ____""", ["a normal database with an audit log", "a public blockchain", "a consortium chain", "a sidechain"], 0,
    "With one writer and no outside verifier, a blockchain adds cost without benefit."),
  F("Complete the description of a consortium chain.", """
who validates: ____
who reads: as agreed by the members""", ["a fixed group of known organisations", "anyone with stake", "one company", "nobody"], 0,
    "A consortium chain is run by several known organisations."),
  X("One line about public chains is wrong.", """
anyone can send transactions
anyone can read all data
anyone can become a validator with enough stake
data on a public chain is private by default""", 3, ["data is public unless it is encrypted or kept off chain", "data is deleted after a year", "only validators can read data"], 0,
    "Public chains publish everything. Privacy needs extra techniques."),
  X("One line about a diploma registry design is wrong.", """
the university is the only writer
employers worldwide must verify
the chain stores a hash or an attestation
the chain stores the student's full transcript""", 3, ["the transcript stays in the university's system", "the chain stores the student's password", "the chain stores nothing at all"], 0,
    "Personal data stays off chain; only proof data goes on chain."),
  O("Order the decision for a new shared record.", ["List who must write", "List who must read and verify", "Decide whom users are willing to trust", "Choose public, consortium, private chain or database"],
    "Roles and trust come before the technology choice."),
  O("Order from most open to most controlled.", ["Public permissionless chain", "Public chain with an allow-listed token", "Consortium chain", "Private chain run by one company"],
    "Each step gives more control to fewer parties."),
],
"lab-eth-build": [
  F("In ETH.BUILD you show that a signature belongs to an address. Complete the wiring.", """
[Message] + [Signature] --> [ ____ ] --> [Address]""", ["Recover", "Hash only", "Key Pair", "Text"], 0,
    "Recover takes a message and a signature and returns the signing address."),
  F("Complete the ETH.BUILD demo of the avalanche effect.", """
type "rent 900"  -> hash 0x8a…
type "rent 990"  -> hash ____""", ["a completely different value", "0x8a… with one changed digit", "the same value", "an error"], 0,
    "One changed character changes the whole hash."),
  X("One reading of the ETH.BUILD Key Pair module is wrong.", """
private key: 64 hex characters, keep secret
public key: derived from the private key
address: 40 hex characters with 0x
you can compute the private key from the address""", 3, ["you cannot compute the private key from the address", "the address is the private key", "the public key is random"], 0,
    "Each derivation step is one-way."),
  X("One step in this hash demo is in the wrong place.", """
add a Text input module
add a Hash module
read the hash output
connect the text output to the hash input""", 3, ["connect before reading: the hash has no input yet", "remove the Hash module", "read the private key"], 0,
    "Without a connection the hash module has nothing to hash."),
  O("Order the ETH.BUILD signing demo.", ["Create a key pair", "Type a message", "Sign the message with the private key", "Recover the address from message and signature", "Compare it with the key pair's address"],
    "Sign with the key, recover with public data, compare."),
  O("Order the build-up of the ETH.BUILD blockchain demo.", ["Make a block with data and a nonce", "Hash the block", "Add a second block that includes the first hash", "Change the first block's data", "See the second block become invalid"],
    "Linking by hash makes a change visible downstream."),
],
"consensus": [
  F("Complete the timing of Ethereum Proof of Stake.", """
slot  = 12 seconds
epoch = 32 slots = ____""", ["6.4 minutes", "12 minutes", "1 hour", "32 seconds"], 0,
    "32 × 12 s = 384 s = 6.4 minutes. Finality takes about two epochs."),
  F("Complete the finality rule.", """
checkpoint is finalised when attestations from ____ of all stake
support it over two epochs""", ["two thirds", "one half", "one third", "all"], 0,
    "A two-thirds supermajority of stake justifies and then finalises checkpoints."),
  X("One line about Proof of Work is wrong.", """
miners search for a nonce that gives a small enough hash
finding it is expensive, checking it is cheap
nodes follow the chain with the most accumulated work
Ethereum still uses Proof of Work for its blocks""", 3, ["Ethereum has used Proof of Stake since September 2022", "Ethereum uses no consensus", "Ethereum uses Proof of Authority on mainnet"], 0,
    "The Merge in 2022 switched Ethereum to Proof of Stake."),
  X("One line about attacking Proof of Stake is wrong.", """
reverting finality needs at least one third of all stake
the protocol detects conflicting votes
the offending validators are slashed
the attackers keep their full stake afterwards""", 3, ["the attackers lose a large part of their stake", "the attackers get a reward", "the attackers are anonymous and safe"], 0,
    "Slashing makes attacks cost the attacker's own capital."),
  O("Order the path of a transaction from inclusion to finality.", ["The transaction is included in a block in slot n", "Validators attest to the block", "The epoch's checkpoint is justified", "One epoch later the checkpoint is finalised", "Exchanges treat the deposit as final"],
    "Included after about 12 s, final after about 13 minutes."),
  O("Order a Proof of Work block from start to acceptance.", ["Collect transactions", "Build the block header", "Try nonces until the hash is below the target", "Broadcast the block", "Other nodes check the hash and the transactions"],
    "Search is costly, verification is quick."),
],
"forks-and-governance": [
  F("Complete what happens when a group refuses a hard fork.", """
if many nodes keep running the old rules:
    result = ____""", ["two chains continue side by side", "the old nodes join automatically", "the fork is cancelled by law", "all funds are lost"], 0,
    "That is how Ethereum Classic continued after the DAO fork in 2016."),
  F("Complete the order of networks for testing an upgrade.", """
devnets -> Sepolia -> ____ -> mainnet""", ["Hoodi", "Goerli", "Ropsten", "Bitcoin"], 0,
    "Sepolia and Hoodi are the public testnets used before mainnet (as of 2026)."),
  X("One line about who governs Ethereum is wrong.", """
anyone can write an EIP
client teams discuss and implement it
node operators choose which software to run
the Ethereum Foundation can force every node to upgrade""", 3, ["nobody can force nodes; they choose to upgrade", "only miners vote", "exchanges write the code"], 0,
    "Adoption is voluntary. Power is spread across developers, operators and users."),
  X("One line about the Glamsterdam delay (autumn 2026) is wrong.", """
Glamsterdam went live on Sepolia in October 2026
the Hoodi step was postponed over gas-repricing risks
some deployed contracts could break under the new rules
mainnet activation was fixed for 1 November 2026""", 3, ["no mainnet date was set as of 20 November 2026", "it was cancelled for good", "it went live on mainnet in October"], 0,
    "As of 20 November 2026 there was no mainnet date."),
  O("Order the life of an Ethereum Improvement Proposal.", ["An author drafts the EIP", "It is discussed publicly and in All Core Devs calls", "It is included in a named upgrade", "Client teams implement and test it on testnets", "The upgrade activates on mainnet"],
    "Draft, discuss, bundle, implement and test, activate."),
  O("Order the events of the 2016 DAO fork.", ["The DAO raises about 150 million dollars in ETH", "An attacker drains about a third with reentrancy", "The community debates a hard fork", "Most nodes adopt the fork that returns the funds", "A minority keeps the old chain as Ethereum Classic"],
    "A code bug led to a social decision and a chain split."),
],
"lab-read-the-chain": [
  F("Complete how to see the latest blocks on Etherscan.", """
open etherscan.io -> section ____""", ["Latest Blocks", "Token Approvals", "Gas Tracker settings", "Verified Contracts"], 0,
    "The home page lists the latest blocks and transactions."),
  F("A transaction on Etherscan has these numbers. Complete the fee.", """
Gas used: 21,000
Gas price: 10 gwei
Fee = ____""", ["210,000 gwei = 0.00021 ETH", "21,010 gwei", "0.21 ETH", "10 ETH"], 0,
    "21,000 × 10 gwei = 210,000 gwei = 0.00021 ETH."),
  X("One reading of a block page is wrong.", """
Block height: the number of the block
Transactions: how many are in it
Fee recipient: the validator that proposed it
Gas used: the ETH price on that day""", 3, ["Gas used: the total gas of all transactions in the block", "Gas used: the number of nodes", "Gas used: the block reward"], 0,
    "Gas used measures work, not price."),
  X("One reading of a token page is wrong.", """
Total supply: tokens in existence
Holders: number of addresses with a balance
Contract: the token's address, verified if green
Holders: the people who created the token""", 3, ["Holders: addresses that currently hold the token", "Holders: validators", "Holders: auditors"], 0,
    "Holders counts addresses with a non-zero balance."),
  O("Order the steps to read your own course transaction.", ["Copy your address from MetaMask", "Search it on sepolia.etherscan.io", "Open the latest transaction", "Check Status, From, To and Value", "Note the fee"],
    "Find, open, read, note."),
  O("Order how to inspect a stablecoin on Etherscan.", ["Search the token name", "Open the token page", "Read total supply and holders", "Open the Contract tab", "Check that the source is verified"],
    "From overview to the verified code."),
],
"ethereum-evm-gas": [
  F("Complete the EIP-1559 fee for 50,000 gas.", """
base fee = 8 gwei, priority fee = 1 gwei
fee = 50,000 * ____""", ["(8 + 1) gwei", "8 gwei", "1 gwei", "(8 - 1) gwei"], 0,
    "Each gas unit costs base fee plus priority fee: 450,000 gwei = 0.00045 ETH."),
  F("Complete what happens to the base fee.", """
base fee part of the fee -> ____
priority fee part         -> validator""", ["burned", "sent to the Ethereum Foundation", "sent to the contract", "refunded"], 0,
    "Since EIP-1559 the base fee is burned."),
  X("One line about account types is wrong.", """
EOAs are controlled by private keys
contract accounts hold code and storage
only EOAs can start transactions
contract accounts can start transactions on their own""", 3, ["contracts only act when called by a transaction", "contracts have private keys", "EOAs hold bytecode"], 0,
    "Contracts react; they never start a transaction by themselves."),
  X("One line about the EVM is wrong.", """
every node runs the same transactions in the same order
the EVM charges gas for each instruction
the EVM cannot read the internet
the EVM can use real random numbers from the node's clock""", 3, ["the EVM has no access to real randomness or the node's clock", "the EVM reads random.org", "each node uses its own time"], 0,
    "Determinism means no outside randomness or clocks; contracts use oracles or special designs."),
  O("Order the costs of these operations from cheapest to most expensive.", ["Add two numbers (ADD)", "Read a storage slot that was already read in this transaction", "Write a new non-zero value to storage", "Deploy a new contract"],
    "Arithmetic costs a few gas, storage writes about 20,000, deployment far more."),
  O("Order how a contract call runs.", ["The wallet signs a call to deposit()", "A validator includes the transaction", "The EVM loads the contract code", "The EVM runs the function and charges gas", "The new state and the receipt are stored"],
    "Signed, included, executed, stored."),
],
"wallets-and-testnets": [
  F("Complete the course setting.", """
real money in the course wallet = ____""", ["0", "0.05 ETH", "as little as possible", "only for gas"], 0,
    "The course wallet never holds real money."),
  F("Complete what EIP-7702 (Pectra, May 2025) lets a normal account do.", """
EOA can temporarily act as a ____""", ["smart account (batch calls, spending rules, sponsored gas)", "validator", "mining pool", "bridge"], 0,
    "EIP-7702 lets an EOA use smart-account features."),
  X("One line about wallets is wrong.", """
a wallet holds keys, not coins
a hardware wallet signs inside a separate device
a custodial exchange wallet means the exchange holds the keys
a browser wallet is as safe as a hardware wallet for real money""", 3, ["a browser wallet is more exposed to malware", "a browser wallet cannot sign", "a hardware wallet holds coins"], 0,
    "Keys on a general-purpose computer face more risks."),
  X("One line about testnets is wrong.", """
Sepolia is the standard testnet for applications
Hoodi is used for validator and staking tests
test ETH comes from faucets
test ETH can be sold for euros""", 3, ["test ETH has no value", "test ETH becomes real after a year", "test ETH is only for validators"], 0,
    "Offers to buy or sell test ETH are scams."),
  O("Order a safe wallet setup for the course.", ["Install MetaMask from the official site", "Create a new wallet just for the course", "Write the recovery phrase on paper", "Switch to the Sepolia network", "Get test ETH from a faucet"],
    "Install, create, back up, then use the testnet."),
  O("Order what you see when you send 0.001 SepoliaETH.", ["MetaMask shows the amount and the fee", "You confirm", "The transaction is pending", "It appears in a block", "Etherscan shows Success"],
    "Confirm, pending, included, visible."),
],
"nodes-and-providers": [
  F("Complete the two programs of an Ethereum node.", """
execution client: runs transactions (e.g. Geth)
consensus client: follows Proof of Stake (e.g. ____)""", ["Lighthouse", "MetaMask", "Etherscan", "Remix"], 0,
    "Lighthouse, Prysm, Teku, Nimbus, Lodestar and Grandine are consensus clients."),
  F("Complete the JSON-RPC method that sends a signed transaction.", """
provider.call("____", [signedTxHex])""", ["eth_sendRawTransaction", "eth_getBalance", "eth_call", "eth_blockNumber"], 0,
    "eth_sendRawTransaction forwards already-signed bytes."),
  X("One line about client diversity is wrong.", """
several clients implement the same protocol
a bug in one client should not affect most validators
no client should have more than one third of validators
it is safest if everyone runs the most popular client""", 3, ["it is safest if validators spread across clients", "client choice does not matter", "only one client exists"], 0,
    "A majority client bug could split the chain or stop finality."),
  X("One line about RPC providers is wrong.", """
providers answer read requests for many apps
they can see which addresses you look up
they could delay or refuse to forward a transaction
they can change your signed transaction without anyone noticing""", 3, ["a change would break the signature", "they can spend from your account", "they hold your key"], 0,
    "Signed data cannot be altered without invalidating the signature."),
  O("Order a balance lookup in MetaMask.", ["MetaMask sends eth_getBalance to the provider", "The provider's node reads the account in its state", "The node returns the balance in wei", "MetaMask converts wei to ETH", "MetaMask shows the balance"],
    "Request, lookup, answer in wei, convert, show."),
  O("Order from least to most trust in someone else's node.", ["Run your own full node", "Run a light client that checks proofs", "Use two independent RPC providers and compare", "Use one RPC provider"],
    "The more you verify yourself, the less you trust others."),
],
"lab-remix-tour": [
  F("Complete the Remix panel order you use in every code lab.", """
File explorer -> Solidity compiler -> ____""", ["Deploy & run transactions", "Plugin manager", "Settings", "Git"], 0,
    "Write, compile, then deploy and run."),
  F("Complete the unit setting for sending 1 ether in Remix.", """
Value: 1   Unit: ____""", ["Ether", "Wei", "Gwei", "Finney"], 0,
    "With Wei selected, 1 would be 10^-18 ether."),
  X("One Remix setting is wrong for deploying the Escrow without paying.", """
Environment: Remix VM
Account: account 1
Value: 1 Ether
Contract: Escrow""", 2, ["Value: 0", "Value: 100 Ether", "Value: 1 Wei"], 0,
    "The constructor is not payable. A deploy with value reverts."),
  X("One reading of the Remix terminal is wrong.", """
a green check means the transaction succeeded
a red cross means it reverted
the line shows from, to and value
the terminal shows your recovery phrase""", 3, ["the terminal never shows secrets", "the terminal shows other students' keys", "the terminal shows the compiler licence"], 0,
    "The terminal shows transactions and logs, never secrets."),
  O("Order the Remix tour.", ["Open remix.ethereum.org", "Create a .sol file", "Compile it", "Deploy it on the Remix VM", "Click a function and read the terminal"],
    "Open, write, compile, deploy, interact."),
  O("Order how to read one transaction in the Remix terminal.", ["Find the line with the green check", "Click it to expand", "Read status and gas used", "Read the decoded input", "Read the logs (events)"],
    "Status first, then input and events."),
],
"lab-simple-storage": [
  F("Complete SimpleStorage so the default value is visible right after deploy.", """
uint256 public storedValue; // starts as ____""", ["0", "1", "undefined", "the deployer's address"], 0,
    "Unset storage variables default to zero."),
  F("Complete the difference between a call and a transaction in Remix.", """
get()  -> blue button, ____
set(42)-> orange button, transaction, costs gas""", ["call, free, no state change", "transaction, costs gas", "deploys a new contract", "sends ETH"], 0,
    "View functions are read with a free call."),
  X("One line in SimpleStorage is wrong: the event must record the writer.", """
event ValueChanged(address indexed writer, uint256 newValue);
function set(uint256 newValue) external {
    storedValue = newValue;
    emit ValueChanged(address(this), newValue);
}""", 3, ["    emit ValueChanged(msg.sender, newValue);", "    emit ValueChanged(tx.origin, 0);", "    return;"], 0,
    "A wrong pointer: address(this) is the contract itself, not the caller."),
  X("One expectation is wrong after set(42) from account 2.", """
get() returns 42
lastWriter() returns account 2
the terminal shows a ValueChanged event
account 2's balance is unchanged""", 3, ["account 2's balance is slightly lower (gas)", "account 2 gained 42 ETH", "account 2 is deleted"], 0,
    "Transactions cost gas, even in the Remix VM."),
  O("Order the read-write-read check in SimpleStorage.", ["Deploy SimpleStorage", "Call get() and see 0", "Call set(42)", "Read the event in the terminal", "Call get() and see 42"],
    "Read, write, check the log, read again."),
  O("Order what happens inside set(42).", ["The transaction reaches the contract", "storedValue becomes 42", "lastWriter becomes msg.sender", "The ValueChanged event is emitted", "The receipt is stored"],
    "State changes, then the log, then the receipt."),
],
}
