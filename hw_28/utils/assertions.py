from jsonschema import validate


# Check status code
def assert_status_code(response, expected_code):
    """Check status code"""
    assert response.status_code == expected_code, \
        f"Expected status {expected_code}, got {response.status_code}. Response: {response.text}"
    return True


# Check JSON schema
def assert_json_schema(response, schema):
    validate(instance=response.json(), schema=schema)
    return True


# Check if response has a specific key
def assert_response_has_key(response, key):
    assert key in response.json(), f"Key '{key}' not found in response"
    return True
