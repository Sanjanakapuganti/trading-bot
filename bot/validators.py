def validate_side(side):
    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")

def validate_order_type(order_type):
    if order_type not in ["MARKET", "LIMIT", "STOP_LIMIT"]:
        raise ValueError("Invalid order type")

def validate_quantity(quantity):
    if quantity <= 0:
        raise ValueError("Quantity must be > 0")

def validate_price(order_type, price):
    if order_type in ["LIMIT", "STOP_LIMIT"] and (price is None or price <= 0):
        raise ValueError("Price required")

def validate_stop_price(order_type, stop_price):
    if order_type == "STOP_LIMIT" and (stop_price is None or stop_price <= 0):
        raise ValueError("Stop price required")
