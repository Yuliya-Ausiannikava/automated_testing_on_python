"""Test data generator"""

from datetime import datetime, timedelta


# Get valid booking data
def get_valid_booking_data():
    return {
        "firstname": "John",
        "lastname": "Smith",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d"),
            "checkout": (datetime.now() + timedelta(days=5)).strftime("%Y-%m-%d")
        },
        "additionalneeds": "Breakfast"
    }


# Get data for full update
def get_updated_booking_data():
    return {
        "firstname": "Updated",
        "lastname": "Name",
        "totalprice": 999,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2025-01-01",
            "checkout": "2025-01-10"
        },
        "additionalneeds": "Dinner"
    }


# Get data for partial update
def get_partial_update_data():
    return {
        "firstname": "PartiallyUpdated",
        "totalprice": 777
    }


# Get invalid booking data for negative tests
def get_invalid_booking_data():
    return {
        "firstname": "John",
        # lastname is missing (required field)
        "totalprice": "not_a_number",
        "depositpaid": "yes",
        "bookingdates": {
            "checkin": "invalid-date",
            "checkout": "invalid-date"
        }
    }


# Get booking data without required fields
def get_booking_without_required_fields():
    return {
        "firstname": "John"
        # missing lastname, totalprice, depositpaid, bookingdates
    }
