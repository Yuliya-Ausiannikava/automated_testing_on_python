"""GET tests for bookings"""

import pytest
from utils.logger import logger
from utils.assertions import assert_status_code, assert_json_schema
from utils.schemas.booking_schemas import BOOKINGS_LIST_SCHEMA, BOOKING_SCHEMA


class TestGetBookings:
    # Positive test: GET /booking - get all bookings
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.get
    @pytest.mark.positive
    def test_get_all_bookings(self, booking_api):
        logger.info("Test: GET all bookings")

        response = booking_api.get_all_bookings()

        assert_status_code(response, 200)
        assert isinstance(response.json(), list)
        assert_json_schema(response, BOOKINGS_LIST_SCHEMA)

        logger.info("GET all bookings test passed")

    # Positive test: GET /booking/{id} - get booking by ID
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.get
    @pytest.mark.positive
    def test_get_booking_by_id(self, booking_api, test_booking):
        booking_id, expected_data = test_booking
        logger.info("Test: get booking by ID %s", booking_id)

        response = booking_api.get_booking_by_id(booking_id)
        assert_status_code(response, 200)
        assert_json_schema(response, BOOKING_SCHEMA)
        assert response.json()["firstname"] == expected_data["firstname"]
        assert response.json()["lastname"] == expected_data["lastname"]

        logger.info("GET booking by id test passed")

    # Negative test: GET /booking/{id} - non-existent ID
    @pytest.mark.get
    @pytest.mark.negative
    def test_get_booking_by_invalid_id(self, booking_api):
        logger.info("Test: get booking with invalid ID")

        response = booking_api.get_booking_by_id("invalid")
        assert_status_code(response, 404)

        logger.info("GET booking with invalid ID test passed")
