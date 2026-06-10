"""DELETE tests for bookings"""

from utils.logger import logger
from utils.assertions import assert_status_code
from utils.data_generator import get_valid_booking_data


class TestDeleteBookings:
    # Positive test: delete booking
    def test_delete_booking(self, booking_api, auth_token):
        logger.info("Test: delete booking")

        booking_data = get_valid_booking_data()
        create_response = booking_api.create_booking(booking_data)
        booking_id = create_response.json()["bookingid"]
        logger.info("Created booking %s for deletion", booking_id)

        response = booking_api.delete_booking(booking_id, auth_token)
        assert_status_code(response, 201)

        get_response = booking_api.get_booking_by_id(booking_id)
        assert get_response.status_code == 404

        logger.info("Deleted booking test passed")

    # Negative test: delete already deleted booking
    def test_delete_already_deleted_booking(self, booking_api, auth_token):
        logger.info("Test: delete already deleted booking")

        booking_data = get_valid_booking_data()
        create_response = booking_api.create_booking(booking_data)
        booking_id = create_response.json()["bookingid"]
        logger.info("Created booking %s for deletion", booking_id)

        response1 = booking_api.delete_booking(booking_id, auth_token)
        assert_status_code(response1, 201)

        logger.info("First deletion succeeded")

        response2 = booking_api.delete_booking(booking_id, auth_token)
        assert response2.status_code in [404, 405]

        logger.info("Second deletion correctly returned error, test passed")

    # Negative test: DELETE without authorization
    def test_delete_booking_without_auth(self, booking_api):
        logger.info("Test: delete booking without auth token")

        booking_data = get_valid_booking_data()
        create_response = booking_api.create_booking(booking_data)
        booking_id = create_response.json()["bookingid"]

        response = booking_api.delete_booking(booking_id, token="")
        assert_status_code(response, 403)

        logger.info("Delete without token denied (403), test passed")
