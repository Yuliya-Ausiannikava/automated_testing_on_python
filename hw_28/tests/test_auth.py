"""Tests for authentication API"""

from utils.logger import logger
from utils.assertions import assert_status_code, assert_json_schema, assert_response_has_key
from utils.schemas.auth_schema import AUTH_SCHEMA
from config.settings import TEST_USER_EMAIL, TEST_USER_PASSWORD


class TestAuth:
    # Positive test: valid credentials
    def test_auth_valid_credentials(self, auth_api):
        logger.info("Testing authentication with valid credentials")

        response = auth_api.auth(TEST_USER_EMAIL, TEST_USER_PASSWORD)
        assert_status_code(response, 200)
        assert_response_has_key(response, "token")
        assert_json_schema(response, AUTH_SCHEMA)

        token = response.json()["token"]
        assert len(token) > 0

        logger.info("Token received: %s", token)
        logger.info("Authentication with valid data test passed")

    # Negative test: invalid credentials
    def test_auth_invalid_credentials(self, auth_api):
        logger.info("Testing authentication with invalid credentials")

        response = auth_api.auth("invalid_user", "invalid_password")

        assert_status_code(response, 200)
        assert response.json().get("reason") == "Bad credentials"

        logger.info("Invalid credentials correctly rejected")
        logger.info("Authentication with invalid data test passed")

    # Negative test: empty credentials
    def test_auth_empty_credentials(self, auth_api):
        logger.info("Test: empty credentials")

        response = auth_api.auth("", "")

        assert_status_code(response, 200)
        assert response.json().get("reason") == "Bad credentials"

        logger.info("Empty credentials correctly rejected")
        logger.info("Authentication with empty credentials test passed")
