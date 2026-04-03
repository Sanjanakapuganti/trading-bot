import click
import matplotlib.pyplot as plt
import random

from bot.orders import place_order
from bot.logging_config import setup_logger

setup_logger()

def show_price_graph():
    prices = [random.randint(60000, 70000) for _ in range(20)]
    plt.plot(prices)
    plt.title("Simulated BTC Price Movement")
    plt.xlabel("Time")
    plt.ylabel("Price")
    plt.show()

def generate_signal():
    signal = random.choice(["BUY", "SELL", "HOLD"])
    print(f"\n🤖 AI Suggestion: {signal}")

@click.command()
@click.option("--symbol", required=True)
@click.option("--side", type=click.Choice(["BUY", "SELL"]), required=True)
@click.option("--order_type", type=click.Choice(["MARKET", "LIMIT", "STOP_LIMIT"]), required=True)
@click.option("--quantity", type=float, required=True)
@click.option("--price", type=float, default=None)
@click.option("--stop_price", type=float, default=None)

def main(symbol, side, order_type, quantity, price, stop_price):
    print("\n=== ORDER REQUEST ===")
    print(symbol, side, order_type, quantity, price)

    try:
        order = place_order(symbol, side, order_type, quantity, price, stop_price)

        print("\n=== ORDER RESPONSE ===")
        print(order)

        print("\n✅ Success")

    except Exception as e:
        print("\n❌ Failed:", str(e))

if __name__ == "__main__":
    main()
