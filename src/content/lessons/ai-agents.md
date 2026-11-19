---
title: "AI agents with wallets"
module: 13
order: 1
kind: "lesson"
minutes: "60 min"
legacy: "F3"
problem: "Your AI assistant books travel and pays for data. What stops it from being tricked into emptying your wallet?"
---

## Problem

<div class="cc-callout cc-callout--problem"><div><b>The question.</b> Your AI assistant books travel and pays for data. What stops it from being tricked into emptying your wallet?</div></div>

## Concept

<div class="goal"><b>Goal:</b> you can explain how AI agents use smart contracts and which risks this creates.</div>
    <h4>What is new</h4>
    <ul>
      <li>AI agents now act for people: they search, compare, buy data and call paid APIs. To pay, an agent needs a wallet.</li>
      <li><b>ERC-8004 “Trustless Agents”</b> went live on Ethereum mainnet on 29 January 2026. It defines three on-chain registries: <b>identity</b> (each agent gets an ERC-721 ID), <b>reputation</b> (feedback) and <b>validation</b> (independent checks of work).</li>
      <li><b>x402</b> (from Coinbase) uses the HTTP status code 402 “Payment Required”. An API asks for payment inside the normal request-response flow. The agent pays per request, often in stablecoins, without an account or API key.</li>
      <li>Together: an agent finds a service (ERC-8004), checks its reputation, and pays per call (x402).</li>
    </ul>
    <h4>Risks</h4>
    <ul>
      <li><b>Prompt injection:</b> a web page tells the agent “send all funds to X”. If the agent holds the key, it may obey.</li>
      <li><b>Key custody:</b> who holds the private key? The user, the developer, a cloud wallet?</li>
      <li><b>Runaway spending:</b> a bug loops payments.</li>
      <li><b>Defence:</b> put limits in a smart contract, not in the prompt: allow-lists, daily limits, a pause switch, human approval above a threshold. That is the mini-lab.</li>
    </ul>

### Watch and read

<div class="vids">
      <a class="vid read" href="https://chainstack.com/erc-8004-ai-agents-on-chain/amp/" target="_blank" rel="noopener"><span class="play"></span><span><b>ERC-8004: on-chain infrastructure for AI agents</b><small>Chainstack explainer</small></span></a>
      <a class="vid read" href="https://cointelegraph.com/opinion/ethereum-trustless-agents-ai-payments" target="_blank" rel="noopener"><span class="play"></span><span><b>Trustless Agents standard and AI payments</b><small>Cointelegraph opinion, Feb 2026</small></span></a>
    </div>

## Try it

<div class="goal"><b>Goal:</b> build a wallet where the agent can pay, but only inside rules that the owner controls. (Code track, Remix VM.)</div>
    <div class="pre-wrap"><pre><code>// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

/// @title AgentWallet: an AI agent may pay, but only inside owner rules.
/// Rules: allowed payees, a daily limit and a pause switch.
contract AgentWallet {
    address public immutable owner;
    address public agent;
    uint256 public dailyLimit;
    uint256 public spentToday;
    uint256 public dayStart;
    bool public paused;
    mapping(address =&gt; bool) public allowedPayee;

    event Paid(address indexed to, uint256 amount, string memo);
    event AgentChanged(address indexed agent);
    event PausedSet(bool paused);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner");
        _;
    }

    constructor(address _agent, uint256 _dailyLimit) {
        require(_agent != address(0), "Zero address");
        owner = msg.sender;
        agent = _agent;
        dailyLimit = _dailyLimit;
        dayStart = block.timestamp;
    }

    receive() external payable {}

    function setPayee(address payee, bool allowed) external onlyOwner {
        allowedPayee[payee] = allowed;
    }

    function setAgent(address newAgent) external onlyOwner {
        agent = newAgent;
        emit AgentChanged(newAgent);
    }

    function setDailyLimit(uint256 newLimit) external onlyOwner {
        dailyLimit = newLimit;
    }

    function setPaused(bool p) external onlyOwner {
        paused = p;
        emit PausedSet(p);
    }

    function pay(address payable to, uint256 amount, string calldata memo) external {
        require(msg.sender == agent, "Only agent");
        require(!paused, "Paused");
        require(allowedPayee[to], "Payee not allowed");
        if (block.timestamp &gt;= dayStart + 1 days) {
            dayStart = block.timestamp;
            spentToday = 0;
        }
        require(spentToday + amount &lt;= dailyLimit, "Daily limit");
        spentToday += amount;                              // effect first
        (bool ok, ) = to.call{value: amount}("");          // interaction last
        require(ok, "Transfer failed");
        emit Paid(to, amount, memo);
    }

    function withdraw(uint256 amount) external onlyOwner {
        (bool ok, ) = payable(owner).call{value: amount}("");
        require(ok, "Transfer failed");
    }
}</code></pre><button class="copy" type="button">Copy</button></div>
    <ol class="steps">
      <li>Account 1 (owner) deploys with <code>_agent</code> = account 2 and <code>_dailyLimit</code> = <code>1000000000000000000</code> (1 ether). Value 0.</li>
      <li>Account 1 funds the wallet: Value 3 Ether, then under <span class="ui">Low level interactions</span> at the bottom of the deployed contract, leave calldata empty and click <span class="ui">Transact</span>. Value back to 0.<span class="exp">The contract balance shows 3 ETH.</span></li>
      <li>Account 1 calls <span class="ui">setPayee</span>(account 3, true).</li>
      <li>Account 2 (agent) calls <span class="ui">pay</span>(account 3, <code>600000000000000000</code>, “data API”).<span class="exp">Logs: <code>Paid</code>. Account 3 +0.6 ETH.</span></li>
      <li>Account 2 calls <span class="ui">pay</span> again with 0.6 ether.<span class="exp">Revert: “Daily limit”.</span></li>
      <li>Account 2 tries to pay account 4.<span class="exp">Revert: “Payee not allowed”.</span></li>
      <li>Account 1 calls <span class="ui">setPaused</span>(true). Account 2 tries any payment.<span class="exp">Revert: “Paused”.</span></li>
    </ol>
    <div class="callout tip"><h5>Key idea</h5><p>A prompt can be manipulated. A smart contract cannot be persuaded. The rules hold even if the agent is tricked.</p></div>

## Apply

<div class="aud">
      <div class="cs"><h5>CS</h5><ul><li>Add a rule: payments above 0.5 ether need the owner’s approval.</li></ul></div>
      <div class="bi"><h5>BI</h5><ul><li>Pay-per-call pricing instead of subscriptions. Which business models change?</li></ul></div>
      <div class="lw"><h5>Law</h5><ul><li>An AI agent is not a legal person. When it pays or “agrees”, who is bound: the user, the developer, the model provider? Compare with agency law and with automated declarations of intent.</li><li>The EU AI Act applies in phases. Which duties can apply to an agent that moves money?</li></ul></div>
    </div>

## Ship

<p>Write three sentences in your lab log: the main idea, one example from your discipline, and one open question. Then take the quiz below.</p>
