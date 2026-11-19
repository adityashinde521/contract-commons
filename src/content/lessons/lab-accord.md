---
title: "Smart legal contract templates (Accord Project)"
module: 12
order: 4
kind: "lab-gui"
minutes: "45 min"
legacy: "G6"
problem: "A law firm has 2,000 leases in Word files. It wants the key terms as data that software can check."
---

## Problem

<div class="cc-callout cc-callout--problem"><div><b>The question.</b> A law firm has 2,000 leases in Word files. It wants the key terms as data that software can check.</div></div>

## Concept

<div class="ov">
      <div><b>You will</b>Write a contract clause as a machine-readable template: legal text, data model and data.</div>
      <div><b>Tool</b><a href="https://playground.accordproject.org" target="_blank" rel="noopener">Accord Project Template Playground</a>, open source, in the browser.</div>
      <div><b>You need</b>A browser. No wallet, no blockchain.</div>
    </div>
    <p>The Accord Project is an open-source standard for smart legal contracts. A template has three layers: a <b>data model</b> (Concerto) that defines variables and types, <b>template text</b> (TemplateMark) that is the legal wording with placeholders, and <b>data</b> (JSON) for one concrete contract. This is the bridge between a lawyer’s document and code.</p>

## Build

<h4>A. Explore a sample</h4>
    <ol class="steps">
      <li>Open <a href="https://playground.accordproject.org" target="_blank" rel="noopener">playground.accordproject.org</a>.<span class="exp">Panels for Concerto Model, TemplateMark, JSON Data and a Preview.</span></li>
      <li>From the sample list, load <span class="ui">Hello World</span>.</li>
      <li>In the JSON Data panel, change the <code>name</code> value to your own name.<span class="exp">The Preview updates at once.</span></li>
      <li>Load two or three other samples. For each, find one variable in the model, the text and the data.</li>
    </ol>
    <h4>B. Write your own clause</h4>
    <ol class="steps">
      <li>Start from Hello World. In the model, define fields for a rental deposit: <code>String landlord</code>, <code>String tenant</code>, <code>Double monthlyRent</code>, <code>Double deposit</code>, <code>Integer returnDays</code>.</li>
      <li>In the TemplateMark, write: “The Tenant {{tenant}} pays a deposit of {{deposit}} EUR to the Landlord {{landlord}}. The Landlord returns the deposit within {{returnDays}} days after the end of the lease, less proven damages.”</li>
      <li>Fill the JSON data with matching values.<span class="exp">The Preview shows your finished clause. Red errors mean the model, text and data do not match.</span></li>
      <li>Change <code>deposit</code> to text, for example <code>"three months"</code>.<span class="exp">A type error. The model protects the contract from invalid data.</span></li>
    </ol>

## Apply

<div class="aud">
      <div class="cs"><h5>CS</h5><ul><li>Generate a Solidity constructor from the Concerto model. Which types map cleanly?</li></ul></div>
      <div class="bi"><h5>BI</h5><ul><li>A company has 2,000 leases. What does a template give the business: search, reporting, reminders?</li></ul></div>
      <div class="lw"><h5>Law</h5><ul><li>Add the §551 BGB cap as a rule: deposit ≤ 3 × monthlyRent. Is this a check in the model, in logic or in the text?</li><li>Compare with the research on Stipula and Catala (F7).</li></ul></div>
    </div>

## Ship

<ul class="outc">
      <li>You can explain the three layers of a smart legal contract template.</li>
      <li>You can turn a natural-language clause into a template with typed variables.</li>
      <li>You can say which parts a machine can check (types, amounts, dates) and which need a human (“proven damages”).</li>
    </ul>
