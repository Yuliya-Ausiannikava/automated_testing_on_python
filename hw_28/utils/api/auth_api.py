"""
Class for working with authentication API
"""

from utils.clients.http_client import HTTPClient
from utils.logger import logger
from config.settings import TEST_USER_EMAIL, TEST_USER_PASSWORD


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

        return self.client.post('/auth', data)

    def get_token(self, username=None, password=None):
        response = self.auth(username, password)
        json_response = response.json()

        logger.debug("Server response: %s", json_response)

        assert response.status_code == 200, f"Auth failed: {response.status_code}"
        assert json_response.get('token'), "Token not in response"

        token = json_response['token']
        logger.info("Token received: %s", token)

        return token
