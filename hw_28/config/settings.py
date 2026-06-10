import os
from dotenv import load_dotenv

load_dotenv()

# API setting and auth credentials
ENVIRONMENT = os.getenv("ENVIRONMENT", "dev")
BASE_URL = os.getenv("BASE_URL", "https://restful-booker.herokuapp.com")
TIMEOUT = int(os.getenv("TIMEOUT", "10"))
TEST_USER_EMAIL = os.getenv("TEST_USER_EMAIL", "admin")
TEST_USER_PASSWORD = os.getenv("TEST_USER_PASSWORD", "password123")

DEFAULT_HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}
