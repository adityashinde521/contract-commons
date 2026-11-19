---
title: "Capstone: the agentic escrow"
minutes: "4 weeks"
---

## Brief

<div class="goal"><b>Scenario:</b> a company’s AI agent buys a dataset from another company’s agent. An escrow contract holds the payment until delivery is verified. Your team designs, builds, documents and defends the system.</div>
    <h4>Deliverables</h4>
    <p>The team hands in all three parts. Split the writing, but every member must be able to explain every part.</p>
    <div class="aud">
      <div class="cs"><h5>Technology</h5><ul><li>Combine Escrow (<a href="/lessons/lab-escrow/">4.3</a>) and AgentWallet (<a href="/lessons/ai-agents/">13.1 AI agents</a>).</li><li>Add a deadline and a pause switch.</li><li>Deploy and verify on Sepolia.</li><li>Tests for each rule (Remix or Foundry).</li></ul></div>
      <div class="bi"><h5>Business</h5><ul><li>Process model (BPMN) with all failure paths.</li><li>Cost model per transaction on L1 and <a href="/lessons/lab-escrow/">4.3 Escrow</a>.</li><li>Comparison with a traditional escrow service.</li></ul></div>
      <div class="lw"><h5>Law</h5><ul><li>The agent mandate: what the agent may do.</li><li>Purchase terms and a dispute clause.</li><li>A clause-to-code map: each clause is “in code”, “partly in code” or “not in code”.</li></ul></div>
    </div>
    <p>You can build parts of the system from market tools instead of code: <a href="/lessons/lab-openzeppelin-wizard/">5.3 OpenZeppelin Wizard</a> or <a href="/lessons/lab-thirdweb/">5.4 thirdweb</a> for the contracts, <a href="/lessons/lab-safe/">11.3 Safe</a> or <a href="/lessons/lab-aragon/">11.4 Aragon DAO</a> as the company treasury, <a href="/lessons/lab-attestations/">9.4 Attestations</a> for delivery evidence, <a href="/lessons/lab-accord/">12.4 Accord Project</a> for the legal template, and <a href="/lessons/lab-tenderly/">8.3 Tenderly</a> simulations to test every role.</p>
    <h4>Milestones</h4>
    <div class="tw"><table>
      <tr><th>Week</th><th>Milestone</th></tr>
      <tr><td>1</td><td>Scenario, roles, process sketch, list of clauses.</td></tr>
      <tr><td>2</td><td>First contract version on Remix VM; draft legal text.</td></tr>
      <tr><td>3</td><td>Sepolia deployment; clause-to-code map; cost model.</td></tr>
      <tr><td>4</td><td>10-minute presentation with a live demo and one failure case.</td></tr>
    </table></div>

## Assessment

<div class="tw"><table>
      <tr><th>Part</th><th>Weight</th><th>Criteria</th></tr>
      <tr><td>Team: system</td><td>40%</td><td>It works on Sepolia. The three parts match: the code does what the text says, and the model shows both.</td></tr>
      <tr><td>Individual: oral check</td><td>40%</td><td>Each student answers questions on any of the three parts, at the level of the learning outcomes.</td></tr>
      <tr><td>Team: presentation</td><td>20%</td><td>Clear problem, live demo, one revert explained, answers in all three lenses.</td></tr>
    </table></div>
