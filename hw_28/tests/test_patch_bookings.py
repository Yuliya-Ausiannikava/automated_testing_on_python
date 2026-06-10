"""PATCH tests for bookings"""

import pytest
from utils.logger import logger
from utils.assertions import assert_status_code
from utils.data_generator import get_partial_update_data


class TestPatchBookings:
    # Positive test: partial update of booking
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.patch
    @pytest.mark.positive
    def test_partial_update_booking(self, booking_api, test_booking_with_data, auth_token):
        booking_id, original_data = test_booking_with_data
        logger.info("Test: partial update of booking ID %s", booking_id)

        partial_data = get_partial_update_data()
        response = booking_api.partial_update_booking(booking_id, partial_data, auth_token)

        assert_status_code(response, 200)
        assert response.json()["firstname"] == partial_data["firstname"]
        assert response.json()["totalprice"] == partial_data["totalprice"]
        assert response.json()["lastname"] == original_data["lastname"]

        logger.info("Partial update of booking test passed")

    # Negative test: PATCH without authorization
    @pytest.mark.patch
    @pytest.mark.negative
    def test_partial_update_without_auth(self, booking_api, test_booking_id):
        logger.info("Test: PATCH without authorization")

        booking_id = test_booking_id

        partial_data = get_partial_update_data()
        response = booking_api.partial_update_booking(booking_id, partial_data, token="")

        assert_status_code(response, 403)

        logger.info("Access denied without token (403), test passed")
