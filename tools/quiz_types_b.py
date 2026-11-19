# New question types for modules 5-9.
from quiz_types_a import F, X, O

ITEMS = {
# ---------- Module 5 ----------
"token-standards": [
  F("Complete the ERC-20 transfer logic in pseudo code.", """
function transfer(to, amount):
    require(balanceOf[sender] >= amount)
    balanceOf[sender] -= amount
    ____
    emit Transfer(sender, to, amount)""", ["balanceOf[to] += amount", "balanceOf[sender] += amount", "totalSupply -= amount", "balanceOf[to] = 0"], 0,
    "A transfer moves the amount: minus for the sender, plus for the receiver. The total supply stays the same."),
  X("One line in this standards table is wrong.", """
ERC-20: fungible tokens, every unit is the same
ERC-721: non-fungible tokens, each token ID is unique
ERC-1155: many token types in one contract
ERC-721: every token has the same value and can be split""", 3, ["ERC-721: each token is unique and cannot be split", "ERC-721: only for stablecoins", "ERC-721: has no owner"], 0,
    "An ERC-721 token is unique (a certificate, a ticket) and has no decimals."),
  O("Order how an approved spender (a DEX) moves your ERC-20 tokens.", ["You call approve(dex, 100)", "allowance[you][dex] becomes 100", "The DEX calls transferFrom(you, pool, 100)", "The token checks and lowers the allowance", "The balances change and a Transfer event is emitted"],
    "Approve first, then the spender pulls with transferFrom. Unlimited approvals are a common risk."),
],
"lab-course-token": [
  F("Complete CourseToken so only the owner can create new tokens.", """
function mint(address to, uint256 amount) external ____ {
    _mint(to, amount);
}""", ["onlyOwner", "payable", "view", "public pure"], 0,
    "The Ownable modifier onlyOwner reverts for everyone except the owner."),
  X("The constructor should give the deployer 1,000 whole tokens. One line is wrong.", """
constructor() ERC20("Course Token", "CRS") Ownable(msg.sender) {
    _mint(msg.sender, 1000);
}""", 1, ["_mint(msg.sender, 1000 * 10 ** decimals());", "_mint(address(0), 1000);", "_mint(msg.sender, 1000 ether ether);"], 0,
    "A unit mistake: with 18 decimals, 1000 means 0.000000000000001 CRS. Multiply by 10 ** decimals()."),
  O("Order the CourseToken lab.", ["Deploy CourseToken in Remix", "Read balanceOf(your address)", "Call transfer to a second account", "Try mint from the second account and see the revert", "Call mint as the owner and check totalSupply"],
    "Deploy, read, transfer, test access control, then mint correctly."),
],
"lab-openzeppelin-wizard": [
  F("In the OpenZeppelin Wizard you build a certificate NFT. Complete the choice.", """
Standard: ____
Features: Mintable, Auto increment IDs
Access control: Ownable""", ["ERC721", "ERC20", "Governor", "ERC1155 with fungible supply"], 0,
    "Each certificate is unique, so it is an ERC-721 token."),
  X("One setting makes this certificate contract risky for a university.", """
Name: Course Certificate
Mintable: yes
Access control: Ownable (university wallet)
Mintable by: anyone""", 3, ["Mintable by: only the owner (the university)", "Mintable by: the student", "Mintable: no, and no access control"], 0,
    "If anyone can mint, anyone can issue fake certificates. Only the issuer should mint."),
  O("Order the Wizard lab.", ["Configure the contract in the Wizard", "Open it in Remix", "Compile and deploy it on the Remix VM", "Mint a certificate to a student address", "Read ownerOf(tokenId) to check the holder"],
    "Configure, open in Remix, deploy, mint, verify ownership."),
],
"lab-thirdweb": [
  F("Complete the claim rule for a ticket drop in thirdweb.", """
claim condition:
    price = 0
    max per wallet = ____""", ["1", "unlimited", "0", "the total supply"], 0,
    "One ticket per wallet stops a single person from claiming the whole drop."),
  X("One step in this thirdweb lab is wrong.", """
connect MetaMask on Sepolia
deploy an Edition Drop contract
set a claim condition
switch to Ethereum mainnet to airdrop the tickets""", 3, ["stay on Sepolia and airdrop with test ETH", "ask a classmate for real ETH", "skip the network check"], 0,
    "All labs stay on Sepolia. No real money is ever used."),
  O("Order the thirdweb ticket lab.", ["Sign in with the course wallet", "Deploy an Edition Drop on Sepolia", "Upload the ticket metadata", "Set the claim condition", "Claim a ticket from a second account"],
    "Deploy, add content, set rules, test as a user."),
],
# ---------- Module 6 ----------
"toolchain": [
  F("Complete the Foundry command that runs all tests.", """
$ forge ____""", ["test", "deploy", "mine", "audit"], 0,
    "forge test compiles the project and runs every test function."),
  X("One line in this tool map is wrong.", """
Remix: browser IDE for writing and deploying
Foundry: command-line testing and scripting
Hardhat: JavaScript-based development environment
Etherscan: compiles your contract locally""", 3, ["Etherscan: block explorer that shows and verifies contracts", "Etherscan: a wallet", "Etherscan: a testnet"], 0,
    "Etherscan is a block explorer. It verifies published source code against deployed bytecode."),
  O("Order a typical professional workflow.", ["Write the contract in an editor", "Write tests for each rule", "Run the tests locally", "Deploy to a testnet with a script", "Verify the source on Etherscan"],
    "Code, tests, local run, testnet deployment, verification."),
],
"testing-contracts": [
  F("Complete the test that the seller cannot release the Escrow payment.", """
function test_SellerCannotRelease() public {
    vm.prank(seller);
    vm.expectRevert("Only buyer or arbiter");
    ____
}""", ["escrow.confirmDelivery();", "escrow.deposit{value: 1 ether}();", "assertEq(escrow.price(), 1 ether);", "vm.warp(0);"], 0,
    "expectRevert must be followed by the call that should fail, made as the seller (vm.prank)."),
  X("This test should check the tenant's refund. One line is wrong.", """
vm.warp(rental.leaseEnd() + 31 days);
vm.prank(landlord);
rental.claimAfterTimeout();
assertEq(tenant.balance, depositAmount);""", 1, ["vm.prank(tenant);", "vm.prank(address(0));", "vm.warp(0);"], 0,
    "Only the tenant may call claimAfterTimeout(). As the landlord the call reverts."),
  O("Order the parts of one good test.", ["Arrange: deploy the contract and set the accounts", "Act: call the function as a chosen account", "Assert: check the state, balances or the revert", "Repeat for the failure case"],
    "Arrange, act, assert, and always test what must fail."),
],
"lab-foundry-test": [
  F("Complete the fuzz test so Foundry tries many amounts.", """
function testFuzz_Deposit(uint256 ____) public {
    vm.assume(amount > 0 && amount < 100 ether);
    bank.deposit{value: amount}();
    assertEq(bank.balances(address(this)), amount);
}""", ["amount", "1 ether", "msg.value", "block.timestamp"], 0,
    "A parameter in the test function makes it a fuzz test. Foundry fills it with many random values."),
  X("One command in this Foundry lab is wrong.", """
$ curl -L https://foundry.paradigm.xyz | bash
$ foundryup
$ forge init escrow-tests
$ forge deploy --mainnet""", 3, ["$ forge test", "$ forge mine", "$ forge sell"], 0,
    "The lab only tests locally. Nothing goes to mainnet."),
  O("Order the Foundry lab.", ["Install Foundry with foundryup", "Create a project with forge init", "Copy the Escrow contract into src/", "Write tests in test/", "Run forge test and read the results"],
    "Install, init, add the contract, write tests, run."),
],
# ---------- Module 7 ----------
"security-basics": [
  F("Complete the access-control rule for a function that changes the fee.", """
function setFee(uint256 newFee) external {
    require(____, "Not allowed");
    fee = newFee;
}""", ["msg.sender == owner", "newFee > 0", "tx.origin == msg.sender", "true"], 0,
    "Missing access control is one of the most common bugs. Any state-changing admin function needs a caller check."),
  X("One line uses the wrong sender check.", """
function withdrawAll() external {
    require(tx.origin == owner, "Only owner");
    payable(owner).transfer(address(this).balance);
}""", 1, ['require(msg.sender == owner, "Only owner");', 'require(tx.origin != owner, "Only owner");', 'require(block.coinbase == owner, "Only owner");'], 0,
    "tx.origin is the wallet that started the transaction. A malicious contract can trick the owner into calling it and then call withdrawAll. Use msg.sender."),
  O("Order checks-effects-interactions in a withdraw function.", ["Check: require that the caller has a balance", "Effect: set the caller's balance to zero", "Interaction: send the ETH", "Check that the transfer succeeded"],
    "Change your own state before calling out. This blocks reentrancy."),
],
"security-in-practice": [
  F("Complete the oracle check that blocks stale prices.", """
(price, updatedAt) = oracle.latest()
require(block.timestamp - updatedAt < ____, "Stale price")""", ["1 hours", "0", "type(uint256).max", "price"], 0,
    "A price that has not been updated for a long time can be wrong. Set a maximum age."),
  X("One step in this signing routine for a company multisig is unsafe.", """
read the transaction on a second device
check the target address and the amount
compare the hash with the other signers
sign because the interface shows the right address""", 3, ["sign only after the decoded data matches on an independent device", "sign quickly to save gas", "let one signer approve for all"], 0,
    "In the 2025 Bybit hack, the signers trusted a manipulated interface. Check the raw transaction independently."),
  O("Order the incident response when a contract is under attack.", ["Pause the contract with the pause switch", "Inform users and the team", "Analyse the attack transactions", "Fix and test the bug", "Unpause or migrate to a fixed version"],
    "Stop the damage first, communicate, then analyse and fix."),
],
"audits-and-analysis": [
  F("Complete the audit finding format.", """
Title: Reentrancy in withdraw()
Severity: ____
Impact: an attacker can drain all deposits""", ["High", "Informational", "Gas optimisation", "None"], 0,
    "Loss of all user funds is the highest severity."),
  X("One line in this audit plan is wrong.", """
read the specification and the code
run a static analyser such as Slither
write tests for each risk
an audit proves the contract has no bugs""", 3, ["an audit lowers risk but cannot prove there are no bugs", "an audit replaces testing", "an audit makes the contract upgradeable"], 0,
    "Audits reduce risk. Many hacked contracts were audited."),
  O("Order a basic security review.", ["Read the specification", "Map who can call each function", "Run static analysis", "Write attack tests", "Report findings with severity and a fix"],
    "Understand intent, map access, use tools, test attacks, report."),
],
"lab-reentrancy": [
  F("Complete FixedBank.withdraw() so it is safe against reentrancy.", """
function withdraw() external {
    uint256 amount = balances[msg.sender];
    require(amount > 0, "No balance");
    ____
    (bool ok, ) = msg.sender.call{value: amount}("");
    require(ok, "Transfer failed");
}""", ["balances[msg.sender] = 0;", "balances[msg.sender] += amount;", "amount = 0;", "require(ok);"], 0,
    "Set the balance to zero before sending (effect before interaction)."),
  X("This is VulnerableBank. Which line makes the attack possible?", """
function withdraw() external {
    uint256 amount = balances[msg.sender];
    require(amount > 0, "No balance");
    (bool ok, ) = msg.sender.call{value: amount}("");
    require(ok, "Transfer failed");
    balances[msg.sender] = 0;
}""", 5, ["move this line above the call, right after the require", "delete this line", "change it to balances[msg.sender] = amount;"], 0,
    "The balance is set to zero too late: the ETH is sent while the balance is still full. The attacker's receive() calls withdraw again and again."),
  O("Order the reentrancy attack in the lab.", ["The attacker deposits 1 ether", "The attacker calls withdraw()", "The bank sends ETH to the attacker", "The attacker's receive() calls withdraw() again", "The bank sends again because the balance is not yet zero"],
    "The loop continues until the bank is empty."),
],
"lab-phalcon": [
  F("In Phalcon, which view shows where the stolen money went?", """
open the attack transaction
switch to the ____ view""", ["Fund Flow", "Gas Profiler", "Source code", "Settings"], 0,
    "Fund Flow shows every transfer of tokens and ETH between addresses."),
  X("One reading of a hack trace is wrong.", """
Invocation flow: the order of calls between contracts
Fund flow: who sent value to whom
Balance changes: what each address gained or lost
Invocation flow: the price of ETH that day""", 3, ["Invocation flow: nested calls, including re-entered functions", "Invocation flow: the block reward", "Invocation flow: gas price"], 0,
    "The invocation flow is the call tree, where reentrancy shows as nested calls."),
  O("Order the Phalcon lab on a real hack.", ["Find the attack transaction hash", "Open it in Phalcon", "Read the invocation flow", "Read the fund flow", "Write the root cause in one sentence"],
    "Find, open, follow the calls, follow the money, explain."),
],
# ---------- Module 8 ----------
"upgrades-and-operations": [
  F("In a proxy upgrade, which contract keeps the data?", """
user --> Proxy (storage) --delegatecall--> Implementation (logic)
upgrade = change the implementation address in ____""", ["the proxy", "the implementation", "the user's wallet", "Etherscan"], 0,
    "The proxy holds the storage and forwards calls with delegatecall. An upgrade only points it to new logic."),
  X("One line in this upgrade policy is risky.", """
upgrades need a 3-of-5 multisig
every upgrade waits 48 hours in a timelock
users can exit during the timelock
one developer key can upgrade at once in an emergency""", 3, ["a pause switch for emergencies, upgrades still through the multisig", "remove the timelock", "let anyone upgrade"], 0,
    "A single key that can change everything is the main risk. Pause quickly, but upgrade only through governance."),
  O("Order a safe upgrade.", ["Write and test the new implementation", "Have it reviewed", "Propose the upgrade in the multisig", "Wait for the timelock", "Execute the upgrade and verify the new code"],
    "Test, review, propose, wait, execute."),
],
"lab-sepolia": [
  F("Complete the deploy setting for the Sepolia lab in Remix.", """
Environment: ____
Network in MetaMask: Sepolia""", ["Injected Provider - MetaMask", "Remix VM (Cancun)", "Mainnet fork", "Custom HTTP with a private key"], 0,
    "Injected Provider uses MetaMask, which signs on the Sepolia network."),
  X("One step in the verification is wrong.", """
deploy the Escrow on Sepolia
copy the contract address
open it on sepolia.etherscan.io
verify with a different compiler version than you used""", 3, ["verify with the same compiler version and settings", "verify without source code", "verify on mainnet Etherscan"], 0,
    "Verification recompiles your source. It only matches with the same compiler version and optimisation settings."),
  O("Order the Sepolia lab.", ["Get Sepolia test ETH from a faucet", "Deploy with Injected Provider", "Confirm in MetaMask", "Verify the source on Etherscan", "Call a function from the Etherscan Write tab"],
    "Fund, deploy, confirm, verify, use."),
],
"lab-tenderly": [
  F("Tenderly can test a call as another account without signing. Complete it.", """
Simulator:
    from = arbiter address
    function = refund()
    mode = ____""", ["simulate (no real transaction)", "send to mainnet", "sign with your key", "mine a block"], 0,
    "A simulation runs the call on a copy of the chain state. Nothing is sent or paid."),
  X("One reading of a Tenderly debugger is wrong.", """
the call trace lists every internal call
the source view highlights the line that ran
state changes show old and new storage values
the revert line is where the gas price was set""", 3, ["the revert line is the require that failed", "the revert line is always line 1", "the revert line is in MetaMask"], 0,
    "The debugger jumps to the failing require, with its message."),
  O("Order the Tenderly lab.", ["Add your Sepolia contract to Tenderly", "Open a failed transaction", "Find the failing line in the debugger", "Simulate the same call as the correct account", "Compare both results"],
    "Import, open, debug, simulate, compare."),
],
"lab-see-inside": [
  F("Which tool draws a class diagram of your contract?", """
$ npx ____ class ./Escrow.sol""", ["sol2uml", "forge", "metamask", "etherscan"], 0,
    "sol2uml turns Solidity into a UML class diagram."),
  X("One annotation on the Escrow diagram is wrong.", """
deposit(): only the buyer
confirmDelivery(): the buyer or the arbiter
refund(): only the arbiter
refund(): the seller""", 3, ["remove it: the seller cannot refund", "refund(): anyone", "refund(): the buyer only"], 0,
    "Only the arbiter can refund."),
  O("Order the See inside lab.", ["Open the verified contract on Etherscan", "Read its storage and events", "Generate a diagram with sol2uml", "Mark who may call each function", "Compare with the legal text"],
    "Read, visualise, annotate, compare."),
],
# ---------- Module 9 ----------
"dapp-architecture": [
  F("Complete the dApp stack.", """
browser front end --> wallet (signs) --> ____ --> smart contract""", ["an RPC node", "a central database", "an email server", "the user's bank"], 0,
    "The front end asks the wallet to sign, and an RPC node sends the transaction to the network."),
  X("One line about dApps is wrong.", """
the contract logic runs on chain
the front end is often a normal website
the website can be changed or blocked
the website is as trustless as the contract""", 3, ["the website is a weak point and can be attacked", "the website is on chain by default", "the website signs for the user"], 0,
    "A hacked front end can show the wrong transaction. That is why wallets show what you sign."),
  O("Order what happens when a user clicks Buy in a dApp.", ["The front end reads the price from the contract", "It builds the transaction", "The wallet asks the user to confirm", "The transaction is sent and mined", "The front end reads the event and updates"],
    "Read, build, sign, include, update."),
],
"oracles": [
  F("Complete the insurance logic that needs outside data.", """
rain = ____.rainfall(city, date)
if rain > threshold:
    pay(farmer)""", ["oracle", "msg.sender", "block.timestamp", "tx.origin"], 0,
    "Contracts cannot see the outside world. An oracle brings in the data."),
  X("One line makes this oracle design fragile.", """
use several independent data sources
take the median value
reject values older than one hour
trust one price from one exchange in the same block""", 3, ["use a decentralised feed or a time-weighted average", "use the highest price", "use no price at all"], 0,
    "A single spot price can be manipulated with a flash loan. Many hacks used this."),
  O("Order the flow of a Chainlink price feed.", ["Independent nodes fetch prices from sources", "Each node reports a value", "The network aggregates the values", "The feed contract stores the result", "Your contract reads the latest value"],
    "Fetch, report, aggregate, store, read."),
],
"decentralised-storage": [
  F("Complete how a contract refers to a large file on IPFS.", """
tokenURI = "ipfs://" + ____""", ["the content identifier (CID) of the file", "the file name", "the owner's address", "the block number"], 0,
    "IPFS addresses content by its hash (CID). If the file changes, the CID changes."),
  X("One line is wrong for personal data under GDPR.", """
store a hash of the document on chain
store the document itself off chain
keep the right to delete the off-chain copy
store the person's full name and address on chain""", 3, ["keep personal data off chain", "encrypt it with a public key on chain", "store it in an event"], 0,
    "Data on chain cannot be deleted. Personal data belongs off chain."),
  O("Order how an NFT certificate is stored.", ["Upload the image to IPFS", "Get its CID", "Write the metadata JSON with the image CID", "Upload the metadata and get its CID", "Mint the token with tokenURI = ipfs://<metadata CID>"],
    "Image first, then metadata pointing to it, then the token pointing to the metadata."),
],
"lab-attestations": [
  F("Complete an EAS schema for a delivery confirmation.", """
schema: bytes32 documentHash, ____ delivered, string note""", ["bool", "address payable", "uint8[]", "mapping"], 0,
    "A yes/no fact is a bool."),
  X("One line in the attestation lab is wrong.", """
create a schema on sepolia.easscan.org
make an attestation about a document hash
anyone can check who attested and when
the attestation proves the document content is true""", 3, ["it proves who claimed it and when, not that the claim is true", "it proves the document is secret", "it proves payment"], 0,
    "An attestation is a signed statement. It shows who said what and when, not whether it is true."),
  O("Order the EAS lab.", ["Hash your document", "Create a schema", "Make an attestation with the hash", "Copy the attestation UID", "Look it up as another student"],
    "Hash, schema, attest, record the UID, verify."),
],
"lab-quickdapp": [
  F("QuickDApp needs to know which contract to connect. Complete the input.", """
contract address: ____
ABI: from the Remix compile output""", ["your Escrow address on Sepolia", "your wallet address", "the faucet address", "0x0"], 0,
    "The app needs the deployed contract's address and its ABI."),
  X("One test step in the QuickDApp lab is wrong.", """
open the generated app
connect MetaMask on Sepolia
the buyer clicks Deposit with the exact price
the seller clicks Confirm delivery and it succeeds""", 3, ["the seller clicks Confirm delivery and sees the revert", "the seller clicks Refund and it succeeds", "the arbiter cannot click anything"], 0,
    "The contract rules are the same in any front end. The seller cannot release."),
  O("Order the QuickDApp lab.", ["Deploy the Escrow on Sepolia", "Open QuickDApp in Remix", "Generate the app from the ABI", "Test each role", "Note what the app shows when a call reverts"],
    "Deploy, generate, test every role."),
],
}
