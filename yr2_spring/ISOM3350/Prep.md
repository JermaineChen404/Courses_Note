# Lecture 1: Cryptographic Hash Function

## 1. What is a Cryptographic Hash Function?
A **hash function** takes an input (any string of arbitrary size) and produces a fixed-size output called a **digest** or **hash**.  
In cryptography, we need special properties to make it useful for security.

### Key Characteristics
- **Input**: any data – a word, a file, a movie – anything.
- **Output**: fixed length, e.g., 256 bits (often shown as 64 hexadecimal digits).
- **Efficiently computable**: the time to compute the hash grows linearly with the input size.

> **Example (SHA-256)**
> ```
> Input:  "HKUST is an awesome place"
> Output: D6F4129E6EF8E5B31BF1714797E541B2FE8CC69062486CA9AC526216CE33AD51
> ```

---

## 2. Essential Properties of a Cryptographic Hash Function

### 🔒 One‑way (Preimage Resistance)
- Given a hash output, it should be **infeasible** to find any input that hashes to that value.
- The function is **not invertible** because many inputs map to the same output (the input space is huge, output space is fixed).

### 🔗 Collision Resistance
- It must be **extremely hard** to find two *different* inputs that produce the **same** hash output.
- If you could find a collision, you could break many security applications.

### 🌊 Avalanche Effect
- A tiny change in the input should cause the output to change **drastically** (about half the bits flip on average).
- This makes the hash look random and unpredictable.

#### Demonstration (SHA-256)
| Input | SHA-256 Hash |
|-------|--------------|
| `HKUST is an awesome place` | `D6F4129E6EF8E5B31BF1714797E541B2FE8CC69062486CA9AC526216CE33AD51` |
| `HKUST is an awesome place!` (added `!`) | `7F1BF88D2CAEC81184C3BA941364F0B6E587D80FDEEF7B921DA4814F866CAFF1` |
| `HKUST is a awesome place!` (`an` → `a`) | `78082C75A77654DD89B7A76182C2892694A2468F52DC329D5E6F9083442D3AF8` |

Notice how the hashes look completely unrelated even though the inputs differ by just one character.

---

## 3. How Strong is Collision Resistance?
- SHA‑256 produces a 256‑bit output → there are \(2^{256}\) possible hash values.
- That number is astronomically large:  
  \(2^{256} \approx 1.16 \times 10^{77}\)
- To find a collision by brute force (trying random inputs) you would need on average \(2^{256}\) attempts.
- Even the fastest supercomputer (93 petaflops) would take **\(5 \times 10^{56}\) years** – far longer than the age of the universe (\(1.38 \times 10^{10}\) years).

Thus, SHA‑256 is considered **collision‑resistant** in practice.

---

## 4. Common Hash Functions and Their Security

| Algorithm | Output Size | Status |
|-----------|-------------|--------|
| **MD5** | 128 bits | **Broken** – collisions found since 2005; not safe for security. |
| **SHA‑1** | 160 bits | **Broken** – first practical collision demonstrated in 2017 (used 6,500 CPU years + 110 GPU years). |
| **SHA‑2 family** (SHA‑256, SHA‑384, SHA‑512) | 256/384/512 bits | **Still secure** – no practical collisions known. |
| **SHA‑3** | variable | Newest standard (2015), alternative to SHA‑2. |

For blockchain and most modern applications, **SHA‑256** is the workhorse.

---

## 5. Applications of Cryptographic Hash Functions

### 🔐 Commitments
- Alice solves a problem first but doesn’t want to reveal her answer yet.
- She computes the hash of her answer and gives that hash to Bob.
- Later, she reveals the actual answer; Bob can hash it and compare with the earlier hash to verify she didn’t change it.
- This “commits” her to the answer without revealing it.

### 📄 Document Integrity (Checksums)
- When you download a file, the website often provides its SHA‑256 hash.
- After downloading, you compute the hash yourself. If it matches, the file hasn’t been tampered with.
- Example: software downloads, ISO images.

> **Try it yourself**:  
> [Online SHA‑256 calculator](https://emn178.github.io/online-tools/sha256_checksum.html)

### ⛓ Blockchain
- Each block contains the hash of the previous block, linking them together.
- If someone tries to alter a past block, its hash changes, breaking the chain – tampering becomes evident.
- (Detailed in Lecture 2)

---

## 6. Real‑world Case: Ashley Madison Data Breach
- The Ashley Madison website (for extramarital affairs) was hacked.
- They had stored user passwords as **unsalted MD5 hashes**.
- Because MD5 is weak and no salt was used, attackers could easily crack many passwords.
- **Lesson**: Using a broken hash function (or misusing a good one) can lead to catastrophic data leaks.

---

## 7. Key Takeaway
- Cryptographic hash functions are **one‑way**, **collision‑resistant**, and exhibit the **avalanche effect**.
- They are the building blocks of blockchain, digital signatures, and data integrity.
- Always use a modern, secure hash like **SHA‑256** (or SHA‑3) for any security‑sensitive application.

---

# Lecture 2: Public Key Encryption and Digital Signature

## 1. Quick Recap: Hash Functions (from Lecture 1)
- Produce a fixed‑size digest from any input.
- One‑way, collision‑resistant, avalanche effect.
- Used to link blocks in a blockchain (tamper‑evident chain).

---

## 2. Building the Blockchain
A blockchain is a **linked list of blocks**.  
Each block contains:
- **Data** (e.g., transactions)
- **Hash of the previous block**
- A pointer (or reference) to the previous block

If any data in a previous block is changed, its hash changes, and all subsequent blocks’ hashes would have to be recomputed to make the chain consistent.  
Without controlling more than half the network’s computing power, this is infeasible.

> **Interactive demo**: [andersbrownworth.com/blockchain/blockchain](https://andersbrownworth.com/blockchain/blockchain)

---

## 3. Why Do We Need Digital Signatures?
- In a digital currency, we must ensure that **only the owner** can spend their money.
- We also need **non‑repudiation** – the owner cannot deny having authorised a transaction.
- This is achieved with **public‑key cryptography** and **digital signatures**.

---

## 4. Public‑Key Cryptography Basics
- Each user generates a **key pair**:
  - **Private key (sk)** – kept secret, like a password.
  - **Public key (pk)** – shared openly, like an account number.
- The private key can **sign** a message; the public key can **verify** the signature.
- It is computationally infeasible to derive the private key from the public key.

### Encryption vs. Signing
- **Encryption**: public key encrypts, private key decrypts (confidentiality).
- **Signing**: private key signs, public key verifies (authenticity and integrity).

> For digital currencies, we only need **signing** – proving ownership.

---

## 5. Digital Signature Scheme
A digital signature scheme consists of three algorithms:

### 🔑 Key Generation
- Generate a random private key `sk` and its corresponding public key `pk`.
- Example: In Bitcoin, `sk` is 256 bits, `pk` is 512 bits (uncompressed).

### ✍️ Signing
- `sig = sign(sk, message)`
- The signer uses their private key to produce a signature on the message.
- Typically the message is **hashed first** (so any length can be signed).

### ✅ Verification
- `verify(pk, message, sig)` returns `true` if the signature is valid, `false` otherwise.
- Anyone with the public key can check that the signature was indeed created by the holder of the corresponding private key.

---

## 6. Properties of a Secure Digital Signature
- **Correctness**: `verify(pk, message, sign(sk, message))` always returns `true`.
- **Unforgeability**: Without knowing the private key, an adversary cannot create a valid signature for any message – even after seeing many valid signatures for other messages.

---

## 7. ECDSA – The Signature Algorithm Used in Bitcoin
- **ECDSA** stands for Elliptic Curve Digital Signature Algorithm.
- Key sizes:
  - Private key: 256 bits
  - Public key: 512 bits (two 256‑bit coordinates)
  - Signature: 512 bits
- Messages are hashed (with SHA‑256) before signing.
- **Important**: The private key must be generated with a **high‑quality random source**. If randomness is poor, an attacker might be able to guess it.

---

## 8. How to Interpret a Signature
Think of a valid signature as the public key “saying” the message:

> If `verify(pk, msg, sig) == true`, you can think: **"`pk` says, '[msg]'"**.

To “speak for” a public key, you must know the matching private key `sk`.

---

## 9. Applying Digital Signatures to Blockchain Transactions
1. **Alice** wants to send 10 bitcoins to Bob.
2. She creates a transaction message:  
   `"Alice pays 10 BTC to Bob"`
3. She **hashes** this message and signs the hash with her private key.
4. She broadcasts the transaction (message + signature) to the network.
5. **Miners** verify the signature using Alice’s public key. If valid, they know Alice authorised the payment.
6. The transaction is then included in a block.

---

## 10. Security of Digital Currencies
- **No double‑spending**: The blockchain ensures each coin is spent only once (hash chain prevents alteration).
- **Only owner can spend**: Digital signatures prove ownership.
- **Anonymity**: Addresses are derived from public keys, not real identities. However, transactions are public, so privacy is limited.
- **Cannot forge currency**: Creating valid signatures without the private key is impossible.

---

## 11. Real‑world Example: Ethereum Blockchain Saving a #MeToo Letter
- In 2018, a Chinese #MeToo letter was censored online.
- Activists stored the letter on the **Ethereum blockchain** (as transaction data).
- Because the blockchain is immutable and decentralised, the letter could not be taken down.
- This demonstrates how blockchain can preserve information in the face of censorship.

---

## 12. Summary
- **Hash functions** link blocks and provide tamper evidence.
- **Digital signatures** (via public‑key crypto) ensure that only the rightful owner can authorise transactions.
- Together they form the core security of any cryptocurrency.

---

# Lecture 3: Cryptocurrency I – Miners and Proof of Work

## 1. Recap: Digital Signatures (from Lecture 2)
- A digital signature proves that the owner of a private key authorised a transaction.
- The transaction message + signature is broadcast to the network.

Now we need to answer: **Who maintains the ledger? Who decides which transactions are valid? Who creates new bitcoins?**

**Answer: Miners.**

---

## 2. What Are Miners?
- Miners are participants in the network who collect pending transactions, verify them, and package them into **blocks**.
- They then compete to add their block to the blockchain.
- The winner is rewarded with **newly created bitcoins** and **transaction fees**.

---

## 3. Miner Rewards

### 🪙 Block Reward
- When a miner successfully adds a block, they receive a fixed amount of bitcoins.
- This is how new bitcoins enter circulation.
- The block reward **halves approximately every 4 years** (every 210,000 blocks).
  - 2009: 50 BTC
  - 2012: 25 BTC
  - 2016: 12.5 BTC
  - 2020: 6.25 BTC
  - **2024: 3.125 BTC** (latest halving)
- Halving continues until around **2140**, when the total number of bitcoins reaches the cap of **21 million**. After that, no new bitcoins will be created.

### 💸 Transaction Fees
- Users can include a fee with their transaction to incentivise miners to include it.
- Miners collect all fees from transactions in the block they mine.
- Higher fees → faster confirmation.

---

## 4. Mining Economics
- Mining requires powerful hardware (ASICs) and electricity.
- **Fixed costs**: hardware, cooling, facility.
- **Variable costs**: electricity.
- The reward depends on the **global hash rate** (total computing power of the network). More miners → more competition → lower chance for any single miner to win a block.
- Miners often relocate to places with cheap electricity (e.g., Texas, with wind power).

> **Case**: "How Texas's wind boom has spawned a Bitcoin mining rush" – miners use excess wind energy to power their rigs, making it profitable even when the network difficulty is high.

---

## 5. Proof of Work (PoW) – The Mining Puzzle
To add a block, a miner must solve a computationally hard puzzle. The puzzle is:

> Find a number (called a **nonce**) such that:
> ```
> SHA‑256( nonce || block_data ) < target
> ```
> where `target` is a very small number.

Equivalently, the resulting hash must start with a certain number of leading zeros.

### Example (February 2023)
- The requirement was **19 leading zeros**.
- A valid block hash looked like:
  ```
  0000000000000000000636caff4a1d96d02b5b357edb7243cef318ba8404058
  ```
- To find such a hash, a miner must try on average \(16^{19} \approx 7.56 \times 10^{22}\) different nonces!

### Why “Proof of Work”?
- The work (trying many nonces) proves that the miner expended significant computational effort.
- This makes it **expensive to attack** the network – an attacker would need more than half the total hashing power to rewrite history.

---

## 6. Difficulty Adjustment
- The Bitcoin network aims to produce a block **every 10 minutes** on average.
- Every **2016 blocks** (about two weeks), every node recalculates the target based on the time it took to mine those blocks.
- If blocks were found too quickly, the target is lowered (making the puzzle harder). If too slowly, the target is raised (making it easier).
- This keeps block time stable despite changes in total hashing power.

---

## 7. What If Two Miners Solve the Puzzle at the Same Time?
- Because the network is global, two miners might find valid blocks almost simultaneously.
- Different parts of the network may hear about one block first, and other parts hear about the other first.
- This creates a temporary **fork** – two competing chains.

### Resolution
- Miners continue working on the chain they believe is correct.
- Eventually, one chain becomes longer (more accumulated work) because more miners build on it.
- The shorter chain is abandoned (orphaned), and its blocks become **stale**.
- The network reaches **consensus** on the longest chain.

---

## 8. Summary
- **Miners** secure the network by solving PoW puzzles.
- They are rewarded with **block rewards** (halving every 4 years) and **transaction fees**.
- The puzzle difficulty adjusts every two weeks to keep block time at 10 minutes.
- Temporary forks are resolved by the longest chain rule.

---

# Lecture 4: Cryptocurrency II – Addresses, Wallets, and Exchange Accounts

## 1. Recap: Incentive and Proof of Work
- Tamper‑proof blockchain requires costly hashing (PoW).
- Miners are compensated with block rewards and fees.
- PoW puzzle: find a nonce so that `H(nonce || block) < target`.

---

## 2. More on Proof of Work Details
- The nonce is a 32‑bit (or larger) field in the block header.
- Miners iterate over nonce values, compute the hash, and check if it meets the target.
- When the nonce space is exhausted, they can change other parts of the block (e.g., the coinbase transaction) and continue.
- The target is a 256‑bit number. The required number of leading zeros is a convenient way to think about it.

### Example: Simulated Mining Exercise
- Set a low difficulty (e.g., two leading zeros).
- Include your name in the transaction.
- Link to a given previous block hash.
- Write a script to find the first nonce that makes the hash below a given target.

This hands‑on exercise demonstrates how mining works in principle.

---

## 3. Bitcoin Addresses – Decentralised Identity
In Bitcoin, you don’t have a “username”. Instead, you have one or more **addresses**.  
An address is derived from your public key and serves as a destination for payments.

### Properties
- Anyone can create a new address at any time – no central authority.
- You can create as many as you want (privacy, organisation).
- Addresses are **not** directly your public key; they are a hashed version.

---

## 4. How to Generate an Address (Step by Step)
1. Generate a random **private key** (256 bits) using a secure random source.
2. Use **ECDSA** to compute the corresponding **public key** (512 bits, uncompressed).
3. Hash the public key with **SHA‑256**, then hash that result with **RIPEMD‑160** to get a 160‑bit hash.
4. Add a version byte (usually `0x00` for mainnet) and compute a checksum (double SHA‑256 of the versioned hash, take first 4 bytes).
5. Encode the result in **Base58Check** – this produces the familiar Bitcoin address (e.g., `1A1zP1eP5QGefi2D...`).

> **Try it online** (for testing only, never use for real funds):  
> [bitaddress.org](https://www.bitaddress.org)

### Example (using bitcore library in JavaScript)
```javascript
var privateKey = new bitcore.PrivateKey();
var publicKey = privateKey.publicKey;
var address = publicKey.toAddress();
console.log(address.toString()); // e.g., mpFbXvm31yRff6rj9a4ecWi5Qybh2wmaNGg
```

---

## 5. Types of Wallets
A **wallet** is software that stores your private keys and allows you to send/receive bitcoins.

### Local Wallets
- **Desktop**: Bitcoin Core, Electrum – keys stored on your computer.
- **Mobile**: apps like Blockchain.info wallet (but beware of third‑party risks).
- **Hardware**: physical devices (Ledger, Trezor) that keep keys offline – very secure.

### Exchange Accounts (e.g., Coinbase, Binance)
- You create an account, buy/sell bitcoin, and the exchange holds the coins in their **omnibus wallets**.
- Your “wallet” on the exchange is just a database entry – you don’t control the private keys.
- The exchange **owes you** that amount, but technically **you do not own the bitcoin on the blockchain**.
- If the exchange gets hacked or goes bankrupt, you could lose your funds.

---

## 6. Exchange Account ≠ Personal Wallet – The Illusion
- When you buy bitcoin on an exchange, you see a balance in your account.
- But the exchange pools all customer funds into a few master wallets.
- They keep an internal ledger of who owns what.
- **You cannot send bitcoin from your exchange “wallet” directly to another person without the exchange’s permission.** You must withdraw to your own wallet first.
- **Key takeaway**: To truly own bitcoin, you must hold the private keys yourself.

> **Video explanation**: [https://www.youtube.com/watch?v=tiy1K6-mf4s](https://www.youtube.com/watch?v=tiy1K6-mf4s)

---

## 7. Why Use an Exchange at All?
- **Convenience**: Easy to buy/sell with fiat currency.
- **Liquidity**: Instant trades.
- But for long‑term storage, you should move coins to a wallet you control.

---

## 8. Security Tips
- **Never share your private key** with anyone.
- Use hardware wallets for large amounts.
- Enable two‑factor authentication on exchange accounts.
- Be wary of online wallet services – they may be scams or vulnerable.

---

## 9. Summary
- Bitcoin addresses are derived from public keys via hashing and Base58Check.
- Wallets store private keys; you must control the keys to truly own the coins.
- Exchange accounts are custodial – you have an IOU, not the actual bitcoin.
- Always withdraw to your own wallet for safekeeping.