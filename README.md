# trading-bot
# 📊 Simplified Trading Bot (Simulated)

## 🚀 Project Description

This project is a Smart Trading Bot developed using Python that simulates trading operations in a structured and interactive way.

The system allows users to place different types of orders such as MARKET, LIMIT, and STOP-LIMIT through a command-line interface. It validates user input, logs all activities, and provides clear output for each transaction.

---

## 🤖 Intelligent Features

In addition to basic trading functionality, the project includes:

- 🔹 AI-based Signal Generator  
  Provides a random BUY / SELL / HOLD suggestion to simulate intelligent decision-making.

- 🔹 Price Visualization  
  Generates and displays a simulated price graph using matplotlib to represent market trends.

- 🔹 Interactive CLI Menu  
  Users can navigate through options like:

  
1.Place Order


<img width="1213" height="434" alt="Screenshot 2026-04-03 213938" src="https://github.com/user-attachments/assets/f0bf31f3-9aaa-4907-b19e-23848cd1706a" />

--NOTE:
VALIDATION CHECKS

 <img width="774" height="487" alt="Screenshot 2026-04-03 213928" src="https://github.com/user-attachments/assets/1ea9a161-937a-42da-821f-f5578a06b9e9" />

 2.Show Price Graph
 
<img width="754" height="658" alt="Screenshot 2026-04-03 213954" src="https://github.com/user-attachments/assets/db10c298-083b-423d-93d5-3ca9699ef844" />

3.Get AI Signal

<img width="382" height="192" alt="image" src="https://github.com/user-attachments/assets/564f64c1-ff41-4e35-8219-354f0ebaaf24" />


4.Exit


<img width="566" height="419" alt="Screenshot 2026-04-03 214005" src="https://github.com/user-attachments/assets/c463432e-3465-45dd-8913-de5c339ec5f1" />

---

## ⚙️ Input Validation & Error Handling

The system validates all user inputs before executing orders.  
For example, invalid inputs like:
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
