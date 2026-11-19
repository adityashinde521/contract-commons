# Deeper explanations, worked examples and common mistakes: modules 4-8.

D = {}

D["what-smart-contracts-are"] = """
### In depth

<p>Nick Szabo coined the term “smart contract” in the 1990s with the example of a vending machine: put in a coin, the machine releases a drink, and nobody needs to trust the shop owner. On Ethereum, a smart contract is a program stored at an address. It holds its own balance and storage, and anyone can call its public functions. It runs exactly as written, and on most contracts nobody can change the code afterwards.</p>
<p>The best way to think about a contract is as a <b>state machine</b>. It is always in one state (for the Escrow: awaiting payment, awaiting delivery, complete, refunded). Each function is a possible <b>transition</b> with conditions: who may call it, in which state, with how much money. If a condition fails, the function <b>reverts</b> and nothing changes. Writing a contract therefore means answering three questions for every action: who, when, and what happens to the money.</p>
<!-- diagram:escrow-states -->
<p>What a contract can enforce is limited to what it can see on chain: addresses, amounts, time, and the state of other contracts. Whether a laptop arrived, whether it is “of acceptable quality”, or whether a party is a minor are outside facts. A contract needs an oracle or an arbiter to bring them in, and the law still decides what happens when the code and the agreement differ.</p>

### Worked example

<div class="worked">
<p><b>Case:</b> turn the laptop sale into rules.</p>
<div class="tw"><table>
  <tr><th>Clause</th><th>Who</th><th>When (state)</th><th>Effect</th></tr>
  <tr><td>§2 The buyer pays the price into escrow</td><td>Buyer only</td><td>AwaitingPayment</td><td>Exactly 1 ETH held; state → AwaitingDelivery</td></tr>
  <tr><td>§4 Payment is released on confirmed delivery</td><td>Buyer or arbiter</td><td>AwaitingDelivery</td><td>1 ETH to seller; state → Complete</td></tr>
  <tr><td>§5 Refund if the goods do not arrive</td><td>Arbiter only</td><td>AwaitingDelivery</td><td>1 ETH back to buyer; state → Refunded</td></tr>
  <tr><td>§6 Partly defective goods: price reduction</td><td colspan="3">Not in code: needs a human decision or a richer contract (lab 4.3, Apply)</td></tr>
</table></div>
</div>

### Common mistakes

<ul>
  <li>“A smart contract is a legal contract.” It may perform part of one. Formation, capacity, mistake and consumer law still apply.</li>
  <li>“The contract runs by itself.” Nothing happens until someone sends a transaction. There are no timers.</li>
  <li>“Code is law.” The code decides what happens on chain; a court can still order the parties to undo it off chain.</li>
</ul>
"""

D["solidity-for-programmers"] = """
### In depth

<p>Solidity looks like JavaScript or Java, but three ideas make it different. First, <b>state is permanent and expensive</b>. Variables declared at contract level live in storage on every node; writing them costs thousands of gas. Local variables in <code>memory</code> disappear after the call. Second, <b>every call has a sender and maybe a value</b>: <code>msg.sender</code> is the direct caller, <code>msg.value</code> is the ETH sent with the call, and only <code>payable</code> functions may receive ETH. Third, <b>failure is all or nothing</b>: <code>require(condition, "message")</code> reverts the whole transaction and undoes every change if the condition is false.</p>
<p>Visibility decides who can call: <code>external</code> and <code>public</code> functions are part of the contract’s interface; <code>internal</code> and <code>private</code> are helpers. <code>view</code> functions only read; <code>pure</code> functions read nothing at all. <b>Modifiers</b> package repeated checks, such as <code>onlyOwner</code>. <b>Events</b> write cheap logs that apps and explorers read; contracts cannot read them back.</p>
<p>Since Solidity 0.8, arithmetic overflow reverts automatically, which removed a whole class of old bugs. Amounts of ETH are always integers in <b>wei</b> (1 ether = 10<sup>18</sup> wei); there are no decimals. Mixing up units is one of the most common beginner mistakes.</p>

### Worked example

<div class="worked">
<p><b>Case:</b> read a function line by line and predict what happens.</p>
<pre><code>function refund() external inState(State.AwaitingDelivery) {
    require(msg.sender == arbiter, "Only arbiter");
    state = State.Refunded;
    (bool ok, ) = payable(buyer).call{value: price}("");
    require(ok, "Transfer failed");
    emit Refunded(buyer, price);
}</code></pre>
<ol>
  <li><code>inState</code> (a modifier) reverts unless the money is currently held.</li>
  <li>The first <code>require</code> reverts unless the caller is the arbiter.</li>
  <li>The state changes <i>before</i> the money leaves (checks, effects, interactions: lesson 7.1).</li>
  <li>The low-level <code>call</code> sends <code>price</code> wei to the buyer and reports success.</li>
  <li>If sending fails, everything is reverted, including the state change.</li>
</ol>
<p><b>Prediction:</b> the seller calls <code>refund()</code> → revert “Only arbiter”, no state change, the seller pays for the gas used.</p>
</div>

### Common mistakes

<ul>
  <li>Forgetting <code>payable</code>: every call with a value reverts.</li>
  <li>Writing <code>1</code> where <code>1 ether</code> was meant: that is 1 wei.</li>
  <li>Using <code>tx.origin</code> for access control instead of <code>msg.sender</code>.</li>
  <li>Thinking <code>private</code> hides data: anyone can read storage directly from the chain.</li>
</ul>
"""

D["token-standards"] = """
### In depth

<p>A token is not a coin that moves; it is a row in a contract’s table. An ERC-20 contract keeps <code>balanceOf[address]</code>. A “transfer” lowers one row and raises another. What makes tokens powerful is the <b>standard interface</b>: because every ERC-20 has the same functions and events, any wallet, exchange or explorer can show and move any token without custom code.</p>
<p>ERC-20 has a second way to move tokens: <b>approve and transferFrom</b>. You first approve a spender (for example an exchange contract) to move up to a certain amount; later the spender pulls the tokens in its own transaction. This lets contracts take payment in tokens, but it is also a risk: many people give unlimited approvals, and a hacked spender can drain them. Newer designs (permit signatures, EIP-7702 batching) reduce the number of steps.</p>
<!-- diagram:approve-flow -->
<p><b>ERC-721</b> tokens are unique: each token ID has one owner and a <code>tokenURI</code> pointing to metadata (name, image). <b>ERC-1155</b> manages many token types in one contract, some unique and some with copies, which saves gas for games and tickets. Tokens can also add rules: pausing, allow-lists of verified holders, or a maximum supply. Those rules are where regulation meets code (lesson 12.3).</p>

### Worked example

<div class="worked">
<p><b>Case:</b> Alice pays 50 CRS course tokens to a shop contract.</p>
<div class="tw"><table>
  <tr><th>Step</th><th>Call</th><th>State after</th></tr>
  <tr><td>Start</td><td></td><td>balanceOf[Alice] = 100, balanceOf[Shop] = 0, allowance[Alice][Shop] = 0</td></tr>
  <tr><td>1</td><td>Alice: <code>approve(Shop, 50)</code></td><td>allowance[Alice][Shop] = 50. Event Approval</td></tr>
  <tr><td>2</td><td>Alice: <code>Shop.buy(itemId)</code>, which calls <code>transferFrom(Alice, Shop, 50)</code></td><td>balanceOf[Alice] = 50, balanceOf[Shop] = 50, allowance = 0. Event Transfer</td></tr>
  <tr><td>Wrong order</td><td>Alice calls <code>buy</code> first</td><td>Revert: insufficient allowance. Nothing changes.</td></tr>
</table></div>
<p>Note the units: with 18 decimals, “50 CRS” is stored as 50 × 10<sup>18</sup>.</p>
</div>

### Common mistakes

<ul>
  <li>“The NFT contains the image.” Usually it contains a link; the image lives elsewhere (lesson 9.3).</li>
  <li>“Owning a token means owning the asset.” Only the legal terms around the token can give that right.</li>
  <li>“Approvals expire.” They do not, until you set them to zero.</li>
</ul>
"""

D["toolchain"] = """
### In depth

<p>Remix is ideal for learning: everything runs in the browser, deployment is a button, and the debugger shows each step. Professional teams work differently, because they need version control, repeatable builds, automated tests and scripted deployments. The usual toolchain has four parts. A <b>framework</b> (Foundry or Hardhat) compiles contracts, runs tests and executes deployment scripts. <b>Git</b> keeps every version and makes code review possible. <b>Libraries</b> such as OpenZeppelin Contracts provide audited building blocks. <b>Explorers and services</b> (Etherscan, Tenderly) verify and monitor what is deployed.</p>
<p><b>Foundry</b> writes tests in Solidity itself and is very fast; it includes <code>forge</code> (build and test), <code>cast</code> (talk to a chain from the command line) and <code>anvil</code> (a local chain). <b>Hardhat</b> writes tests and scripts in JavaScript or TypeScript, which suits teams that also build the web front end. Both can <b>fork</b> mainnet: run a local copy of the real chain state, so you can test your contract against real tokens and protocols without spending anything.</p>
<p>A deployment is not finished until the source is <b>verified</b>: the explorer recompiles your source with the same compiler settings and checks that the bytecode matches. Only then can users read what they interact with.</p>

### Worked example

<div class="worked">
<p><b>Case:</b> the life of one change in a team.</p>
<ol>
  <li>A developer creates a Git branch and adds a fee to the Escrow.</li>
  <li><code>forge test</code> runs 30 tests locally in two seconds; one old test fails because the seller now receives price minus fee. She updates the test on purpose.</li>
  <li>She opens a pull request. A colleague reviews the diff; CI runs the tests and a static analyser (Slither) automatically.</li>
  <li>After approval, <code>forge script</code> deploys to Sepolia and verifies the source on Etherscan in one command.</li>
  <li>Only after a testnet trial and, for real funds, an audit does the same script run against mainnet.</li>
</ol>
</div>

### Common mistakes

<ul>
  <li>“Remix is not professional.” It is excellent for exploring and debugging; it is just not enough for a team process.</li>
  <li>Deploying with a private key pasted into a script file that ends up on GitHub. Use encrypted keystores or hardware wallets.</li>
</ul>
"""

D["testing-contracts"] = """
### In depth

<p>A deployed contract usually cannot be fixed, and it holds money. Testing is therefore the main way to gain confidence before launch. Good tests check three kinds of behaviour. <b>Happy paths</b>: the normal flow works (deposit, confirm, seller paid). <b>Failure paths</b>: every forbidden action reverts with the right message (seller confirms, wrong amount, wrong state). <b>Properties</b>: rules that must hold whatever happens, such as “the contract never pays out more than it received”.</p>
<p>Four techniques build on each other. <b>Unit tests</b> call one function with chosen inputs. <b>Fuzz tests</b> let the framework try hundreds of random inputs for a parameter; they find edge cases you did not think of, such as zero or the maximum value. <b>Invariant tests</b> call random sequences of functions and check a property after each one. <b>Fork tests</b> run against a copy of mainnet to see how your contract behaves with real tokens.</p>
<p>A useful habit for this course: derive tests directly from the legal clauses. Every “only”, “must”, “after” and “at most” in the text becomes at least one failure test. This is where the three lenses meet: the lawyer writes the rule, the business analyst names the edge cases, the developer turns both into code.</p>

### Worked example

<div class="worked">
<p><b>Case:</b> clause §4 of the Escrow, “The buyer or the arbiter may release the payment once it is held”.</p>
<div class="tw"><table>
  <tr><th>Test</th><th>Type</th><th>Expectation</th></tr>
  <tr><td>Buyer confirms after deposit</td><td>Unit, happy path</td><td>Seller balance + price; state Complete</td></tr>
  <tr><td>Arbiter confirms after deposit</td><td>Unit, happy path</td><td>Same result</td></tr>
  <tr><td>Seller confirms</td><td>Failure</td><td>Revert “Only buyer or arbiter”</td></tr>
  <tr><td>Buyer confirms before deposit</td><td>Failure</td><td>Revert “Wrong state”</td></tr>
  <tr><td>Any random caller address</td><td>Fuzz</td><td>Reverts unless caller is buyer or arbiter</td></tr>
  <tr><td>After any sequence of calls</td><td>Invariant</td><td>Contract balance is either 0 or exactly price</td></tr>
</table></div>
</div>

### Common mistakes

<ul>
  <li>Testing only the happy path. Most real bugs are actions that should have failed but did not.</li>
  <li>“100% line coverage means no bugs.” Coverage shows which lines ran, not whether the rules are right.</li>
</ul>
"""

D["security-basics"] = """
### In depth

<p>Smart contracts are attractive targets: the code is public, the money is in the contract, and transactions cannot be reversed. Four bug classes explain a large share of code-level losses.</p>
<p><b>Reentrancy.</b> When a contract sends ETH to another contract, the receiver’s code runs. If the sender has not yet updated its own records, the receiver can call back into the sender and withdraw again, in a loop. The defence is the <b>checks-effects-interactions</b> order: check conditions, update state, and only then call out; or use a reentrancy guard. Variants cross contracts (one contract updated, another not yet), as in the GMX attack of July 2025 (lab 7.5).</p>
<!-- diagram:reentrancy -->
<p><b>Missing access control.</b> A function that changes owners, mints tokens or withdraws funds is left callable by anyone, or is protected with <code>tx.origin</code>, which a malicious contract can abuse. <b>Oracle manipulation.</b> A protocol reads a price from one pool that an attacker can move within the same transaction using a flash loan. <b>Logic and arithmetic errors.</b> Wrong comparisons, rounding in the attacker’s favour, or a missing state check. Since Solidity 0.8, overflow reverts, but rounding and unit mistakes remain.</p>

### Worked example

<div class="worked">
<p><b>Case:</b> the reentrancy loop in numbers (lab 7.4).</p>
<ol>
  <li>The bank holds 10 ETH from honest users. The attacker deposits 1 ETH: balance[attacker] = 1, bank holds 11.</li>
  <li>The attacker calls <code>withdraw()</code>. The bank checks balance = 1 and sends 1 ETH. The bank holds 10.</li>
  <li>Sending runs the attacker’s <code>receive()</code>, which calls <code>withdraw()</code> again. The bank still sees balance = 1, because the line that sets it to zero has not run yet. It sends 1 more. The bank holds 9.</li>
  <li>This repeats until the bank is empty: the attacker gets 11 ETH for a deposit of 1.</li>
  <li><b>Fix:</b> move <code>balances[msg.sender] = 0</code> above the transfer. The second call now sees 0 and reverts.</li>
</ol>
</div>

### Common mistakes

<ul>
  <li>“Audited means safe.” Many exploited protocols were audited; audits reduce risk.</li>
  <li>“Using <code>transfer</code> prevents reentrancy.” It limits gas today, but gas costs change; use the correct order or a guard.</li>
  <li>“Only code bugs matter.” In 2025 the largest losses came from stolen keys and tricked signers (lesson 7.2).</li>
</ul>
"""

D["security-in-practice"] = """
### In depth

<p>The numbers for 2025 changed the security picture. About $3.4 billion was stolen, and almost half of it in a single incident: the Bybit hack of February 2025, about $1.5 billion. The contracts worked perfectly. The attackers compromised a computer used by the wallet provider’s developers and injected code into the signing website, so the exchange’s signers saw a normal transfer while they actually approved a change that gave the attackers control of the cold wallet.</p>
<p>This is the main lesson: <b>operational security</b> now matters as much as code. Typical attack paths are stolen or phished private keys, compromised front ends and software supply chains, social engineering of staff (including fake job applicants), and governance or admin keys with too much power. Hackers linked to North Korea were responsible for at least $2.02 billion in 2025, often through such human routes.</p>
<p>Defences follow from the attack paths. Use multisig with independent signers and hardware wallets. Verify transactions on a second device, by reading the raw data or a simulation, not only the website. Limit what admin keys can do, add timelocks, and monitor contracts so you can pause quickly. At the same time, attackers use AI too: in December 2025, AI agents in the SCONE-bench study exploited more than half of recent real-world vulnerable contracts in simulation.</p>

### Worked example

<div class="worked">
<p><b>Case:</b> review a company’s payment process against the Bybit pattern.</p>
<div class="tw"><table>
  <tr><th>Step today</th><th>Risk</th><th>Better</th></tr>
  <tr><td>Three signers approve in the same web app</td><td>One compromised app fools all three</td><td>Each signer checks the decoded transaction on a hardware wallet or an independent tool</td></tr>
  <tr><td>Signers check the receiver address only</td><td>The attack changed the call type, not the address</td><td>Check the function, the value and whether it is a delegatecall</td></tr>
  <tr><td>Admin key on one laptop</td><td>Malware takes full control</td><td>Admin in a multisig with a 48-hour timelock</td></tr>
  <tr><td>No monitoring</td><td>Loss found hours later</td><td>Alerts on large transfers and admin calls; a pause switch</td></tr>
</table></div>
</div>

### Common mistakes

<ul>
  <li>“A multisig is safe by design.” It is only as safe as the way its signers check what they sign.</li>
  <li>“Hacks are mostly clever code exploits.” The largest losses are increasingly human and operational.</li>
</ul>
"""

D["audits-and-analysis"] = """
### In depth

<p>Before a contract holds real money, professionals combine several methods, because each one finds different problems. <b>Manual review</b> by experienced auditors finds logic and design flaws that tools cannot understand, such as an unfair liquidation rule. <b>Static analysis</b> (Slither, Aderyn) scans the source for known patterns, such as reentrancy or unchecked return values, in seconds; it reports many false positives. <b>Symbolic execution and formal verification</b> (Mythril, Certora, Halmos) try to prove that a property holds for all inputs, or produce a counterexample. <b>Fuzzing and invariant testing</b> attack the contract with random sequences.</p>
<p>Audits end in a <b>report</b>: each finding has a title, a severity (critical, high, medium, low, informational), a description of the impact and a recommended fix, and the team’s response. After launch, <b>bug bounties</b> (for example on Immunefi) pay outside researchers to report issues instead of exploiting them, and <b>audit contests</b> let many auditors compete for a fixed prize pool.</p>
<p>AI tools are now part of the toolbox. Research in 2025 found that language models are useful for explaining code and proposing hypotheses, but not yet reliable enough to replace classic analysers; combinations work best. Every AI finding must be confirmed by a test.</p>

### Worked example

<div class="worked">
<p><b>Case:</b> plan the security budget for a contract that will hold €2 million.</p>
<ol>
  <li>Internal: full test suite with fuzz and invariant tests; Slither in CI. Cost: team time.</li>
  <li>One independent audit by a firm, about two to four weeks. Typical prices are tens of thousands of euros for a small codebase.</li>
  <li>Fix findings, then a short re-review of the fixes.</li>
  <li>Launch with limits: a deposit cap of €200,000 for the first month and a pause switch held by a multisig.</li>
  <li>Bug bounty: for example 10% of funds at risk, capped, for critical findings.</li>
</ol>
<p><b>Reasoning:</b> spending 3–5% of the value at risk on security is common; losing it all is the alternative.</p>
</div>

### Common mistakes

<ul>
  <li>“An audit is a guarantee.” It is a time-limited review of one version of the code.</li>
  <li>Changing code after the audit without a new review.</li>
</ul>
"""

D["upgrades-and-operations"] = """
### In depth

<p>Immutability protects users from sudden rule changes, but it also means bugs cannot be fixed. Many protocols therefore use a <b>proxy</b>. Users always talk to one fixed proxy address. The proxy holds the data and forwards every call with <code>delegatecall</code> to an <b>implementation</b> contract that holds the logic. To upgrade, an admin points the proxy at a new implementation; the address and data stay, the logic changes.</p>
<!-- diagram:proxy -->
<p>Upgradeability moves trust from code to people: whoever controls the upgrade key can change everything, including taking the funds. Good practice limits that power. Put the admin role in a <b>multisig</b>, add a <b>timelock</b> (for example 48 hours) so users can see an upgrade coming and exit, and publish who the signers are. Rating sites such as L2BEAT grade protocols on exactly these points. Proxies also have technical traps: the storage layout of a new implementation must match the old one, and implementations must not be initialisable by strangers.</p>
<p>Operating a live contract also means <b>monitoring</b> (alerts on large transfers or admin calls), an <b>incident plan</b> (who can pause, how fast, who informs users), and key management for every privileged role. Many losses happen not at launch but months later, when an admin key is stolen.</p>

### Worked example

<div class="worked">
<p><b>Case:</b> a bug is found in a live, upgradeable Escrow platform.</p>
<ol>
  <li><b>Hour 0:</b> a researcher reports a bug through the bounty programme. The team confirms it with a test on a mainnet fork.</li>
  <li><b>Hour 1:</b> two of three multisig signers call <code>pause()</code>. Deposits stop; funds stay safe.</li>
  <li><b>Day 1–3:</b> the fix is written, tested and reviewed. The storage layout is checked with a tool.</li>
  <li><b>Day 3:</b> the upgrade is proposed in the multisig and enters a 48-hour timelock, announced publicly.</li>
  <li><b>Day 5:</b> the upgrade executes; the source of the new implementation is verified; the contract is unpaused.</li>
</ol>
<p><b>Trade-off:</b> the timelock slows the fix but stops a stolen key from upgrading instantly.</p>
</div>

### Common mistakes

<ul>
  <li>“Upgradeable contracts are unsafe.” They are a trust choice; with a multisig and a timelock they can be safer than unfixable code.</li>
  <li>Adding a new variable at the top of the storage layout in an upgrade, which overwrites existing data.</li>
</ul>
"""
