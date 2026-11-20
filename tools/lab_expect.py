"""Expected results for lab steps that had none, plus "checked on" notes and interface updates.
Keys are "slug#n": the n-th step across all <ol class="steps"> lists in that lab (1-based).
Run: python3 tools/lab_expect.py  (idempotent: steps that already have an expected result are skipped).
"""
import pathlib, re, json

ROOT = pathlib.Path(__file__).resolve().parent.parent
CHECKED = '20 November 2026'

E = {
 "lab-eth-build#1": "An empty canvas with a menu. A double-click or right-click opens the module list.",
 "lab-eth-build#2": "Two boxes joined by a line. The hash box shows a 0x… value of 64 hex characters, which changes with every key you type.",
 "lab-eth-build#4": "Three values: a private key (64 hex characters), a longer public key, and a 0x address of 40 hex characters derived from it.",
 "lab-read-the-chain#2": "A number such as 15,000,000 (50%). Ethereum targets about half-full blocks; fuller blocks raise the base fee.",
 "lab-read-the-chain#6": "The token page shows total supply, number of holders, the contract address with a green check (verified) and a list of recent transfers.",
 "lab-remix-tour#3": "A green check on the compiler icon after each save. Errors appear in red under the compile button.",
 "lab-remix-tour#5": "Account shows 0x5B38… with 100 ether in the Remix VM; Value shows 0 and Wei.",
 "lab-remix-tour#6": "An empty terminal with a welcome text. After the next deploy, a line with a green check and “[vm] from: 0x5B3… to: … value: 0 wei”.",
 "lab-remix-tour#7": "A ZIP file in your downloads, or a Git panel with your first commit.",
 "lab-escrow#2": "The Deployed Contracts list is empty.",
 "lab-escrow#3": "Two full addresses (42 characters each, starting 0x) in your text file.",
 "lab-escrow#4": "The Account field shows 0x5B38… The deployer becomes the buyer.",
 "lab-escrow#5": "Value 0 Wei; the Contract dropdown shows Escrow – Escrow.sol.",
 "lab-escrow#6": "Three empty input fields and a transact button.",
 "lab-escrow#12": "A second Escrow under Deployed Contracts with a new address. Its state() returns 0 (AwaitingPayment).",
 "lab-rental-deposit#1": "A green compiler check and one address in your clipboard (ends in 35cb2 in the Remix VM).",
 "lab-rental-deposit#2": "A RentalDeposit instance. depositAmount() returns 2000000000000000000; leaseEnd() equals the block time (lease already ended).",
 "lab-rental-deposit#5": "A new instance; leaseEnd() is about 30 × 86,400 seconds later than now. paid() returns true after the tenant’s payment.",
 "lab-document-registry#1": "A DocumentRegistry instance with buttons hashText, register, verify and records.",
 "lab-openzeppelin-wizard#1": "The Wizard shows ERC721 settings on the left and Solidity code on the right.",
 "lab-openzeppelin-wizard#2": "The code updates live: contract CourseCertificate is ERC721, with “Course Certificate”, “CERT” in the constructor.",
 "lab-openzeppelin-wizard#4": "No ERC721Burnable import in the code. Your team’s one-sentence answer is in the lab log.",
 "lab-openzeppelin-wizard#6": "A deployed CourseCertificate with orange buttons safeMint and transferFrom and blue buttons such as owner and name.",
 "lab-thirdweb#1": "Your thirdweb dashboard (thirdweb.com/team) with a project. The contract catalogue is still at thirdweb.com/explore.",
 "lab-thirdweb#3": "The deploy form shows your address as primary sale recipient and Sepolia as the network.",
 "lab-thirdweb#6": "One claim phase listed for token 0: price 0, limit 1 per wallet, start time now.",
 "lab-foundry-test#3": "src/ contains only Escrow.sol; forge build prints “Compiler run successful”.",
 "lab-foundry-test#5": "A new file test/Escrow.t.sol. forge build compiles it without errors.",
 "lab-reentrancy#1": "A green compiler check. The Contract dropdown lists VulnerableBank, Attacker and FixedBank.",
 "lab-reentrancy#2": "A VulnerableBank instance; its address is in your clipboard.",
 "lab-reentrancy#4": "An Attacker instance whose bank() returns the bank’s address.",
 "lab-reentrancy#6": "The debugger’s call stack shows withdraw inside receive inside withdraw, several levels deep, before the line balances[msg.sender] = 0 runs.",
 "lab-reentrancy#7": "A FixedBank instance; balanceOf the contract (or its Balance in the list) shows 5 ETH.",
 "lab-reentrancy#8": "A second Attacker whose bank() returns the FixedBank address.",
 "lab-phalcon#1": "Phalcon shows the call tree of your transaction with the function confirmDelivery and one ETH transfer to the seller.",
 "lab-phalcon#4": "An attack transaction hash on Arbitrum that starts with 0x, dated 9 July 2025.",
 "lab-phalcon#6": "A highlighted point where the attacker’s contract is called back, followed by further calls into the GMX Vault inside that callback.",
 "lab-phalcon#7": "A graph where value flows from GMX contracts to the attacker’s address; the balance-change view shows the attacker gaining tens of millions of dollars in tokens.",
 "lab-phalcon#8": "Each claim in the write-up matched to one node in the call tree or one edge in the fund flow, in your lab log.",
 "lab-sepolia#1": "MetaMask shows Sepolia at the top and a balance of at least 0.05 SepoliaETH.",
 "lab-sepolia#6": "A new Contract Verification icon in the left bar.",
 "lab-sepolia#10": "Two addresses in your text file: seller and arbiter.",
 "lab-sepolia#11": "MetaMask asks to confirm a contract deployment with a small fee. After about 12 seconds the Escrow appears under Deployed Contracts with a Sepolia address.",
 "lab-sepolia#13": "Etherscan shows a green check and “Contract Source Code Verified” on the Escrow’s Contract tab.",
 "lab-tenderly#1": "An empty Tenderly dashboard with a project. No payment details asked. (The free plan’s features change; if the debugger is limited, use the Remix debugger for part B.)",
 "lab-tenderly#5": "The line state = State.Complete; is highlighted; the state panel shows state changing from 1 to 2.",
 "lab-tenderly#6": "msg.sender shows the buyer’s address; price shows 1000000000000000 (0.001 ether).",
 "lab-tenderly#7": "A verified Escrow on Sepolia in state AwaitingDelivery (state() returns 1).",
 "lab-tenderly#8": "The simulator form with From, To (your Escrow), function refund and no value.",
 "lab-see-inside#1": "The ETH.BUILD canvas with a short video on the start page.",
 "lab-see-inside#4": "The debugger opens on the attack transaction with a step slider and the call stack on the left.",
 "lab-see-inside#6": "sol2uml --version prints a version number. An Etherscan API key (32 characters) saved somewhere private, not in your code.",
 "lab-see-inside#9": "Every public function in the diagram has a note: anyone, buyer, seller, arbiter or owner.",
 "lab-attestations#2": "A form with a schema builder: field type, field name, and a Revocable switch.",
 "lab-attestations#3": "Four rows in the schema builder in that order.",
 "lab-attestations#5": "A form with the recipient field and one input per schema field.",
 "lab-attestations#6": "All fields filled; documentHash starts with 0x and has 64 hex characters.",
 "lab-attestations#11": "An attestation with an “Offchain” badge and a UID; no MetaMask fee, only a signature request.",
 "lab-quickdapp#1": "The Escrow is under Deployed Contracts with a Sepolia address. QuickDApp is built for public networks; the Remix VM has limited support.",
 "lab-quickdapp#2": "The QuickDApp panel opens with the Escrow as Primary Contract and options for the front-end location.",
 "lab-quickdapp#3": "After Generate DApp, RemixAI proposes files; approve them (or Approve All). A live preview opens in the QuickDApp tab.",
 "lab-quickdapp#6": "The release path ends with the seller paid; the refund path shows a readable “Only arbiter” error when a non-arbiter clicks Refund.",
 "lab-quickdapp#7": "A table in your lab log with one row per button.",
 "lab-quickdapp#8": "After Ask AI to Update → Update with AI, a refreshed preview with your change. Use Refresh Preview if it does not update.",
 "lab-dashboards#1": "A table of rollups ordered by value secured, each with a stage (0, 1 or 2) and a risk rosette.",
 "lab-dashboards#3": "Three notes per rollup, for example “Security Council can upgrade without delay; users cannot exit first”.",
 "lab-dashboards#4": "A list of hacks with date, amount, chain and technique, plus totals by year.",
 "lab-dashboards#6": "A two-line comparison in your lab log: total from key and infrastructure attacks versus contract-logic bugs in 2025, with your conclusion.",
 "lab-dashboards#7": "A list of public dashboards with charts and the SQL query behind each.",
 "lab-dashboards#9": "Your own dashboard with one chart that uses your changed parameter.",
 "lab-safe#1": "The Safe app shows Sepolia and your connected address. You may be asked to accept Safe Labs’ terms first.",
 "lab-safe#2": "A setup screen with the name and network.",
 "lab-safe#3": "Three owner rows and “2 out of 3 owner(s)” for the threshold. After creation and a MetaMask confirmation, your Safe has its own address.",
 "lab-safe#6": "A transaction in the queue with 1 of 2 confirmations.",
 "lab-safe#8": "The queued transaction shows a Confirm button for account 2.",
 "lab-safe#10": "The proposal shows as rejected; no ETH moved. On Etherscan the Safe’s nonce still advances.",
 "lab-safe#11": "The input data of execTransaction contains a signatures field with two 65-byte signatures (130 bytes in total).",
 "lab-aragon#1": "The DAO creation wizard opens.",
 "lab-aragon#2": "Sepolia is selected. If the app does not list Ethereum Sepolia, choose another testnet it offers, such as Hoodi or Base Sepolia, and get test ETH for that network first.",
 "lab-aragon#3": "The name and description appear in the summary on the right or at the last step.",
 "lab-aragon#4": "Three member addresses; proposal creation limited to members; threshold set in the next step.",
 "lab-aragon#10": "The proposal stays open or expires without execution; the member list is unchanged.",
 "lab-accord#2": "Hello World loads: the Concerto Model, TemplateMark and JSON Data panels fill, and the Preview shows “Hello John Doe!” or similar.",
 "lab-accord#4": "For each sample, one variable written down three times: its type in the model, {{name}} in the text, its value in the data.",
 "lab-accord#5": "The model panel shows no errors and the five fields with their types.",
 "lab-accord#6": "The Preview shows the sentence with your values. A typo in a variable name shows an error instead.",
}

NOTE = {
 'lab-gui': f'<div class="checked"><b>Checked on {CHECKED}</b> against the tool’s official documentation. Tools change their screens often. If a button has a different name, look for the closest one and note the difference in your lab log.</div>',
 'lab-remix': f'<div class="checked"><b>Checked on {CHECKED}.</b> The contract code in this lab compiles with Solidity 0.8.24 to 0.8.30. Remix screens change between releases: if a label differs, look for the closest one and note it in your lab log.</div>',
}


def main():
    M = json.loads((ROOT / 'src/data/modules.json').read_text())
    labs = [l for m in M for l in m['lessons'] if l.startswith('lab-')]
    added = 0
    for slug in labs:
        p = ROOT / 'src/content/lessons' / f'{slug}.md'
        s = p.read_text(encoding='utf-8')
        kind = re.search(r'kind: "([\w-]+)"', s).group(1)
        n = [0]
        def per_ol(m):
            head, inner = m.group(1), m.group(2)
            parts = re.split(r'(?=<li>)', inner)
            out = []
            for part in parts:
                if part.startswith('<li>'):
                    n[0] += 1
                    key = f'{slug}#{n[0]}'
                    if key in E and 'class="exp"' not in part:
                        exp = f'<span class="exp">{E[key]}</span>'
                        if '</li>' in part:
                            i = part.rindex('</li>'); part = part[:i] + exp + part[i:]
                        else:
                            part = part.rstrip() + exp
                        nonlocal_added[0] += 1
                out.append(part)
            return head + ''.join(out) + '</ol>'
        nonlocal_added = [0]
        s = re.sub(r'(<ol class="steps"[^>]*>)(.*?)</ol>', per_ol, s, flags=re.S)
        added += nonlocal_added[0]
        s = re.sub(r'\n*<div class="checked">.*?</div>\n*', '\n\n', s, flags=re.S)
        note = NOTE.get(kind)
        if note:
            s = re.sub(r'## Build\n+', '## Build\n\n' + note + '\n\n', s, count=1)
        p.write_text(s, encoding='utf-8')
    print('expected results added:', added, 'of', len(E))

main()
