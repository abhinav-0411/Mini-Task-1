import random

# Create mock validators

# PoW miner with power
miner = {"name": "Miner1", "power": random.randint(50, 150)}

# PoS staker with stake
staker = {"name": "Staker1", "stake": random.randint(100, 500)}

# DPoS delegates
delegates = [
    {"name": "DelegateA", "votes": 0},
    {"name": "DelegateB", "votes": 0},
    {"name": "DelegateC", "votes": 0},
]

# Voters randomly voting for delegates
voters = [
    {"voter": "Voter1", "vote": random.choice(delegates)["name"]},
    {"voter": "Voter2", "vote": random.choice(delegates)["name"]},
    {"voter": "Voter3", "vote": random.choice(delegates)["name"]},
]

# Count votes per delegate
for vote in voters:
    for delegate in delegates:
        if delegate["name"] == vote["vote"]:
            delegate["votes"] += 1
            break

# PoW: select miner with highest power (only one miner here)
pow_winner = miner

# PoS: select staker with highest stake (only one staker here)
pos_winner = staker

# DPoS: select delegate with most votes, break ties randomly
max_votes = max(delegate["votes"] for delegate in delegates)
top_delegates = [d for d in delegates if d["votes"] == max_votes]
dpos_winner = random.choice(top_delegates)

# Output results
print("Proof of Work (PoW) selected validator:")
print(pow_winner)
print(f"Selection logic: Miner with highest power wins. Here, power={miner['power']}.\n")

print("Proof of Stake (PoS) selected validator:")
print(pos_winner)
print(f"Selection logic: Staker with highest stake wins. Here, stake={staker['stake']}.\n")

print("Delegated Proof of Stake (DPoS) selected delegate:")
print(dpos_winner)
print("Selection logic: Delegate with most votes wins.")
print("Votes count:", {d['name']: d['votes'] for d in delegates})
print("Votes cast by voters:", {v['voter']: v['vote'] for v in voters})
