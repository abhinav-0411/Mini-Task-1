import hashlib
import time

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def __str__(self):
        return (
            f"Block #{self.index}\n"
            f"Timestamp     : {self.timestamp}\n"
            f"Data          : {self.data}\n"
            f"Previous Hash : {self.previous_hash}\n"
            f"Hash          : {self.hash}\n"
            f"Nonce         : {self.nonce}\n"
            "----------------------------------------"
        )

def create_genesis_block():
    return Block(0, time.ctime(), "Genesis Block", "0")

def create_next_block(previous_block, data):
    return Block(previous_block.index + 1, time.ctime(), data, previous_block.hash)

# Step 1: Create a blockchain with 3 blocks
blockchain = [create_genesis_block()]
blockchain.append(create_next_block(blockchain[-1], "Second block data"))
blockchain.append(create_next_block(blockchain[-1], "Third block data"))

print("🟢 Original Blockchain:")
for block in blockchain:
    print(block)

# Step 2: Tamper with Block 1's data
print("\n🔴 Tampering Block #1's Data...")
blockchain[1].data = "Tampered Data"
blockchain[1].hash = blockchain[1].calculate_hash()

# Step 3: Show updated blockchain without fixing hashes
print("\n🔴 Blockchain After Tampering (Invalid Chain):")
for block in blockchain:
    print(block)

# Step 4 (Optional): Fix hashes to restore validity
print("\n🟡 Fixing subsequent block hashes manually...")
blockchain[2].previous_hash = blockchain[1].hash
blockchain[2].hash = blockchain[2].calculate_hash()

print("\n🟢 Blockchain After Fixing:")
for block in blockchain:
    print(block)
