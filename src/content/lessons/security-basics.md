---
title: "Security basics"
module: 7
order: 1
kind: "lesson"
minutes: "40 min"
legacy: "T8"
problem: "In 2016 an attacker took about a third of the funds in The DAO using the contract exactly as written. Which four mistakes cause most such losses?"
---

## Problem

<div class="cc-callout cc-callout--problem"><div><b>The question.</b> In 2016 an attacker took about a third of the funds in The DAO using the contract exactly as written. Which four mistakes cause most such losses?</div></div>

## Concept

<div class="goal"><b>Goal:</b> you can name four common bugs and the defence for each.</div>
    <div class="tw"><table>
      <tr><th>Bug</th><th>What happens</th><th>Defence</th></tr>
      <tr><td>Reentrancy</td><td>The contract sends ETH before it updates state. The receiver calls back and withdraws again.</td><td>Checks-effects-interactions, or OpenZeppelin <code>ReentrancyGuard</code>. Lab <a href="/lessons/lab-reentrancy/">7.4 Reentrancy</a>.</td></tr>
      <tr><td>Missing access control</td><td>Anyone can call an admin function, for example <code>withdraw</code> or <code>mint</code>.</td><td>Check <code>msg.sender</code> or use <code>Ownable</code>. Lab <a href="/lessons/lab-course-token/">5.2 Course token</a>.</td></tr>
      <tr><td><code>tx.origin</code> authentication</td><td>A malicious contract tricks the user into calling it, then acts with the user’s authority.</td><td>Use <code>msg.sender</code>.</td></tr>
      <tr><td>Oracle manipulation</td><td>The contract trusts one bad price or data source.</td><td>Use several sources or a trusted oracle network.</td></tr>
    </table></div>
    <p>Bugs cost real money because code is public and immutable. Audits, tests and bug bounties are standard practice. In 2025, most large losses came from operations (stolen keys, tricked signers) rather than code bugs: see <a href="/lessons/security-in-practice/">7.2 Security in practice</a>.</p>
    <div class="callout law"><h5>Law lens</h5><p>The DAO attacker in 2016 used the code exactly as written. Was it theft? Prosecutors have since charged people for similar “code exploits”, for example in the US Mango Markets case, with mixed results in court. The idea “code is law” is a good topic for debate, not a legal defence.</p></div>

<!-- deep:start -->
### In depth

<p>Smart contracts are attractive targets: the code is public, the money is in the contract, and transactions cannot be reversed. Four bug classes explain a large share of code-level losses.</p>
<p><b>Reentrancy.</b> When a contract sends ETH to another contract, the receiver’s code runs. If the sender has not yet updated its own records, the receiver can call back into the sender and withdraw again, in a loop. The defence is the <b>checks-effects-interactions</b> order: check conditions, update state, and only then call out; or use a reentrancy guard. Variants cross contracts (one contract updated, another not yet), as in the GMX attack of July 2025 (lab 7.5).</p>
<!-- diagram:reentrancy -->
<figure class="dg"><div class="sv"><svg viewBox="0 0 720 320" role="img" aria-label="Reentrancy attack sequence" xmlns="http://www.w3.org/2000/svg"><defs><marker id="ah-reentrancyattacksequ-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="m-a" d="M0 0L10 5L0 10z"/></marker><marker id="ah-reentrancyattacksequ-ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="m-ar" d="M0 0L10 5L0 10z"/></marker><marker id="ah-reentrancyattacksequ-ag" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="m-ag" d="M0 0L10 5L0 10z"/></marker><marker id="ah-reentrancyattacksequ-am" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="m-am" d="M0 0L10 5L0 10z"/></marker></defs><rect class="k-danger" x="20" y="12" width="200" height="40" rx="12"/><text class="tb" x="120.0" y="36.7" text-anchor="middle" font-size="13.5">Attacker contract</text><line class="k-life" x1="120" y1="52" x2="120" y2="310"/><rect class="k-cs" x="370" y="12" width="200" height="40" rx="12"/><text class="tb" x="470.0" y="36.7" text-anchor="middle" font-size="13.5">VulnerableBank</text><line class="k-life" x1="470" y1="52" x2="470" y2="310"/><line class="k-a" x1="120" y1="80" x2="468" y2="80" marker-end="url(#ah-reentrancyattacksequ-a)"/><text class="tl" x="294.0" y="73.0" text-anchor="middle" font-size="12.5">withdraw()</text><text class="tl" x="485" y="104" text-anchor="start" font-size="12.5">balance = 1 ✓</text><line class="k-ar" x1="470" y1="124" x2="122" y2="124" marker-end="url(#ah-reentrancyattacksequ-ar)"/><text class="tl" x="296.0" y="117.0" text-anchor="middle" font-size="12.5">send 1 ETH</text><text class="tl" x="135" y="150" text-anchor="start" font-size="12.5">receive() runs …</text><line class="k-a" x1="120" y1="170" x2="468" y2="170" marker-end="url(#ah-reentrancyattacksequ-a)"/><text class="tl" x="294.0" y="163.0" text-anchor="middle" font-size="12.5">withdraw() again</text><text class="tl" x="485" y="194" text-anchor="start" font-size="12.5">balance still 1 ✓</text><line class="k-ar" x1="470" y1="214" x2="122" y2="214" marker-end="url(#ah-reentrancyattacksequ-ar)"/><text class="tl" x="296.0" y="207.0" text-anchor="middle" font-size="12.5">send 1 ETH</text><text class="tl" x="295" y="250" text-anchor="middle" font-size="13">… repeats until the bank is empty</text><text class="tl" x="485" y="286" text-anchor="start" font-size="12.5">balance = 0  (too late)</text><text class="tlg" x="485" y="304" text-anchor="start" font-size="12.5">fix: set to 0 before sending</text></svg></div><figcaption><b>The bank pays before it updates its books.</b> Sending ETH runs the attacker’s code, which calls <code>withdraw()</code> again while the balance is still 1. Checks-effects-interactions closes the loop.</figcaption></figure>
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
<!-- deep:end -->

### Watch and read

<div class="vids">
      <a class="vid" href="https://www.youtube.com/watch?v=4Mm3BCyHtDY" target="_blank" rel="noopener"><span class="play"></span><span><b>Reentrancy (Hack Solidity)</b><small>Smart Contract Programmer</small></span></a>
      <a class="vid" href="https://ethereum.org/videos/dao-hack-ethereum-classic/" target="_blank" rel="noopener"><span class="play"></span><span><b>The DAO hack: story of Ethereum Classic</b><small>10 min</small></span></a>
      <a class="vid read" href="https://consensys.github.io/smart-contract-best-practices/attacks/reentrancy/" target="_blank" rel="noopener"><span class="play"></span><span><b>Best practices: reentrancy</b><small>ConsenSys article</small></span></a>
    </div>

## Try it

<p>Read the vulnerable <code>withdraw</code> function in <a href="../lab-reentrancy/">lab 7.4</a> and write, in one sentence, the order in which it should do its three steps. Then run the lab.</p>

## Apply

<div class="aud"><div class="cs"><h5>Technology lens</h5><ul><li>Which defence would you add first to a new contract, and why?</li></ul></div><div class="bi"><h5>Business lens</h5><ul><li>Compare the cost of an audit with the funds at risk.</li></ul></div><div class="lw"><h5>Law lens</h5><ul><li>Was the DAO attacker a thief or a user of the code as written?</li></ul></div></div>

## Ship

<p>Write three sentences in your lab log: the main idea, one example for each lens (technology, business, law), and one open question. Then take the quiz below.</p>
