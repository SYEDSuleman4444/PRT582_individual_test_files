"""
Conservative starter Locust scenario for a local Django movie-booking app.
Inspect actual URLs and authentication requirements before using.
Only run against systems you own or are authorised to test.
"""
from locust import HttpUser, task, between

class MovieBookingUser(HttpUser):
    wait_time = between(1, 3)

    @task(4)
    def home(self):
        self.client.get("/", name="GET home")

    @task(3)
    def movie_list(self):
        # Adjust this route to the real movie-list URL in the application.
        self.client.get("/movie/", name="GET movie list", allow_redirects=True)

    @task(2)
    def search(self):
        # Adjust query parameter/path to match the app's actual search form.
        self.client.get("/movie/?q=Venom", name="GET search", allow_redirects=True)

    @task(1)
    def booking_history_without_login(self):
        # This intentionally checks unauthenticated behaviour only on local test data.
        # A secure app should redirect to login or return an intentional 401/403,
        # not expose a traceback or return an unhandled HTTP 500.
        with self.client.get(
            "/booking/my-bookings/",
            name="GET booking history (logged out)",
            allow_redirects=False,
            catch_response=True,
        ) as response:
            if response.status_code == 500:
                response.failure("HTTP 500 for logged-out booking-history request")
            elif response.status_code in (200, 302, 401, 403, 404):
                response.success()
            else:
                response.failure(f"Unexpected status: {response.status_code}")
