# Online Platform
## Amazon's Profitability and Breadth of Business
### Postponed profits and focused on growth
- Expanding warehousing capacity
- Building e-commerce operations worldwide
- Developing a cloud computing platform
- Pioneering in eBook readers
## Emperor of Ecommerce
- Three pillars of the business
	- Large selection
	- Convenience
	- Lower prices

work together to create additional assets for competitive advantages

## Value of Technology
Increasingly depends on
- Technology's stand-alone value
- network effect value
## Network effects - Metcalfe's Law
**The value of product or service increases as its number of users expands (value increases with $n^2$)**
- AKA network effect
- most products are not subject to it
- Influence the choice of one product over another
## Platform
A platform business provides **a digital marketplace**, which brings together **two or more independent groups**
- Create value by facilitating exchanges, but **not** owning the means of production
### Platform vs. Pipeline
- Pipeline firms' assets are internal resources (tangible and intangible) such as raw materials and production systems
- Platform firms' critical assets are the **network** of producers and consumers
### Business Trends
- Pipeline business $\to$ Platform business
- Controlling internal resources $\to$ coordinating external interactions
- **Digital Transformation**: Pipeline firms' efforts to adopt platform strategy for their business systems
## Two-Sided Business
- Definition: Products or services create a two-sided market when
	- they serve two distinct types of consumers
	- they facilitate them to interact with each other
	- at least one type of users care about the size of the other type of users
- Examples
	- E-bay
	- LinkedIn
	- Credit card: cardholders and merchants
## Platform as Two-Sided Business
- Supplier $\Leftarrow$ **Conventional business** $\Leftarrow$ Customer
	- Value moves from left to right (producers to consumers)
	- To the left is cost; to the right is revenue
- Market Side A $\iff$ **Platform** $\iff$ Market Side B
	- cost and revenue are both to the left and the right
## Network Effect for Two-Sided Market
For one-sided market
- Same-side network effect
	- Preference regarding number of other users on own side
	- Positive: more players $\to$ more online interactions
		- player-to-player contact in Xbox game
	- Negative: more sellers $\to$ more competitions
		- competing suppliers in auction

For two-sided market
- Cross-side network effect
  - Preference regarding number of users on other side
    - Positive
	    - developers and end-users for windows
	  - Negative
		  - more advertisement in programs and less users

![[Ust_Note/Attachment/Pasted image 20250523233629.png]]
## Sharing Economy
- Extract value from the asset we already have, dividing them into **space and time**, in order to be consumed as a service
- Platform allow pricing, meeting and sharing
### Characteristics
- Digital platforms connect spare capacity and demand
	- more concise, real-time measurement of space capacity
	- connections to occur between demand and that capacity
	- Example: Airbnb
- Access instead of sharing
	- offer access rather than ownership through different methods
- More collaborative forms of consumption
	- more comfortable with consuming products
	- deeper social interactions than traditional exchange
## Strategy Challenges in Platform Business
- Chicken-and-egg problem
- Pricing: which side to subsidize
- Winner-takes-all market
- Threat of envelopment
### Chicken-and-egg problem
For initial users
- No network to benefit from
- Depends on the standalone value of the platform
#### Solution
- The big-bang adoption strategy
	- Use one or more traditional push marketing strategies to reach a high volume of interest from both sides of the platform
	- 支付宝扫五福, 微信红包
- The piggyback strategy
	- Connect with an existing user base from a different platform and attract them  to participate in your platform
	- E.g., 视频号 on WeChat
- The seeding strategy
	- Reach out to some users, key users, or users that benefit more from the  standalone value of the platform. When these users are attracted to the  platform, other users who want to engage in interactions with them will follow  to join.
### Pricing
Platform providers have to choose price for each side, factoring in the impact on the other side’s growth and willingness to pay.
- Subsidy side: highly valued, attracted in volume
	- quality- and price- sensitive users
	- sets lower price
- Money side: the other way around
- Goal: generate cross-side network effects
	- If the platform provider can attract enough subsidy-side users, money-side  users will pay more to reach them
### Winner-Takes-All Markets
Winner-takes-all markets are caused by network effects
#### Characteristics
- Multi-homing costs are high for at least one side
	- Homing cost: upfront, ongoing, and termination costs borne by users due to  platform affiliation
- Network effects are positive and strong (self-reinforcing)
- Niche specialization is low
	- Users have relatively homogeneous needs
	- Neither side’s users have a strong preference for special features
#### Homing and Switching Cost
- Mono-homing: 1 setup + 1 ongoing
- Switching: 2 setups + 1 termination + 1 ongoing
- Multi-homing: 2 setups + 2 ongoing
### Threat of Envelopment
Platform envelopment: rival platform with same users offers your functionality
- Bundled as part of a bigger offer
- Blurs market boundaries
- 视频号 vs. Douyin
A platform’s envelopment seeks to achieve platform leadership by diversely utilizing its established network effects.
# Business Analytics
## Problem with the traditional file environment
- Files maintained separately
- Data redundancy
- Data inconsistency
- Poor security
- Lack of data sharing and availability
## Database
- Database  
	- collection of tables, each table is one entity of your business  
	- E.g., transaction database includes customer table, item table, order table, and distributor table  
- Entity  
	- Generalized category representing person, place, thing on which we store and maintain information  
	- E.g., customer table, order table, item table  
- Field (or Attribute)  $\to$ **table column**
	- Specific characteristics of each entity
	- name, number, or characters that describe an aspect of a business object or activity → table column  
	- E.g., Supplier’s name, Supplier’s address, Part’s description, Part’s unit price
- Record $\to$ **table row**
	- A collection of fields that describe an instance of an entity → table row  
	- A record contains meaningful information regarding a subject  
	- Example: student record of ISOM2010 (name, id, email, major. ...)

![[Ust_Note/Attachment/Pasted image 20250524003014.png]]
- Table 
	- Contains logically related records  
	- Examples  
		- records of all students in this class  
- Primary key  
	- A special field, or group of special fields, that uniquely identifies an individual record
	- Cannot be duplicated  
	- NOT every attribute can be a primary key.  
	- Never changing, never null  
	- Examples  
		- your ID number can be used to identify you and only you in Canvas database

![[Ust_Note/Attachment/Pasted image 20250524003034.png]]
## Data Redundancy
- Extra data-entry time/cost  
- Extra storage space required  
- Data inconsistency (data-entry errors)  

Solution: Keep tables separate but define relationships to link tables → Relational Database 
## Relational Database
- Use common fields between tables to create linkage between them
- This common field must be the primary key for one of the tables  
linked, and it is called a foreign key for the other table, and vice versa.

![[Ust_Note/Attachment/Pasted image 20250524003843.png]]
## Entity-relationship diagram
- Entities  
	- A entity is a person, place, object, event or concept for which data has to be collected  
- Relationships  
	- Link between entities  
	- Corresponds to primary key-foreign key equivalencies in related tables  
- Attribute  
	- Property or characteristic of an entity or relationship type  
	- Often corresponds to a field in a table
## Cardinality of Relationships
- One-to-One  
	- Each instance in the relationship will have exactly one related instance  
	- Each student has an ID number and each ID number is given to only one student.  
- One-to-Many  
	- An instance on one side of the relationship can have many related instances, but an instance on the other side will have a maximum of one related instance  
	- A painter may have many paintings.  
- Many-to-Many  
	- Instances on both sides of the relationship can have many related instances on the other side  
	- A student may take many courses and each course may have many students.

![[Ust_Note/Attachment/Pasted image 20250524004514.png]]
## Many-to-Many Relationship
- It is redundant to link two entities with many-to-many relationship directly 
- We introduce an intermediary as a bridge and dissolve a many-to-many relationship into two one-to-many relations.
![[Ust_Note/Attachment/Pasted image 20250524005534.png]]
- e.g., assign a new primary key for each transaction
## Operation of a Relational Database
- Select  
	- Creates a subset of all records meeting stated criteria  
	- Shrink the table vertically by eliminating unwanted rows  
- Join  
	- Combines relational tables to present the server with more information than is available from individual tables  
- Project  
	- Creates a subset consisting of columns in a table  
	- Permits user to create new tables containing only desired information  
	- Shrink the table horizontally by removing unwanted columns  
## Database Management System (DBMS)
- Specific type of software for creating, storing, organizing, and accessing data from a database
- Separates the logical and physical views of the data  
	- Logical view: how end users view data  
	- Physical view: how data are actually structured and organized
## Ensuring Data Quality
- Integrity Constraint: 
	- Every record must have a primary key
	- The primary key is often numeric. No “NULL” values
	- Sales price cannot be negative
	- Phone numbers must have an area code
- Data quality audit
- Data cleansing
## Types of Business Analytics
- Descriptive Analytics: What happened?  
	- Identifying past relationships and trends using historical data
	- Describe the main features of data
		- Tools: samplings, mean, standard deviation
	- Data visualization is key
- Predictive Analytics: What might happen? 
	- Finding patterns in historical data to identify risks and opportunities
	- Tools: Regression, cluster analysis
- Prescriptive Analytics: What should we do?
	- Prescribe optimal actions that will result in the best outcomes
	- Tools: Linear Programming, sensitivity analysis
## Challenges
- Data
	- High quality = accurate and complete
- Capabilities
	- Technical: Database, Analytical tools
	- Human: Analytical skills, Business insights
- Corporate Cultural
	- Data Driven Decision-making approach
# Big Data Analytics
## Characteristics
- Volume
	- huge amounts of data spread across multiple storage devices
	- **Hadoop** and other technologies facilitate massively parallel processing 
	- Low-cost storage and cloud storage is becoming more prevalent
- Variety
	- Vary by type (media, text) and how well they are structured
	- Semantic Data Stores, **NoSQL**, and other big data frameworks are designed to accommodate varying data types and data models
- Velocity
	- dynamically analyze data in real-time
	- Advanced algorithms can identify useful data to keep and low value data to discard in order to preserve storage space
## From Traditional Approach to Big Data
- Analyze small subsets of data
	- $\to$ Analyze all data
- Govern data to the highest standard, store it, then use it for multiple purposes
	- $\to$ Understand data and usage, govern to the *appropriate* level, use it, and iterate
- Start with hypothesis and test against selected data
	- $\to$ Explore all data and identify correlations
- Analyze data after it’s been processed and landed
	- $\to$ Analyze data in motion as it’s generated, in real-time
## Big Data Elements
- NoSQL
- Hadoop
## Storing Data: NoSQL
![[Ust_Note/Attachment/Pasted image 20250524013522.png]]
### Relational Databases (SQL)
- structured way of storing data  
- Store data in a table  
- Schema must be clearly defined  
- Time consuming to understand and design the structure of the database  
- Vertically scalable  
- Can be scaled by increasing the horse-power of the h/w
### NoSQL (Big Data Elements)
- non-relational database for massive unstructured data  
- Document oriented: Store data in JSON document, key/value pairs, or graphs  
- Do not require a fixed table schema  
- Runs well on the cloud  
- Scales well horizontally  
- Can be scaled by increasing the databases servers to reduce the load
## Big Data Processing: Hadoop
Hadoop: Open-source data storage and processing platform
### Idea
Divide Work $\to$ Combine Results
![[Ust_Note/Attachment/Pasted image 20250524014308.png]]
### Usage
- Large data sets & cheap scaling  
- Fast parallel data processing  
- Data from multiple sources/formats
### Advantage
- Flexibility  
- Scalability  
- Cost effectiveness  
- Fault tolerance
## Big Data Analytics
### Machine Learning
- finding patterns in data and using those patterns to make predictions
- an approach, or subset, of AI, with an emphasis on “learning” rather than just computer programming
- learn by analyzing large amounts of data, recognize patterns among the data, and make a prediction
#### Supervised Learning
- Learn the mapping function from the input to the output
- Iteratively *makes predictions* on the training data and is corrected. Learning stops when the algorithm achieves an *acceptable level of performance*.
- To predict with the help of *labeled dataset* (known output)
	- Classification
	![[Ust_Note/Attachment/Pasted image 20250524015128.png]]
	- Regression
	![[Ust_Note/Attachment/Pasted image 20250524015155.png]]
#### Unsupervised Learning
- only have input data (X) and no corresponding output variables.  
- To model the underlying structure or distribution in the data in order to learn more about the data.
- Algorithms are left to their own devises to discover and present the interesting structure in the data.
- Trained using *unlabeled data* (unknown output)
	- Clustering
	- Association
	![[Ust_Note/Attachment/Pasted image 20250524015826.png]]
### Deep Learning
- Subset of Machine Learning
- Stimulate *Artificial Neural Network* with massive data and computing power
	- Neural networks imitate the human brain’s connectivity, classifying data sets and finding correlations between them.  
	- With its newfound knowledge, the machine can then apply its insights to other data sets
- Semi-supervised learning using both labeled and unlabeled data
#### DL Model Types
- Discriminative
	- classify or predict
	- trained on labeled data
	- learn the relationship
- Generative
	- Generate new data similar to trained data
	- understand distribution
	- predict next word in a sequence
### ML vs. DL
- ML start with **manually extracted relevant features**
![[Ust_Note/Attachment/Pasted image 20250524020319.png]]
- DL automatically extract relevant features
	 - End-to-end learning: automatically perform the task with raw data

![[Ust_Note/Attachment/Pasted image 20250524020453.png]]
### Generative AI
- AI that creates new content based on what it has learned from existing content
- Subset of (Generative) DL
	- Use Artificial Neural Networks
	- process both labeled and unlabeled data
	- using supervised, unsupervised, and semi-supervised methods
	- Large Language Model is also subset of DL
- Only is GenAI if the output is
	- Natural Language
	- Image
	- Audio
# Emerging Technologies
## Web 3

|Era| Web 1| Web 2|Web 3|
| --- | --- | --- | --- |
|Unlocks| Information | Publishing | Ownership|
|Tools| Website | Post | Token |
### Cryptocurrency
A digital asset to handle transactions in a secure way.
- Take advantages of Blockchain
- No intrinsic value: unlike gold
- No physical form: exists only in the network
- fully decentralized
### Blockchain
- a distributed and decentralized ledger that records and verifies transactions and ownership.
- highly secure, decentralized, and distributed
- transactions are recorded to a *block* that are linked in a chronological *chain*
- transactions recorded on many different computers
### Bitcoin
- First real implementation of Blockchain
- Open-Source peer-to-peer payment network
- recorded in blockchain
- created as a reward for a mining
- exchanged for other currencies
#### Consensus Algorithm: Proof-of-Work (PoW)
- The mechanism to reach consensus among the Bitcoin system  
- A transaction is considered valid when it is included in the blockchain that contains the greatest amount of computational work  
	- This makes double-spending more difficult as the size of the overall network grows. 
- Competitors are called “miners”.  
	- compete to be the first to find a nonce that satisfies the hash requirement 
- “winner” will get some Bitcoin as the reward  
- the only way to generate new bitcoins  
### Blockchain Tech
- Cryptographic Hash Function: Tamper Evident
- Digital Signature Cryptography: Ownership
### Hash
- Blockchain is a linked series of blocks 
- Each block contains data, the hash of the previous block, and a pointer to the previous block
- To change any part of a blockchain, the head pointer must be changed
- only need to check the head pointer to detect tempering
- A hash is a one-way mathematical function that applied to input data of any size, it will generate a fixed size output
	- One-way trapdoor
	- Avalanche effect: small changes lead to extensive differences
	- Collision resistance: hard to find two input with the same output
### Digital Signatures
 use a pair of keys to ensure the integrity of messages
 - a message is signed with the sender's Private Key (Secret Key) and can be verified by anyone who has access to the sender's Public Key.  
- whatever is encrypted with a Private Key may only be decrypted by its corresponding Public Key and vice versa.
- A transaction is accepted only if the signature verifies
## Benefits of Blockchain
- Disintermediation
	- Reduces costs, delay, risk
	- real time processing and settlement
- Potential to make business more
	- Secure and resilient
	- Transparent and trusted
## Applications
- Record keeping
	- Static registry
	- Identity
	- Smart contracts
- Transaction
	- Dynamic registry
	- Payment infrastructure
	- Verifiable data