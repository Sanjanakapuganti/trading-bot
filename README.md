# trading-bot
# 📊 Simplified Trading Bot (Simulated)

## 🚀 Overview
This project is a simplified trading bot built in Python.  
It allows users to place MARKET, LIMIT, and STOP-LIMIT orders through a CLI interface.

Due to Binance API access restrictions (KYC requirement), the order execution is simulated.  
However, the system is designed in a modular way and can be easily connected to real APIs.

---

## ✨ Features
- Supports BUY and SELL orders
- Order types:
  - MARKET
  - LIMIT
  - STOP-LIMIT
- CLI-based input using Click
- Input validation
- Logging of requests and responses
- Exception handling

---

## 📁 Project Structure
trading_bot/
│
├── bot/
│ ├── client.py
│ ├── orders.py
│ ├── validators.py
│ ├── logging_config.py
│
├── cli.py
├── README.md
├── requirements.txt

---

## ⚙️ Installation

```bash
pip install -r requirements.txt
▶️ Usage
MARKET Order
python cli.py --symbol BTCUSDT --side BUY --order_type MARKET --quantity 0.001


=== ORDER REQUEST ===
Symbol: BTCUSDT
Side: BUY
Type: MARKET

=== ORDER RESPONSE ===
Order ID: 123456
Status: FILLED
Executed Qty: 0.001
Avg Price: 65000

✅ Order placed successfully!
