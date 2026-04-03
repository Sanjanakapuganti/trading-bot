import random
from datetime import datetime

class SimulatedClient:
    def create_order(self, symbol, side, order_type, quantity, price=None):
        if order_type == "MARKET":
            return {
                "orderId": random.randint(100000, 999999),
                "status": "FILLED",
                "executedQty": quantity,
                "avgPrice": random.randint(60000, 70000),
                "time": str(datetime.now())
            }

        elif order_type == "LIMIT":
            return {
                "orderId": random.randint(100000, 999999),
                "status": "NEW",
                "executedQty": 0,
                "avgPrice": price,
                "time": str(datetime.now())
            }

        elif order_type == "STOP_LIMIT":
            return {
                "orderId": random.randint(100000, 999999),
                "status": "TRIGGER_PENDING",
                "executedQty": 0,
                "avgPrice": price,
                "time": str(datetime.now())
            }
