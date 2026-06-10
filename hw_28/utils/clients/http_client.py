import requests
from hw_28.settings import BASE_URL, DEFAULT_HEADERS, TIMEOUT


class HTTPClient:
    def __init__(self):
        self.base_url = BASE_URL
        self.default_headers = DEFAULT_HEADERS.copy()
        self.timeout = TIMEOUT

    # Header + token
    def _get_headers(self, token=None):
        headers = self.default_headers.copy()
        if token:
            headers["Cookie"] = f"token={token}"
        return headers

    # Base URL + endpoint
    def _build_url(self, endpoint):
        return f"{self.base_url}{endpoint}"

    # GET method
    def get(self, endpoint, params=None, token=None):
        url = self._build_url(endpoint)
        headers = self._get_headers(token)
        return requests.get(url, params=params, headers=headers, timeout=self.timeout)

    # POST method
    def post(self, endpoint, data=None, token=None):
        url = self._build_url(endpoint)
        headers = self._get_headers(token)
        return requests.post(url, json=data, headers=headers, timeout=self.timeout)

    # PUT method
    def put(self, endpoint, data=None, token=None):
        url = self._build_url(endpoint)
        headers = self._get_headers(token)
        return requests.put(url, json=data, headers=headers, timeout=self.timeout)

    # PATCH method
    def patch(self, endpoint, data=None, token=None):
        url = self._build_url(endpoint)
        headers = self._get_headers(token)
        return requests.patch(url, json=data, headers=headers, timeout=self.timeout)

    # DELETE method
    def delete(self, endpoint, token=None):
        url = self._build_url(endpoint)
        headers = self._get_headers(token)
        return requests.delete(url, headers=headers, timeout=self.timeout)
