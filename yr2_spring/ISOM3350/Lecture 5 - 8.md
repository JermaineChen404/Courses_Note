---
title: FinTech and Cryptoventures – Exam Prep (Lect 5–8)
tags:
  - fintech
  - blockchain
  - cryptocurrency
  - smart-contracts
  - lightning-network
  - exam-prep
aliases:
  - Exam Prep Lect 5-8
  - Crypto and Smart Contracts Notes
---

# FinTech and Cryptoventures – Exam Prep (Lect 5–8)

> [!info] How to use this note
> This note follows a lecture-by-lecture, numbered-section format for fast review. Focus on the **definitions**, **mechanisms**, **comparisons**, and **trade-offs**.

---

# Lecture 5: Cryptocurrency III – Transactions, Consensus, and Bitcoin Controversies

## 1. Big Picture
Lecture 5 explains how **Bitcoin transactions actually work**, why Bitcoin uses a **transaction-based ledger** instead of a standard account-based ledger, how the network reaches **distributed consensus**, and how Bitcoin deals with **double-spending**, **forks**, and **protocol upgrades**.

> [!important] Exam Focus
> Know the difference between **inputs vs outputs**, **account-based vs transaction-based ledger**, **soft fork vs hard fork**, and why **6 confirmations** matter.

---

## 2. How a Bitcoin Transaction Works
A basic Bitcoin payment works like this:
1. The receiver gives the sender a **public Bitcoin address**.
2. The sender creates a transaction specifying the destination address and amount.
3. The sender signs the transaction with the **private key** associated with the coins being spent.
4. The transaction is broadcast to the Bitcoin network.
5. Nodes/miners verify it before including it in a block.

### Core idea
- Anyone can send BTC to a public address.
- Only the holder of the corresponding **private key** can spend coins from that address.
- Bitcoin transactions are **irreversible** once confirmed.

---

## 3. What Is Inside a Bitcoin Transaction?
A Bitcoin transaction has two main parts:

### Inputs
- Each input refers to a **previous transaction output**.
- Each referenced input must be **signed by the owner** of that previous output.
- There can be **multiple inputs**.

### Outputs
- Each output specifies:
  - a destination address
  - an amount
- There can be **multiple outputs**.

### Accounting rule
- **Sum of inputs >= sum of outputs**
- Any leftover amount becomes the **transaction fee**, which goes to the miner.

> [!tip] Memory hook
> **Inputs = where the coins come from**
> **Outputs = where the coins go**

---

## 4. Special Transaction Types
### Multisig transactions
- Spending requires **M out of N signatures**.
- Example: **2-of-3 escrow** involving buyer, seller, and third party.
- Useful when no single party should control the funds alone.

### Null transactions / data storage
- Use a script that cannot be redeemed.
- Can burn a small amount of BTC and store arbitrary data in the script field.
- The lecture presents these as **simple examples of smart-contract-like functionality**.

> [!warning] Common trap
> Bitcoin is not only “send coins from A to B.” Even in Bitcoin, scripts allow limited programmable logic.

---

## 5. UTXO Logic: Why Bitcoin Uses a Transaction-Based Ledger
Bitcoin tracks balances through **unspent transaction outputs (UTXOs)** rather than a running account balance.

![[image.png]]

### Key implications
- Coins in a Bitcoin address are tied to **specific outputs** from earlier transactions.
- These outputs are **not mixed up** into one abstract balance.
- Bitcoin inputs are treated as **indivisible references** to prior outputs.

> [!NOTE] Bitcoin inputs are indivisible
> If you use one previous output as an input, you do **not** spend only part of that output. You **consume the whole output** and create new output(s) from it.
>
> **Example**
> - Suppose you control one previous output worth **8 BTC**
> - You want to pay **6 BTC** to David
>
> You cannot take just **6 BTC** out of that old output and leave the original output with **2 BTC** left.
>
> Instead, you spend the **entire 8 BTC output** as the input, then create:
> - **6 BTC → David**
> - **2 BTC → back to yourself as change**
> - minus any **transaction fee**
### Change address logic
If a user spends an output that is larger than the desired payment:
- one output goes to the recipient
- another output returns the remainder to the sender

This returned remainder is commonly called **change**.

### Why not an account-based ledger?
In an account-based ledger, verifying a balance may require scanning backward through all prior account activity. In Bitcoin’s transaction-based design, **hash pointers** to earlier outputs make validity checks more localized and efficient.

> [!important] Compare
> **Account-based ledger**: tracks net balances per account.
> **Transaction-based ledger (UTXO)**: tracks spendable outputs from earlier transactions.

---

## 6. Consensus in a Distributed Network
Bitcoin is a **distributed network** where nodes communicate only by messages. There is no central authority making the final decision.

### Consensus process
- Miners compete to seal the next block.
- Different miners may receive transactions in different orders.
- The first miner to find a valid block broadcasts it.
- If two miners succeed at nearly the same time, a **fork** can occur.
- Miners continue working on the branch they see as valid.
- The protocol rule is to work on the **longest chain**.

### Why this matters
This allows the network to agree on one ledger history even though nodes are separated, asynchronous, and some may be malicious.

---

## 7. How Bitcoin Prevents Double-Spending
Double-spending means trying to spend the same BTC twice.

### What happens?
- Alice creates two incompatible transactions using the same coin.
- Different miners may place them into different candidate blocks.
- Since they conflict, both cannot survive on the same accepted branch.
- Eventually, only the transaction in the **longest valid chain** remains.

### Confirmations
A transaction becomes safer as more blocks are built on top of it.

- These later blocks are called **confirmations**.
- The lecture notes that **6 confirmations** are typically considered safe in Bitcoin.

> [!tip] Memory hook
> More confirmations = harder to reverse.

---

## 8. Updating Bitcoin: Soft Fork vs Hard Fork
Changing Bitcoin is difficult because not all nodes upgrade at the same time.

### Soft fork
- Makes validation rules **stricter**.
- Old software still accepts new blocks.
- New software may reject some blocks accepted by old software.
- If a majority upgrades, new rules can be enforced.

### Hard fork
- Introduces features previously considered invalid.
- Old and new chains become **incompatible**.
- The blockchain can split into two separate chains.
- Whether both survive depends on the community and miners.

### Example
- **Bitcoin Cash** hard fork (August 1, 2017)
- Increased block size from **1 MB to 8 MB**

> [!important] Exam shortcut
> **Soft fork = backward compatible**
> **Hard fork = chain split risk**

---

## 9. Real-World Examples and Controversies
### Bitcoin Pizza purchase
- In May 2010, Laszlo offered **10,000 BTC for two pizzas**.
- This is remembered as the first famous real-world Bitcoin purchase.

### Silk Road
The lecture presents Silk Road as the first major “real” use case:
1. anonymous communication via **Tor**
2. **Bitcoin** payments with escrow
3. eBay-style vendor feedback

This illustrates how crypto can be used in legally controversial or illegal markets.

---

## 10. Pros and Cons of Bitcoin
### Pros
- Not controlled by a government
- Avoids inflationary monetary policy from central authorities
- Reduces need for intermediaries
- Enables easier international transfers
- Robust distributed ledger security
- Makes double-spending very costly
- Reduces cost of verifying and transferring ownership

### Cons
- Not backed by collateral or a state entity
- Value depends on acceptance
- High price volatility
- Heavy energy consumption
- Can support money laundering / illegal uses
- Weak scalability relative to card networks
	- about **7 Transactions Per Second** for Bitcoin vs about **2,000 TPS** for Visa/Mastercard

---

## 11. Key Takeaways
- Bitcoin transactions are built from **inputs and outputs**, not account balances.
- The **UTXO model** is central.
- Consensus is achieved through miners following the **longest chain**.
- **Double-spending** is prevented probabilistically through confirmations.
- **Soft forks** and **hard forks** are not the same.
- Bitcoin offers major innovation, but also serious trade-offs in **energy use, legality, and scalability**.

---

# Lecture 6: Cryptocurrency IV – Enterprise Applications of Blockchain

## 1. Big Picture
Lecture 6 shifts from cryptocurrency mechanics to **blockchain as enterprise infrastructure**. The main theme is that blockchain is not just digital money; it is a **distributed, append-only database** with potential applications in finance and business.

> [!important] Exam Focus
> Be ready to compare **public vs private blockchain**, **proof-based vs voting-based consensus**, and evaluate whether blockchain actually improves real financial workflows.

---

## 2. Blockchain Revisited
The lecture defines blockchain as:
- distributed
- append-only
- cryptographically secured
- sequentially linked
- replicated across nodes
- updated through software-driven consensus

### Core insight
Blockchain is fundamentally a **special type of database**, not just a coin system.

---

## 3. Consensus Types
### Proof-based consensus
Nodes must prove they are qualified to append blocks.
Examples:
- **Proof of Work** (Bitcoin)
- **Proof of Stake** (Ethereum 2.0 in the slide)

### Voting-based consensus
Nodes exchange their verification results before finalizing a new block.
This is more common in enterprise/private settings.

> [!tip] Compare
> **Proof-based** = competition
> **Voting-based** = coordinated validation

---

## 4. Public vs Private Blockchain
### Public blockchain
Examples:
- Bitcoin
- Ethereum

Characteristics:
- permissionless
- open to everyone
- anonymous or pseudonymous
- usually proof-based consensus
- slower and more resource intensive
- more decentralized

### Private blockchain
Examples mentioned:
- Hyperledger
- R3 Corda

Characteristics:
- permissioned
- only pre-approved participants
- single organization or consortium
- known identity
- often voting-based consensus
- faster and more scalable

> [!warning] Common trap
> Private blockchain is not “more decentralized.” It is usually faster because participation is restricted.

---

## 5. Pros and Cons of Blockchain in Enterprise Use
### Claimed advantages
- faster multi-party settlement
- less reconciliation work
- fewer intermediaries and lower processing cost
- immutable audit trail lowers tampering/collusion risk

### Concerns
For proof-based public chains:
- 51% attack risk
- slow confirmation time
- resource waste from mining competition
- security depends on participation level

For private chains:
- better performance, but weaker decentralization ideal
- more like a controlled shared database than an open public network

---

## 6. Blockchain’s Top Three Enterprise Advantages
The lecture highlights three top benefits:
1. **Time saved**: settlement can be much faster than traditional reconciliation-heavy processes.
2. **Cost reduced**: fewer “middlemen” in business-to-business processing.
3. **Risk mitigated**: immutable audit trail helps reduce tampering and collusion.

These are important for exam answers because they form the business case for enterprise blockchain.

---

## 7. Finance Application: International Money Transfer and SWIFT
### How ordinary interbank transfer works
- Intra-bank transfer: the bank debits one account and credits another.
- Inter-bank transfer: often requires correspondent banking relationships or an intermediary such as a central bank.
- SWIFT is a **messaging system**, not the money itself.

### SWIFT pain points from the lecture
- takes **1–5 business days**
- costly (slide mentions **$50 or more** in some cases)
- many correspondent banks may be involved
- uncertainty in timing and fees
- compliance checks slow things down

### Important distinction
SWIFT does not actually move the money directly; it coordinates messages between institutions.

---

## 8. SWIFT Frauds and the “Weakest Link” Problem
Although SWIFT uses PKI and should be secure, the lecture uses the **Bangladesh Bank heist** to show that a secure system can still fail if one participant is compromised.

### Lesson
Security depends on the **weakest link**, not just the protocol.

This is a classic exam point when comparing blockchain and traditional finance systems.

---

## 9. SWIFT GPI and Hyperledger Fabric PoC
### SWIFT GPI
Goal: improve transparency and speed.

Lecture points:
- launched in 2017
- more than **100 billion USD daily** in the slide
- around **50% credited within 30 minutes**
- around **90% within 24 hours**
- includes tracking, fee transparency, and stop-transfer ability

### Hyperledger Fabric proof of concept
Used for **real-time liquidity monitoring and reconciliation**.

Problem addressed:
- banks often do not know their correspondent account balances in real time

Why private blockchain here?
- closed user group
- permissioned access
- data privacy preserved between counterparties
- consensus every **2 seconds** in the slide example

### SWIFT’s conclusion from the lecture
DLT was **not yet ready** for large-scale replacement because of:
- limited benefits for large banks
- high investment cost
- operational complexity
- confidentiality issues
- large number of sub-ledgers needed

> [!important] Exam angle
> The lecture is not blindly pro-blockchain. It explicitly shows a case where incumbents tested DLT and concluded the benefits were limited.

---

## 10. Ripple / XRP as a Payment Alternative
The lecture presents Ripple as a **real-time gross settlement system (RTGS)** focused on banking rather than retail users.

### Problems Ripple tries to solve
- costly settlement
- settlement delay
- uncertainty in transaction cost
- too many correspondent banking relationships
- need for pre-funding liquidity

### Differences from Bitcoin
- no mining
- **100 billion XRP** created at launch
- smaller validating-node structure than Bitcoin/Ethereum
- banks and FX market makers act as gateways
- slide says settlement can occur in **3–5 seconds**

### Ripple products in the slides
#### xCurrent
- real-time messaging and settlement coordination
- most adopters in the lecture use this

#### xRapid
- sources liquidity through exchanges / market makers
- can use XRP as a bridge asset between currencies

### Big insight
Many institutions may adopt the **messaging and settlement improvements** without fully adopting XRP as a mainstream standalone currency.

---

## 11. Key Takeaways
- Blockchain should be understood as a **database and coordination technology**, not only a currency system.
- **Public** and **private** blockchains solve different problems.
- Enterprise adoption depends on whether blockchain delivers a better **time-cost-risk trade-off** than existing systems.
- In cross-border payments, blockchain competes with improved legacy infrastructure like **SWIFT GPI**.
- The lecture’s attitude is analytical: **blockchain can help, but it does not solve everything automatically**.

---

# Lecture 7: Smart Contracts – Definitions, Logic, and Use Cases

## 1. Big Picture
Lecture 7 introduces **smart contracts** as programmable agreements and shows why blockchain matters for them. It also compares **Bitcoin script** and **Ethereum smart contracts**, then ends by motivating the need for scaling solutions.

> [!important] Exam Focus
> Know the **definition**, **core characteristics**, **Bitcoin vs Ethereum implementation difference**, and **use cases**.

---

## 2. What Is a Smart Contract?
The lecture gives several definitions:

### Wikipedia-style idea
A smart contract is a computer protocol intended to digitally facilitate, verify, or enforce contract performance.

### Nick Szabo (1994)
A smart contract is a computerized transaction protocol that executes the terms of a contract.

### IBM-style definition
Smart contracts are lines of code stored on a blockchain that automatically execute when pre-set conditions are met.

### Simplified definition for exams
A smart contract is a **self-executing program that encodes the rules of an agreement**.

---

## 3. Characteristics of Smart Contracts
The lecture emphasizes that smart contracts are simply **computer programs acting as agreements**.

### Key properties
- terms can be programmed
- execution can be automated
- logic can be enforced by software

### Primitive ancestor
- **Vending machine**: put coins in, soda comes out

This is a useful analogy: smart contracts are “if-this-then-that” agreements, but implemented with stronger rules and potentially on-chain enforcement.

---

## 4. Why Put Smart Contracts on Blockchain?
The lecture says smart contracts on blockchain gain three major properties:
1. **Immutability** (at least partially irreversible)
2. **Security**
3. **Transparency**

### Compared with traditional contracts
- higher certainty in contract terms once coded
- potentially more transparent
- less dependence on manual enforcement

### Compared with ordinary digital contracts
Blockchain-based contracts can be harder to alter and easier to verify publicly.

> [!warning] Common trap
> “Smart” does not necessarily mean legally complete, fair, or bug-free. It means the contract logic is encoded and can self-execute.

---

## 5. Blockchain Rules as Code
The “21 Million Cap” slide is a reminder that blockchain systems already enforce important rules through code.

```cpp
CAmount GetBlockValue(int nHeight, const CAmount& nFees)
{
    CAmount nSubsidy = 50 * COIN;
    int halvings = nHeight / Params().SubsidyHalvingInterval();

    // Force block reward to zero when right shift is undefined.
    if (halvings >= 64)
        return nFees;

    // Subsidy is cut in half every 210,000 blocks which will occur approximately every 4 years.
    nSubsidy >>= halvings;

    return nSubsidy + nFees;
}
```
### Example idea
Bitcoin’s issuance schedule is not merely a promise; it is implemented in protocol logic.

This supports the lecture’s broader point:
- smart contracts are not alien to blockchain
- blockchain itself already relies on **programmable rules**

---

## 6. How Smart Contracts Work: Bitcoin vs Ethereum
### Bitcoin
- built mainly for cryptocurrency
- the protocol itself is computer code
- uses **Script**, a stack-based linear instruction structure
- common use: send BTC to a public key / address
- also supports features like **multisig** and **locking**

### Ethereum
- designed more explicitly for computation and smart contracts
- uses **Solidity**
- runs code on the **Ethereum Virtual Machine (EVM)**
- execution is not free; it costs **Ether / gas**

> [!important] Compare
> **Bitcoin** = limited scripting, payment-first design
> **Ethereum** = computation-first design, richer smart contract support

---

## 7. Ethereum Contract Lifecycle
The lecture describes three basic steps:
1. upload the code and associated data to the network
2. the blockchain assigns it a unique address
3. users execute the contract by calling that address

### Ethereum transaction types in the lecture
a. transfer of Ether  
b. creating a smart contract  
c. interacting with a smart contract  

This is a high-value exam section because it directly tests operational understanding.

---

## 8. Use Cases of Smart Contracts
### Current use cases
- banking and financial service contracts
- money transfer
- flight delay insurance
- securities trading, clearing, and settlement
- prediction markets
- escrow replacement
- token sales such as **ICO** and **STO**

### Future use cases
- transfer of blockchain-registered assets
- land / house / vehicle transfer
- digital rights and copyrighted content

---

## 9. Case Study Motivation: Scaling Problem
The lecture ends by linking smart contracts to Bitcoin’s scaling problem.

### Why are Bitcoin transactions slow?
- ledger updates are broadcast via consensus to all participants
- block size and block time constrain throughput

### Slide comparison
- Visa peak: **47,000 TPS** in the slide
- Bitcoin: about **7 TPS** with 1 MB block size

### Implication
If Bitcoin tried to match Visa by simply increasing block size, the network could become unstable or extremely centralized.

### Transition question
How can we support micropayments without putting every small payment on-chain?

Answer in Lecture 8: **Lightning Network**.

---

## 10. Key Takeaways
- Smart contracts are **self-executing code-based agreements**.
- Blockchain adds **immutability, security, and transparency**.
- **Bitcoin Script** and **Ethereum Solidity/EVM** are not the same.
- Smart contracts already matter in finance and asset transfer.
- Scaling limits motivate **Layer 2** solutions.

---

# Lecture 8: Smart Contracts II – Lightning Network and Layer 2

## 1. Big Picture
Lecture 8 explains the **Lightning Network** as a **Layer 2** solution for Bitcoin. The goal is to keep Bitcoin secure while improving **speed**, **fees**, and **scalability** by moving many transactions **off-chain**.

> [!important] Exam Focus
> Understand the logic of **payment channels**, **commitment transactions**, **revocation/penalties**, and **HTLCs**.

---

## 2. What Is Layer 2?
A Layer 2 solution is:
- a secondary protocol built on top of the main blockchain
- designed to address scalability, speed, and fee limitations
- based on processing transactions off-chain and reconciling later on-chain

### Types listed in the lecture
- channels
- sidechains
- off-chain computation networks

---

## 3. Lightning Network: Core Idea
Lightning is meant for repeated transactions between parties where only the **net result** ultimately matters.

### Everyday analogies from the lecture
- coffee shop tab
- restaurant bill
- credit card statement
- cellphone bill

### Three core features
1. **Bidirectional payment channels**: two parties keep an internal balance ledger.
2. **Networked payments**: channels can be connected across multiple parties.
3. **Blockchain as arbiter**: blockchain is used mainly when cooperation fails or when channels open/close.

> [!tip] Memory hook
> Lightning = “put it on my tab, settle later.”

---

## 4. Basic Channel Flow
### Step 1: Open a channel
- Two parties create a payment channel.
- At least one party must commit BTC.
- The channel has a capacity.
- The lecture uses a **multisignature wallet** structure.

### Step 2: Transact off-chain
- Parties can make many payments for days, weeks, or longer.
- Each payment updates the channel balance.
- These balance updates are **not broadcast** to the blockchain.
- Each side stores the relevant transactions locally.

### Step 3: Close the channel
- Final balances are written to the blockchain.

### Result
Instead of posting every payment on-chain, only the **opening** and **closing** matter on-chain.

---

## 5. Why Off-Chain Payments Still Need Security
A natural concern is: if balances stay off-chain, what stops cheating?

### Answer
- Off-chain transactions still require **signatures**.
- Unauthorized spending is still prevented by cryptography.
- The bigger issue is preventing someone from broadcasting an **old state**.

### Key Lightning idea
If someone broadcasts an outdated balance, they can be **penalized**.

---

## 6. Building Blocks of Lightning Network
The lecture highlights five building blocks:

### 1. Unconfirmed transactions
Transactions prepared but not yet broadcast.

### 2. Bitcoin’s double-spend protection
Still foundational for final settlement.

### 3. Multisig / P2SH
Often **2-of-2 multisig** in Lightning channels.

### 4. Time-locks
Coins can be made spendable only after some future time/block delay.

### 5. Hash values and secrets
A secret is a long unguessable value; its hash is used to structure conditional payments.

> [!important] Exam shortcut
> Lightning = **multisig + timelocks + hashes/secrets + penalties**

---

## 7. Opening a Channel in More Detail
The lecture’s example:
- Alice and Bob want to transact repeatedly.
- They each fund **5 BTC**, so the channel has **10 BTC** total.

### Two-step setup
#### Opening transaction
- Funds the channel.
- Alice and Bob send BTC to a **2-of-2 multisig address**.

#### Commitment transaction
- Records the current channel balance.
- Example after Alice sends 1 BTC to Bob:
  - Alice: **4 BTC**
  - Bob: **6 BTC**

### Requirements for a valid channel design
1. each party must be able to **unilaterally enforce** the current state
2. old states must be safely invalidated when balances update

### Technique used
- each party creates a **secret** and shares the corresponding **hash**
- commitment transactions contain penalty logic tied to those secrets

---

## 8. Commitment Transactions and Penalty Logic
Suppose Alice has a commitment transaction signed by Bob.

### Why this matters
- Alice can broadcast it without needing Bob again.
- So she can enforce the current state unilaterally.

### But how do we stop her from using an outdated version later?
The commitment structure is designed so that if she broadcasts an old state:
- part of the money may be delayed by a **timelock**
- the counterparty can use the revealed secret to claim the funds as a **penalty**

### Consequence
Once a state is revoked, broadcasting it becomes dangerous.

> [!warning] Core exam sentence
> Lightning does not “trust” the other party to be honest; it makes cheating **too expensive**.

---

## 9. Updating the Channel
Later, suppose Bob sends Alice 1 BTC back.

### New state
- balance becomes **5 BTC / 5 BTC**

### What happens?
- a new commitment transaction is created
- both parties exchange **new hashes/secrets**
- both sign the new commitment state
- both reveal the **old secrets** from the prior state

### Why reveal old secrets?
This is what effectively revokes the old state.
If someone later broadcasts that outdated state, the counterparty can use the old secret during the timelock window and claim the funds.

### Example from the lecture
If Bob tries to broadcast an old state where he had 6 BTC:
1. Alice gets 4 BTC immediately
2. Bob must wait before claiming his 6 BTC
3. During that delay, Alice can use Bob’s revealed secret to take the 6 BTC

### Result
Whoever cheats can lose **all BTC in the channel**.

---

## 10. Monitoring Requirement
Lightning does not remove the need for vigilance.

### Why monitoring matters
If the other side broadcasts an outdated state, you must react before the timelock expires.

### How to handle this
- monitor the chain yourself with a full node, or
- outsource monitoring to a third party for a fee

> [!warning] Common trap
> Off-chain does **not** mean no security work is needed.

---

## 11. Creating a Network: Paying Through Intermediaries
Alice may want to pay Carol even if they do not share a direct channel.
If both Alice–Bob and Bob–Carol channels exist, Bob can act as an intermediary.

### Naive problem
What if:
- Alice pays Bob but Bob never pays Carol?
- Bob pays Carol but cannot safely recover from Alice?

Simple trust is not enough.

---

## 12. HTLCs: Hash Time-Locked Contracts
To solve the intermediary problem, Lightning uses **HTLCs**.

### High-level logic
1. Carol creates a secret and gives its **hash** to Alice.
2. Alice offers payment to Bob if Bob can reveal Carol’s secret.
3. Bob offers payment to Carol under the same condition.
4. Carol reveals the secret to claim her payment.
5. Bob learns the secret and uses it to claim payment from Alice.

### Why this works
The channels become **linked** by the same hash/secret condition.
Bob only gets paid if Carol’s payment is actually completed.

### Timeout ordering
The lecture stresses that:
- Bob must get the value from Carol **before** Alice gets it from Bob.
- therefore Bob–Carol timeout must expire **before** Alice–Bob timeout.

This sequencing protects the intermediary.

---

## 13. All Must Be Off-Chain
The lecture notes that the networked HTLC idea would be too slow if every step still had to hit the blockchain.

### Solution
Use **bidirectional payment channels with HTLC logic**, so the routing and conditional payment process also stays off-chain as much as possible.

### Main design philosophy
Bitcoin remains the ultimate enforcement layer, but routine interaction should stay away from the base chain.

---

## 14. Closing the Channel
If Alice and Bob cooperate:
- they close the channel peacefully
- they create a closing transaction that pays each party their fair share

### Elegant result
In the normal case, only **two on-chain transactions** are needed:
1. opening transaction
2. closing transaction

That is the core scalability win.

---

## 15. Lightning Network Status and Limitations (as Presented in the Slides)
### Current status slide
The lecture lists approximately:
- **6,700 nodes**
- **30,000 channels**
- **$2.7 million capacity**

### Limitations listed
- intermediate failure
- no offline payment
- need active monitoring
- poor fit for very large payments
- every node on the route must have enough capacity
- similar in some ways to correspondent banking

### Summary slide points
- Lightning is not an independent network; it sits on top of Bitcoin.
- It is more like a **deferral of state**, since final enforcement still relies on Bitcoin.
- Developers mentioned include **Lightning Labs, ACINQ, and Blockstream**.
- Interoperability is good.
- Tor routing is used by default.
- A related project mentioned is **Liquid Sidechain** for larger B2B-style payments.

---

## 16. Key Takeaways
- Lightning is a **Layer 2** scaling solution for Bitcoin.
- It uses **payment channels** to keep many transactions off-chain.
- Security comes from **cryptography + revocation penalties + timelocks + HTLCs**.
- The blockchain remains the final judge, but normal use avoids hitting it repeatedly.
- Lightning improves scalability, but it still has important **operational and routing limitations**.

---

# Final Cross-Lecture Summary

## 1. Main storyline from Lectures 5–8
- **Lecture 5**: How Bitcoin transactions, consensus, forks, and double-spending work.
- **Lecture 6**: How blockchain might be used in enterprise and finance.
- **Lecture 7**: What smart contracts are and why programmable agreements matter.
- **Lecture 8**: How smart contracts enable Layer 2 scaling through Lightning.

## 2. Must-Know Comparisons
### UTXO vs account-based
- Bitcoin uses **UTXO**, not running balances.

### Public vs private blockchain
- Public = open, slower, proof-based, more decentralized.
- Private = permissioned, faster, voting-based, less decentralized.

### Bitcoin vs Ethereum smart contracts
- Bitcoin = limited scripting.
- Ethereum = richer contract platform via Solidity + EVM.

### On-chain vs off-chain
- On-chain = stronger direct settlement, but slower and more expensive.
- Off-chain = faster and cheaper, but requires channel design and monitoring.

### Soft fork vs hard fork
- Soft fork = stricter rules, backward compatible.
- Hard fork = incompatible rule change, possible chain split.

---

## 3. Fast Memorization List
- **Inputs + outputs + signatures + fees**
- **UTXO + change address**
- **Longest chain + confirmations**
- **Soft fork vs hard fork**
- **Proof-based vs voting-based consensus**
- **Public vs private blockchain**
- **Smart contract = self-executing code**
- **Bitcoin Script vs Ethereum Solidity/EVM**
- **Lightning = channels + penalties + HTLCs**

---

## 4. One-Sentence Exam Answer Bank
- **Bitcoin transaction**: a signed transfer that spends previous outputs and creates new outputs.
- **UTXO**: an unspent transaction output that can be used as an input in a future transaction.
- **Soft fork**: a backward-compatible tightening of validation rules.
- **Hard fork**: a non-backward-compatible protocol change that can split the chain.
- **Private blockchain**: a permissioned distributed ledger with known participants and usually voting-based consensus.
- **Smart contract**: a self-executing program that encodes and enforces contract logic.
- **Lightning Network**: a Layer 2 protocol that enables off-chain Bitcoin payments through channels and HTLCs.

---

## 5. Final Takeaway
These four lectures connect into one core message:

**Blockchain starts as a way to secure transactions, expands into enterprise coordination, becomes programmable through smart contracts, and then needs Layer 2 design like Lightning to scale.**
