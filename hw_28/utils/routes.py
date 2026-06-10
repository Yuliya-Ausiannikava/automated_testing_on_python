from enum import Enum


class APIRoutes(str, Enum):
    AUTH = '/auth'
    BOOKINGS = '/booking'

    @staticmethod
    def get_booking(booking_id):
        """Get endpoint for specific booking"""
        return f"{APIRoutes.BOOKINGS}/{booking_id}"
