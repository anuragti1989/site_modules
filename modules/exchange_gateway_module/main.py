# modules/exchange_gateway_module/main.py
import time
import random

def run():
    print("[+] Initializing Decentralized Exchange & Fiat Gateway (exchange_gateway_module)...")
    
    # User Account Balances
    balances = {
        "BTC": 0.17763463,
        "ETH": 2.45000000,
        "USDT": 1250.50,
        "USD_FIAT": 0.00
    }
    
    print(f"    - Initial User Balances: {balances}")
    
    # 1. Simulate Deposit & Receive
    print("\n    [1] Processing Deposit / Receive Request...")
    deposit_amount = 0.05
    balances["BTC"] += deposit_amount
    print(f"        * Received {deposit_amount} BTC to Native Bech32 Address.")
    print(f"        * Updated BTC Balance: {balances['BTC']:.8f} BTC")
    
    # 2. Simulate Buy & Sell (Order Book Execution)
    print("\n    [2] Executing Spot Order (Buy/Sell)...")
    sell_amount_btc = 0.02
    btc_price_usd = 64500.00
    fiat_proceeds = sell_amount_btc * btc_price_usd
    balances["BTC"] -= sell_amount_btc
    balances["USDT"] += fiat_proceeds
    print(f"        * Sold {sell_amount_btc} BTC at ${btc_price_usd:,.2f}/BTC")
    print(f"        * Credited USDT: +${fiat_proceeds:,.2f}")
    
    # 3. Simulate Cross-Chain Swap (BTC -> ETH)
    print("\n    [3] Executing Cross-Chain Atomic Swap...")
    swap_amount_usdt = 500.00
    eth_price_usd = 3200.00
    eth_acquired = swap_amount_usdt / eth_price_usd
    balances["USDT"] -= swap_amount_usdt
    balances["ETH"] += eth_acquired
    print(f"        * Swapped ${swap_amount_usdt:.2f} USDT for {eth_acquired:.4f} ETH")
    
    # 4. Simulate Withdrawal to PayPal (Fiat Gateway)
    print("\n    [4] Processing Withdrawal to PayPal Account...")
    paypal_email = "anurag.tiwari@gateway-local.internal"
    withdrawal_fiat = 250.00
    
    if balances["USDT"] >= withdrawal_fiat:
        balances["USDT"] -= withdrawal_fiat
        balances["USD_FIAT"] += withdrawal_fiat
        print(f"        * Converting {withdrawal_fiat} USDT to USD Fiat...")
        print(f"        * Initiating PayPal Instant Payout to: {paypal_email}")
        print(f"        * Status: SUCCESS (Transaction ID: PP-TXN-{random.randint(100000, 999999)})")
    else:
        print("        * Status: FAILED - Insufficient liquidity.")
        
    print(f"\n    - Final Portfolio State:")
    for asset, amt in balances.items():
        print(f"      * {asset}: {amt:,.4f}")
        
    print("[+] exchange_gateway_module task completed successfully.\n")

if __name__ == "__main__":
    run()



