# Second and third fill / fix / order items per unit: modules 4-7.
from quiz_types_a import F, X, O

ITEMS = {
"what-smart-contracts-are": [
  F("Complete the refund clause of the Escrow as a rule.", """
action: refund()
who:    ____
when:   AwaitingDelivery
effect: price back to buyer, state = Refunded""", ["arbiter only", "seller only", "anyone", "buyer or seller"], 0,
    "In the course Escrow only the arbiter can refund."),
  F("Complete what happens when a condition fails.", """
require(condition, "message")
if condition is false: ____""", ["the whole transaction reverts and nothing changes", "the function skips that line", "the contract deletes itself", "the money goes to the miner"], 0,
    "A revert undoes every change of the transaction; gas used is still paid."),
  X("One line about smart contracts is wrong.", """
a contract is a program at an address
it runs exactly as written
it can hold and send ETH
it runs on a timer without any transaction""", 3, ["nothing runs until someone sends a transaction", "it runs every block by itself", "it runs when the price changes"], 0,
    "Contracts have no timers; someone must call them."),
  X("One rule in this clause-to-code table is wrong.", """
deposit(): buyer, AwaitingPayment, exact price
confirmDelivery(): buyer or arbiter, AwaitingDelivery
refund(): arbiter, AwaitingDelivery
confirmDelivery(): seller, AwaitingPayment""", 3, ["delete it: the seller can never release", "seller in any state", "anyone in Complete"], 0,
    "The seller confirming delivery would defeat the escrow."),
  O("Order the Escrow states in a successful sale.", ["AwaitingPayment", "AwaitingDelivery", "Complete"],
    "Pay in, wait, release."),
  O("Order how to turn a clause into code.", ["Write the clause in plain language", "Name who may act", "Name the state in which the action is allowed", "Name what happens to the money", "Write the function with require checks"],
    "Who, when, what, then code."),
],
"solidity-for-programmers": [
  F("Complete the unit so that price is one ether.", """
uint256 public price = 1 ____;""", ["ether", "wei", "gwei", "eth()"], 0,
    "1 ether = 10^18 wei. Writing 1 alone means 1 wei."),
  F("Complete the function type that only reads state.", """
function getState() external ____ returns (State) { return state; }""", ["view", "payable", "pure", "virtual"], 0,
    "view reads state without changing it; pure reads nothing."),
  X("One line in this modifier is wrong.", """
modifier onlyOwner() {
    require(msg.sender == owner, "Only owner");
}""", 2, ["    _;\n}", "    return;\n}", "    revert();\n}"], 0,
    "A modifier must contain _; where the function body runs. Without it the function body never executes."),
  X("One line breaks the privacy assumption.", """
uint256 private secretBid;   // students think: nobody can read this
function bid(uint256 v) external { secretBid = v; }
// comment: private means hidden from the public
// comment: use commit-reveal to hide bids""", 2, ["// comment: private only hides it from other contracts; anyone can read storage", "// comment: private encrypts the value", "// comment: private deletes the value after a block"], 0,
    "All storage is public on chain. private only limits access from other contracts."),
  O("Order the parts of a function declaration.", ["function", "name and parameters", "visibility (external)", "state mutability (payable)", "returns (...) if any", "body in braces"],
    "For example: function deposit() external payable { … }."),
  O("Order what happens when a modifier is used.", ["The function is called", "The modifier's checks run", "At _; the function body runs", "Code after _; in the modifier runs", "The transaction finishes"],
    "Modifiers wrap the body."),
],
"lab-escrow": [
  F("Complete the Escrow constructor so the deployer becomes the buyer.", """
constructor(address _seller, address _arbiter, uint256 _price) {
    buyer = ____;
    seller = _seller; arbiter = _arbiter; price = _price;
}""", ["msg.sender", "_seller", "tx.origin", "address(this)"], 0,
    "The account that deploys is msg.sender in the constructor."),
  F("Complete refund() so it is only possible while money is held.", """
function refund() external inState(____) {
    require(msg.sender == arbiter, "Only arbiter");
    ...""", ["State.AwaitingDelivery", "State.AwaitingPayment", "State.Complete", "State.Refunded"], 0,
    "Money is held only in AwaitingDelivery."),
  X("This confirmDelivery has one wrong line. Find it.", """
function confirmDelivery() external inState(State.AwaitingDelivery) {
    require(msg.sender == buyer || msg.sender == arbiter, "Only buyer or arbiter");
    state = State.Complete;
    (bool ok, ) = payable(buyer).call{value: price}("");
    require(ok, "Transfer failed");
}""", 3, ["    (bool ok, ) = payable(seller).call{value: price}(\"\");", "    (bool ok, ) = payable(arbiter).call{value: price}(\"\");", "    (bool ok, ) = payable(msg.sender).call{value: 0}(\"\");"], 0,
    "A wrong pointer: on release the money goes to the seller, not back to the buyer."),
  X("One step in this Remix test is wrong.", """
account 1 deploys with seller, arbiter, price and Value 0
account 1 calls deposit with Value = price
account 2 (seller) calls confirmDelivery and it succeeds
account 3 (arbiter) calls refund in a new instance and it succeeds""", 2, ["account 2 calls confirmDelivery and sees “Only buyer or arbiter”", "account 2 calls deposit", "account 2 deploys a new Escrow"], 0,
    "The seller can never release the payment."),
  O("Order the refund path in Remix.", ["Deploy a new Escrow as account 1", "Account 1 deposits the exact price", "Account 2 tries refund and sees the revert", "Account 3 (arbiter) calls refund", "state() returns Refunded and the buyer's balance went up"],
    "Only the arbiter can refund while money is held."),
  O("Order what happens inside a successful confirmDelivery().", ["Check the state is AwaitingDelivery", "Check the caller is buyer or arbiter", "Set state to Complete", "Send the price to the seller", "Emit the event"],
    "Checks, effects, interactions, log."),
],
"lab-rental-deposit": [
  F("Complete claimAfterTimeout() so the tenant can recover the deposit.", """
function claimAfterTimeout() external {
    require(msg.sender == tenant, "Only tenant");
    require(paid && !settled, "Nothing to claim");
    require(block.timestamp >= leaseEnd + ____, "Too early");
    ...""", ["30 days", "0", "1 hours", "365 days"], 0,
    "The tenant can claim if the landlord stays silent for 30 days after the lease ends."),
  F("Complete the payout of a settlement with damage.", """
landlordShare = damageAmount
tenantShare   = ____""", ["depositAmount - damageAmount", "damageAmount", "depositAmount", "0"], 0,
    "The tenant gets back what is left after the damage claim."),
  X("One line in payDeposit is wrong.", """
function payDeposit() external payable {
    require(msg.sender == landlord, "Only tenant");
    require(!paid, "Already paid");
    require(msg.value == depositAmount, "Wrong amount");
    paid = true;
}""", 1, ['    require(msg.sender == tenant, "Only tenant");', '    require(msg.sender != tenant, "Only tenant");', '    require(msg.value == 0, "Only tenant");'], 0,
    "The tenant pays the deposit; the condition must match the message."),
  X("One line breaks the settlement rule.", """
function settle(uint256 damageAmount) external {
    require(msg.sender == landlord, "Only landlord");
    require(block.timestamp >= leaseEnd, "Lease not ended");
    require(damageAmount <= depositAmount, "Damage too high");
    _payOut(damageAmount);
    settled = true;
}""", 4, ["    settled = true; (moved above _payOut)", "    delete this line", "    _payOut(depositAmount);"], 0,
    "Set settled before paying out (checks, effects, interactions), so a re-entering call cannot settle twice."),
  O("Order the RentalDeposit lab with damage.", ["Landlord deploys with tenant, amount and 0 lease days", "Tenant pays the deposit", "Landlord settles with a damage amount", "The contract pays damage to the landlord", "The rest goes back to the tenant"],
    "Deploy, pay, settle, split."),
  O("Order the legal analysis of the RentalDeposit.", ["Read §551 BGB on residential deposits", "Compare the cap with depositAmount", "Check who decides the damage in the code", "Check the unfair-terms rule (§307 BGB)", "Propose a code or clause change"],
    "Rule, comparison, power, fairness, fix."),
],
"lab-document-registry": [
  F("Complete verify() so it reports whether a hash exists.", """
function verify(bytes32 docHash) external view returns (bool exists, address owner, uint256 timestamp) {
    Record memory r = records[docHash];
    return (____, r.owner, r.timestamp);
}""", ["r.timestamp != 0", "r.timestamp == 0", "r.owner == msg.sender", "true"], 0,
    "A registered record has a non-zero timestamp."),
  F("Complete what the registry stores per document.", """
records[hash] = Record(____, block.timestamp)""", ["msg.sender", "the document text", "the file name", "tx.gasprice"], 0,
    "It stores who registered the hash and when."),
  X("One line in register() is wrong.", """
function register(bytes32 docHash) external {
    require(records[docHash].timestamp == 0, "Already registered");
    records[docHash] = Record(msg.sender, 0);
    emit DocumentRegistered(docHash, msg.sender, block.timestamp);
}""", 2, ["    records[docHash] = Record(msg.sender, block.timestamp);", "    records[docHash] = Record(address(0), 0);", "    delete records[docHash];"], 0,
    "Storing 0 as the time would allow re-registration and lose the proof of existence."),
  X("One step in the evidence chain is wrong.", """
the party keeps the original file
anyone recomputes the hash from the file
verify(hash) returns exists, owner and time
the registry proves who wrote the document""", 3, ["it proves this exact file existed at that time, not who wrote it", "it proves the content is true", "it proves both parties signed"], 0,
    "Authorship and agreement need signatures or other evidence."),
  O("Order the DocumentRegistry lab.", ["Deploy the registry", "Call hashText with your text", "Register the returned hash", "Call verify with the same hash", "Change one letter, hash again, and verify: not found"],
    "Hash, register, verify, then show tampering fails."),
  O("Order the privacy-safe design for registering a lease.", ["Keep the lease PDF in the landlord's archive", "Compute its hash locally", "Register only the hash on chain", "Share the PDF only with the parties and a court if needed"],
    "Personal data stays off chain; the hash proves integrity."),
],
"token-standards": [
  F("Complete the ERC-20 function a DEX uses to pull your tokens.", """
token.____(you, pool, amount)""", ["transferFrom", "transfer", "approve", "mint"], 0,
    "After approve, the spender calls transferFrom."),
  F("Complete the ERC-721 function that returns a certificate's holder.", """
holder = cert.____(tokenId)""", ["ownerOf", "balanceOf", "totalSupply", "allowance"], 0,
    "ownerOf returns the owner of one unique token."),
  X("One line about approvals is wrong.", """
approve sets how much a spender may move
transferFrom lowers the allowance
an unlimited approval is a risk if the spender is hacked
approvals expire automatically after one day""", 3, ["approvals stay until you set them to zero", "approvals expire after one block", "approvals are only for NFTs"], 0,
    "Revoke old approvals; they do not expire."),
  X("One line about token units is wrong.", """
CourseToken uses 18 decimals
1 CRS is stored as 10**18 units
balanceOf returns the raw number of units
transfer(to, 5) sends 5 whole CRS""", 3, ["transfer(to, 5) sends 5 units, 0.000000000000000005 CRS", "transfer(to, 5) sends 5 ETH", "transfer(to, 5) fails"], 0,
    "Amounts are raw integers; multiply by 10**decimals."),
  O("Order a token payment to a shop contract.", ["Check your token balance", "Approve the shop for the price", "Call the shop's buy function", "The shop calls transferFrom", "Balances and allowance update"],
    "Approve before the shop can pull."),
  O("Order from most to least fungible.", ["ERC-20 token (every unit equal)", "ERC-1155 edition with 100 copies", "ERC-721 certificate (one of a kind)"],
    "Identical units, limited copies, unique items."),
],
"lab-course-token": [
  F("Complete CourseToken's parent contracts.", """
contract CourseToken is ERC20, ____ {""", ["Ownable", "ERC721", "ReentrancyGuard", "Pausable only"], 0,
    "Ownable gives the onlyOwner modifier used by mint."),
  F("Complete the call that lets account 2 spend 10 CRS of account 1.", """
// as account 1
approve(account2, ____)""", ["10 * 10**18", "10", "10 ether ether", "0"], 0,
    "With 18 decimals, 10 CRS is 10 × 10^18 units."),
  X("One line in this mint is unsafe.", """
function mint(address to, uint256 amount) external {
    _mint(to, amount);
}
// comment: anyone can create tokens""", 0, ["function mint(address to, uint256 amount) external onlyOwner {", "function mint(address to, uint256 amount) internal view {", "function mint(address to) external {"], 0,
    "Without onlyOwner anyone can inflate the supply."),
  X("One expected result is wrong.", """
after deploy, balanceOf(owner) = 1000 * 10**18
after transfer of 100 CRS, owner has 900 CRS
account 2 calls mint and it reverts
totalSupply drops when tokens are transferred""", 3, ["totalSupply stays the same on transfers", "totalSupply doubles", "totalSupply becomes 0"], 0,
    "Transfers move tokens; only mint and burn change the supply."),
  O("Order the allowance part of the CourseToken lab.", ["Account 1 approves account 2 for 10 CRS", "Read allowance(account1, account2)", "Account 2 calls transferFrom(account1, account3, 10 CRS)", "Read the three balances", "Read the allowance again: 0"],
    "Approve, check, spend, verify."),
  O("Order the parts of the CourseToken file.", ["SPDX licence line", "pragma solidity", "import OpenZeppelin ERC20 and Ownable", "contract CourseToken is ERC20, Ownable", "constructor that mints the start supply", "mint function with onlyOwner"],
    "Header, imports, contract, constructor, functions."),
],
"lab-openzeppelin-wizard": [
  F("Complete the Wizard choice for a certificate that the university can withdraw.", """
Standard: ERC721
Features: Mintable, ____""", ["Burnable by the owner only (custom rule)", "Votes", "Flash minting", "Permit"], 0,
    "Withdrawing a certificate means burning it; who may burn is a design and legal choice."),
  F("Complete the safeMint call in Remix.", """
safeMint(to = student address, uri = ____)""", ["a short text or an IPFS link to the metadata", "the private key", "the token price", "0x0"], 0,
    "The URI points to the certificate's metadata."),
  X("One Wizard setting conflicts with the design goal: only the university issues certificates.", """
Name: Course Certificate
Symbol: CERT
Mintable: yes
Access control: none""", 3, ["Access control: Ownable (university)", "Access control: anyone", "Symbol: none"], 0,
    "Without access control anyone can mint."),
  X("One expected result after safeMint is wrong.", """
a Transfer event from the zero address
ownerOf(0) returns the student's address
balanceOf(student) returns 1
ownerOf(0) returns the university's address""", 3, ["ownerOf(0) returns the student", "ownerOf(0) returns 0x0", "ownerOf(0) reverts"], 0,
    "The certificate belongs to the student who received it."),
  O("Order the Wizard lab from configuration to first certificate.", ["Choose ERC721 in the Wizard", "Set name, symbol and features", "Open the code in Remix", "Deploy with your address as initialOwner", "Mint a certificate to a teammate"],
    "Configure, open, deploy, mint."),
  O("Order the check of a minted certificate.", ["Copy the transaction from the terminal", "Read the Transfer event", "Call ownerOf(tokenId)", "Call tokenURI(tokenId)"],
    "Event, owner, metadata."),
],
"lab-thirdweb": [
  F("Complete the thirdweb concept: an item that exists but nobody owns yet.", """
NFTs tab -> Create -> token 0, supply ____""", ["0 (lazy minted)", "1", "100", "unlimited"], 0,
    "Lazy minting creates the template; tokens appear when people claim."),
  F("Complete the claim phase for a free workshop ticket.", """
price = 0
max per wallet = 1
start = ____""", ["now", "never", "after the workshop", "block 0"], 0,
    "The phase must have started for claims to work."),
  X("One line about thirdweb's Edition Drop is wrong.", """
it is an ERC-1155 contract
each token ID is one item with many copies
claim phases set price, limits and timing
each holder gets a different unique token ID""", 3, ["holders of the same item share one token ID", "every claim deploys a new contract", "token IDs are random"], 0,
    "ERC-1155 copies share an ID; ERC-721 tokens are unique."),
  X("One step is wrong for the course.", """
sign in with the course wallet
deploy on Sepolia
set the primary sale recipient to your address
pay the platform fee in real ETH""", 3, ["no real money: free claims on Sepolia", "pay in test USDC from an exchange", "ask the professor for ETH"], 0,
    "Everything stays on the testnet."),
  O("Order the thirdweb lab.", ["Sign in and open your project", "Deploy an Edition Drop on Sepolia", "Create token 0 in the NFTs tab", "Add the initial claim phase", "Claim from a second account and check the balance"],
    "Deploy, create, set rules, claim."),
  O("Order the comparison with the Wizard contract.", ["Open the thirdweb contract on Etherscan", "Count the thirdweb contract's functions", "Open your Wizard contract", "Count the Wizard contract's functions", "Write which one is easier to audit and why"],
    "Compare the size and readability of both."),
],
"toolchain": [
  F("Complete the Foundry tool for talking to a chain from the command line.", """
$ ____ call <address> "price()(uint256)" --rpc-url $SEPOLIA""", ["cast", "forge", "anvil", "chisel only"], 0,
    "cast sends calls and transactions; forge builds and tests; anvil runs a local chain."),
  F("Complete the step that lets users read deployed code.", """
deploy -> ____ on Etherscan -> users read the source""", ["verify", "pin", "burn", "mint"], 0,
    "Verification matches source and bytecode."),
  X("One line in this team workflow is unsafe.", """
work on a Git branch
run forge test before each push
open a pull request for review
commit the deployer's private key in .env to GitHub""", 3, ["keep keys in an encrypted keystore, never in Git", "commit the key in a private repo", "paste the key in the README"], 0,
    "Leaked keys are drained within minutes."),
  X("One tool is matched to the wrong job.", """
forge: compile and test
anvil: run a local chain
cast: send calls and transactions
Etherscan: run unit tests for your contract""", 3, ["Etherscan: explore and verify deployed contracts", "Etherscan: compile Rust", "Etherscan: host your front end"], 0,
    "Etherscan is an explorer."),
  O("Order a change from idea to testnet.", ["Create a branch", "Change the code and tests", "Run the tests locally", "Get a review and merge", "Deploy and verify on Sepolia with a script"],
    "Branch, change, test, review, deploy."),
  O("Order the tools from most beginner-friendly to most professional for a team.", ["Remix in the browser", "Remix with GitHub sync", "Foundry or Hardhat project with Git", "Framework plus CI, static analysis and scripted deployment"],
    "Each step adds repeatability and review."),
],
"testing-contracts": [
  F("Complete the invariant for the Escrow.", """
invariant: address(escrow).balance == 0 || address(escrow).balance == ____""", ["price", "2 * price", "1 wei", "buyer.balance"], 0,
    "The escrow holds either nothing or exactly the price."),
  F("Complete the test type that tries hundreds of random inputs.", """
function testFuzz_Deposit(uint256 amount) public { ... }
// type: ____""", ["fuzz test", "unit test", "fork test", "manual test"], 0,
    "A parameter in the test makes Foundry fuzz it."),
  X("One line in this test is wrong.", """
function test_ArbiterRefunds() public {
    vm.prank(buyer); escrow.deposit{value: 1 ether}();
    vm.prank(seller); escrow.refund();
    assertEq(uint(escrow.state()), uint(Escrow.State.Refunded));
}""", 2, ["    vm.prank(arbiter); escrow.refund();", "    vm.prank(buyer); escrow.refund();", "    escrow.refund{value: 1 ether}();"], 0,
    "Only the arbiter can refund; as the seller the call reverts and the test fails."),
  X("One claim about testing is wrong.", """
happy paths check that normal use works
failure tests check forbidden actions revert
invariants check rules after any sequence
100% line coverage proves the contract is correct""", 3, ["coverage shows which lines ran, not that rules are right", "coverage proves gas is low", "coverage replaces audits"], 0,
    "Coverage is a hint, not a proof."),
  O("Order the derivation of tests from a clause.", ["Read the clause", "Mark each “only”, “after” and “at most”", "Write one happy-path test", "Write one failure test per condition", "Write one invariant for the money"],
    "From legal words to tests."),
  O("Order the four test techniques from narrowest to broadest.", ["Unit test with chosen inputs", "Fuzz test with random inputs for one function", "Invariant test with random sequences of calls"],
    "Each step covers more of the real world."),
],
"lab-foundry-test": [
  F("Complete the Foundry cheat code that sets the next caller.", """
vm.____(buyer);
escrow.deposit{value: 1 ether}();""", ["prank", "warp", "deal", "roll"], 0,
    "prank sets msg.sender for the next call; warp changes time; deal sets balances."),
  F("Complete the test setup that gives the buyer ETH.", """
function setUp() public {
    escrow = new Escrow(seller, arbiter, 1 ether);
    vm.____(buyer, 10 ether);
}""", ["deal", "prank", "expectRevert", "label"], 0,
    "deal sets an address's balance in the test."),
  X("One line in this revert test is wrong.", """
function test_SellerCannotConfirm() public {
    vm.prank(buyer); escrow.deposit{value: 1 ether}();
    escrow.confirmDelivery();
    vm.expectRevert("Only buyer or arbiter");
}""", 2, ["    vm.expectRevert(\"Only buyer or arbiter\"); vm.prank(seller); escrow.confirmDelivery();", "    vm.prank(arbiter); escrow.confirmDelivery();", "    delete this line"], 0,
    "expectRevert must come before the call, and the call must be made as the seller."),
  X("One expectation about forge test output is wrong.", """
[PASS] lines for passing tests
[FAIL] lines with the reason for failures
a gas number for each test
[PASS] means the contract is audited""", 3, ["[PASS] means only that this test's assertions held", "[PASS] means it is deployed", "[PASS] means it has no bugs"], 0,
    "Tests check what you wrote, nothing more."),
  O("Order a Foundry revert test.", ["Deposit as the buyer", "Set the caller to the seller and expect the revert message", "Call confirmDelivery", "Run forge test and see [PASS]"],
    "Set up, expect, act, run."),
  O("Order the Foundry lab setup.", ["Install with foundryup", "forge init the project", "Remove the Counter samples", "Copy the Escrow into src/", "forge build"],
    "Install, init, clean, add, build."),
],
"security-basics": [
  F("Complete the defence against reentrancy with a library.", """
contract Bank is ____ {
    function withdraw() external nonReentrant { ... }
}""", ["ReentrancyGuard", "Ownable", "ERC20", "Pausable"], 0,
    "OpenZeppelin's ReentrancyGuard provides the nonReentrant modifier."),
  F("Complete the order rule.", """
checks -> effects -> ____""", ["interactions", "events", "approvals", "audits"], 0,
    "Call other contracts last, after your own state is updated."),
  X("One line in this withdraw is in the wrong order.", """
function withdraw() external {
    uint256 a = balances[msg.sender];
    require(a > 0, "No balance");
    (bool ok, ) = msg.sender.call{value: a}("");
    balances[msg.sender] = 0;
    require(ok, "Failed");
}""", 3, ["move the balance update above the call", "remove the require", "send a + 1"], 0,
    "Sending before updating lets the receiver re-enter."),
  X("One defence is matched to the wrong bug.", """
reentrancy: checks-effects-interactions
missing access control: onlyOwner or roles
tx.origin authentication: use msg.sender
oracle manipulation: use tx.origin""", 3, ["oracle manipulation: decentralised feeds and sanity checks", "oracle manipulation: remove events", "oracle manipulation: more gas"], 0,
    "Price manipulation needs robust oracles."),
  O("Order checks-effects-interactions in a payout.", ["Check the caller and the state", "Check the amount", "Update the state and balances", "Send the money", "Emit the event"],
    "State first, money last."),
  O("Order the 2016 DAO incident.", ["The DAO holds a large ETH balance", "The attacker calls the split function", "The contract sends ETH before updating the balance", "The attacker's code calls back again", "About a third of the funds are drained"],
    "The classic reentrancy pattern."),
],
"security-in-practice": [
  F("Complete what Bybit's signers should have checked in February 2025.", """
check on an independent device:
    target address, value and ____""", ["the call type and data (e.g. a delegatecall that changes the wallet)", "the colour of the website", "the gas price only", "the block number"], 0,
    "The attack changed the call type, not the visible receiver."),
  F("Complete the 2025 figure (Chainalysis).", """
stolen in 2025 ≈ $3.4 billion
largest single incident ≈ ____""", ["Bybit, about $1.5 billion", "GMX, about $42 million", "The DAO", "Ronin"], 0,
    "Bybit was about 44% of the year's total."),
  X("One line in this treasury policy is weak.", """
3-of-5 multisig with hardware wallets
signers verify the decoded transaction independently
admin actions wait in a 48-hour timelock
all signers use the same laptop to save time""", 3, ["each signer uses a separate device", "one signer approves for all", "skip the timelock"], 0,
    "Shared devices create a single point of failure."),
  X("One reading of the 2025 numbers is wrong.", """
about $3.4 billion was stolen in 2025
North Korea-linked hackers took at least $2.02 billion
many losses came from keys and operations
most losses came from simple reentrancy bugs""", 3, ["operational attacks caused most losses", "no losses came from code", "losses fell to zero"], 0,
    "Code bugs matter, but operations dominated in 2025."),
  O("Order the Bybit attack chain (2025).", ["Attackers compromise a developer machine of the wallet provider", "They inject code into the signing website", "Signers see a normal transfer", "Signers approve a hidden change to the wallet", "Attackers drain the cold wallet"],
    "A supply-chain and interface attack, not a contract bug."),
  O("Order how a signer checks a multisig payment safely.", ["Receive the proposed transaction", "Decode it on an independent device", "Compare target, value and call type with the request", "Sign on the hardware wallet", "Wait for the other signers before execution"],
    "Independent checking is the step Bybit's signers lacked."),
],
"audits-and-analysis": [
  F("Complete the tool category.", """
Slither, Aderyn -> ____ analysis (fast pattern scans)""", ["static", "dynamic", "manual", "economic"], 0,
    "Static analysers read the code without running it."),
  F("Complete the audit finding.", """
Title: Owner can drain user deposits
Severity: ____
Fix: remove the function or put it behind a timelock""", ["High or Critical", "Informational", "Gas", "Low"], 0,
    "Loss of user funds is high or critical."),
  X("One line in this audit process is wrong.", """
freeze the code version to audit
auditors review and report findings
the team fixes and the auditors re-check the fixes
the team adds new features after the audit and deploys them unreviewed""", 3, ["new code needs a new review", "new features need no tests", "the audit covers future code"], 0,
    "An audit covers one version."),
  X("One claim about AI tools is wrong (2025 research).", """
LLMs help explain code
LLMs can propose vulnerability hypotheses
hybrids of LLMs and classic tools work best
LLMs alone reliably replace Slither and auditors""", 3, ["LLMs are not yet reliable enough alone; confirm with tests", "LLMs cannot read Solidity", "LLMs are banned in audits"], 0,
    "Every AI finding needs confirmation."),
  O("Order a security programme for a launch.", ["Internal tests and static analysis", "External audit", "Fix findings and re-review", "Launch with caps and a pause switch", "Raise the caps after weeks without incidents"],
    "Layers of defence before and after launch."),
  O("Order the parts of an audit finding.", ["Title", "Severity", "Description and impact", "Recommended fix", "Team response"],
    "What, how bad, why, how to fix, what was done."),
],
"lab-reentrancy": [
  F("Complete the Attacker's receive() so it re-enters while the bank has money.", """
receive() external payable {
    if (address(bank).balance >= ____) {
        bank.withdraw();
    }
}""", ["1 ether", "0", "address(this).balance", "type(uint256).max"], 0,
    "It keeps withdrawing 1 ether while the bank can still pay it."),
  F("Complete the attack start.", """
function attack() external payable {
    bank.deposit{value: 1 ether}();
    bank.____();
}""", ["withdraw", "deposit", "transfer", "selfdestruct"], 0,
    "Deposit once, then withdraw to start the loop."),
  X("One line in FixedBank is still wrong.", """
function withdraw() external {
    uint256 amount = balances[msg.sender];
    require(amount > 0, "No balance");
    (bool ok, ) = msg.sender.call{value: amount}("");
    balances[msg.sender] = 0;
    require(ok, "Transfer failed");
}""", 4, ["move it above the call", "change it to balances[msg.sender] = amount;", "delete it"], 0,
    "This is still the vulnerable order. The update must come before the call."),
  X("One expected result after attacking FixedBank is wrong.", """
the attack transaction reverts or withdraws only 1 ether
the bank still holds the other users' 5 ether
the attacker's balance in the bank becomes 0
the attacker drains all 6 ether""", 3, ["the attacker cannot take more than its own deposit", "the bank pays double", "the bank is deleted"], 0,
    "The fix stops the loop."),
  O("Order the reentrancy lab.", ["Deploy VulnerableBank", "Other users deposit 5 ether", "Deploy Attacker with the bank's address", "Call attack with 1 ether", "See the bank drained"],
    "Set up victims first, then attack."),
  O("Order the second half of the lab.", ["Deploy FixedBank", "Account 2 deposits 5 ether", "Deploy a new Attacker for FixedBank", "Call attack with 1 ether", "See the attack fail and the 5 ether stay"],
    "Same attack, fixed order, no loss."),
],
"lab-phalcon": [
  F("Complete what the Balance Changes view shows.", """
Balance Changes: for each address, ____""", ["tokens and ETH gained or lost in the transaction", "its private key", "its total history", "its gas price"], 0,
    "It summarises who won and lost in that one transaction."),
  F("Complete the GMX V1 case (9 July 2025).", """
guard on one contract, attacker re-entered ____""", ["a different contract (the Vault) during a callback", "the same function only", "Bitcoin", "the oracle network"], 0,
    "Cross-contract reentrancy bypassed a single-contract guard."),
  X("One reading of a Phalcon trace is wrong.", """
indentation shows calls inside calls
a callback to the attacker shows as a nested call
the fund flow shows value moving between addresses
the gas profiler shows who owns the stolen funds""", 3, ["the gas profiler shows where gas was spent", "the gas profiler shows private keys", "the gas profiler shows the attacker's name"], 0,
    "Ownership changes are in balance changes and fund flow."),
  X("One step of the lab is in the wrong place.", """
find the attack transaction hash
open it in Phalcon
write the root cause in one sentence
read the invocation flow""", 2, ["read the invocation and fund flow before writing the root cause", "skip the invocation flow", "write the root cause before finding the hash"], 0,
    "Conclusions come after reading the evidence."),
  O("Order the Phalcon lab on your own transaction.", ["Copy your Sepolia confirmDelivery hash", "Open Phalcon and choose Sepolia", "Paste the hash", "Read the call tree", "Find the ETH transfer to the seller"],
    "Start with a simple case you understand."),
  O("Order the analysis of a real hack.", ["Get the attack hash from an incident library", "Open the invocation flow", "Find the callback to the attacker", "Open the fund flow", "Compare with the published root cause"],
    "Calls, then money, then the expert view."),
],
}
