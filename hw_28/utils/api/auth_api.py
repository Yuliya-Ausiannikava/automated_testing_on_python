"""
Class for working with authentication API
"""

from hw_28.utils.clients.http_client import HTTPClient
from hw_28.utils.routes import APIRoutes
from hw_28.settings import TEST_USER_EMAIL, TEST_USER_PASSWORD
from hw_28.utils.logger import logger


class AuthAPI:
    def __init__(self):
        self.client = HTTPClient()
        logger.debug("AuthAPI initialized")

    def auth(self, username=None, password=None):
        if username is None:
            username = TEST_USER_EMAIL
        if password is None:
            password = TEST_USER_PASSWORD

        logger.debug("User authorization attempt:  %s", username)
        data = {
            "username": username,
            "password": password
        }

        return self.client.post(APIRoutes.AUTH, data)

    def get_token(self, username=None, password=None):
        response = self.auth(username, password)
        json_response = response.json()

        logger.debug("Server response: %s", json_response)

        assert response.status_code == 200, f"Auth failed: {response.status_code}"
        assert json_response.get('token'), "Token not in response"

        token = json_response['token']
        logger.info("Token received: %s", token)

        return token
