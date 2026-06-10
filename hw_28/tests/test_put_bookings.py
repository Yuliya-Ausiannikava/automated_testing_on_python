"""PUT tests for bookings"""

from utils.logger import logger
from utils.assertions import assert_status_code, assert_json_schema
from utils.schemas.booking_schemas import BOOKING_SCHEMA
from utils.data_generator import get_updated_booking_data


class TestPutBookings:
    # Positive test: full update of booking
    def test_update_booking_full(self, booking_api, test_booking_id, auth_token):
        booking_id = test_booking_id
        logger.info("Test: full update of booking ID %s", booking_id)

        updated_data = get_updated_booking_data()
        response = booking_api.update_booking(booking_id, updated_data, auth_token)

        assert_status_code(response, 200)
        assert_json_schema(response, BOOKING_SCHEMA)
        assert response.json()["firstname"] == updated_data["firstname"]
        assert response.json()["lastname"] == updated_data["lastname"]
        assert response.json()["totalprice"] == updated_data["totalprice"]

        logger.info("Full update of booking test passed")

    # Negative test: update without auth token
    def test_update_booking_without_auth(self, booking_api, test_booking_id):
        logger.info("Test: update booking without auth token")

        booking_id = test_booking_id
        updated_data = get_updated_booking_data()
        response = booking_api.update_booking(booking_id, updated_data, token="")
        assert_status_code(response, 403)

        logger.info("Access denied without token (403), test passed")

    # Negative test: update non-existent booking
    def test_update_nonexistent_booking(self, booking_api, auth_token):
        logger.info("Test: update non-existent booking")

        updated_data = get_updated_booking_data()
        response = booking_api.update_booking("non-existent", updated_data, auth_token)
        assert response.status_code in [404, 405]

        logger.info("Non-existent booking update returned error, test passed")
