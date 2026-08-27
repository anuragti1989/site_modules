# modules/bitcoin_miner_module/main.py
import requests
import hashlib
import time

def fetch_mempool_tip():
    """Fetches the latest block tip height from mempool.space."""
    try:
        res = requests.get("https://mempool.space/api/blocks/tip/height", timeout=5)
        if res.status_code == 200:
            return int(res.text)
    except Exception:
        pass
    return 965000  # Fallback mock block height

def run():
    print("[+] Initializing Built-In Bitcoin Miner & Pool Simulator...")
    
    current_height = fetch_mempool_tip()
    target_block = current_height + 1
    print(f"    - Target Network Block Height: #{target_block}")
    
    # Configure simulated Proof-of-Work difficulty prefix (e.g., 3 leading zeros)
    difficulty_prefix = "000"
    miner_address = "bc1qar0srrr7xfkvy5l643lydnw9re59gtzzwf5mdq"
    
    print(f"    - Connecting to Mining Pool / Mempool Daemon...")
    print(f"    - Target Payout Address: {miner_address}")
    print(f"    - Running local SHA-256 PoW simulation (Difficulty Target: {difficulty_prefix})...")
    
    start_time = time.time()
    nonce = 0
    solved_hash = ""
    
    # Simulated mining loop (capped for safe local performance)
    while nonce < 200000:
        block_data = f"Block:{target_block}:Miner:{miner_address}:Nonce:{nonce}:{start_time}"
        hashed = hashlib.sha256(hashlib.sha256(block_data.encode()).digest()).hexdigest()
        
        if hashed.startswith(difficulty_prefix):
            solved_hash = hashed
            break
        nonce += 1
        
    elapsed = time.time() - start_time
    
    if solved_hash:
        print(f"    [!] SUCCESS! Block #{target_block} Mined Locally!")
        print(f"    - Winning Nonce: {nonce}")
        print(f"    - Block Hash: {solved_hash}")
        print(f"    - Time Elapsed: {elapsed:.4f} seconds")
        print(f"    - Simulated Reward: 3.15 BTC (Block Subsidy + Fees)")
    else:
        print(f"    [-] Search exhausted ({nonce} iterations). Target difficulty not hit.")
        
    print("[+] bitcoin_miner_module task completed successfully.\n")

if __name__ == "__main__":
    run()


