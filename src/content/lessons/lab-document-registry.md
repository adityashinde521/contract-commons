---
title: "Document registry: proof of existence"
module: 4
order: 5
kind: "lab-remix"
minutes: "30 min"
legacy: "L4"
problem: "You need to prove later that a document existed today, without publishing it."
---

## Problem

<div class="cc-callout cc-callout--problem"><div><b>The question.</b> You need to prove later that a document existed today, without publishing it.</div></div>

## Concept

<div class="ov">
      <div><b>You will</b>Register the fingerprint of a document and verify it later.</div>
      <div><b>Concepts</b><ul><li>Hashes as fingerprints</li><li><code>mapping</code> and <code>struct</code></li><li>What a timestamp proves</li></ul></div>
      <div><b>You produce</b>A registered hash and a failed verification of a changed text.</div>
    </div>
    <div class="pre-wrap"><pre><code>// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

/// @title DocumentRegistry: prove that a document existed at a time.
/// Stores only the hash, never the document.
contract DocumentRegistry {
    struct Record {
        address owner;
        uint256 timestamp;
    }

    mapping(bytes32 =&gt; Record) public records;

    event DocumentRegistered(bytes32 indexed docHash, address indexed owner, uint256 timestamp);

    function register(bytes32 docHash) external {
        require(records[docHash].timestamp == 0, "Already registered");
        records[docHash] = Record(msg.sender, block.timestamp);
        emit DocumentRegistered(docHash, msg.sender, block.timestamp);
    }

    function verify(bytes32 docHash)
        external
        view
        returns (bool exists, address owner, uint256 timestamp)
    {
        Record memory r = records[docHash];
        return (r.timestamp != 0, r.owner, r.timestamp);
    }

    /// Helper for the lab only. In real use, hash the file off-chain.
    function hashText(string calldata text) external pure returns (bytes32) {
        return keccak256(bytes(text));
    }
}</code></pre><button class="copy" type="button">Copy</button></div>

## Build

<ol class="steps">
      <li>Create <code>DocumentRegistry.sol</code>, paste, compile, deploy (account 1, Value 0).</li>
      <li>Call <span class="ui">hashText</span> with <code>Contract v1: rent 900 EUR</code>. Copy the <code>0x…</code> result.<span class="exp">A 66-character value starting with 0x. Free: it is a <code>pure</code> function.</span></li>
      <li>Call <span class="ui">register</span> with this hash.<span class="exp">Logs: <code>DocumentRegistered</code> with your address and a timestamp.</span></li>
      <li>Call <span class="ui">verify</span> with the same hash.<span class="exp"><code>exists: true</code>, your address, a timestamp in Unix seconds.</span></li>
      <li>Hash <code>Contract v1: rent 990 EUR</code> and verify that hash.<span class="exp"><code>exists: false</code>. One character changed, completely different hash.</span></li>
      <li>Register the first hash again.<span class="exp">Revert: “Already registered”. The first registration cannot be overwritten.</span></li>
    </ol>
    <div class="callout tip"><h5>Convert the timestamp</h5><p>Paste the Unix timestamp into any epoch converter, or compare it with today’s date: about 1.79 billion seconds in November 2026.</p></div>

## Apply

<div class="aud">
      <div class="cs"><h5>Technology lens</h5><ul><li><code>hashText</code> sends the text in the transaction input when called as a transaction. Why is that a privacy leak? Hash off-chain instead.</li></ul></div>
      <div class="bi"><h5>Business lens</h5><ul><li>Compare with a notary, a timestamp service (RFC 3161) or registered mail: cost, speed, legal weight.</li></ul></div>
      <div class="lw"><h5>Law lens</h5><ul><li>Is the record admissible evidence in a German court (free evaluation of evidence, §286 ZPO)?</li><li>GDPR: is the hash of a short personal text still personal data?</li></ul></div>
    </div>

## Ship

<ul class="outc">
      <li>You can explain what a record proves (this text existed at this time) and what it does not (authorship, agreement, legality).</li>
      <li>You can explain why real systems hash the file off-chain.</li>
    </ul>
