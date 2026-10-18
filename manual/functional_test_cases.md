# Manual Functional Acceptance Test Cases

**Target:** local Online Movie Booking System  
**Tester:** Syed Suleman Uddin Farhad Syed  
**Environment/date:** fill in only after the actual run.

| ID | Scenario | Expected result | Actual result | Status | Evidence filename |
|---|---|---|---|---|---|
| FT-M01 | Open home page | Home page loads without an unhandled error | To record | Not run | |
| FT-M02 | Search for `Venom` | Matching movie is displayed if present in fixture data | To record | Not run | |
| FT-M03 | Search for a nonexistent title | Clear empty-state message appears | To record | Not run | |
| FT-M04 | Register with a unique test email | Account is created or next step is clearly shown | To record | Not run | |
| FT-M05 | Register with duplicate test email | Duplicate account is rejected with useful feedback | To record | Not run | |
| FT-M06 | Try a weak password such as `123` using a disposable test account | Weak password is rejected with guidance | To record | Not run | |
| FT-M07 | Open My Bookings while signed in | Current user's bookings are shown | To record | Not run | |
| FT-M08 | Open My Bookings while signed out | Redirect to sign-in or intentional 401/403; no traceback | To record | Not run | |
| FT-M09 | Attempt to book an already-booked seat in test data | Server rejects duplicate booking and explains why | To record | Not run | |

Use only test accounts and test data. Never use real passwords or payment details. Record `Blocked` when a test cannot run due to missing data/environment; do not mark it passed.
