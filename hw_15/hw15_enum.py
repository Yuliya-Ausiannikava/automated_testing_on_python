"""
The Enum class was created, containing possible order statuses.
"""

from enum import Enum


class OrderStatus(Enum):
    PENDING = 'PENDING'
    IN_PROGRESS = 'IN_PROGRESS'
    READY = 'READY'
    COMPLETED = 'COMPLETED'
    CANCELLED = 'CANCELLED'


class Order:
    def __init__(self, order_id: int, status: OrderStatus = OrderStatus.PENDING):
        self.order_id = order_id
        self.status = status

    # Updates the order status
    def update_status(self, new_status):
        self.status = new_status

    # Displays the current order status
    def display_status(self):
        return self.status


application_1 = Order(1, OrderStatus.PENDING)
print(application_1.display_status())

application_1.update_status(OrderStatus.COMPLETED)
print(application_1.display_status())
