# Cuckoo Hashing Implementation in Python
## Description
This project provides a Python implementation of the Cuckoo Hashing algorithm, a popular method for resolving collisions within hash tables using two or more hash functions. Cuckoo Hashing offers constant search time, alongside amortized constant insertion and deletion times, making it a robust choice for applications requiring efficient data retrieval and manipulation.


## Installation
### Prerequisites
- Python 3.6 or higher
- Linux environment (recommended for testing and development)

### Setup
Clone this repository to your local machine:
```terminal
git clone https://github.com/rajat-k1/Cuckoo-Hash.git
```
Navigate to the cloned directory:
```terminal
cd Cuckoo-Hash
```
### Usage
To use the Cuckoo Hashing implementation, import the CuckooHash class from cuckoo_hash.py. Here's a simple example to get started:
```python
from cuckoo_hash import CuckooHash

# Initialize the Cuckoo Hash Table
cuckoo_hash_table = CuckooHash(init_size=10)

# Insert elements
cuckoo_hash_table.insert(key) #returns a boolean value

# Search for an element
value = cuckoo_hash_table.search(key) #returns a boolean value

# Delete an element
cuckoo_hash_table.delete(key)

#Rehashing
cuckoo_hash_table.rehash(new_table_size)
```
<br>
Refer to the requirements.py file for detailed explanations of each member function and additional guidelines.
