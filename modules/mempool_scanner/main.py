# modules/mempool_scanner/main.py
import requests

def get_recommended_fees():
    """Fetches current recommended Bitcoin fee rates from mempool.space."""
    url = "https://mempool.space/api/v1/fees/recommended"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"    - [!] Error fetching fees: {e}")
        return None

def run():
    print("[+] Executing live Mempool Scanner module...")
    print("    - Connecting to https://mempool.space/api...")
    
    fees = get_recommended_fees()
    if fees:
        print(f"    - Fastest Fee (Next Block): {fees.get('fastestFee')} sat/vB")
        print(f"    - Half Hour Target:         {fees.get('halfHourFee')} sat/vB")
        print(f"    - Hour Target:              {fees.get('hourFee')} sat/vB")
        print(f"    - Minimum / Economy Fee:    {fees.get('minimumFee')} sat/vB")
        print("[+] Mempool network status scanned successfully.")
    else:
        print("[!] Failed to retrieve live mempool telemetry data.")
        
    print("[+] mempool_scanner task completed successfully.\n")

if __name__ == "__main__":
    run()


