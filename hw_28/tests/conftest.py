import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

import pytest
import requests
from utils.logger import logger
from utils.api.auth_api import AuthAPI
from utils.api.booking_api import BookingAPI
from utils.data_generator import get_valid_booking_data
from config.settings import TEST_USER_EMAIL, TEST_USER_PASSWORD


@pytest.fixture(scope="session")
def auth_api():
    logger.debug("Creating auth_api fixture")
    return AuthAPI()


@pytest.fixture(scope="session")
def booking_api():
    logger.debug("Creating booking_api fixture")
    return BookingAPI()


@pytest.fixture(scope="session")
def auth_token(auth_api):
    """Fixture: authentication token (once per session)"""
    logger.info("Getting auth token via fixture")
    token = auth_api.get_token(TEST_USER_EMAIL, TEST_USER_PASSWORD)
    logger.info("Token obtained successfully")
    return token


@pytest.fixture(scope="function")
def test_booking(booking_api):
    """
    Fixture: creates a booking before test
    and deletes it after test
    """

    logger.info("Fixture test_booking: creating test booking")

    # Setup: create booking
    booking_data = get_valid_booking_data()
    response = booking_api.create_booking(booking_data)
    assert response.status_code == 200
    booking_id = response.json()["bookingid"]

    logger.info("Test booking created with ID: %s", booking_id)

    yield booking_id, booking_data

    # Teardown: delete booking
    logger.info("Fixture test_booking: deleting test booking %s", booking_id)
    try:
        auth = AuthAPI()
        token = auth.get_token(TEST_USER_EMAIL, TEST_USER_PASSWORD)
        booking_api.delete_booking(booking_id, token)
        logger.debug("Booking %s deleted successfully", booking_id)
    except requests.exceptions.RequestException as e:
        logger.warning("Failed to delete booking %s: %s", booking_id, e)



@pytest.fixture
def test_booking_id(booking_api):
    """Fixture: returns only booking ID"""

    booking_data = get_valid_booking_data()
    response = booking_api.create_booking(booking_data)
    booking_id = response.json()["bookingid"]

    yield booking_id

    try:
        auth = AuthAPI()
        token = auth.get_token(TEST_USER_EMAIL, TEST_USER_PASSWORD)
        booking_api.delete_booking(booking_id, token)
    except requests.exceptions.RequestException:
        pass


@pytest.fixture
def test_booking_with_data(booking_api):
    """Fixture: returns (booking_id, booking_data)"""

    booking_data = get_valid_booking_data()
    response = booking_api.create_booking(booking_data)
    booking_id = response.json()["bookingid"]

    yield booking_id, booking_data

    try:
        auth = AuthAPI()
        token = auth.get_token(TEST_USER_EMAIL, TEST_USER_PASSWORD)
        booking_api.delete_booking(booking_id, token)
    except requests.exceptions.RequestException:
        pass
