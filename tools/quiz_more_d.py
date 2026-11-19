# Second and third fill / fix / order items per unit: modules 11-13.
from quiz_types_a import F, X, O

ITEMS = {
"defi": [
  F("Complete the swap in a pool with 100 ETH and 300,000 USDC after selling 10 ETH (no fee).", """
k = 100 * 300,000 = 30,000,000
new USDC reserve = 30,000,000 / 110 = 272,727
trader receives = ____""", ["27,273 USDC", "30,000 USDC", "272,727 USDC", "3,000 USDC"], 0,
    "300,000 − 272,727 = 27,273 USDC, an average below the starting price (slippage)."),
  F("Complete the liquidation rule.", """
if loan > collateral_value * ____:
    liquidate(position)""", ["the loan-to-value limit, e.g. 0.75", "2", "0", "the ETH price"], 0,
    "Positions above the limit are liquidated to protect lenders."),
  X("One line about stablecoins is wrong.", """
fiat-backed: reserves held by an issuer
crypto-backed: over-collateralised by other tokens
algorithmic: held by incentives; TerraUSD failed in 2022
fiat-backed coins can never lose their peg""", 3, ["they depend on the issuer's reserves and redemptions", "they are backed by gold only", "they have no issuer"], 0,
    "USDC briefly depegged in March 2023 when part of its reserves sat in a failing bank."),
  X("One line about MEV is wrong.", """
MEV is profit from ordering transactions
sandwich bots buy before and sell after a large swap
users can reduce it with slippage limits and private order flow
MEV only exists on Bitcoin""", 3, ["MEV exists wherever block builders order transactions", "MEV was removed by the Merge", "MEV is a token"], 0,
    "MEV is a central topic on Ethereum and its rollups."),
  O("Order a sandwich attack.", ["A user sends a large swap to the mempool", "A bot sees it", "The bot buys first, raising the price", "The user's swap executes at the worse price", "The bot sells right after"],
    "Front-run, victim, back-run."),
  O("Order borrowing on a lending protocol.", ["Deposit collateral", "Borrow up to the limit", "The collateral price falls", "The position crosses the liquidation threshold", "A liquidator repays part and takes collateral"],
    "Collateral, loan, price drop, liquidation."),
],
"daos-and-governance": [
  F("Complete the defence against flash-loan voting.", """
votingPower(member) = balanceAt(member, ____)""", ["the snapshot block when the proposal was created", "the current block", "the next block", "any block the member picks"], 0,
    "Past balances cannot be borrowed in the voting transaction."),
  F("Complete the DAO rule that gives members time to leave.", """
passed proposal -> ____ -> execute""", ["timelock", "airdrop", "new vote", "bridge"], 0,
    "A timelock delays execution after a vote passes."),
  X("One rule in this student-club DAO is risky.", """
voting power from a snapshot block
quorum of 30% of tokens
2-day timelock before execution
proposals can execute in the same block they are created""", 3, ["proposals need a voting period and timelock", "proposals skip the quorum", "proposals execute before voting"], 0,
    "Same-block execution enabled the Beanstalk attack."),
  X("One legal statement is wrong.", """
an unregistered DAO can be treated as a partnership
members may then be personally liable
legal wrappers include foundations and associations
token holders are never liable under any law""", 3, ["liability depends on the law and structure", "only developers are liable", "DAOs cannot be sued"], 0,
    "Ooki DAO and Sarcuni v. bZx (2023) show liability risk."),
  O("Order the Beanstalk attack (2022).", ["Take a flash loan of governance-relevant tokens", "Gain a majority of votes", "Pass a malicious proposal", "Execute it to send treasury funds to the attacker", "Repay the flash loan"],
    "All in one transaction because there was no delay."),
  O("Order a delegated governance cycle.", ["Members delegate votes to a representative", "The delegate studies the proposal", "The delegate votes", "The proposal passes or fails", "Members can change their delegate"],
    "Delegation keeps voting power active."),
],
"lab-safe": [
  F("Complete the Safe for a team of three where one lost key must not block payments.", """
owners = 3
threshold = ____""", ["2", "3", "1", "0"], 0,
    "2-of-3: no single signer can pay, and one lost key does not lock the funds."),
  F("Complete what holds the signatures when a Safe transaction executes.", """
execTransaction(..., ____)""", ["signatures", "privateKeys", "recoveryPhrases", "passwords"], 0,
    "The signatures field contains the owners' approvals."),
  X("One line about the Safe is wrong.", """
a Safe is a smart contract wallet
it has its own address
owners approve; execution needs the threshold
the Safe has its own private key that can bypass owners""", 3, ["it has no key; only owner signatures move funds", "the Safe Labs team can sign", "the deployer can bypass it"], 0,
    "Control comes from the owners and the threshold."),
  X("One step of the lab is wrong.", """
create the Safe on Sepolia with three owners
send 0.01 SepoliaETH to the Safe
owner 1 proposes and signs a payment
the payment executes before owner 2 signs""", 3, ["it executes only after owner 2 also signs", "owner 1 signs twice", "the receiver signs"], 0,
    "One signature is below the threshold."),
  O("Order the Safe lab.", ["Create the Safe with three owners and threshold 2", "Fund the Safe with test ETH", "Owner 1 proposes and signs a payment", "Owner 2 confirms", "Execute and check Etherscan"],
    "Create, fund, propose, confirm, execute."),
  O("Order a rejected payment.", ["Owner 3 proposes a payment", "Owner 1 creates a rejection for the same nonce", "Owner 2 signs the rejection", "The rejection executes", "No ETH leaves the Safe"],
    "Rejections also need the threshold."),
],
"lab-aragon": [
  F("Complete the Aragon multisig setting.", """
members = 3
approval threshold = ____ (a majority)""", ["2", "1", "3", "0"], 0,
    "Two of three is a majority."),
  F("Complete the fallback if Ethereum Sepolia is not listed in the Aragon App.", """
choose another testnet the app offers, e.g. ____""", ["Hoodi or Base Sepolia", "Ethereum mainnet", "Bitcoin", "any network with real ETH"], 0,
    "Stay on a testnet and get test ETH for it."),
  X("One line about the Aragon DAO is wrong.", """
the DAO has its own treasury address
members create proposals
a proposal executes after enough approvals
any wallet can execute a proposal before approval""", 3, ["execution needs the approvals first", "only Aragon staff can execute", "proposals execute automatically on creation"], 0,
    "Approvals come first."),
  X("One comparison with the Safe is wrong.", """
both need several members to move funds
the DAO adds proposals with descriptions
the DAO can add plugins such as token voting
the Safe has built-in token voting""", 3, ["the Safe uses owner signatures, not token votes", "the Safe has no owners", "the Safe is a DAO token"], 0,
    "Safes use signatures; DAOs add governance features."),
  O("Order the Aragon lab from setup to payment.", ["Create the DAO on a testnet", "Add three members and a threshold", "Fund the treasury", "Create a payment proposal", "Approve and execute it"],
    "Set up, fund, propose, decide, act."),
  O("Order the failing proposal.", ["Create a proposal to add a fourth member", "Only one member approves", "The voting period ends", "The proposal is not executed", "The member list stays the same"],
    "Below threshold means no change."),
],
"law-and-business": [
  F("Complete the claim if a minor's contract is invalid but the payment was made on chain.", """
on chain: payment final
in law: the seller must return it under ____""", ["unjust enrichment (§ 812 BGB)", "the gas rules", "the token standard", "MiCA"], 0,
    "Courts order people to pay back; the chain does not reverse itself."),
  F("Complete the business test for a smart contract project.", """
automate if: many parties + clear conditions + digital assets + need for ____""", ["an independent shared record", "a central database", "paper copies", "more intermediaries"], 0,
    "Without these, a normal system is cheaper."),
  X("One line in this legal analysis is wrong.", """
identity: an address does not show who or how old
mandatory law: tenancy rules can override code
GDPR: immutable storage meets the right to erasure
jurisdiction: blockchain contracts are outside all national law""", 3, ["courts apply conflict-of-law rules to the parties", "only US law applies", "only the developers' law applies"], 0,
    "Parties are always somewhere; courts decide which law applies."),
  X("One line confuses the two meanings of contract.", """
legal contract: binding agreement by offer and acceptance
smart contract: software that moves assets by rules
code can perform a legal agreement
every smart contract is a legal contract""", 3, ["a smart contract may or may not be part of one", "no smart contract can be part of one", "legal contracts must be on chain"], 0,
    "It depends on the parties' agreement and the law."),
  O("Order the clause-to-code method for any agreement.", ["Write each clause in plain language", "Find the code that implements it", "Mark in code, partly, or not in code", "List what the code cannot express", "Propose a clause or code change"],
    "The core method of the course."),
  O("Order the minor-buyer case.", ["A 16-year-old deposits into the Escrow", "The seller is paid on confirmation", "The parents refuse consent", "The contract is invalid", "The seller must pay back under civil law"],
    "Code completes; law corrects."),
],
"smart-legal-contracts": [
  F("Complete the priority clause.", """
"In case of conflict between this text and the code, ____ prevails." """, ["the text (as the parties choose)", "the gas price", "the blockchain", "nobody"], 0,
    "The parties should decide in writing."),
  F("Complete the Accord Project parts.", """
template = text (TemplateMark) + model (Concerto) + ____""", ["logic", "blockchain", "wallet", "gas"], 0,
    "Data fills the variables for each deal."),
  X("One line about the UK Law Commission forms is wrong.", """
natural-language: text is the contract, code performs
hybrid: some terms in text, some in code
code-only: the code is the whole agreement
code-only contracts are always invalid in England""", 3, ["English law can support them, with practical challenges", "they are mandatory", "they are only for banks"], 0,
    "The 2021 report found existing law can accommodate them."),
  X("One line about the EU Data Act (Article 36) is wrong.", """
it covers smart contracts that execute data-sharing agreements
it requires access control and robustness
it requires safe termination or interruption
it bans all smart contracts in the EU""", 3, ["it sets requirements; it does not ban them", "it applies only to tokens", "it applies only in Germany"], 0,
    "It sets essential requirements for certain smart contracts."),
  O("Order building a template in the Accord Playground.", ["Define the fields in the model", "Write the text with {{variables}}", "Fill the data", "Check the preview", "Fix any variable errors"],
    "Model, text, data, check."),
  O("Order from more text to more code.", ["Natural-language contract", "Hybrid contract", "Code-only contract"],
    "The UK Law Commission's three forms."),
],
"regulation": [
  F("Complete MiCA's stablecoin category for a basket of currencies.", """
references one official currency -> EMT
references several assets or a basket -> ____""", ["ART (asset-referenced token)", "utility token", "NFT", "security"], 0,
    "Asset-referenced tokens reference a basket or other assets."),
  F("Complete when the GENIUS Act takes effect at the latest.", """
signed July 2025 -> takes effect by ____""", ["18 January 2027", "1 January 2026", "July 2025", "never"], 0,
    "The earlier of 18 months after enactment or 120 days after final rules."),
  X("One line about MiCA is wrong.", """
it applies fully since 30 December 2024
CASPs need a licence to serve EU clients
the transitional period ended on 1 July 2026
it regulates tokens that are financial instruments""", 3, ["those fall under MiFID II, not MiCA", "it regulates only NFTs", "it regulates only banks"], 0,
    "MiCA covers crypto-assets outside existing financial law."),
  X("One line about token labels is wrong.", """
the rights a token gives decide its classification
a profit share points to a security
redeemable 1:1 for euros points to an EMT
calling it a utility token avoids securities law""", 3, ["the label does not matter; the economics do", "utility tokens are always securities", "labels are mandatory"], 0,
    "Substance over form."),
  O("Order a classification check.", ["Describe the token's rights", "Test for a financial instrument (MiFID II)", "If not, test EMT or ART under MiCA", "Otherwise treat it as another crypto-asset", "List the duties of issuer and service providers"],
    "Securities law first, then MiCA categories, then duties."),
  O("Order these EU rules by when they started to apply.", ["DLT Pilot Regime (March 2023)", "MiCA fully applicable (December 2024)", "End of MiCA transition (July 2026)", "New EU AML Regulation (July 2027)"],
    "2023, 2024, 2026, 2027."),
],
"lab-accord": [
  F("Complete a Concerto field for the deposit amount.", """
o Double ____""", ["deposit", "{{deposit}}", "EUR", "true"], 0,
    "Model fields have a type and a name; braces belong in the text."),
  F("Complete the TemplateMark sentence.", """
The Landlord returns the deposit within ____ days.""", ["{{returnDays}}", "returnDays", "o Integer returnDays", "\"returnDays\""], 0,
    "Variables in the text use double braces."),
  X("One line in this model is wrong.", """
o String landlord
o String tenant
o Double deposit
o Integer returnDays = "fourteen\"""", 3, ["o Integer returnDays (value comes from the data)", "o String returnDays", "remove the field"], 0,
    "Values belong in the JSON data, and an Integer cannot be a word."),
  X("One reading of the Playground is wrong.", """
Concerto Model: types of the variables
TemplateMark: legal text with variables
JSON Data: values for one deal
Preview: the code that runs on Ethereum""", 3, ["Preview: the rendered contract text", "Preview: the gas cost", "Preview: the wallet"], 0,
    "The preview shows the text filled with data."),
  O("Order the rental-deposit template.", ["Start from Hello World", "Add the five fields to the model", "Write the clause with variables", "Enter the values in the data", "Check the preview"],
    "Model, text, data, preview."),
  O("Order the analysis after building the template.", ["Mark which clauses could run as code", "Mark which need a human decision", "Add the §551 BGB cap as a rule", "Decide whether it belongs in the model, logic or text"],
    "From text to rules to placement."),
],
"ai-agents": [
  F("Complete the HTTP status code an x402 service returns before payment.", """
GET /data -> ____ Payment Required""", ["402", "200", "404", "500"], 0,
    "x402 builds on the long-unused HTTP 402 status."),
  F("Complete the ERC-8004 registry that records feedback.", """
identity registry, ____ registry, validation registry""", ["reputation", "payment", "token", "storage"], 0,
    "Identity, reputation and validation."),
  X("One line in this agent setup is unsafe.", """
the agent uses a contract wallet with a daily limit
the owner keeps an allow-list of payees
the owner can pause the wallet
the agent also holds the owner's private key""", 3, ["the agent holds only its own limited key", "the agent holds the recovery phrase", "the agent has no key"], 0,
    "Separate the agent's power from the owner's."),
  X("One expectation after a prompt-injection attack is wrong.", """
the agent tries to pay a new address
the contract checks the allow-list
the payment reverts
the contract pays because the agent asked politely""", 3, ["the rules in code decide, not the agent's request", "the contract asks the owner by e-mail", "the contract splits the payment"], 0,
    "Code limits the damage an agent can do."),
  O("Order a paid API call by an agent.", ["Find the service in the ERC-8004 registry", "Check its reputation", "Call the API and receive 402 with a price", "Pay through the wallet contract", "Receive the data"],
    "Discover, trust, request, pay, receive."),
  O("Order the AgentWallet checks in pay().", ["Caller is the agent", "Wallet is not paused", "Payee is allowed", "Amount fits the daily limit", "Increase spentToday, then send"],
    "Checks, then effect, then interaction."),
],
"quantum": [
  F("Complete the algorithm that breaks elliptic-curve signatures.", """
quantum attack on ECDSA: ____'s algorithm""", ["Shor", "Grover", "Dijkstra", "RSA"], 0,
    "Shor's algorithm breaks the discrete-logarithm problem; Grover only speeds up search."),
  F("Complete when an Ethereum account's public key becomes visible.", """
public key exposed after the account ____""", ["sends its first transaction", "receives ETH", "is created", "is viewed on Etherscan"], 0,
    "Signatures reveal the public key; receiving does not."),
  X("One statement about quantum-safe cryptography is wrong.", """
ECDSA and BLS signatures are vulnerable to Shor
Keccak-256 keeps about 128-bit security against Grover
NIST IR 8547 deprecates vulnerable signatures after 2030
hash-based signatures are broken by quantum computers""", 3, ["hash-based signatures are considered quantum-safe", "Keccak is broken", "NIST bans hashes"], 0,
    "SLH-DSA is a hash-based post-quantum standard."),
  X("One step in the migration plan is in the wrong place.", """
list all uses of signatures
make the verifier replaceable
retire the old key
switch to the post-quantum scheme""", 2, ["switch to the new scheme before retiring the old key", "never retire the key", "retire first, then list"], 0,
    "Retiring the old key first would leave no valid signer."),
  O("Order the NIST timeline.", ["Post-quantum standards FIPS 203-205 published (2024)", "NIST IR 8547 finalised (October 2026)", "Vulnerable signatures deprecated (after 2030)", "Vulnerable signatures disallowed (after 2035)"],
    "Standards, plan, deprecation, ban."),
  O("Order the exposure of an account.", ["Generate a key", "Receive ETH (public key still hidden)", "Send a transaction (public key revealed)", "A future quantum attacker could derive the private key"],
    "Exposure begins at the first signature."),
],
"research": [
  F("Complete the paper summary format.", """
problem -> method -> result -> ____""", ["one line per lens and one limitation", "the authors' salaries", "the journal's logo", "nothing"], 0,
    "Tie each paper to technology, business and law."),
  F("Complete the check before citing a preprint.", """
is it ____?""", ["peer reviewed or still a preprint", "on mainnet", "a token", "in German"], 0,
    "arXiv papers are not yet peer reviewed."),
  X("One line in this source evaluation is wrong.", """
check the date and venue
check the method and sample
read the limitations
a high citation count proves the result is correct""", 3, ["citations show attention, not correctness", "citations prove nothing at all", "citations are fake"], 0,
    "Judge the method, not popularity."),
  X("One line in this review plan is in the wrong place.", """
define the question
search Google Scholar and arXiv
write the conclusion
select and summarise five papers""", 2, ["write the conclusion last", "skip the search", "summarise before searching"], 0,
    "Conclusions follow the reading."),
  O("Order a mini literature review.", ["Define the question", "Search", "Select five papers", "Summarise each", "Write what is still open"],
    "Question to gap."),
  O("Order reading a paper efficiently.", ["Title and abstract", "Conclusion", "Figures and tables", "Method", "Limitations"],
    "Skim first, then go deep where it matters."),
],
"tools-to-evaluate": [
  F("Complete the first safety check for a new tool.", """
does it ever ask for the ____? -> stop""", ["recovery phrase", "network name", "contract name", "e-mail"], 0,
    "No legitimate tool needs your recovery phrase."),
  F("Complete the transparency check.", """
can you read and ____ the generated contract on Etherscan?""", ["verify", "burn", "mint", "hide"], 0,
    "Unverifiable code is a red flag."),
  X("One property of this no-code tool is a red flag.", """
open-source contracts
deployments verified on Etherscan
works on Sepolia
admin key held by the tool's company with no timelock""", 3, ["admin rights with a timelock or none", "admin key shared on Discord", "no admin and no code"], 0,
    "Hidden admin power is a risk to users."),
  X("One step of the evaluation is in the wrong place.", """
read who built it
try it on Sepolia
recommend it to the class
read the generated contract""", 2, ["recommend only after reading the contract", "never read the contract", "recommend before trying"], 0,
    "Evidence before recommendation."),
  O("Order the tool evaluation.", ["Read who built it and when", "Try it on Sepolia", "Read the generated contract", "Check admin powers", "Score it with the checklist"],
    "Origin, trial, code, control, score."),
  O("Order the red flags from most to least severe.", ["Asks for your recovery phrase", "Deploys unverified code", "Admin can upgrade without delay", "No documentation"],
    "Key theft first, then hidden code and power."),
],
}
