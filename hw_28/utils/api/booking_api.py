"""
Class for working with booking API
"""

from hw_28.utils.logger import logger
from hw_28.utils.clients.http_client import HTTPClient
from hw_28.utils.routes import APIRoutes


class BookingAPI:
    def __init__(self):
        self.client = HTTPClient()
        logger.debug("BookingAPI initialized")

    # GET /booking - get all bookings
    def get_all_bookings(self, params=None):
        logger.info("Requesting all bookings")
        response = self.client.get(APIRoutes.BOOKINGS, params=params)
        logger.info("Received %d bookings", len(response.json()))
        return response

    # GET /booking/{id} - get booking by ID
    def get_booking_by_id(self, booking_id):
        logger.info("Requesting booking with ID: %s", booking_id)
        return self.client.get(APIRoutes.get_booking(booking_id))

    # POST /booking - create booking
    def create_booking(self, booking_data):
        logger.info("Creating new booking: %s %s",
                    booking_data.get('firstname'), booking_data.get('lastname'))
        response = self.client.post(APIRoutes.BOOKINGS, data=booking_data)

        if response.status_code == 200:
            booking_id = response.json().get('bookingid')
            logger.info("Booking created with ID: %s", booking_id)
        return response

    # PUT /booking/{id} - fully update booking
    def update_booking(self, booking_id, booking_data, token):
        logger.info("Full update of booking ID: %s", booking_id)
        return self.client.put(APIRoutes.get_booking(booking_id), data=booking_data, token=token)

    # PATCH /booking/{id} - partially update booking
    def partial_update_booking(self, booking_id, booking_data, token):
        logger.info("Partial update of booking ID: %s", booking_id)
        return self.client.patch(APIRoutes.get_booking(booking_id), data=booking_data, token=token)

    # DELETE /booking/{id} - delete booking
    def delete_booking(self, booking_id, token):
        logger.warning("Deleting booking ID: %s", booking_id)
        return self.client.delete(APIRoutes.get_booking(booking_id), token=token)
