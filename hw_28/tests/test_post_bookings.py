"""POST tests for bookings"""

from utils.logger import logger
from utils.assertions import assert_status_code, assert_json_schema, assert_response_has_key
from utils.schemas.booking_schemas import CREATE_BOOKING_SCHEMA
from utils.data_generator import (get_valid_booking_data, get_invalid_booking_data,
                                  get_booking_without_required_fields)


class TestPostBookings:
    # Positive test: create booking with valid data
    def test_create_booking_valid_data(self, booking_api):
        logger.info("Test: create booking with valid data")

        booking_data = get_valid_booking_data()
        response = booking_api.create_booking(booking_data)

        assert_status_code(response, 200)
        assert_response_has_key(response, "bookingid")
        assert_response_has_key(response, "booking")
        assert_json_schema(response, CREATE_BOOKING_SCHEMA)

        created = response.json()["booking"]
        assert created["firstname"] == booking_data["firstname"]
        assert created["lastname"] == booking_data["lastname"]

        logger.info("Create booking with valid data test passed")

    # Negative test: create booking with invalid data
    def test_create_booking_invalid_data(self, booking_api):
        logger.info("Test: create booking with invalid data")

        booking_data = get_invalid_booking_data()
        response = booking_api.create_booking(booking_data)

        assert response.status_code in [400, 500]

        logger.info("Invalid data correctly rejected")
        logger.info("Create booking with invalid data test passed")

    # Negative test: create booking without required fields
    def test_create_booking_without_required_fields(self, booking_api):
        logger.info("Test: create booking without required fields")

        incomplete_data = get_booking_without_required_fields()
        response = booking_api.create_booking(incomplete_data)
        assert response.status_code in [400, 500]

        logger.info("Missing required fields correctly rejected")
        logger.info("Create booking without required fields test passed")
