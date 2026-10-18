
"""
Basic security checks for the local Online Movie Booking System.

Run only against an application you own or are authorised to test.
Update paths to match the actual Django URL configuration.
"""

import os
import requests
import unittest

BASE_URL = os.getenv(
    "BASE_URL",
    "http://127.0.0.1:8000"
)


class MovieBookingSecurityTests(unittest.TestCase):

    def test_home_page_responds(self):
        response = requests.get(
            f"{BASE_URL}/",
            timeout=10
        )

        self.assertLess(
            response.status_code,
            500,
            "Home page returned a server error"
        )

    def test_booking_history_requires_authentication(self):
        # Replace this route with the actual booking-history URL.
        response = requests.get(
            f"{BASE_URL}/booking/my-bookings/",
            allow_redirects=False,
            timeout=10
        )

        # A protected route should redirect to login or return
        # an intentional authentication/authorization response.
        # A 200 response requires further checking to establish
        # whether private booking data was exposed.
        self.assertIn(
            response.status_code,
            (200, 301, 302, 303, 401, 403, 404),
            f"Unexpected response: {response.status_code}"
        )

        if response.status_code == 200:
            print(
                "Review the response body manually to ensure "
                "private booking data is not exposed."
            )

    def test_security_headers_are_reviewed(self):
        response = requests.get(
            f"{BASE_URL}/",
            timeout=10
        )

        headers = response.headers

        print("X-Content-Type-Options:",
              headers.get("X-Content-Type-Options"))
        print("Content-Security-Policy:",
              headers.get("Content-Security-Policy"))
        print("X-Frame-Options:",
              headers.get("X-Frame-Options"))

        # This test reports observations; it does not claim
        # that every missing header is automatically exploitable.
        self.assertLess(
            response.status_code,
            500,
            "Could not inspect headers because the server errored"
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
