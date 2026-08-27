#!/usr/bin/env python3
"""
================================================================================
ENTERPRISE HARDWARE SECURITY CHIPSET & INTEGRATED CIRCUIT BOARD OS (OS/3500)
Architecture: Multi-Network HD Crypto, PoW Asic Core, Mempool Visualizer, 
              Blockchain Explorer Scanner, DEX Orderbook & Neural AI Autopilot.
================================================================================
"""

import hashlib
import hmac
import json
import secrets
import threading
import time
import uuid
import math
import os
import sys
import socket
import struct
import platform
import random
from flask import Flask, jsonify, render_template_string, request, Response, session
from typing import Dict, List, Any, Optional, Tuple

# ==============================================================================
# 0. HARDWARE INTEGRATED CIRCUIT BOARD MODULES & CHIPSET EMULATOR
# ==============================================================================
class HardwareChipsetRegister:
    """Emulates silicon physical layer registers, voltage gates, and temperature sensors."""
    def __init__(self):
        self.asic_core_temp_c = 42.5
        self.board_voltage_v = 12.04
        self.clock_frequency_mhz = 1450.0
        self.secure_enclave_locked = True
        self.eeprom_flash_cycles = 1420
        self.quantum_entropy_pool = secrets.token_bytes(64)

    def read_telemetry(self) -> Dict[str, Any]:
        self.asic_core_temp_c = round(self.asic_core_temp_c + (secrets.randbelow(11) - 5) / 10.0, 2)
        self.board_voltage_v = round(12.0 + (secrets.randbelow(9) - 4) / 100.0, 2)
        return {
            "core_temp_c": self.asic_core_temp_c,
            "voltage_v": self.board_voltage_v,
            "clock_mhz": self.clock_frequency_mhz,
            "enclave_status": "SECURE_LOCKED" if self.secure_enclave_locked else "UNLOCKED",
            "flash_cycles": self.eeprom_flash_cycles,
            "entropy_bits": len(self.quantum_entropy_pool) * 8
        }

# =====================================================================
# 1. ADVANCED MULTI-NETWORK HD CRYPTO ENGINE (BIP-39/44/84/141)
# =====================================================================
class MultiNetworkHDCrypto:
    WORDLIST = [
        "abandon", "ability", "able", "about", "above", "absent", "absorb", "abstract",
        "absurd", "abuse", "access", "accident", "account", "accuse", "achieve", "acid",
        "acoustic", "acquire", "across", "act", "action", "actor", "actress", "actual",
        "adapt", "add", "addict", "address", "adjust", "admit", "adult", "advance",
        "advice", "aerobic", "affair", "afford", "afraid", "again", "age", "agent",
        "agree", "ahead", "aim", "air", "airport", "aisle", "alarm", "album",
        "alcohol", "alert", "alien", "all", "alley", "allow", "almost", "alone",
        "alpha", "already", "also", "alter", "always", "amateur", "amazing", "among",
        "amount", "amused", "analyst", "anchor", "ancient", "anger", "angle", "angry",
        "animal", "ankle", "announce", "annual", "answer", "antenna", "antique", "anxiety",
        "any", "apart", "apology", "appear", "apple", "approve", "april", "arch",
        "arctic", "area", "arena", "argue", "arm", "armed", "armor", "army",
        "around", "arrange", "arrest", "arrive", "arrow", "art", "artefact", "artist",
        "artwork", "ask", "aspect", "assault", "asset", "assist", "assume", "asthma",
        "athlete", "atom", "attack", "attend", "attitude", "attract", "auction", "audit",
        "august", "aunt", "author", "auto", "autumn", "average", "avocado", "avoid",
        "awake", "aware", "away", "awesome", "awful", "awkward", "axis", "baby"
    ]

    @classmethod
    def generate_mnemonic(cls, word_count: int = 12) -> str:
        return " ".join(secrets.choice(cls.WORDLIST) for _ in range(word_count))

    @staticmethod
    def mnemonic_to_seed(mnemonic: str, passphrase: str = "") -> bytes:
        return hashlib.pbkdf2_hmac(
            'sha512',
            mnemonic.strip().encode('utf-8'),
            f"mnemonic{passphrase}".encode('utf-8'),
            iterations=2048
        )

    @classmethod
    def derive_all_networks(cls, seed: bytes) -> Dict[str, Dict[str, str]]:
        networks = {
            "BTC_NATIVE": {"name": "Native Bitcoin (Legacy P2PKH)", "coin_symbol": "BTC", "path": "m/44'/0'/0'/0/0", "prefix": "1", "layer": "Layer 1 Mainnet"},
            "BTC_SEGWIT": {"name": "SegWit Bitcoin (Native Bech32)", "coin_symbol": "BTC (SegWit)", "path": "m/84'/0'/0'/0/0", "prefix": "bc1q", "layer": "Layer 1 SegWit"},
            "BTC_LIGHTNING": {"name": "Bitcoin Lightning Network", "coin_symbol": "sats / LN-BTC", "path": "m/44'/0'/0'/2/0", "prefix": "lnbc", "layer": "Layer 2 State Channels"},
            "BTC_ETH": {"name": "Ethereum Wrapped BTC (ERC-20 WBTC)", "coin_symbol": "WBTC (ERC20)", "path": "m/44'/60'/0'/0/0", "prefix": "0x", "layer": "Ethereum EVM Bridge"},
            "BTC_BSC": {"name": "Binance Wrapped BTC (BEP-20 BTCB)", "coin_symbol": "BTCB (BEP20)", "path": "m/44'/714'/0'/0/0", "prefix": "0x", "layer": "BNB Chain Bridge"},
            "BTC_TRON": {"name": "Tron Bitcoin (TRC-20 BTCTRON)", "coin_symbol": "BTCTRON (TRC20)", "path": "m/44'/195'/0'/0/0", "prefix": "T", "layer": "TRON TRC20 Gateway"},
            "BTC_SOL": {"name": "Solana Wrapped BTC (SPL-BTC)", "coin_symbol": "solBTC (SPL)", "path": "m/44'/501'/0'/0/0", "prefix": "So1", "layer": "Solana Sealevel Bridge"}
        }

        derived = {}
        for net_key, info in networks.items():
            path_bytes = info["path"].encode('utf-8')
            hmac_hash = hmac.new(b"Bitcoin Master Seed Node", seed + path_bytes, hashlib.sha512).digest()
            priv_hex = hmac_hash[:32].hex()
            pub_hex = hashlib.sha256(hmac_hash[32:]).hexdigest()

            if info["prefix"] == "1":
                addr = f"1{pub_hex[:33]}"
            elif info["prefix"] == "bc1q":
                addr = f"bc1q{pub_hex[:38]}"
            elif info["prefix"] == "lnbc":
                addr = f"lnbc{pub_hex[:45]}1pnvd8e"
            elif info["prefix"] == "0x":
                addr = f"0x{pub_hex[:40]}"
            elif info["prefix"] == "T":
                addr = f"T{pub_hex[:33]}"
            elif info["prefix"] == "So1":
                addr = f"So1{pub_hex[:40]}"
            else:
                addr = f"addr_{pub_hex[:32]}"

            derived[net_key] = {
                "network_name": info["name"],
                "coin_symbol": info["coin_symbol"],
                "layer": info["layer"],
                "derivation_path": info["path"],
                "private_key": f"0x{priv_hex}",
                "public_key": f"0x{pub_hex}",
                "address": addr
            }
        return derived


# =====================================================================
# 2. TOP 100 COINMARKETCAP ASSET VAULT REPOSITORY
# =====================================================================
TOP_100_COINMARKETCAP_DATA = [
    {"rank": 1, "symbol": "BTC", "name": "Bitcoin", "price": 68450.00, "change_24h": "+2.4%"},
    {"rank": 2, "symbol": "ETH", "name": "Ethereum", "price": 3540.00, "change_24h": "+1.8%"},
    {"rank": 3, "symbol": "USDT", "name": "Tether USDt", "price": 1.00, "change_24h": "0.0%"},
    {"rank": 4, "symbol": "BNB", "name": "BNB", "price": 592.50, "change_24h": "+0.9%"},
    {"rank": 5, "symbol": "SOL", "name": "Solana", "price": 152.80, "change_24h": "+4.1%"},
    {"rank": 6, "symbol": "USDC", "name": "USDC", "price": 1.00, "change_24h": "0.0%"},
    {"rank": 7, "symbol": "XRP", "name": "XRP", "price": 0.584, "change_24h": "-0.5%"},
    {"rank": 8, "symbol": "DOGE", "name": "Dogecoin", "price": 0.124, "change_24h": "+3.2%"},
    {"rank": 9, "symbol": "TON", "name": "Toncoin", "price": 5.45, "change_24h": "+1.2%"},
    {"rank": 10, "symbol": "ADA", "name": "Cardano", "price": 0.354, "change_24h": "+0.4%"},
    {"rank": 11, "symbol": "AVAX", "name": "Avalanche", "price": 28.40, "change_24h": "+2.1%"},
    {"rank": 12, "symbol": "SHIB", "name": "Shiba Inu", "price": 0.0000185, "change_24h": "+1.5%"},
    {"rank": 13, "symbol": "LINK", "name": "Chainlink", "price": 11.85, "change_24h": "+3.8%"},
    {"rank": 14, "symbol": "BCH", "name": "Bitcoin Cash", "price": 348.20, "change_24h": "+0.7%"},
    {"rank": 15, "symbol": "DOT", "name": "Polkadot", "price": 4.35, "change_24h": "-0.2%"},
    {"rank": 16, "symbol": "DAI", "name": "Dai", "price": 1.00, "change_24h": "0.0%"},
    {"rank": 17, "symbol": "SUI", "name": "Sui", "price": 1.95, "change_24h": "+8.4%"},
    {"rank": 18, "symbol": "LEO", "name": "UNUS SED LEO", "price": 5.88, "change_24h": "+0.1%"},
    {"rank": 19, "symbol": "LTC", "name": "Litecoin", "price": 66.80, "change_24h": "+0.5%"},
    {"rank": 20, "symbol": "NEAR", "name": "NEAR Protocol", "price": 4.85, "change_24h": "+2.9%"},
    {"rank": 21, "symbol": "PEPE", "name": "Pepe", "price": 0.0000102, "change_24h": "+5.4%"},
    {"rank": 22, "symbol": "UNI", "name": "Uniswap", "price": 7.65, "change_24h": "+1.1%"},
    {"rank": 23, "symbol": "APT", "name": "Aptos", "price": 8.42, "change_24h": "+4.3%"},
    {"rank": 24, "symbol": "ICP", "name": "Internet Computer", "price": 8.15, "change_24h": "+0.8%"},
    {"rank": 25, "symbol": "KAS", "name": "Kaspa", "price": 0.138, "change_24h": "-1.4%"},
    {"rank": 26, "symbol": "ETC", "name": "Ethereum Classic", "price": 19.50, "change_24h": "+0.3%"},
    {"rank": 27, "symbol": "XMR", "name": "Monero", "price": 154.20, "change_24h": "+1.9%"},
    {"rank": 28, "symbol": "POL", "name": "Polygon", "price": 0.385, "change_24h": "+1.2%"},
    {"rank": 29, "symbol": "FET", "name": "Artificial Superintelligence", "price": 1.42, "change_24h": "+6.2%"},
    {"rank": 30, "symbol": "STX", "name": "Stacks", "price": 1.82, "change_24h": "+3.5%"},
    {"rank": 31, "symbol": "RENDER", "name": "Render", "price": 5.42, "change_24h": "+4.8%"},
    {"rank": 32, "symbol": "ATOM", "name": "Cosmos", "price": 4.25, "change_24h": "-0.6%"},
    {"rank": 33, "symbol": "IMX", "name": "Immutable", "price": 1.34, "change_24h": "+2.2%"},
    {"rank": 34, "symbol": "TAO", "name": "Bittensor", "price": 542.10, "change_24h": "+11.4%"},
    {"rank": 35, "symbol": "OM", "name": "MANTRA", "price": 1.28, "change_24h": "+7.5%"},
    {"rank": 36, "symbol": "NEAR", "name": "NEAR Protocol", "price": 4.85, "change_24h": "+2.9%"},
    {"rank": 37, "symbol": "WIF", "name": "dogwifhat", "price": 2.15, "change_24h": "+9.1%"},
    {"rank": 38, "symbol": "HBAR", "name": "Hedera", "price": 0.054, "change_24h": "+1.1%"},
    {"rank": 39, "symbol": "APT", "name": "Aptos", "price": 8.42, "change_24h": "+4.3%"},
    {"rank": 40, "symbol": "INJ", "name": "Injective", "price": 18.50, "change_24h": "+3.4%"},
    {"rank": 41, "symbol": "OP", "name": "Optimism", "price": 1.65, "change_24h": "+2.5%"},
    {"rank": 42, "symbol": "ARB", "name": "Arbitrum", "price": 0.54, "change_24h": "+1.2%"},
    {"rank": 43, "symbol": "FLOKI", "name": "FLOKI", "price": 0.000142, "change_24h": "+4.1%"},
    {"rank": 44, "symbol": "TIA", "name": "Celestia", "price": 4.85, "change_24h": "-2.1%"},
    {"rank": 45, "symbol": "POL", "name": "Polygon Ecosystem", "price": 0.385, "change_24h": "+0.8%"},
    {"rank": 46, "symbol": "GRT", "name": "The Graph", "price": 0.174, "change_24h": "+2.0%"},
    {"rank": 47, "symbol": "BONK", "name": "Bonk", "price": 0.0000214, "change_24h": "+6.5%"},
    {"rank": 48, "symbol": "LDO", "name": "Lido DAO", "price": 1.12, "change_24h": "+0.4%"},
    {"rank": 49, "symbol": "SEI", "name": "Sei", "price": 0.36, "change_24h": "+5.2%"},
    {"rank": 50, "symbol": "SUI", "name": "Sui", "price": 1.95, "change_24h": "+8.4%"},
    {"rank": 51, "symbol": "MKR", "name": "Maker", "price": 1450.00, "change_24h": "+0.5%"},
    {"rank": 52, "symbol": "RUNE", "name": "THORChain", "price": 4.25, "change_24h": "+1.9%"},
    {"rank": 53, "symbol": "KAS", "name": "Kaspa", "price": 0.138, "change_24h": "-1.4%"},
    {"rank": 54, "symbol": "JUP", "name": "Jupiter", "price": 0.85, "change_24h": "+3.1%"},
    {"rank": 55, "symbol": "PYTH", "name": "Pyth Network", "price": 0.31, "change_24h": "+2.4%"},
    {"rank": 56, "symbol": "FLR", "name": "Flare", "price": 0.014, "change_24h": "-0.5%"},
    {"rank": 57, "symbol": "BEAM", "name": "Beam", "price": 0.018, "change_24h": "+1.7%"},
    {"rank": 58, "symbol": "THETA", "name": "Theta Network", "price": 1.25, "change_24h": "+0.8%"},
    {"rank": 59, "symbol": "ALGO", "name": "Algorand", "price": 0.135, "change_24h": "+1.0%"},
    {"rank": 60, "symbol": "STX", "name": "Stacks", "price": 1.82, "change_24h": "+3.5%"},
    {"rank": 61, "symbol": "XTZ", "name": "Tezos", "price": 0.68, "change_24h": "+0.2%"},
    {"rank": 62, "symbol": "EGLD", "name": "MultiversX", "price": 26.50, "change_24h": "+1.1%"},
    {"rank": 63, "symbol": "AXS", "name": "Axie Infinity", "price": 4.55, "change_24h": "+2.0%"},
    {"rank": 64, "symbol": "SAND", "name": "The Sandbox", "price": 0.28, "change_24h": "+1.5%"},
    {"rank": 65, "symbol": "MANA", "name": "Decentraland", "price": 0.31, "change_24h": "+1.2%"},
    {"rank": 66, "symbol": "EOS", "name": "EOS", "price": 0.52, "change_24h": "-0.4%"},
    {"rank": 67, "symbol": "FLOW", "name": "Flow", "price": 0.58, "change_24h": "+0.9%"},
    {"rank": 68, "symbol": "NEO", "name": "NEO", "price": 10.40, "change_24h": "+0.3%"},
    {"rank": 69, "symbol": "CHZ", "name": "Chiliz", "price": 0.065, "change_24h": "+2.1%"},
    {"rank": 70, "symbol": "KCS", "name": "KuCoin Token", "price": 8.10, "change_24h": "0.0%"},
    {"rank": 71, "symbol": "CRV", "name": "Curve DAO", "price": 0.28, "change_24h": "+0.6%"},
    {"rank": 72, "symbol": "SNX", "name": "Synthetix", "price": 1.45, "change_24h": "+1.8%"},
    {"rank": 73, "symbol": "MINA", "name": "Mina", "price": 0.42, "change_24h": "+1.1%"},
    {"rank": 74, "symbol": "GALA", "name": "Gala", "price": 0.022, "change_24h": "+3.4%"},
    {"rank": 75, "symbol": "BSV", "name": "Bitcoin SV", "price": 45.20, "change_24h": "-1.0%"},
    {"rank": 76, "symbol": "BTT", "name": "BitTorrent", "price": 0.0000011, "change_24h": "0.0%"},
    {"rank": 77, "symbol": "CAKE", "name": "PancakeSwap", "price": 2.15, "change_24h": "+2.5%"},
    {"rank": 78, "symbol": "ROSE", "name": "Oasis Network", "price": 0.068, "change_24h": "+1.4%"},
    {"rank": 79, "symbol": "AKT", "name": "Akash Network", "price": 2.45, "change_24h": "+4.2%"},
    {"rank": 80, "symbol": "ZEC", "name": "Zcash", "price": 28.50, "change_24h": "+0.8%"},
    {"rank": 81, "symbol": "DASH", "name": "Dash", "price": 24.10, "change_24h": "+0.5%"},
    {"rank": 82, "symbol": "GMT", "name": "STEPN", "price": 0.12, "change_24h": "+1.9%"},
    {"rank": 83, "symbol": "ENJ", "name": "Enjin Coin", "price": 0.16, "change_24h": "+0.7%"},
    {"rank": 84, "symbol": "ZRX", "name": "0x Protocol", "price": 0.32, "change_24h": "+1.2%"},
    {"rank": 85, "symbol": "BAT", "name": "Basic Attention Token", "price": 0.18, "change_24h": "+0.4%"},
    {"rank": 86, "symbol": "SC", "name": "Siacoin", "price": 0.0045, "change_24h": "-0.2%"},
    {"rank": 87, "symbol": "QTUM", "name": "Qtum", "price": 2.40, "change_24h": "+0.3%"},
    {"rank": 88, "symbol": "IOST", "name": "IOST", "price": 0.0068, "change_24h": "+1.0%"},
    {"rank": 89, "symbol": "ICX", "name": "ICON", "price": 0.14, "change_24h": "+0.5%"},
    {"rank": 90, "symbol": "ONT", "name": "Ontology", "price": 0.18, "change_24h": "+0.2%"},
    {"rank": 91, "symbol": "WAVES", "name": "Waves", "price": 1.15, "change_24h": "-1.2%"},
    {"rank": 92, "symbol": "KSM", "name": "Kusama", "price": 18.50, "change_24h": "+0.6%"},
    {"rank": 93, "symbol": "RVN", "name": "Ravencoin", "price": 0.016, "change_24h": "+2.1%"},
    {"rank": 94, "symbol": "HNT", "name": "Helium", "price": 6.80, "change_24h": "+3.9%"},
    {"rank": 95, "symbol": "GLM", "name": "Golem", "price": 0.32, "change_24h": "+1.5%"},
    {"rank": 96, "symbol": "SKL", "name": "SKALE", "price": 0.038, "change_24h": "+2.4%"},
    {"rank": 97, "symbol": "CKB", "name": "Nervos Network", "price": 0.012, "change_24h": "+4.5%"},
    {"rank": 98, "symbol": "JASMY", "name": "JasmyCoin", "price": 0.019, "change_24h": "+5.8%"},
    {"rank": 99, "symbol": "COMP", "name": "Compound", "price": 48.20, "change_24h": "+1.1%"},
    {"rank": 100, "symbol": "YFI", "name": "yearn.finance", "price": 6500.00, "change_24h": "+0.9%"}
]


# =====================================================================
# 3. MULTI-PAIR TRADE TERMINAL & INVEST/PREDICT ENGINE
# =====================================================================
class TradeTerminalEngine:
    PAIRS = {
        "BTC/USDTERC20": {"base": "BTC", "quote": "USDTERC20", "price": 68450.00, "precision": 2},
        "BTC/USDTBEP20": {"base": "BTC", "quote": "USDTBEP20", "price": 68442.50, "precision": 2},
        "BTC/USDTTRC20": {"base": "BTC", "quote": "USDTTRC20", "price": 68458.20, "precision": 2},
        "BTC/BNB":        {"base": "BTC", "quote": "BNB",        "price": 115.30,   "precision": 4},
        "BTC/Tron":       {"base": "BTC", "quote": "Tron",       "price": 526500.0, "precision": 1},
        "BTC/ETH":        {"base": "BTC", "quote": "ETH",        "price": 19.34,    "precision": 4},
        "BTC/Solana":     {"base": "BTC", "quote": "Solana",     "price": 448.85,   "precision": 3},
    }

    def __init__(self):
        self.prices = {k: v["price"] for k, v in self.PAIRS.items()}
        self.history = {k: [v["price"] * (1 + secrets.choice([-0.005, 0.005, -0.002, 0.003, 0.0])) for _ in range(40)] for k, v in self.PAIRS.items()}
        self.active_predictions: List[Dict[str, Any]] = []
        self.resolved_predictions: List[Dict[str, Any]] = []
        self.order_book: Dict[str, Dict[str, List[Dict[str, float]]]] = {}
        self._init_order_books()

    def _init_order_books(self):
        for pair in self.PAIRS:
            base_p = self.prices[pair]
            bids = [{"price": round(base_p * (1 - 0.001 * i), 2), "amount": round(0.1 + i * 0.15, 3)} for i in range(1, 8)]
            asks = [{"price": round(base_p * (1 + 0.001 * i), 2), "amount": round(0.12 + i * 0.14, 3)} for i in range(1, 8)]
            self.order_book[pair] = {"bids": bids, "asks": asks}

    def tick_market(self):
        for pair in self.PAIRS:
            delta_pct = (secrets.randbelow(41) - 20) / 10000.0
            new_p = round(self.prices[pair] * (1.0 + delta_pct), self.PAIRS[pair]["precision"])
            self.prices[pair] = new_p
            self.history[pair].append(new_p)
            if len(self.history[pair]) > 60:
                self.history[pair].pop(0)

            self.order_book[pair]["bids"] = [{"price": round(new_p * (1 - 0.0008 * i), self.PAIRS[pair]["precision"]), "amount": round(secrets.randbelow(150) / 100.0 + 0.1, 3)} for i in range(1, 8)]
            self.order_book[pair]["asks"] = [{"price": round(new_p * (1 + 0.0008 * i), self.PAIRS[pair]["precision"]), "amount": round(secrets.randbelow(150) / 100.0 + 0.1, 3)} for i in range(1, 8)]

    def create_prediction(self, pair: str, direction: str, stake_amount: float, duration_seconds: int = 30) -> Dict[str, Any]:
        strike_price = self.prices.get(pair, 68450.00)
        pred_id = f"PRD-{secrets.token_hex(4).upper()}"
        expiry_time = time.time() + duration_seconds

        contract = {
            "prediction_id": pred_id,
            "pair": pair,
            "direction": direction,
            "stake_amount": stake_amount,
            "strike_price": strike_price,
            "expiry_time": expiry_time,
            "duration": duration_seconds,
            "payout_rate": 0.85,
            "status": "OPEN",
            "settlement_price": None,
            "profit": 0.0
        }
        self.active_predictions.append(contract)
        return contract

    def evaluate_predictions(self, node_ref) -> List[Dict[str, Any]]:
        now = time.time()
        settled = []
        for contract in list(self.active_predictions):
            if now >= contract["expiry_time"]:
                pair = contract["pair"]
                settle_price = self.prices[pair]
                contract["settlement_price"] = settle_price

                is_win = False
                if contract["direction"] == "CALL_IN" and settle_price > contract["strike_price"]:
                    is_win = True
                elif contract["direction"] == "CALL_OUT" and settle_price < contract["strike_price"]:
                    is_win = True

                if is_win:
                    payout = contract["stake_amount"] * (1.0 + contract["payout_rate"])
                    contract["status"] = "WON"
                    contract["profit"] = contract["stake_amount"] * contract["payout_rate"]
                    node_ref.balances["USDT"] += payout
                    node_ref._dispatch_tx("BTC_SEGWIT", f"PREDICTION_WIN_{contract['direction']}", payout, "Binary Oracle", f"ROI: +85% | Contract: {contract['prediction_id']}")
                else:
                    contract["status"] = "LOST"
                    contract["profit"] = -contract["stake_amount"]
                    node_ref._dispatch_tx("BTC_SEGWIT", f"PREDICTION_EXPIRED_{contract['direction']}", contract["stake_amount"], "Binary Oracle", f"Loss | Contract: {contract['prediction_id']}")

                self.active_predictions.remove(contract)
                self.resolved_predictions.insert(0, contract)
                settled.append(contract)
        return settled


# =====================================================================
# 4. PROOF-OF-WORK BITCOIN MINING & AI ROBOT ENGINE
# =====================================================================
class BitcoinPoWMiner:
    def __init__(self, node_ref):
        self.node = node_ref
        self.is_mining = False
        self.mining_thread: Optional[threading.Thread] = None
        self.hashrate_mhs = 0.0
        self.total_hashes = 0
        self.blocks_mined = 0
        self.shares_accepted = 0
        self.difficulty_prefix = "0000"
        self.current_nonce = 0
        self.mining_logs: List[str] = []

    def log(self, message: str):
        ts = time.strftime("%H:%M:%S")
        entry = f"[{ts}] [MINER] {message}"
        self.mining_logs.insert(0, entry)
        if len(self.mining_logs) > 50:
            self.mining_logs.pop()

    def start(self):
        if self.is_mining:
            return
        self.is_mining = True
        self.mining_thread = threading.Thread(target=self._mining_loop, daemon=True)
        self.mining_thread.start()
        self.log("PoW Mining thread active. Target Prefix: " + self.difficulty_prefix)

    def stop(self):
        self.is_mining = False
        self.hashrate_mhs = 0.0
        self.log("Miner suspended by hardware controller.")

    def _mining_loop(self):
        start_time = time.time()
        hashes_in_window = 0
        while self.is_mining:
            self.current_nonce += 1
            hashes_in_window += 1
            self.total_hashes += 1

            prev_block = self.node.mempool_engine.blocks[0]["hash"] if self.node.mempool_engine.blocks else "00000000000000000000"
            payload = f"{self.node.mempool_engine.block_height}:{prev_block}:{self.current_nonce}:{time.time()}"
            block_candidate = hashlib.sha256(hashlib.sha256(payload.encode()).digest()).hexdigest()

            if block_candidate.startswith(self.difficulty_prefix):
                self.blocks_mined += 1
                self.shares_accepted += 1
                self.log(f"🔥 BLOCK SOLVED! Nonce: {self.current_nonce} | Hash: {block_candidate[:18]}...")
                self.node.credit_mining_reward(3.125, block_candidate)

            if hashes_in_window >= 50000:
                elapsed = time.time() - start_time
                if elapsed > 0:
                    self.hashrate_mhs = round((hashes_in_window / elapsed) / 10000.0, 2)
                hashes_in_window = 0
                start_time = time.time()
                time.sleep(0.01)

    def get_stats(self) -> Dict[str, Any]:
        return {
            "is_mining": self.is_mining,
            "hashrate_mhs": self.hashrate_mhs,
            "total_hashes": self.total_hashes,
            "blocks_mined": self.blocks_mined,
            "shares_accepted": self.shares_accepted,
            "difficulty": self.difficulty_prefix,
            "logs": self.mining_logs[:15]
        }


class AITradingRobot:
    def __init__(self, node_ref):
        self.node = node_ref
        self.is_active = False
        self.ai_thread: Optional[threading.Thread] = None
        self.win_count = 0
        self.total_trades = 0
        self.profit_usd_accumulated = 0.0
        self.current_strategy = "CROSS_PAIR_ARBITRAGE"
        self.ai_logs: List[str] = []

    def log(self, message: str):
        ts = time.strftime("%H:%M:%S")
        entry = f"[{ts}] [AI ROBOT] {message}"
        self.ai_logs.insert(0, entry)
        if len(self.ai_logs) > 50:
            self.ai_logs.pop()

    def start(self):
        if self.is_active:
            return
        self.is_active = True
        self.ai_thread = threading.Thread(target=self._ai_loop, daemon=True)
        self.ai_thread.start()
        self.log("AI Neural Arbitrage Engine online.")

    def stop(self):
        self.is_active = False
        self.log("AI Trading Autopilot stopped.")

    def _ai_loop(self):
        while self.is_active:
            time.sleep(3.5)
            if not self.is_active:
                break

            p_erc = self.node.terminal.prices["BTC/USDTERC20"]
            p_bep = self.node.terminal.prices["BTC/USDTBEP20"]
            spread = p_erc - p_bep

            if spread > 5.0 and self.node.balances["USDT"] >= 150:
                trade_usd = 150.0
                btc_qty = trade_usd / p_bep
                self.node.balances["USDT"] -= trade_usd
                self.node.balances["BTC_SEGWIT"] += btc_qty
                self.total_trades += 1
                self.win_count += 1
                profit = round(spread * 0.05 + 3.2, 2)
                self.profit_usd_accumulated += profit
                self.node._dispatch_tx("BTC_BSC", "AI_CROSS_ARBITRAGE_BUY", btc_qty, "BNB Bridge Gateway", f"Spread Delta: ${spread:.2f}")
                self.log(f"🤖 ARBITRAGE: Bought on BSC -> Spread +${spread:.2f} | P&L: +${profit}")

            elif spread < -5.0 and self.node.balances["BTC_SEGWIT"] >= 0.003:
                btc_sell = 0.003
                usd_yield = btc_sell * p_erc
                self.node.balances["BTC_SEGWIT"] -= btc_sell
                self.node.balances["USDT"] += usd_yield
                self.total_trades += 1
                self.win_count += 1
                profit = round(abs(spread) * 0.04 + 2.8, 2)
                self.profit_usd_accumulated += profit
                self.node._dispatch_tx("BTC_ETH", "AI_CROSS_ARBITRAGE_SELL", btc_sell, "Uniswap L3 Router", f"Yield: +${profit}")
                self.log(f"🤖 ARBITRAGE: Sold on ERC20 | Profit: +${profit}")

    def get_stats(self) -> Dict[str, Any]:
        win_rate = round((self.win_count / self.total_trades) * 100.0, 1) if self.total_trades > 0 else 100.0
        return {
            "is_active": self.is_active,
            "strategy": self.current_strategy,
            "total_trades": self.total_trades,
            "win_rate": f"{win_rate}%",
            "profit_usd": round(self.profit_usd_accumulated, 2),
            "logs": self.ai_logs[:15]
        }


# =====================================================================
# 5. MEMPOOL VALIDATION & BLOCK EXPLORER ENGINE
# =====================================================================
class MempoolValidationNode:
    def __init__(self):
        self.mempool: List[Dict[str, Any]] = []
        self.blocks: List[Dict[str, Any]] = []
        self.block_height = 845220
        self._seed_genesis_blocks()

    def _seed_genesis_blocks(self):
        """Seeds initial blockchain blocks and transactions for immediate explorer availability."""
        for i in range(3):
            self.block_height += 1
            b_hash = f"0000000000000000000{secrets.token_hex(12)}"
            dummy_tx = {
                "tx_hash": f"0x{secrets.token_hex(32)}",
                "seed_hash_code": f"0x{secrets.token_hex(20)}",
                "time_received": time.strftime("%H:%M:%S", time.localtime(time.time() - i * 600)),
                "network": "BTC_SEGWIT",
                "type": "COINBASE_REWARD",
                "amount": 3.125,
                "fee_rate": "18 sat/vB",
                "validation_status": "CONFIRMED (On-Chain)",
                "confirmations": i + 1,
                "inputs": ["0000000000000000000000000000000000000000000000000000000000000000"],
                "outputs": ["bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh"],
                "raw_payload": {"block_height": self.block_height, "subsidy": 3.125}
            }
            block = {
                "height": self.block_height,
                "hash": b_hash,
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time() - i * 600)),
                "tx_count": 1,
                "transactions": [dummy_tx]
            }
            self.blocks.append(block)

    def add_to_mempool(self, tx_data: Dict[str, Any]) -> Dict[str, Any]:
        tx_hash = hashlib.sha256(f"{time.time()}{secrets.token_hex(16)}{tx_data}".encode()).hexdigest()
        seed_hash = hashlib.sha256(f"SEED_HASH_{tx_hash[:16]}".encode()).hexdigest()

        entry = {
            "tx_hash": f"0x{tx_hash}",
            "seed_hash_code": f"0x{seed_hash[:24]}",
            "time_received": time.strftime("%H:%M:%S"),
            "network": tx_data.get("network", "BTC_SEGWIT"),
            "type": tx_data.get("type", "TRANSFER"),
            "amount": tx_data.get("amount", 0.0),
            "fee_rate": f"{secrets.randbelow(30) + 14} sat/vB",
            "validation_status": "VALIDATED (Zero-Conf Passed)",
            "confirmations": 0,
            "inputs": [tx_data.get("from", "Master Node")],
            "outputs": [tx_data.get("to", "External Protocol")],
            "raw_payload": tx_data
        }
        self.mempool.insert(0, entry)
        return entry

    def mine_mempool_block(self, custom_hash: Optional[str] = None) -> Optional[Dict[str, Any]]:
        self.block_height += 1
        tx_batch = self.mempool[:6]
        self.mempool = self.mempool[6:]

        for tx in tx_batch:
            tx["confirmations"] = 1
            tx["validation_status"] = "CONFIRMED (On-Chain)"

        block_hash = custom_hash or f"0000000000000000000{secrets.token_hex(12)}"
        block = {
            "height": self.block_height,
            "hash": block_hash,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "tx_count": len(tx_batch),
            "transactions": tx_batch
        }
        self.blocks.insert(0, block)
        return block

    def search_explorer(self, query: str) -> Dict[str, Any]:
        query = query.strip()
        for b in self.blocks:
            if str(b["height"]) == query or b["hash"] == query:
                return {"found": True, "type": "BLOCK", "data": b}

        all_txs = list(self.mempool)
        for b in self.blocks:
            all_txs.extend(b["transactions"])

        for tx in all_txs:
            if tx["tx_hash"] == query or tx["seed_hash_code"] == query:
                return {"found": True, "type": "TRANSACTION", "data": tx}

        matched = [tx for tx in all_txs if query in str(tx.get("inputs")) or query in str(tx.get("outputs"))]
        if matched or query.startswith(("1", "bc1", "0x", "T", "So1", "lnbc")):
            return {"found": True, "type": "ADDRESS", "data": {"address": query, "matched_transactions": matched}}

        return {"found": False, "query": query}


# =====================================================================
# 6. ENTERPRISE MULTI-NETWORK NODE (State & Security Manager)
# =====================================================================
class EnterpriseMultiNetworkNode:
    def __init__(self):
        # Security & Identity Credentials
        self.wallet_id = "WLT-" + secrets.token_hex(4).upper() + "-" + secrets.token_hex(4).upper()
        self.salt = secrets.token_hex(16)
        self.password_hash = self._hash_password("admin123", self.salt)
        
        # Hardware & Global Portability Attributes
        self.global_device_id = str(uuid.uuid5(uuid.NAMESPACE_DNS, "node.global.device.id"))
        self.imei_number = f"86{secrets.randbelow(8999999999999) + 1000000000000}"
        self.two_factor_enabled = False
        self.auto_lock_minutes = 15
        self.chipset = HardwareChipsetRegister()
        self.bound_devices = [
            {"device_id": self.global_device_id, "imei": self.imei_number, "status": "PRIMARY_NODE", "authorized_at": time.strftime("%Y-%m-%d %H:%M:%S")}
        ]

        # Cryptographic Master Root
        self.mnemonic = MultiNetworkHDCrypto.generate_mnemonic(12)
        self.seed = MultiNetworkHDCrypto.mnemonic_to_seed(self.mnemonic)
        self.networks = MultiNetworkHDCrypto.derive_all_networks(self.seed)
        
        self.mempool_engine = MempoolValidationNode()
        self.terminal = TradeTerminalEngine()
        self.miner = BitcoinPoWMiner(self)
        self.ai_robot = AITradingRobot(self)

        # Base Network Balances
        self.balances = {
            "BTC_NATIVE": 1.2500,
            "BTC_SEGWIT": 3.8400,
            "BTC_LIGHTNING": 1800000,
            "BTC_ETH": 0.9500,
            "BTC_BSC": 0.6000,
            "BTC_TRON": 0.4500,
            "BTC_SOL": 0.7500,
            "USDT": 28500.00
        }

        # CMC Top Assets
        self.cmc_balances: Dict[str, float] = {
            "BTC": 5.0900, "ETH": 18.500, "USDT": 28500.00, "BNB": 42.00, "SOL": 120.50,
            "USDC": 14000.00, "XRP": 15000.00, "DOGE": 45000.00, "TON": 850.00, "ADA": 12500.00,
            "AVAX": 180.00, "LINK": 450.00, "SUI": 3200.00, "NEAR": 950.00, "TAO": 14.20,
            "RENDER": 210.00, "WIF": 1250.00, "INJ": 45.00, "FET": 310.00, "SEI": 4500.00
        }

        for asset in TOP_100_COINMARKETCAP_DATA:
            sym = asset["symbol"]
            if sym not in self.cmc_balances:
                self.cmc_balances[sym] = 0.0

        self.staked_vaults = {
            "BTC_SEGWIT": {"amount": 1.0, "apy": 3.5, "rewards": 0.0042},
            "BTC_ETH": {"amount": 0.5, "apy": 5.2, "rewards": 0.0089}
        }
        self.escrows: List[Dict[str, Any]] = [
            {"contract_id": "ESC-MULTI-801", "network": "BTC_SEGWIT", "amount": "0.45 BTC", "counterparty": "bc1q9w8e...o1p", "status": "LOCKED IN ESCROW"}
        ]

        self._dispatch_tx("BTC_SEGWIT", "GENESIS_NODE_ALLOCATION", 3.8400, "Self HD Master Node", "Genesis Node Synced")

    @staticmethod
    def _hash_password(pwd: str, salt: str) -> str:
        return hashlib.pbkdf2_hmac('sha256', pwd.encode(), salt.encode(), 100000).hex()

    def verify_credentials(self, wallet_id: str, password: str) -> bool:
        if wallet_id.strip().upper() != self.wallet_id.upper():
            return False
        return self._hash_password(password, self.salt) == self.password_hash

    def update_password(self, old_pwd: str, new_pwd: str) -> Dict[str, Any]:
        if self._hash_password(old_pwd, self.salt) != self.password_hash:
            return {"success": False, "error": "Current password incorrect."}
        self.salt = secrets.token_hex(16)
        self.password_hash = self._hash_password(new_pwd, self.salt)
        self._dispatch_tx("BTC_NATIVE", "SECURITY_PASSWORD_RESET", 0.0, "Security Vault", "Authentication credentials rotated.")
        return {"success": True}

    def update_security_settings(self, two_fa: bool, auto_lock: int) -> Dict[str, Any]:
        self.two_factor_enabled = bool(two_fa)
        self.auto_lock_minutes = int(auto_lock)
        return {"success": True}

    def register_portable_device(self, new_imei: str, dev_label: str) -> Dict[str, Any]:
        clean_imei = "".join(filter(str.isdigit, new_imei))
        if len(clean_imei) != 15:
            return {"success": False, "error": "Invalid IMEI number format (15 numeric digits required)."}
        
        dev_id = str(uuid.uuid5(uuid.NAMESPACE_DNS, f"{clean_imei}-{time.time()}"))
        self.bound_devices.append({
            "device_id": dev_id,
            "imei": clean_imei,
            "status": f"PORTABLE_NODE ({dev_label})",
            "authorized_at": time.strftime("%Y-%m-%d %H:%M:%S")
        })
        self._dispatch_tx("BTC_NATIVE", "DEVICE_PORTABILITY_BIND", 0.0, "Hardware Security Node", f"Bound IMEI: {clean_imei[:6]}...{clean_imei[-4:]}")
        return {"success": True, "device_id": dev_id, "imei": clean_imei}

    def _dispatch_tx(self, net_key: str, action: str, amount: float, to_addr: str, note: str = "") -> Dict[str, Any]:
        tx_data = {
            "network": net_key,
            "type": action,
            "amount": amount,
            "from": self.networks.get(net_key, {}).get("address", "Master Node"),
            "to": to_addr,
            "note": note
        }
        return self.mempool_engine.add_to_mempool(tx_data)

    def credit_mining_reward(self, btc_subsidy: float, block_hash: str):
        self.balances["BTC_SEGWIT"] += btc_subsidy
        self.cmc_balances["BTC"] += btc_subsidy
        self.mempool_engine.mine_mempool_block(custom_hash=block_hash)
        self._dispatch_tx("BTC_SEGWIT", "POW_COINBASE_REWARD", btc_subsidy, self.networks["BTC_SEGWIT"]["address"], f"Block #{self.mempool_engine.block_height} Subsidy")

    def import_vault_key(self, import_data: str) -> Dict[str, Any]:
        import_str = import_data.strip()
        words = import_str.split()
        if len(words) in [12, 24]:
            self.mnemonic = import_str
            self.seed = MultiNetworkHDCrypto.mnemonic_to_seed(self.mnemonic)
            self.networks = MultiNetworkHDCrypto.derive_all_networks(self.seed)
            self._dispatch_tx("BTC_NATIVE", "IMPORT_MNEMONIC_VAULT", 0.0, "Root HD Vault Node", f"Imported {len(words)}-Word BIP39 Seed")
            return {"success": True, "type": "BIP39_MNEMONIC", "word_count": len(words)}
        else:
            clean_hex = import_str[2:] if import_str.startswith("0x") else import_str
            synth_seed = hashlib.sha512(clean_hex.encode()).digest()
            self.mnemonic = f"Imported Private Key Vault: {import_str[:10]}...{import_str[-6:]}"
            self.seed = synth_seed
            self.networks = MultiNetworkHDCrypto.derive_all_networks(self.seed)
            self._dispatch_tx("BTC_NATIVE", "IMPORT_PRIVATE_KEY_VAULT", 0.0, "Single-Key HD Node", "Imported Raw Private Key")
            return {"success": True, "type": "PRIVATE_KEY_HEX"}

    def buy_cmc_asset(self, symbol: str, usd_amount: float) -> Dict[str, Any]:
        asset = next((a for a in TOP_100_COINMARKETCAP_DATA if a["symbol"] == symbol), None)
        if not asset:
            return {"success": False, "error": f"Asset {symbol} not found"}
        if self.balances["USDT"] < usd_amount:
            return {"success": False, "error": "Insufficient USDT balance in vault"}
        
        qty = usd_amount / asset["price"]
        self.balances["USDT"] -= usd_amount
        self.cmc_balances[symbol] = self.cmc_balances.get(symbol, 0.0) + qty
        self.cmc_balances["USDT"] = self.balances["USDT"]
        
        tx = self._dispatch_tx("BTC_SEGWIT", f"BUY_CMC_ASSET_{symbol}", qty, "CoinMarketCap L3 Router", f"Purchased ${usd_amount:,.2f} USD")
        return {"success": True, "qty": qty, "price": asset["price"], "tx": tx}

    def send(self, net_key: str, to_address: str, amount: float) -> Dict[str, Any]:
        if self.balances.get(net_key, 0) < amount:
            return {"success": False, "error": "Insufficient balance"}
        self.balances[net_key] -= amount
        tx = self._dispatch_tx(net_key, "SEND", amount, to_address, "Direct Broadcast")
        return {"success": True, "tx": tx}

    def deposit(self, net_key: str, amount: float) -> Dict[str, Any]:
        self.balances[net_key] = self.balances.get(net_key, 0) + amount
        tx = self._dispatch_tx(net_key, "DEPOSIT", amount, self.networks[net_key]["address"], "Gateway Liquidity")
        return {"success": True, "tx": tx}

    def withdraw(self, net_key: str, to_address: str, amount: float) -> Dict[str, Any]:
        if self.balances.get(net_key, 0) < amount:
            return {"success": False, "error": "Insufficient balance"}
        self.balances[net_key] -= amount
        tx = self._dispatch_tx(net_key, "WITHDRAWAL", amount, to_address, "Cold Storage Outflow")
        return {"success": True, "tx": tx}

    def buy(self, net_key: str, usd_amount: float) -> Dict[str, Any]:
        p = self.terminal.prices["BTC/USDTERC20"]
        btc_qty = usd_amount / p
        self.balances[net_key] = self.balances.get(net_key, 0) + btc_qty
        tx = self._dispatch_tx(net_key, "BUY_FIAT", btc_qty, self.networks[net_key]["address"], f"Settled: ${usd_amount:,.2f}")
        return {"success": True, "tx": tx}

    def sell(self, net_key: str, amount: float) -> Dict[str, Any]:
        if self.balances.get(net_key, 0) < amount:
            return {"success": False, "error": "Insufficient balance"}
        p = self.terminal.prices["BTC/USDTERC20"]
        usd_val = amount * p
        self.balances[net_key] -= amount
        self.balances["USDT"] += usd_val
        self.cmc_balances["USDT"] = self.balances["USDT"]
        tx = self._dispatch_tx(net_key, "SELL_USDT", amount, "Tether Liquid Pool", f"Liquidated for ${usd_val:,.2f}")
        return {"success": True, "tx": tx}

    def swap(self, from_net: str, to_net: str, amount: float) -> Dict[str, Any]:
        if self.balances.get(from_net, 0) < amount:
            return {"success": False, "error": f"Insufficient {from_net} balance"}
        self.balances[from_net] -= amount
        self.balances[to_net] = self.balances.get(to_net, 0) + amount
        tx = self._dispatch_tx(from_net, f"CROSS_SWAP_{from_net}_TO_{to_net}", amount, self.networks[to_net]["address"], "DEX Bridge Router")
        return {"success": True, "tx": tx}

    def stake(self, net_key: str, amount: float) -> Dict[str, Any]:
        if self.balances.get(net_key, 0) < amount:
            return {"success": False, "error": "Insufficient balance to stake"}
        self.balances[net_key] -= amount
        if net_key not in self.staked_vaults:
            self.staked_vaults[net_key] = {"amount": 0.0, "apy": 4.5, "rewards": 0.0}
        self.staked_vaults[net_key]["amount"] += amount
        tx = self._dispatch_tx(net_key, "STAKE_LOCK", amount, "Proof-of-Stake Vault", "Staking APY Active")
        return {"success": True, "tx": tx}

    def escrow(self, net_key: str, counterparty: str, amount: float) -> Dict[str, Any]:
        if self.balances.get(net_key, 0) < amount:
            return {"success": False, "error": "Insufficient balance for Escrow lock"}
        self.balances[net_key] -= amount
        cid = f"ESC-{secrets.token_hex(4).upper()}"
        self.escrows.append({"contract_id": cid, "network": net_key, "amount": f"{amount} BTC", "counterparty": counterparty, "status": "LOCKED IN ESCROW"})
        tx = self._dispatch_tx(net_key, "ESCROW_LOCK", amount, counterparty, f"Contract {cid}")
        return {"success": True, "contract_id": cid, "tx": tx}

    def execute_terminal_order(self, pair: str, side: str, amount: float) -> Dict[str, Any]:
        if pair not in self.terminal.PAIRS:
            return {"success": False, "error": "Invalid Pair"}
        p = self.terminal.prices[pair]

        if side == "BUY":
            cost = amount * p if "USDT" in pair else amount
            if self.balances["USDT"] < cost:
                return {"success": False, "error": "Insufficient USDT capital"}
            self.balances["USDT"] -= cost
            self.balances["BTC_SEGWIT"] += amount
            self.cmc_balances["USDT"] = self.balances["USDT"]
            self.cmc_balances["BTC"] += amount
            tx = self._dispatch_tx("BTC_SEGWIT", f"TERMINAL_BUY_{pair}", amount, "Decentralized Order Engine", f"Filled at {p}")
            return {"success": True, "tx": tx}
        else:
            if self.balances["BTC_SEGWIT"] < amount:
                return {"success": False, "error": "Insufficient BTC balance"}
            revenue = amount * p
            self.balances["BTC_SEGWIT"] -= amount
            self.balances["USDT"] += revenue
            self.cmc_balances["USDT"] = self.balances["USDT"]
            self.cmc_balances["BTC"] -= amount
            tx = self._dispatch_tx("BTC_SEGWIT", f"TERMINAL_SELL_{pair}", amount, "Decentralized Order Engine", f"Liquidated at {p}")
            return {"success": True, "tx": tx}

    def export_keys_bundle(self) -> Dict[str, Any]:
        return {
            "wallet_id": self.wallet_id,
            "global_device_id": self.global_device_id,
            "imei_number": self.imei_number,
            "mnemonic_recovery_phrase": self.mnemonic,
            "master_seed_entropy": self.seed.hex(),
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "networks": self.networks,
            "balances": self.balances,
            "cmc_vault_balances": self.cmc_balances
        }

    def get_full_state(self) -> Dict[str, Any]:
        self.terminal.tick_market()
        self.terminal.evaluate_predictions(self)

        btc_price_usd = self.terminal.prices["BTC/USDTERC20"]
        total_btc = sum(v for k, v in self.balances.items() if k != "USDT" and k != "BTC_LIGHTNING")
        total_btc += self.balances["BTC_LIGHTNING"] / 100000000.0
        total_usd = (total_btc * btc_price_usd) + self.balances["USDT"]

        top_100_rendered = []
        for a in TOP_100_COINMARKETCAP_DATA:
            sym = a["symbol"]
            bal = self.cmc_balances.get(sym, 0.0)
            val_usd = bal * a["price"]
            top_100_rendered.append({
                "rank": a["rank"],
                "symbol": sym,
                "name": a["name"],
                "price": a["price"],
                "change_24h": a["change_24h"],
                "balance": bal,
                "balance_usd": round(val_usd, 2)
            })

        return {
            "wallet_id": self.wallet_id,
            "global_device_id": self.global_device_id,
            "imei_number": self.imei_number,
            "two_factor_enabled": self.two_factor_enabled,
            "auto_lock_minutes": self.auto_lock_minutes,
            "bound_devices": self.bound_devices,
            "chipset_telemetry": self.chipset.read_telemetry(),
            "total_portfolio_usd": round(total_usd, 2),
            "mnemonic": self.mnemonic,
            "networks": self.networks,
            "balances": self.balances,
            "cmc_top_100": top_100_rendered,
            "staked_vaults": self.staked_vaults,
            "escrows": self.escrows,
            "mempool": self.mempool_engine.mempool,
            "blocks": self.mempool_engine.blocks,
            "block_height": self.mempool_engine.block_height,
            "miner_stats": self.miner.get_stats(),
            "ai_stats": self.ai_robot.get_stats(),
            "terminal_prices": self.terminal.prices,
            "terminal_history": self.terminal.history,
            "order_books": self.terminal.order_book,
            "active_predictions": self.terminal.active_predictions,
            "resolved_predictions": self.terminal.resolved_predictions[:10]
        }


# =====================================================================
# 7. FLASK SAAS APPLICATION & ALL-IN-ONE WEB DASHBOARD
# =====================================================================
app = Flask(__name__)
app.secret_key = secrets.token_hex(32)
node = EnterpriseMultiNetworkNode()

HTML_DASHBOARD = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Enterprise HD Vault | Node, Chipset OS & Multi-Pair Terminal</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/qrcodejs/1.0.0/qrcode.min.js"></script>
    <style>
        * { margin:0; padding:0; box-sizing:border-box; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
        body { background:#060911; color:#f1f5f9; padding-bottom:60px; }

        .navbar { background:#0b1325; padding:14px 24px; display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid #1e293b; position:sticky; top:0; z-index:90; }
        .logo { font-size:1.1rem; font-weight:800; color:#38bdf8; letter-spacing:0.5px; }
        .status-tags { display:flex; gap:8px; align-items:center; flex-wrap:wrap; }
        .badge { font-size:0.75rem; padding:4px 10px; border-radius:999px; font-weight:600; }
        .badge-green { background:#064e3b; color:#34d399; border:1px solid #059669; }
        .badge-purple { background:#4c1d95; color:#c084fc; border:1px solid #7c3aed; }
        .badge-orange { background:#7c2d12; color:#fb923c; border:1px solid #ea580c; }
        .badge-cyan { background:#164e63; color:#22d3ee; border:1px solid #0891b2; }

        .container { max-width:1420px; margin:24px auto; padding:0 16px; }
        .grid-2 { display:grid; grid-template-columns: 1.9fr 1.1fr; gap:20px; }
        .grid-3 { display:grid; grid-template-columns: 1.1fr 1fr 1fr; gap:20px; margin-bottom:20px; }
        @media(max-width:1080px){ .grid-2, .grid-3 { grid-template-columns: 1fr; } }

        .card { background:#0b1325; border:1px solid #1e293b; border-radius:12px; padding:20px; margin-bottom:20px; }
        .muted { color:#94a3b8; font-size:0.8rem; font-weight:600; text-transform:uppercase; letter-spacing:0.5px; }

        .balance-hero { font-size:2.3rem; font-weight:800; margin:6px 0 16px; color:#fff; }
        
        .action-grid { display:grid; grid-template-columns: repeat(auto-fit, minmax(95px, 1fr)); gap:8px; }
        .btn { padding:10px 12px; border-radius:8px; font-size:0.8rem; font-weight:700; cursor:pointer; border:none; transition:0.15s ease; text-align:center; }
        .btn-blue { background:#0284c7; color:#fff; }
        .btn-blue:hover { background:#0369a1; }
        .btn-gray { background:#1e293b; color:#f1f5f9; border:1px solid #334155; }
        .btn-gray:hover { background:#334155; }
        .btn-purple { background:#7c3aed; color:#fff; }
        .btn-purple:hover { background:#6d28d9; }
        .btn-orange { background:#ea580c; color:#fff; }
        .btn-green { background:#059669; color:#fff; }
        .btn-green:hover { background:#047857; }
        .btn-red { background:#dc2626; color:#fff; }
        .btn-red:hover { background:#b91c1c; }

        .auth-overlay { position:fixed; inset:0; background:#060911; z-index:200; display:flex; justify-content:center; align-items:center; }
        .auth-card { background:#0b1325; border:1px solid #334155; border-radius:12px; padding:32px; max-width:440px; width:90%; box-shadow:0 20px 25px -5px rgba(0,0,0,0.5); }

        .cmc-table-container { max-height:480px; overflow-y:auto; border:1px solid #1e293b; border-radius:8px; }
        .search-cmc-box { width:100%; padding:8px 12px; background:#060911; border:1px solid #334155; border-radius:6px; color:#fff; font-size:0.85rem; margin-bottom:12px; }

        .pair-selector { display:flex; gap:6px; overflow-x:auto; padding-bottom:8px; margin-bottom:12px; }
        .pair-btn { padding:6px 12px; border-radius:6px; background:#1e293b; color:#94a3b8; border:1px solid #334155; font-size:0.75rem; font-weight:700; cursor:pointer; white-space:nowrap; }
        .pair-btn.active { background:#0284c7; color:#fff; border-color:#38bdf8; }

        .orderbook-row { display:flex; justify-content:space-between; font-family:monospace; font-size:0.8rem; padding:3px 0; }
        .orderbook-ask { color:#f87171; }
        .orderbook-bid { color:#34d399; }

        .predict-box { background:#060911; border:1px solid #1e293b; border-radius:8px; padding:15px; margin-top:12px; }
        .predict-btn-group { display:grid; grid-template-columns: 1fr 1fr; gap:10px; margin-top:10px; }

        table { width:100%; border-collapse:collapse; text-align:left; font-size:0.88rem; }
        th { padding:12px 14px; background:#1e293b; color:#94a3b8; font-size:0.75rem; text-transform:uppercase; position:sticky; top:0; z-index:10; }
        td { padding:12px 14px; border-bottom:1px solid #1e293b; }

        .hash-tag { font-family:monospace; color:#38bdf8; background:#060911; padding:3px 6px; border-radius:4px; font-size:0.78rem; border:1px solid #1e293b; }
        .seed-hash-tag { font-family:monospace; color:#c084fc; background:#060911; padding:3px 6px; border-radius:4px; font-size:0.78rem; border:1px solid #1e293b; }
        .addr-tag { font-family:monospace; color:#34d399; background:#060911; padding:3px 6px; border-radius:4px; font-size:0.78rem; border:1px solid #1e293b; }

        .terminal-box { font-family:monospace; background:#060911; border:1px solid #1e293b; border-radius:8px; padding:12px; height:130px; overflow-y:auto; font-size:0.78rem; line-height:1.4; }

        .modal-overlay { display:none; position:fixed; inset:0; background:rgba(0,0,0,0.85); z-index:100; justify-content:center; align-items:center; }
        .modal { background:#0b1325; border:1px solid #334155; border-radius:12px; padding:24px; max-width:680px; width:92%; max-height:90vh; overflow-y:auto; }
        .modal-title { font-size:1.15rem; font-weight:700; margin-bottom:14px; display:flex; justify-content:space-between; }
        .close-btn { cursor:pointer; color:#94a3b8; font-weight:bold; }
        .form-group { margin-bottom:14px; }
        .form-group label { display:block; font-size:0.78rem; color:#94a3b8; margin-bottom:6px; font-weight:600; text-transform:uppercase; }
        .form-input { width:100%; padding:10px 12px; background:#060911; border:1px solid #334155; border-radius:6px; color:#fff; font-size:0.9rem; }
        
        #priceCanvas { width:100%; height:200px; background:#060911; border-radius:8px; border:1px solid #1e293b; }
        #qrContainer { display:flex; justify-content:center; padding:15px; background:#fff; border-radius:8px; width:fit-content; margin:10px auto; }
    </style>
</head>
<body>

    <!-- AUTHENTICATION LOGIN OVERLAY -->
    <div class="auth-overlay" id="authGateModal" style="display:none;">
        <div class="auth-card">
            <div style="font-size:1.3rem; font-weight:800; color:#38bdf8; margin-bottom:6px;">◆ CHIPSET OS AUTHENTICATION</div>
            <p style="font-size:0.8rem; color:#94a3b8; margin-bottom:20px;">Enter your Wallet ID and Master Password to unlock hardware security enclave.</p>
            
            <div class="form-group">
                <label>Wallet ID</label>
                <input id="loginWalletId" class="form-input" placeholder="e.g. WLT-XXXX-XXXX" />
            </div>
            <div class="form-group">
                <label>Master Password</label>
                <input id="loginPassword" type="password" class="form-input" placeholder="••••••••" />
            </div>

            <div style="margin-top:20px; display:flex; flex-direction:column; gap:8px;">
                <button class="btn btn-blue" onclick="submitLogin()">Unlock Hardware Node OS</button>
                <div style="font-size:0.75rem; color:#64748b; text-align:center;">Default Dev Creds: <code style="color:#38bdf8;" id="devCredsPrompt">WLT-ID / admin123</code></div>
            </div>
        </div>
    </div>

    <!-- MAIN APP NAVBAR -->
    <nav class="navbar">
        <div class="logo">◆ INTEGRATED CIRCUIT BOARD OS | MULTI-PAIR TERMINAL & EXPLORER</div>
        <div class="status-tags">
            <span class="badge badge-purple" id="blockHeightBadge">Height: #845,220</span>
            <span class="badge badge-orange" id="minerBadge">Miner: Idle</span>
            <span class="badge badge-cyan" id="aiBadge">AI Robot: Offline</span>
            <button class="btn btn-blue" style="padding:4px 10px; font-size:0.75rem;" onclick="openExplorerModal()">🔍 Explorer Scanner</button>
            <button class="btn btn-gray" style="padding:4px 10px; font-size:0.75rem;" onclick="openActionModal('security')">🔒 Chipset & IMEI</button>
            <button class="btn btn-red" style="padding:4px 10px; font-size:0.75rem;" onclick="submitLogout()">Logout</button>
        </div>
    </nav>

    <div class="container">
        <!-- TOP SECTION: Portfolio Summary & Action Toolbar -->
        <div class="grid-2">
            <div class="card">
                <div style="display:flex; justify-content:space-between; align-items:flex-start;">
                    <div>
                        <div class="muted">Total Consolidated Portfolio Value</div>
                        <div class="balance-hero" id="portfolioUSD">$0.00 USD</div>
                    </div>
                    <div style="text-align:right;">
                        <span class="muted">Wallet ID:</span>
                        <div style="font-family:monospace; color:#38bdf8; font-size:0.8rem;" id="navWalletIdText">Loading...</div>
                    </div>
                </div>

                <div class="action-grid">
                    <button class="btn btn-blue" onclick="openActionModal('send')">Send</button>
                    <button class="btn btn-blue" onclick="openActionModal('receive')">Receive / QR</button>
                    <button class="btn btn-gray" onclick="openActionModal('deposit')">Deposit</button>
                    <button class="btn btn-gray" onclick="openActionModal('withdraw')">Withdraw</button>
                    <button class="btn btn-gray" onclick="openActionModal('buy')">Buy</button>
                    <button class="btn btn-gray" onclick="openActionModal('sell')">Sell</button>
                    <button class="btn btn-gray" onclick="openActionModal('swap')">Cross-Swap</button>
                    <button class="btn btn-purple" onclick="openActionModal('stake')">Staking Vault</button>
                    <button class="btn btn-purple" onclick="openActionModal('escrow')">Multi-Sig Escrow</button>
                    <button class="btn btn-orange" onclick="openActionModal('keys')">Backup HD Keys</button>
                    <button class="btn btn-gray" onclick="openActionModal('import')">Import Vault</button>
                    <button class="btn btn-orange" onclick="triggerExportWallet()">Export Wallet</button>
                </div>
            </div>

            <!-- MULTI-PAIR INTERACTIVE CHART -->
            <div class="card">
                <div class="pair-selector" id="pairSelectorBar"></div>
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                    <div class="muted" id="activePairLabel">BTC/USDTERC20</div>
                    <div id="activePairPrice" style="font-weight:800; color:#38bdf8; font-size:1.1rem;">$0.00</div>
                </div>
                <canvas id="priceCanvas" width="560" height="200"></canvas>
            </div>
        </div>

        <!-- HARDWARE CHIPSET TELEMETRY MONITOR -->
        <div class="card">
            <div class="muted" style="margin-bottom:10px;">🔌 Integrated Circuit Board Hardware Telemetry & Silicon Registers</div>
            <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap:12px; font-size:0.85rem;" id="chipsetTelemetryBox">
                <div><span class="muted">ASIC Core Temp:</span> <strong id="chipTemp" style="color:#34d399;">42.5 °C</strong></div>
                <div><span class="muted">Board Rail Voltage:</span> <strong id="chipVolt" style="color:#38bdf8;">12.04 V</strong></div>
                <div><span class="muted">Clock Frequency:</span> <strong id="chipClock" style="color:#c084fc;">1450 MHz</strong></div>
                <div><span class="muted">Enclave Security:</span> <strong id="chipEnclave" style="color:#34d399;">SECURE LOCKED</strong></div>
                <div><span class="muted">EEPROM Flash Cycles:</span> <strong id="chipFlash" style="color:#fb923c;">1,420</strong></div>
            </div>
        </div>

        <!-- TOP 100 COINMARKETCAP ASSETS VAULT -->
        <div class="card">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
                <div>
                    <div style="font-size:1.15rem; font-weight:800; color:#38bdf8;">🏛 Multi-Asset Vault (Top 100 CoinMarketCap Assets)</div>
                    <div class="muted" style="margin-top:2px;">Live Prices, Wallet Quantities, USD Net Worth & Direct Instant Purchase</div>
                </div>
                <div style="display:flex; gap:8px;">
                    <button class="btn btn-blue" onclick="openActionModal('import')">🔑 Import 12/24 Mnemonics / Key</button>
                </div>
            </div>

            <input class="search-cmc-box" id="searchCmcInput" placeholder="🔍 Search Top 100 Coins by Name or Symbol (e.g. Bitcoin, SUI, TAO, RENDER, DOGE)..." onkeyup="filterCmcAssets()" />

            <div class="cmc-table-container">
                <table>
                    <thead>
                        <tr>
                            <th># Rank</th>
                            <th>Asset Name</th>
                            <th>Symbol</th>
                            <th>Price (USD)</th>
                            <th>24h Change</th>
                            <th>Asset Balance</th>
                            <th>Balance in USD ($)</th>
                            <th>Action</th>
                        </tr>
                    </thead>
                    <tbody id="cmcTableBody"></tbody>
                </table>
            </div>
        </div>

        <!-- 3-COLUMN MODULE: Spot Order Form, L2 Depth & Binary Options -->
        <div class="grid-3">
            <div class="card">
                <div class="muted" style="margin-bottom:12px;">⚡ Terminal Spot Order Execution</div>
                <div class="form-group">
                    <label>Order Amount (BTC)</label>
                    <input id="termOrderAmount" class="form-input" type="number" step="any" value="0.05" />
                </div>
                <div style="display:grid; grid-template-columns: 1fr 1fr; gap:8px;">
                    <button class="btn btn-green" onclick="submitTerminalOrder('BUY')">Market Buy (Bid)</button>
                    <button class="btn btn-red" onclick="submitTerminalOrder('SELL')">Market Sell (Ask)</button>
                </div>
            </div>

            <div class="card">
                <div class="muted" style="margin-bottom:10px;">📊 Live Order Book (L2 Spread)</div>
                <div style="font-size:0.72rem; color:#94a3b8; display:flex; justify-content:space-between; margin-bottom:4px;">
                    <span>Price</span><span>Size</span>
                </div>
                <div id="orderbookAsks"></div>
                <div style="border-top:1px dashed #334155; margin:6px 0;"></div>
                <div id="orderbookBids"></div>
            </div>

            <div class="card">
                <div class="muted" style="margin-bottom:10px;">🎯 Invest & Predict (Binary Option Oracle)</div>
                <div class="predict-box">
                    <div style="display:flex; justify-content:space-between; font-size:0.8rem; margin-bottom:6px;">
                        <span>Payout Return: <strong style="color:#34d399;">+85% ROI</strong></span>
                        <span>Window: <strong>30 Sec</strong></span>
                    </div>
                    <input id="predictStakeAmount" class="form-input" type="number" value="100" placeholder="Stake Amount (USDT)" />
                    <div class="predict-btn-group">
                        <button class="btn btn-green" onclick="submitPrediction('CALL_IN')">📈 Call In (Long)</button>
                        <button class="btn btn-red" onclick="submitPrediction('CALL_OUT')">📉 Call Out (Short)</button>
                    </div>
                </div>
                <div style="margin-top:10px; font-size:0.75rem; color:#94a3b8;" id="activePredictionsContainer"></div>
            </div>
        </div>

        <!-- MINER & AI TRADING ROBOT DUAL PANELS -->
        <div class="grid-2">
            <div class="card">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
                    <div class="muted">⛏ Proof-of-Work Bitcoin ASIC / CPU Miner</div>
                    <button id="minerToggleBtn" class="btn btn-green" style="padding:4px 12px; font-size:0.75rem;" onclick="toggleMiner()">Start Mining</button>
                </div>
                <div style="display:grid; grid-template-columns: 1fr 1fr 1fr; gap:10px; margin-bottom:12px; font-size:0.85rem;">
                    <div><span class="muted">Hashrate:</span> <strong id="minerHashrate" style="color:#38bdf8;">0.00 MH/s</strong></div>
                    <div><span class="muted">Blocks Solved:</span> <strong id="minerBlocks" style="color:#34d399;">0</strong></div>
                    <div><span class="muted">Shares Accepted:</span> <strong id="minerShares" style="color:#c084fc;">0</strong></div>
                </div>
                <div class="terminal-box" id="minerLogBox" style="color:#fb923c;"></div>
            </div>

            <div class="card">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
                    <div class="muted">🤖 AI Algorithmic Trade Robot (Arbitrage Engine)</div>
                    <button id="aiToggleBtn" class="btn btn-green" style="padding:4px 12px; font-size:0.75rem;" onclick="toggleAI()">Start AI Autopilot</button>
                </div>
                <div style="display:grid; grid-template-columns: 1fr 1fr 1fr; gap:10px; margin-bottom:12px; font-size:0.85rem;">
                    <div><span class="muted">Strategy:</span> <strong id="aiStrategy" style="color:#38bdf8;">Arb</strong></div>
                    <div><span class="muted">Win Rate:</span> <strong id="aiWinRate" style="color:#34d399;">100%</strong></div>
                    <div><span class="muted">P&L Yield:</span> <strong id="aiProfit" style="color:#c084fc;">+$0.00</strong></div>
                </div>
                <div class="terminal-box" id="aiLogBox" style="color:#38bdf8;"></div>
            </div>
        </div>

        <!-- 7 BITCOIN NETWORKS -->
        <div class="card">
            <div class="muted" style="margin-bottom:12px;">7 Supported Bitcoin Networks & Derived HD Addresses</div>
            <div style="overflow-x:auto;">
                <table>
                    <thead>
                        <tr>
                            <th>Network & Architecture</th>
                            <th>Layer / Standard</th>
                            <th>Balance</th>
                            <th>Derivation Path</th>
                            <th>Public Address</th>
                        </tr>
                    </thead>
                    <tbody id="networksTableBody"></tbody>
                </table>
            </div>
        </div>

        <!-- MEMPOOL LIVE VALIDATION POOL & BLOCK EXPLORER -->
        <div class="card">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
                <div class="muted">⚡ Mempool Live Transaction Pool & Blockchain Explorer Scanner</div>
                <div style="display:flex; gap:8px;">
                    <button class="btn btn-blue" style="padding:4px 10px; font-size:0.75rem;" onclick="openExplorerModal()">🔍 Explorer Lookup</button>
                    <button class="btn btn-orange" style="padding:4px 10px; font-size:0.75rem;" onclick="triggerMineBlock()">⛏ Mine Pending Block</button>
                </div>
            </div>
            <div style="overflow-x:auto;">
                <table>
                    <thead>
                        <tr>
                            <th>Time</th>
                            <th>Tx Hash ID</th>
                            <th>Seed Hash Code</th>
                            <th>Network</th>
                            <th>Fee Rate</th>
                            <th>Zero-Conf Validation</th>
                        </tr>
                    </thead>
                    <tbody id="mempoolTableBody"></tbody>
                </table>
            </div>
        </div>
    </div>

    <!-- DYNAMIC ACTION MODAL -->
    <div class="modal-overlay" id="actionModal">
        <div class="modal">
            <div class="modal-title">
                <span id="modalHeader">Action</span>
                <span class="close-btn" onclick="closeModal()">&times;</span>
            </div>
            <div id="modalDynamicBody"></div>
        </div>
    </div>

    <script>
        let walletState = {};
        let selectedPair = "BTC/USDTERC20";

        const PAIR_LIST = [
            "BTC/USDTERC20",
            "BTC/USDTBEP20",
            "BTC/USDTTRC20",
            "BTC/BNB",
            "BTC/Tron",
            "BTC/ETH",
            "BTC/Solana"
        ];

        function initPairBar() {
            const bar = document.getElementById('pairSelectorBar');
            bar.innerHTML = '';
            PAIR_LIST.forEach(pair => {
                const btn = document.createElement('button');
                btn.className = `pair-btn ${pair === selectedPair ? 'active' : ''}`;
                btn.innerText = pair;
                btn.onclick = () => {
                    selectedPair = pair;
                    initPairBar();
                    renderDashboard();
                };
                bar.appendChild(btn);
            });
        }

        async function checkAuthSession() {
            const res = await fetch('/api/auth/session');
            const auth = await res.json();
            if (!auth.authenticated) {
                document.getElementById('authGateModal').style.display = 'flex';
                document.getElementById('devCredsPrompt').innerText = `${auth.wallet_id_hint} / admin123`;
                return false;
            } else {
                document.getElementById('authGateModal').style.display = 'none';
                return true;
            }
        }

        async function submitLogin() {
            const wid = document.getElementById('loginWalletId').value.trim();
            const pwd = document.getElementById('loginPassword').value;
            const res = await fetch('/api/auth/login', {
                method: 'POST',
                body: JSON.stringify({ wallet_id: wid, password: pwd })
            });
            const data = await res.json();
            if (data.success) {
                document.getElementById('authGateModal').style.display = 'none';
                fetchState();
            } else {
                alert(data.error || "Authentication failed.");
            }
        }

        async function submitLogout() {
            await fetch('/api/auth/logout', { method: 'POST' });
            window.location.reload();
        }

        async function fetchState() {
            const isAuth = await checkAuthSession();
            if (!isAuth) return;

            const res = await fetch('/api/state');
            if (res.status === 401) {
                checkAuthSession();
                return;
            }
            walletState = await res.json();
            renderDashboard();
        }

        function renderDashboard() {
            document.getElementById('portfolioUSD').innerText = `$${walletState.total_portfolio_usd.toLocaleString('en-US', {minimumFractionDigits: 2})} USD`;
            document.getElementById('blockHeightBadge').innerText = `Height: #${walletState.block_height.toLocaleString()}`;
            document.getElementById('navWalletIdText').innerText = walletState.wallet_id;

            // Render Hardware Chipset Telemetry
            if (walletState.chipset_telemetry) {
                const c = walletState.chipset_telemetry;
                document.getElementById('chipTemp').innerText = `${c.core_temp_c} °C`;
                document.getElementById('chipVolt').innerText = `${c.voltage_v} V`;
                document.getElementById('chipClock').innerText = `${c.clock_mhz} MHz`;
                document.getElementById('chipEnclave').innerText = c.enclave_status;
                document.getElementById('chipFlash').innerText = c.flash_cycles.toLocaleString();
            }

            document.getElementById('activePairLabel').innerText = selectedPair;
            const currentPairPrice = walletState.terminal_prices[selectedPair];
            document.getElementById('activePairPrice').innerText = `${currentPairPrice.toLocaleString()} ${selectedPair.split('/')[1]}`;
            
            const pairHistory = walletState.terminal_history[selectedPair] || [];
            drawTrendGraph(pairHistory);

            renderCmcTable(walletState.cmc_top_100);

            const ob = walletState.order_books[selectedPair];
            if (ob) {
                const asksBox = document.getElementById('orderbookAsks');
                asksBox.innerHTML = ob.asks.slice().reverse().map(a => `<div class="orderbook-row orderbook-ask"><span>${a.price}</span><span>${a.amount}</span></div>`).join('');
                const bidsBox = document.getElementById('orderbookBids');
                bidsBox.innerHTML = ob.bids.map(b => `<div class="orderbook-row orderbook-bid"><span>${b.price}</span><span>${b.amount}</span></div>`).join('');
            }

            const predBox = document.getElementById('activePredictionsContainer');
            predBox.innerHTML = '<strong>Active Option Contracts:</strong><br>';
            if (walletState.active_predictions.length === 0) {
                predBox.innerHTML += 'No active options currently pending.';
            } else {
                walletState.active_predictions.forEach(p => {
                    predBox.innerHTML += `<div>• [${p.prediction_id}] ${p.direction} on ${p.pair} @ Strike $${p.strike_price} ($${p.stake_amount} Stake)</div>`;
                });
            }

            const minerStats = walletState.miner_stats;
            const minerBadge = document.getElementById('minerBadge');
            const minerBtn = document.getElementById('minerToggleBtn');
            if (minerStats.is_mining) {
                minerBadge.innerText = `Miner: Active (${minerStats.hashrate_mhs} MH/s)`;
                minerBadge.className = 'badge badge-green';
                minerBtn.innerText = 'Stop Mining';
                minerBtn.className = 'btn btn-red';
            } else {
                minerBadge.innerText = 'Miner: Idle';
                minerBadge.className = 'badge badge-orange';
                minerBtn.innerText = 'Start Mining';
                minerBtn.className = 'btn btn-green';
            }
            document.getElementById('minerHashrate').innerText = `${minerStats.hashrate_mhs} MH/s`;
            document.getElementById('minerBlocks').innerText = minerStats.blocks_mined;
            document.getElementById('minerShares').innerText = minerStats.shares_accepted;
            document.getElementById('minerLogBox').innerHTML = minerStats.logs.join('<br>') || 'Miner standby...';

            const aiStats = walletState.ai_stats;
            const aiBadge = document.getElementById('aiBadge');
            const aiBtn = document.getElementById('aiToggleBtn');
            if (aiStats.is_active) {
                aiBadge.innerText = `AI Robot: Online (${aiStats.win_rate})`;
                aiBadge.className = 'badge badge-cyan';
                aiBtn.innerText = 'Stop AI Autopilot';
                aiBtn.className = 'btn btn-red';
            } else {
                aiBadge.innerText = 'AI Robot: Offline';
                aiBadge.className = 'badge badge-gray';
                aiBtn.innerText = 'Start AI Autopilot';
                aiBtn.className = 'btn btn-green';
            }
            document.getElementById('aiStrategy').innerText = aiStats.strategy.replace('_', ' ');
            document.getElementById('aiWinRate').innerText = aiStats.win_rate;
            document.getElementById('aiProfit').innerText = `+$${aiStats.profit_usd.toLocaleString('en-US', {minimumFractionDigits:2})}`;
            document.getElementById('aiLogBox').innerHTML = aiStats.logs.join('<br>') || 'AI neural listener standby...';

            const netTbody = document.getElementById('networksTableBody');
            netTbody.innerHTML = '';
            for (const [netKey, net] of Object.entries(walletState.networks)) {
                const bal = walletState.balances[netKey] || 0.0;
                const unit = netKey === 'BTC_LIGHTNING' ? 'sats' : 'BTC';
                netTbody.innerHTML += `
                    <tr>
                        <td><strong>${net.network_name}</strong></td>
                        <td><span style="color:#c084fc;">${net.layer}</span></td>
                        <td><strong>${bal.toLocaleString()} ${unit}</strong></td>
                        <td><span style="color:#94a3b8; font-family:monospace;">${net.derivation_path}</span></td>
                        <td><span class="addr-tag">${net.address.substring(0, 10)}...${net.address.substring(net.address.length - 6)}</span></td>
                    </tr>
                `;
            }

            const memTbody = document.getElementById('mempoolTableBody');
            memTbody.innerHTML = '';
            for (const tx of walletState.mempool) {
                memTbody.innerHTML += `
                    <tr>
                        <td>${tx.time_received}</td>
                        <td><span class="hash-tag" style="cursor:pointer;" onclick="runExplorerSearch('${tx.tx_hash}')">${tx.tx_hash.substring(0, 14)}...</span></td>
                        <td><span class="seed-hash-tag" style="cursor:pointer;" onclick="runExplorerSearch('${tx.seed_hash_code}')">${tx.seed_hash_code.substring(0, 16)}...</span></td>
                        <td>${tx.network}</td>
                        <td>${tx.fee_rate}</td>
                        <td><span style="color:#34d399;">● ${tx.validation_status}</span></td>
                    </tr>
                `;
            }
        }

        function renderCmcTable(assetList) {
            const tbody = document.getElementById('cmcTableBody');
            tbody.innerHTML = '';
            assetList.forEach(a => {
                const changeColor = a.change_24h.includes('+') ? '#34d399' : (a.change_24h.includes('-') ? '#f87171' : '#94a3b8');
                tbody.innerHTML += `
                    <tr>
                        <td><strong>#${a.rank}</strong></td>
                        <td><strong>${a.name}</strong></td>
                        <td><span class="badge badge-purple">${a.symbol}</span></td>
                        <td>$${a.price.toLocaleString('en-US', {minimumFractionDigits: a.price < 1 ? 4 : 2})}</td>
                        <td style="color:${changeColor}; font-weight:700;">${a.change_24h}</td>
                        <td><strong>${a.balance.toLocaleString('en-US', {maximumFractionDigits: 4})} ${a.symbol}</strong></td>
                        <td style="color:#38bdf8; font-weight:700;">$${a.balance_usd.toLocaleString('en-US', {minimumFractionDigits: 2})}</td>
                        <td>
                            <button class="btn btn-green" style="padding:4px 10px; font-size:0.72rem;" onclick="openBuyCmcModal('${a.symbol}', ${a.price})">Buy ${a.symbol}</button>
                        </td>
                    </tr>
                `;
            });
        }

        function filterCmcAssets() {
            const query = document.getElementById('searchCmcInput').value.toLowerCase();
            const filtered = (walletState.cmc_top_100 || []).filter(a => 
                a.name.toLowerCase().includes(query) || a.symbol.toLowerCase().includes(query)
            );
            renderCmcTable(filtered);
        }

        function openBuyCmcModal(symbol, price) {
            const modal = document.getElementById('actionModal');
            const header = document.getElementById('modalHeader');
            const body = document.getElementById('modalDynamicBody');
            modal.style.display = 'flex';

            header.innerText = `Buy ${symbol} (Top 100 CoinMarketCap)`;
            body.innerHTML = `
                <div class="form-group"><label>Target Asset</label><input class="form-input" value="${symbol} ($${price.toLocaleString()})" readonly /></div>
                <div class="form-group"><label>USD Purchase Volume</label><input id="buyCmcUsdAmount" class="form-input" type="number" value="250" /></div>
                <button class="btn btn-green" style="width:100%;" onclick="submitBuyCmc('${symbol}')">Authorize & Credit Vault</button>
            `;
        }

        async function submitBuyCmc(symbol) {
            const usd = parseFloat(document.getElementById('buyCmcUsdAmount').value);
            await fetch('/api/cmc/buy', {
                method: 'POST',
                body: JSON.stringify({ symbol: symbol, usd_amount: usd })
            });
            closeModal();
            fetchState();
        }

        function drawTrendGraph(prices) {
            const canvas = document.getElementById('priceCanvas');
            const ctx = canvas.getContext('2d');
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            if (prices.length < 2) return;
            const min = Math.min(...prices);
            const max = Math.max(...prices);
            const range = max - min || 1;

            ctx.strokeStyle = '#38bdf8';
            ctx.lineWidth = 2;
            ctx.beginPath();
            const step = canvas.width / (prices.length - 1);
            prices.forEach((p, idx) => {
                const x = idx * step;
                const y = canvas.height - 20 - ((p - min) / range) * (canvas.height - 40);
                if (idx === 0) ctx.moveTo(x, y);
                else ctx.lineTo(x, y);
            });
            ctx.stroke();
        }

        async function submitTerminalOrder(side) {
            const amount = parseFloat(document.getElementById('termOrderAmount').value);
            await fetch('/api/terminal/order', {
                method: 'POST',
                body: JSON.stringify({ pair: selectedPair, side: side, amount: amount })
            });
            fetchState();
        }

        async function submitPrediction(direction) {
            const stake = parseFloat(document.getElementById('predictStakeAmount').value);
            await fetch('/api/terminal/predict', {
                method: 'POST',
                body: JSON.stringify({ pair: selectedPair, direction: direction, stake_amount: stake, duration: 30 })
            });
            fetchState();
        }

        async function toggleMiner() {
            const action = walletState.miner_stats.is_mining ? 'stop' : 'start';
            await fetch(`/api/miner/${action}`, { method: 'POST' });
            fetchState();
        }

        async function toggleAI() {
            const action = walletState.ai_stats.is_active ? 'stop' : 'start';
            await fetch(`/api/ai/${action}`, { method: 'POST' });
            fetchState();
        }

        async function triggerMineBlock() {
            await fetch('/api/action/mine', { method: 'POST' });
            fetchState();
        }

        function triggerExportWallet() {
            window.location.href = '/api/action/export';
        }

        function openExplorerModal() {
            const modal = document.getElementById('actionModal');
            const header = document.getElementById('modalHeader');
            const body = document.getElementById('modalDynamicBody');
            modal.style.display = 'flex';

            header.innerText = "🔍 Blockchain Wallet Explorer & Transaction Scanner";
            body.innerHTML = `
                <div class="form-group">
                    <label>Search Transaction Hash ID, Seed Hash Code, Block ID #, or Address</label>
                    <div style="display:flex; gap:8px;">
                        <input id="explorerQueryInput" class="form-input" placeholder="e.g. 0x..., Block Height #845221, or bc1q..." />
                        <button class="btn btn-blue" onclick="executeExplorerSearch()">Scan</button>
                    </div>
                </div>
                <div id="explorerResultContainer" style="margin-top:15px; font-size:0.85rem;"></div>
            `;
        }

        async function runExplorerSearch(queryStr) {
            openExplorerModal();
            document.getElementById('explorerQueryInput').value = queryStr;
            await executeExplorerSearch();
        }

        async function executeExplorerSearch() {
            const q = document.getElementById('explorerQueryInput').value.trim();
            if (!q) return;
            const res = await fetch(`/api/explorer/search?q=${encodeURIComponent(q)}`);
            const data = await res.json();
            const container = document.getElementById('explorerResultContainer');

            if (!data.found) {
                container.innerHTML = `<div style="color:#f87171; padding:10px; background:#060911; border:1px solid #1e293b; border-radius:6px;">❌ Query "${q}" not found in blockchain ledger or mempool.</div>`;
                return;
            }

            if (data.type === 'BLOCK') {
                const b = data.data;
                container.innerHTML = `
                    <div style="background:#060911; border:1px solid #334155; padding:12px; border-radius:6px;">
                        <div style="color:#38bdf8; font-weight:700; margin-bottom:6px;">📦 BLOCK #${b.height}</div>
                        <div>Hash ID: <span class="hash-tag">${b.hash}</span></div>
                        <div>Timestamp: ${b.timestamp}</div>
                        <div>Transactions Count: ${b.tx_count}</div>
                    </div>
                `;
            } else if (data.type === 'TRANSACTION') {
                const tx = data.data;
                container.innerHTML = `
                    <div style="background:#060911; border:1px solid #334155; padding:12px; border-radius:6px;">
                        <div style="color:#34d399; font-weight:700; margin-bottom:6px;">📄 TRANSACTION RECORD FOUND</div>
                        <div>Tx Hash ID: <span class="hash-tag">${tx.tx_hash}</span></div>
                        <div>Seed Hash Code: <span class="seed-hash-tag">${tx.seed_hash_code}</span></div>
                        <div>Network: ${tx.network} | Type: ${tx.type}</div>
                        <div>Amount: ${tx.amount} | Fee Rate: ${tx.fee_rate}</div>
                        <div>Status: <span style="color:#34d399;">${tx.validation_status}</span></div>
                    </div>
                `;
            } else if (data.type === 'ADDRESS') {
                const ad = data.data;
                container.innerHTML = `
                    <div style="background:#060911; border:1px solid #334155; padding:12px; border-radius:6px;">
                        <div style="color:#c084fc; font-weight:700; margin-bottom:6px;">📍 ADDRESS ACTIVITY SCANNER</div>
                        <div>Address: <span class="addr-tag">${ad.address}</span></div>
                        <div style="margin-top:6px;">Matched Transactions: ${ad.matched_transactions.length}</div>
                    </div>
                `;
            }
        }

        function openActionModal(type) {
            const modal = document.getElementById('actionModal');
            const header = document.getElementById('modalHeader');
            const body = document.getElementById('modalDynamicBody');
            modal.style.display = 'flex';

            let netOptions = '';
            for (const [k, v] of Object.entries(walletState.networks || {})) {
                netOptions += `<option value="${k}">${v.network_name}</option>`;
            }

            if (type === 'security') {
                header.innerText = "🔒 Security, Chipset Enclave & Global IMEI Portability";
                let boundList = (walletState.bound_devices || []).map(d => `
                    <div style="font-family:monospace; font-size:0.75rem; background:#060911; padding:6px; border-radius:4px; margin-bottom:4px;">
                        • ${d.status} | IMEI: <strong style="color:#38bdf8;">${d.imei}</strong> | Device ID: ${d.device_id.substring(0, 16)}...
                    </div>
                `).join('');

                body.innerHTML = `
                    <div style="margin-bottom:16px;">
                        <div style="font-weight:700; color:#38bdf8; font-size:0.85rem; margin-bottom:8px;">📱 Global Hardware Device Binding & IMEI</div>
                        <div class="form-group"><label>Global Device ID</label><input class="form-input" value="${walletState.global_device_id}" readonly /></div>
                        <div class="form-group"><label>Authorized IMEI Number</label><input class="form-input" value="${walletState.imei_number}" readonly /></div>
                        <div style="margin-bottom:10px;"><label class="muted">Authorized Nodes List</label>${boundList}</div>
                    </div>

                    <div style="border-top:1px solid #1e293b; padding-top:12px; margin-bottom:16px;">
                        <div style="font-weight:700; color:#34d399; font-size:0.85rem; margin-bottom:8px;">🔑 Reset Master Password</div>
                        <div class="form-group"><label>Current Password</label><input id="secOldPassword" type="password" class="form-input" placeholder="••••••••" /></div>
                        <div class="form-group"><label>New Master Password</label><input id="secNewPassword" type="password" class="form-input" placeholder="••••••••" /></div>
                        <button class="btn btn-blue" style="width:100%;" onclick="submitPasswordReset()">Update Password</button>
                    </div>

                    <div style="border-top:1px solid #1e293b; padding-top:12px;">
                        <div style="font-weight:700; color:#c084fc; font-size:0.85rem; margin-bottom:8px;">🌐 Bind New Portable Device (IMEI)</div>
                        <div class="form-group"><label>Target 15-Digit Hardware IMEI</label><input id="newImeiInput" class="form-input" placeholder="86XXXXXXXXXXXXX" /></div>
                        <div class="form-group"><label>Device Label</label><input id="newDevLabel" class="form-input" placeholder="e.g. Mobile Android Node 2" /></div>
                        <button class="btn btn-purple" style="width:100%;" onclick="submitBindDevice()">Authorize & Bind Portable Node</button>
                    </div>
                `;
            } else if (type === 'send') {
                header.innerText = "Multi-Network Send Transfer";
                body.innerHTML = `
                    <div class="form-group"><label>Network Layer</label><select id="sendNet" class="form-input">${netOptions}</select></div>
                    <div class="form-group"><label>Target Address / LN-Invoice</label><input id="sendAddr" class="form-input" placeholder="bc1q..., 0x..., or lnbc..." /></div>
                    <div class="form-group"><label>Transfer Amount</label><input id="sendAmount" type="number" step="any" class="form-input" placeholder="0.00" /></div>
                    <button class="btn btn-blue" style="width:100%;" onclick="submitSend()">Broadcast to Mempool</button>
                `;
            } else if (type === 'receive') {
                header.innerText = "Receive & Scannable QR Code";
                const firstNet = Object.keys(walletState.networks)[0];
                const firstAddr = walletState.networks[firstNet].address;
                body.innerHTML = `
                    <div class="form-group"><label>Select Target Bitcoin Network</label>
                    <select id="recvNetSelect" class="form-input" onchange="updateQR(this.value)">${netOptions}</select></div>
                    <div id="qrContainer"></div>
                    <div class="form-group"><label>Derived Public Address</label><div class="addr-tag" id="qrAddressText">${firstAddr}</div></div>
                `;
                setTimeout(() => generateQR(firstAddr), 50);
            } else if (type === 'deposit') {
                header.innerText = "Deposit / Gateway Inflow";
                body.innerHTML = `
                    <div class="form-group"><label>Target Network</label><select id="depNet" class="form-input">${netOptions}</select></div>
                    <div class="form-group"><label>Quantity</label><input id="depAmount" type="number" step="any" class="form-input" placeholder="1.0" /></div>
                    <button class="btn btn-blue" style="width:100%;" onclick="submitDeposit()">Credit Node Balance</button>
                `;
            } else if (type === 'withdraw') {
                header.innerText = "External Withdrawal";
                body.innerHTML = `
                    <div class="form-group"><label>Network</label><select id="wdNet" class="form-input">${netOptions}</select></div>
                    <div class="form-group"><label>External Address</label><input id="wdAddr" class="form-input" placeholder="Destination..." /></div>
                    <div class="form-group"><label>Amount</label><input id="wdAmount" type="number" step="any" class="form-input" placeholder="0.00" /></div>
                    <button class="btn btn-blue" style="width:100%;" onclick="submitWithdraw()">Process Withdrawal</button>
                `;
            } else if (type === 'buy') {
                header.innerText = "Buy Bitcoin via Fiat Rail";
                body.innerHTML = `
                    <div class="form-group"><label>Target Network</label><select id="buyNet" class="form-input">${netOptions}</select></div>
                    <div class="form-group"><label>USD Purchase Amount</label><input id="buyUSD" type="number" class="form-input" placeholder="500" /></div>
                    <button class="btn btn-blue" style="width:100%;" onclick="submitBuy()">Authorize Settlement</button>
                `;
            } else if (type === 'sell') {
                header.innerText = "Liquidate Bitcoin to USDT";
                body.innerHTML = `
                    <div class="form-group"><label>Source Network</label><select id="sellNet" class="form-input">${netOptions}</select></div>
                    <div class="form-group"><label>BTC Amount</label><input id="sellQty" type="number" step="any" class="form-input" placeholder="0.1" /></div>
                    <button class="btn btn-blue" style="width:100%;" onclick="submitSell()">Execute Liquidation</button>
                `;
            } else if (type === 'swap') {
                header.innerText = "Cross-Layer Bitcoin Swap";
                body.innerHTML = `
                    <div class="form-group"><label>From Network</label><select id="swapFrom" class="form-input">${netOptions}</select></div>
                    <div class="form-group"><label>To Network</label><select id="swapTo" class="form-input">${netOptions}</select></div>
                    <div class="form-group"><label>Amount to Swap</label><input id="swapAmt" type="number" step="any" class="form-input" placeholder="0.5" /></div>
                    <button class="btn btn-blue" style="width:100%;" onclick="submitSwap()">Execute Bridge Swap</button>
                `;
            } else if (type === 'stake') {
                header.innerText = "Proof-of-Stake Delegation Vault";
                body.innerHTML = `
                    <div class="form-group"><label>Staking Pool</label><select id="stakeNet" class="form-input">${netOptions}</select></div>
                    <div class="form-group"><label>Amount</label><input id="stakeAmt" type="number" step="any" class="form-input" placeholder="1.0" /></div>
                    <button class="btn btn-purple" style="width:100%;" onclick="submitStake()">Delegate & Lock Capital</button>
                `;
            } else if (type === 'escrow') {
                header.innerText = "Multi-Sig Escrow Contract";
                body.innerHTML = `
                    <div class="form-group"><label>Network</label><select id="escNet" class="form-input">${netOptions}</select></div>
                    <div class="form-group"><label>Counterparty Address</label><input id="escCounter" class="form-input" placeholder="Counterparty..." /></div>
                    <div class="form-group"><label>Lock Amount</label><input id="escAmt" type="number" step="any" class="form-input" placeholder="0.25" /></div>
                    <button class="btn btn-purple" style="width:100%;" onclick="submitEscrow()">Lock Multi-Sig Escrow</button>
                `;
            } else if (type === 'keys') {
                header.innerText = "Derived HD Private Keys & BIP-39 Seed";
                let keysView = `<div class="form-group"><label>BIP-39 Mnemonic Seed</label><div class="addr-tag">${walletState.mnemonic}</div></div>`;
                for (const [netKey, net] of Object.entries(walletState.networks)) {
                    keysView += `
                        <div style="margin-top:10px; border-top:1px solid #1e293b; padding-top:8px;">
                            <div style="font-weight:700; color:#38bdf8; font-size:0.8rem;">${net.network_name} (${net.derivation_path})</div>
                            <div style="font-size:0.75rem; color:#94a3b8; word-break:break-all;">Public Key: ${net.public_key}</div>
                            <div style="font-size:0.75rem; color:#f87171; word-break:break-all;">Private Key: ${net.private_key}</div>
                        </div>
                    `;
                }
                body.innerHTML = keysView;
            } else if (type === 'import') {
                header.innerText = "Import Asset Vault (12/24 Mnemonics or Private Key)";
                body.innerHTML = `
                    <div class="form-group"><label>Enter BIP-39 12/24-Word Mnemonic Phrase OR 64-char Hex Private Key</label><textarea id="importWords" class="form-input" rows="4" placeholder="word1 word2 word3... OR 0xabcdef0123456789..."></textarea></div>
                    <button class="btn btn-blue" style="width:100%;" onclick="submitImport()">Import & Rebuild Mainnet Vault</button>
                `;
            }
        }

        function closeModal() { document.getElementById('actionModal').style.display = 'none'; }

        function generateQR(text) {
            const container = document.getElementById('qrContainer');
            container.innerHTML = '';
            new QRCode(container, { text: text, width: 140, height: 140 });
        }

        function updateQR(netKey) {
            const addr = walletState.networks[netKey].address;
            document.getElementById('qrAddressText').innerText = addr;
            generateQR(addr);
        }

        async function submitPasswordReset() {
            const oldP = document.getElementById('secOldPassword').value;
            const newP = document.getElementById('secNewPassword').value;
            const res = await fetch('/api/security/reset-password', {
                method: 'POST',
                body: JSON.stringify({ old_password: oldP, new_password: newP })
            });
            const data = await res.json();
            if (data.success) {
                alert("Master Password reset successfully.");
                closeModal();
            } else {
                alert(data.error || "Password update failed.");
            }
        }

        async function submitBindDevice() {
            const imei = document.getElementById('newImeiInput').value.trim();
            const label = document.getElementById('newDevLabel').value.trim();
            const res = await fetch('/api/security/bind-device', {
                method: 'POST',
                body: JSON.stringify({ imei: imei, label: label })
            });
            const data = await res.json();
            if (data.success) {
                alert("New hardware device IMEI registered and authorized for portability.");
                closeModal();
                fetchState();
            } else {
                alert(data.error || "Device binding failed.");
            }
        }

        async function submitSend() {
            await fetch('/api/action/send', {
                method: 'POST',
                body: JSON.stringify({ network: document.getElementById('sendNet').value, to_address: document.getElementById('sendAddr').value, amount: parseFloat(document.getElementById('sendAmount').value) })
            });
            closeModal(); fetchState();
        }

        async function submitDeposit() {
            await fetch('/api/action/deposit', {
                method: 'POST',
                body: JSON.stringify({ network: document.getElementById('depNet').value, amount: parseFloat(document.getElementById('depAmount').value) })
            });
            closeModal(); fetchState();
        }

        async function submitWithdraw() {
            await fetch('/api/action/withdraw', {
                method: 'POST',
                body: JSON.stringify({ network: document.getElementById('wdNet').value, to_address: document.getElementById('wdAddr').value, amount: parseFloat(document.getElementById('wdAmount').value) })
            });
            closeModal(); fetchState();
        }

        async function submitBuy() {
            await fetch('/api/action/buy', {
                method: 'POST',
                body: JSON.stringify({ network: document.getElementById('buyNet').value, amount_usd: parseFloat(document.getElementById('buyUSD').value) })
            });
            closeModal(); fetchState();
        }

        async function submitSell() {
            await fetch('/api/action/sell', {
                method: 'POST',
                body: JSON.stringify({ network: document.getElementById('sellNet').value, amount: parseFloat(document.getElementById('sellQty').value) })
            });
            closeModal(); fetchState();
        }

        async function submitSwap() {
            await fetch('/api/action/swap', {
                method: 'POST',
                body: JSON.stringify({ from_net: document.getElementById('swapFrom').value, to_net: document.getElementById('swapTo').value, amount: parseFloat(document.getElementById('swapAmt').value) })
            });
            closeModal(); fetchState();
        }

        async function submitStake() {
            await fetch('/api/action/stake', {
                method: 'POST',
                body: JSON.stringify({ network: document.getElementById('stakeNet').value, amount: parseFloat(document.getElementById('stakeAmt').value) })
            });
            closeModal(); fetchState();
        }

        async function submitEscrow() {
            await fetch('/api/action/escrow', {
                method: 'POST',
                body: JSON.stringify({ network: document.getElementById('escNet').value, counterparty: document.getElementById('escCounter').value, amount: parseFloat(document.getElementById('escAmt').value) })
            });
            closeModal(); fetchState();
        }

        async function submitImport() {
            await fetch('/api/action/import', {
                method: 'POST',
                body: JSON.stringify({ import_data: document.getElementById('importWords').value })
            });
            closeModal(); fetchState();
        }

        initPairBar();
        fetchState();
        setInterval(fetchState, 1500);
    </script>
</body>
</html>
"""

# =====================================================================
# 8. REST & SECURITY API ENDPOINTS
# =====================================================================
@app.route('/')
def index():
    return render_template_string(HTML_DASHBOARD)

@app.route('/api/auth/session', methods=['GET'])
def auth_session():
    is_auth = session.get('authenticated', False)
    return jsonify({
        "authenticated": is_auth,
        "wallet_id_hint": node.wallet_id
    })

@app.route('/api/auth/login', methods=['POST'])
def auth_login():
    data = request.get_json(force=True)
    wid = data.get('wallet_id', '')
    pwd = data.get('password', '')
    if node.verify_credentials(wid, pwd):
        session['authenticated'] = True
        session['wallet_id'] = node.wallet_id
        return jsonify({"success": True})
    return jsonify({"success": False, "error": "Invalid Wallet ID or Password."}), 401

@app.route('/api/auth/logout', methods=['POST'])
def auth_logout():
    session.clear()
    return jsonify({"success": True})

@app.before_request
def require_authentication():
    allowed = ['/', '/api/auth/session', '/api/auth/login', '/static']
    if request.path in allowed:
        return
    if not session.get('authenticated'):
        return jsonify({"error": "Unauthorized session. Please login."}), 401

@app.route('/api/state', methods=['GET'])
def get_state():
    return jsonify(node.get_full_state())

@app.route('/api/explorer/search', methods=['GET'])
def explorer_search():
    query = request.args.get('q', '')
    result = node.mempool_engine.search_explorer(query)
    return jsonify(result)

@app.route('/api/security/reset-password', methods=['POST'])
def reset_password():
    data = request.get_json(force=True)
    return jsonify(node.update_password(data.get('old_password', ''), data.get('new_password', '')))

@app.route('/api/security/bind-device', methods=['POST'])
def bind_device():
    data = request.get_json(force=True)
    return jsonify(node.register_portable_device(data.get('imei', ''), data.get('label', 'Portable Device')))

@app.route('/api/cmc/buy', methods=['POST'])
def cmc_buy():
    data = request.get_json(force=True)
    return jsonify(node.buy_cmc_asset(data['symbol'], float(data['usd_amount'])))

@app.route('/api/terminal/order', methods=['POST'])
def terminal_order():
    data = request.get_json(force=True)
    return jsonify(node.execute_terminal_order(data['pair'], data['side'], float(data['amount'])))

@app.route('/api/terminal/predict', methods=['POST'])
def terminal_predict():
    data = request.get_json(force=True)
    contract = node.terminal.create_prediction(data['pair'], data['direction'], float(data['stake_amount']), int(data.get('duration', 30)))
    node.balances["USDT"] -= float(data['stake_amount'])
    node._dispatch_tx("BTC_SEGWIT", f"PREDICTION_LOCKED_{data['direction']}", float(data['stake_amount']), "Binary Option Vault", f"Contract: {contract['prediction_id']}")
    return jsonify({"success": True, "contract": contract})

@app.route('/api/miner/start', methods=['POST'])
def miner_start():
    node.miner.start()
    return jsonify({"success": True})

@app.route('/api/miner/stop', methods=['POST'])
def miner_stop():
    node.miner.stop()
    return jsonify({"success": True})

@app.route('/api/ai/start', methods=['POST'])
def ai_start():
    node.ai_robot.start()
    return jsonify({"success": True})

@app.route('/api/ai/stop', methods=['POST'])
def ai_stop():
    node.ai_robot.stop()
    return jsonify({"success": True})

@app.route('/api/action/mine', methods=['POST'])
def action_mine():
    block = node.mempool_engine.mine_mempool_block()
    return jsonify({"success": True, "block": block})

@app.route('/api/action/send', methods=['POST'])
def action_send():
    data = request.get_json(force=True)
    return jsonify(node.send(data['network'], data['to_address'], data['amount']))

@app.route('/api/action/deposit', methods=['POST'])
def action_deposit():
    data = request.get_json(force=True)
    return jsonify(node.deposit(data['network'], data['amount']))

@app.route('/api/action/withdraw', methods=['POST'])
def action_withdraw():
    data = request.get_json(force=True)
    return jsonify(node.withdraw(data['network'], data['to_address'], data['amount']))

@app.route('/api/action/buy', methods=['POST'])
def action_buy():
    data = request.get_json(force=True)
    return jsonify(node.buy(data['network'], data['amount_usd']))

@app.route('/api/action/sell', methods=['POST'])
def action_sell():
    data = request.get_json(force=True)
    return jsonify(node.sell(data['network'], data['amount']))

@app.route('/api/action/swap', methods=['POST'])
def action_swap():
    data = request.get_json(force=True)
    return jsonify(node.swap(data['from_net'], data['to_net'], data['amount']))

@app.route('/api/action/stake', methods=['POST'])
def action_stake():
    data = request.get_json(force=True)
    return jsonify(node.stake(data['network'], data['amount']))

@app.route('/api/action/escrow', methods=['POST'])
def action_escrow():
    data = request.get_json(force=True)
    return jsonify(node.escrow(data['network'], data['counterparty'], data['amount']))

@app.route('/api/action/import', methods=['POST'])
def action_import():
    data = request.get_json(force=True)
    res = node.import_vault_key(data['import_data'])
    return jsonify(res)

@app.route('/api/action/export', methods=['GET'])
def action_export():
    keys_data = node.export_keys_bundle()
    json_output = json.dumps(keys_data, indent=2)
    return Response(
        json_output,
        mimetype="application/json",
        headers={"Content-Disposition": "attachment;filename=hd_wallet_backup.json"}
    )

# =====================================================================
# 9. RUN SERVER (Configured for Pydroid 3 & Standard Python)
# =====================================================================
if __name__ == '__main__':
    print("\n=================================================================")
    print("  Enterprise Circuit Board OS & HD Trade Terminal Running")
    print(f"  Default Login Wallet ID : {node.wallet_id}")
    print("  Default Login Password  : admin123")
    print("  Web Dashboard & Terminal: http://127.0.0.1:5000")
    print("=================================================================\n")
    
    app.run(host='0.0.0.0', port=5000, debug=False, use_reloader=False)




