# New question types for modules 10-13.
from quiz_types_a import F, X, O

ITEMS = {
# ---------- Module 10 ----------
"ethereum-today": [
  F("Complete how an optimistic rollup handles a wrong state claim.", """
operator posts new state root to Ethereum
if someone proves it wrong within the challenge window:
    ____""", ["the claim is rejected and the operator's bond is slashed", "the claim is accepted anyway", "Ethereum stops", "the user pays a fine"], 0,
    "Optimistic rollups assume claims are valid unless a fraud proof shows otherwise during the challenge window."),
  X("One line about Ethereum in 2025–2026 is wrong.", """
Ethereum uses proof of stake since The Merge (2022)
rollups (L2s) run most user transactions
EIP-4844 blobs made rollup data cheaper
L2 transactions never depend on Ethereum security""", 3, ["L2s post data and proofs to Ethereum and rely on it for security", "L2s use Bitcoin for security", "L2s need no data at all"], 0,
    "Rollups inherit security from Ethereum because they post their data and proofs there. L2BEAT shows how far each one does."),
  O("Order the life of a rollup transaction.", ["The user sends the transaction to the L2 sequencer", "The sequencer orders it and gives a fast receipt", "A batch of transactions is posted to Ethereum as a blob", "A proof or the challenge window confirms the batch", "The transaction is final on Ethereum"],
    "Fast on L2 first, final on L1 later."),
],
"channels-sidechains-bridges": [
  F("Complete the lock-and-mint bridge logic.", """
on chain A: lock 10 tokens in the bridge contract
on chain B: ____""", ["mint 10 wrapped tokens to the user", "burn 10 tokens", "mint 20 tokens", "do nothing"], 0,
    "The wrapped tokens on chain B are backed by the locked tokens on chain A. If the bridge is hacked, they lose their backing."),
  X("One line in this bridge risk list is wrong.", """
the bridge holds large amounts of locked tokens
a few keys often control the bridge
many large hacks targeted bridges
wrapped tokens stay safe even if the locked tokens are stolen""", 3, ["wrapped tokens lose their value if the locked tokens are stolen", "wrapped tokens double in value", "wrapped tokens move back automatically"], 0,
    "Wrapped tokens are claims on the locked assets. Ronin and Wormhole showed what happens when those are stolen."),
  O("Order a payment channel.", ["Both parties lock funds in a contract on chain", "They exchange signed balance updates off chain", "Each new update replaces the old one", "One party submits the latest update on chain", "The contract pays out the final balances"],
    "Open on chain, trade off chain, close on chain."),
],
"zero-knowledge": [
  F("Complete the age check with a zero-knowledge proof.", """
prover knows: date_of_birth
public statement: "age >= 18"
verifier learns: ____""", ["only that the statement is true", "the date of birth", "the passport number", "nothing, not even if it is true"], 0,
    "A ZK proof shows that a statement is true without revealing the secret behind it."),
  X("One line about ZK rollups is wrong.", """
a ZK rollup posts a validity proof to Ethereum
Ethereum checks the proof in a contract
no challenge window is needed for correctness
the proof reveals all user data publicly""", 3, ["the proof shows the state change is valid; data availability is a separate question", "the proof is a password", "the proof is checked by users by hand"], 0,
    "The proof shows correctness. Whether data is published is a separate design choice."),
  O("Order a zero-knowledge proof flow.", ["Define the statement to prove", "The prover computes a proof with the secret", "The proof is sent to the verifier", "The verifier checks it with public inputs", "The verifier accepts without seeing the secret"],
    "Statement, prove, send, verify, accept."),
],
"lab-dashboards": [
  F("Complete the Dune query that counts daily transactions of a contract.", """
SELECT date_trunc('day', block_time) AS day, COUNT(*) AS txs
FROM ethereum.transactions
WHERE "to" = 0x...contract
GROUP BY ____""", ["1", "txs", "hash", "value"], 0,
    "GROUP BY 1 groups by the first column, the day."),
  X("One reading of an L2BEAT page is wrong.", """
TVS: value secured by the rollup
Stage 0/1/2: how much users depend on the operators
Data availability: where the transaction data is published
Stage 0 means fully decentralised with no training wheels""", 3, ["Stage 0 means the operators still have strong control", "Stage 0 means the rollup is closed", "Stage 0 means ZK only"], 0,
    "Stage 0 still has training wheels. Stage 2 is the most decentralised."),
  O("Order the dashboards lab.", ["Pick a question, for example which L2 is growing", "Find the data on L2BEAT or Dune", "Build a chart", "Check the definitions behind the numbers", "Write one conclusion with its limits"],
    "Question, data, chart, check definitions, conclude."),
],
# ---------- Module 11 ----------
"defi": [
  F("Complete the constant-product rule of an automated market maker.", """
x * y = ____""", ["k (a constant)", "0", "the price", "x + y"], 0,
    "In a Uniswap-style pool, the product of the two reserves stays constant. Trades move the price along this curve."),
  X("One line in this loan logic is wrong.", """
collateral_value = collateral * oracle_price
max_loan = collateral_value * 0.75
if loan > max_loan:
    allow a new loan""", 3, ["liquidate part of the collateral", "lower the interest", "ignore it"], 0,
    "If the loan is above the limit, the position is under-collateralised and gets liquidated."),
  O("Order a flash-loan price attack.", ["Borrow a large amount in a flash loan", "Swap it to push a pool price far away", "A victim contract reads that manipulated price", "Take out value at the wrong price", "Repay the flash loan in the same transaction"],
    "Everything happens in one transaction. The defence is robust oracles."),
],
"daos-and-governance": [
  F("Complete the DAO rule for passing a proposal.", """
if votes_for > votes_against and total_votes >= ____:
    queue(proposal)""", ["quorum", "0", "the proposal ID", "the gas price"], 0,
    "A quorum stops a tiny group from deciding when few members vote."),
  X("One line in this DAO design is risky.", """
votes are weighted by tokens held at a snapshot block
passed proposals wait in a timelock
members can exit during the timelock
votes count tokens borrowed in the same block""", 3, ["count tokens held at an earlier snapshot block", "count only the founder's votes", "count no tokens"], 0,
    "Flash-loaned tokens can buy a vote (Beanstalk 2022). Snapshots block this."),
  O("Order a DAO proposal.", ["A member creates a proposal", "The voting period opens", "Members vote", "If it passes, it waits in the timelock", "The proposal executes on chain"],
    "Propose, vote, wait, execute."),
],
"lab-safe": [
  F("Complete the Safe setup for a company wallet.", """
owners = [CEO, CFO, Legal]
threshold = ____""", ["2", "1", "0", "4"], 0,
    "2-of-3: no single person can move funds, and one lost key does not lock the wallet."),
  X("One step in the Safe lab is wrong.", """
create a Safe on Sepolia with three owner accounts
set the threshold to 2
propose a payment from owner 1
execute after owner 1 signs alone""", 3, ["execute after a second owner also signs", "execute without any signature", "execute from a non-owner"], 0,
    "With threshold 2, one signature is not enough."),
  O("Order a Safe payment.", ["Owner 1 proposes the payment", "Owner 1 signs", "Owner 2 checks the details and signs", "One owner executes the transaction", "The payment appears on Etherscan"],
    "Propose, sign twice, execute, verify."),
],
"lab-aragon": [
  F("Complete the Aragon DAO setting that gives members time to react.", """
voting plugin: token voting
minimum participation: 30%
proposal delay before execution: ____""", ["a timelock period, for example 2 days", "0 seconds", "never", "one block"], 0,
    "A delay lets members check a passed proposal and exit if they disagree."),
  X("One line in the Aragon lab is wrong.", """
create a DAO on Sepolia
add three members with tokens
create a proposal to pay from the treasury
the proposal executes as soon as it is created""", 3, ["it executes only after the vote passes", "it executes on mainnet", "it executes without a treasury"], 0,
    "Nothing executes without a passed vote."),
  O("Order the Aragon lab.", ["Create the DAO on Sepolia", "Set the members and voting rules", "Fund the treasury with test ETH", "Create and vote on a proposal", "Execute it and check the treasury balance"],
    "Create, configure, fund, decide, execute."),
],
# ---------- Module 12 ----------
"law-and-business": [
  F("Complete the decision rule that the code cannot make alone.", """
if goods delivered and buyer confirms:
    release payment
if buyer claims the goods are partly defective:
    ____""", ["the arbiter decides on a price reduction (for example §441 BGB)", "the code pays 50% automatically", "the seller keeps all", "the contract deletes itself"], 0,
    "Code knows only clear conditions. Legal questions like partial defects need a human decision or a richer contract."),
  X("One line in this cost comparison is wrong.", """
bank escrow: fees and days of processing
smart contract escrow: gas fees and minutes
smart contract escrow: an arbiter may still be needed
smart contract escrow: legal advice is never needed""", 3, ["legal terms are still needed for disputes and liability", "gas is always zero", "the bank must sign"], 0,
    "The code automates performance, not the legal relationship."),
  O("Order a clause-to-code analysis.", ["Write the clause in plain language", "Find the function that implements it", "Mark it: in code, partly in code, or not in code", "List what the code cannot express", "Propose a legal clause or a code change for the gap"],
    "This is the core method of the course."),
],
"smart-legal-contracts": [
  F("In an Accord Project template, which part holds the values for one deal?", """
template = legal text + model + ____""", ["data", "gas", "a private key", "a block"], 0,
    "The text has variables, the model defines their types, and the data fills them in for one contract."),
  X("One line about smart legal contracts is wrong.", """
a smart legal contract is a legal contract with parts in code
the legal text stays readable for people
the data model links variables to code
the code always overrides the written terms""", 3, ["the parties agree which prevails; often the text does", "the code has no legal effect at all", "the code is the judge"], 0,
    "Which document prevails in case of conflict is itself a legal choice."),
  O("Order the creation of a smart legal contract.", ["Write the legal text with variables", "Define the data model", "Fill in the data for the deal", "Link the logic to code", "Both parties sign"],
    "Text, model, data, logic, signatures."),
],
"regulation": [
  F("Complete a simple MiCA classification in pseudo code.", """
if token is a financial instrument:
    MiFID II applies
else if token references one official currency:
    type = ____""", ["e-money token (EMT)", "utility token", "NFT", "no rules"], 0,
    "MiCA: a token pegged to one official currency is an e-money token; a basket gives an asset-referenced token (ART)."),
  X("One line in this GDPR check is wrong.", """
personal data on a public chain cannot be deleted
use hashes or off-chain storage for personal data
identify the controller of the processing
a pseudonymous address is never personal data""", 3, ["an address can be personal data if it can be linked to a person", "addresses are always secret", "GDPR does not apply in the EU"], 0,
    "If an address can be linked to a person, it is personal data."),
  O("Order a regulatory check for a token project.", ["Describe what the token does", "Check whether it is a financial instrument", "If not, classify it under MiCA", "Check the duties: white paper, licence, disclosure", "Check data protection and consumer rules"],
    "Function first, then the right regime, then duties."),
],
"lab-accord": [
  F("In the Template Playground, a variable in the text is written like this. Complete it.", """
The buyer pays {{____}} to the seller.""", ["price", "0x0", "msg.sender", "gasLimit"], 0,
    "The template variable links the text to the data model."),
  X("One step in the Accord lab is wrong.", """
open the Template Playground
choose a sample template
change the data, such as the price
the legal text stays the same when the data changes""", 3, ["the rendered text updates with the new data", "the template deletes itself", "the price must be in ETH"], 0,
    "Changing the data changes the rendered contract text."),
  O("Order the Accord lab.", ["Open the Template Playground", "Load a sample template", "Read the text, model and data", "Change a value and see the text update", "Write which clauses could run as code"],
    "Load, read, change, analyse."),
],
# ---------- Module 13 ----------
"ai-agents": [
  F("Complete AgentWallet.pay() so the agent cannot pay a stranger.", """
function pay(address payable to, uint256 amount, string calldata memo) external {
    require(msg.sender == agent, "Only agent");
    require(!paused, "Paused");
    require(____, "Payee not allowed");
    ...
}""", ["allowedPayee[to]", "!allowedPayee[to]", "to == agent", "amount > dailyLimit"], 0,
    "The owner keeps an allow-list. The agent can pay only approved payees."),
  X("One line in AgentWallet.pay() is wrong.", """
require(spentToday + amount <= dailyLimit, "Daily limit");
(bool ok, ) = to.call{value: amount}("");
spentToday += amount;
require(ok, "Transfer failed");""", 2, ["move it above the call: effect before interaction", "delete it", "change it to spentToday = 0;"], 0,
    "The spending counter must rise before the external call, or a malicious payee can re-enter and overspend."),
  O("Order the AgentWallet lab.", ["The owner deploys with the agent address and a daily limit", "The owner funds the wallet and allows a payee", "The agent pays within the limit", "The agent tries to pay over the limit and sees the revert", "The owner pauses the wallet"],
    "Rules first, then normal use, then the limits and the pause switch."),
],
"quantum": [
  F("Complete the crypto-agility pattern.", """
function verify(message, signature):
    return ____.verify(message, signature)
function setVerifier(newVerifier) onlyGovernance""", ["verifier (a replaceable contract)", "ecrecover only, forever", "msg.sender", "block.timestamp"], 0,
    "If the signature scheme can be replaced, the contract can move to post-quantum signatures later. Who may replace it is a governance risk."),
  X("One line about quantum risk is wrong.", """
large quantum computers could break ECDSA signatures
hash functions are weakened less than signatures
NIST standardised post-quantum signatures in 2024
all addresses are broken today""", 3, ["no quantum computer can break ECDSA today; the risk is future", "only Bitcoin is affected", "hashes break first"], 0,
    "The risk is real but future. Exposed public keys are the first target."),
  O("Order a migration plan to post-quantum signatures.", ["List where signatures are used", "Choose a post-quantum scheme", "Make the verifier replaceable", "Test and migrate accounts", "Retire the old scheme"],
    "Inventory, choose, prepare, migrate, retire."),
],
"research": [
  F("Complete the three-line paper summary.", """
Problem: what question does the paper answer?
Method: ____
Result: what did it find?""", ["how did the authors answer it?", "who paid for it?", "how long is it?", "which journal printed it?"], 0,
    "Problem, method, result: then one line per lens."),
  X("One line in this research checklist is wrong.", """
check the date and the venue
read the abstract and the conclusion first
note the method and its limits
a preprint is always peer reviewed""", 3, ["a preprint is not yet peer reviewed", "a preprint is a law", "a preprint is a blog post only"], 0,
    "Preprints (for example on arXiv) are not yet peer reviewed."),
  O("Order a short literature review.", ["Define the research question", "Search Google Scholar and arXiv", "Select five relevant papers", "Summarise each in three lines", "Write what is still open"],
    "Question, search, select, summarise, find the gap."),
],
"tools-to-evaluate": [
  F("Complete the tool evaluation checklist.", """
does it run on a testnet only?
who controls the deployed contract?
can you ____ the generated code?""", ["read and verify", "sell", "hide", "delete from the chain"], 0,
    "A no-code tool is useful only if you can see and verify what it deploys."),
  X("One line in this evaluation is a red flag.", """
the tool shows the full contract source
deployments are verified on Etherscan
the tool works on Sepolia
the tool asks for your recovery phrase to connect""", 3, ["it connects through the wallet without the phrase", "it uses email only", "it needs no wallet"], 0,
    "Any tool that asks for a recovery phrase is a scam."),
  O("Order the evaluation of a new no-code tool.", ["Read who built it and when", "Try it on Sepolia", "Read the generated contract", "Check who controls admin functions", "Score it with the checklist"],
    "Origin, trial, code, control, score."),
],
}
