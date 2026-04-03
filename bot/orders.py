import logging
from bot.validators import *
from bot.client import SimulatedClient

client = SimulatedClient()

def place_order(symbol, side, order_type, quantity, price=None, stop_price=None):
    try:
        validate_side(side)
        validate_order_type(order_type)
        validate_quantity(quantity)
        validate_price(order_type, price)
        validate_stop_price(order_type, stop_price)

        logging.info(f"Order Request: {symbol} {side} {order_type}")

        order = client.create_order(symbol, side, order_type, quantity, price)

        logging.info(f"Order Response: {order}")
        return order

    except Exception as e:
        logging.exception("Error:")
        raise
