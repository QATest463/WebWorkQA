# Authentication Module Checklist

| №  | Check Item                                             | Type                    | Priority | Status |
|----|---------------------------------------------------------|-------------------------|----------|--------|
| 1  | User can register with valid credentials                | Functional              | High     |        |
| 2  | Duplicate email registration is blocked                 | Functional              | High     |        |
| 3  | User can log in with valid credentials                  | Functional              | High     |        |
| 4  | User cannot log in with invalid credentials             | Functional              | High     |        |
| 5  | Forgot Password flow sends email                        | Functional              | High     |        |
| 6  | Password can be reset with valid link                   | Functional              | High     |        |
| 7  | User can log out successfully                           | Functional              | High     |        |
| 8  | Session persists after page refresh                     | Functional              | Medium   |        |
| 9  | Session expires after inactivity timeout                | Functional              | High     |        |
| 10 | Social login (Google, Facebook) works as expected       | Functional              | Medium   |        |
| 11 | Registration with invalid email format is blocked       | Negative & Edge Case    | High     |        |
| 12 | Blank fields show proper validation errors              | Negative & Edge Case    | High     |        |
| 13 | Rate limiting / account lockout after failed logins     | Security & Access       | High     |        |
| 14 | Password with max length and special characters accepted | Negative & Edge Case    | Medium   |        |
| 15 | Multiple concurrent sessions handled correctly          | Negative & Edge Case    | Medium   |        |
| 16 | Expired password reset link is rejected                 | Negative & Edge Case    | High     |        |
| 17 | Prevent registration when already logged in             | Negative & Edge Case    | Medium   |        |
| 18 | Password visibility toggle works                        | UI/UX                   | Medium   |        |
| 19 | Error messages are clear and specific                   | UI/UX                   | High     |        |
| 20 | Forms are responsive on all devices                     | UI/UX                   | Medium   |        |
| 21 | Input validation highlights incorrect fields            | UI/UX                   | High     |        |
| 22 | Forgot Password link is visible                         | UI/UX                   | High     |        |
| 23 | Styling is consistent across browsers                   | UI/UX                   | Medium   |        |
| 24 | Rate limiting enforced on login                         | Security & Access       | High     |        |
| 25 | Tokens expire after inactivity                          | Security & Access       | High     |        |
| 26 | Secure cookie flags set (HttpOnly, Secure)              | Security & Access       | High     |        |
| 27 | Protected routes inaccessible without login             | Security & Access       | High     |        |
| 28 | 2FA works as expected                                   | Security & Access       | High     |        |
| 29 | Logout invalidates session/token                        | Security & Access       | High     |        |
| 30 | Login responds within acceptable time (<1 second)       | Performance             | Medium   |        |
| 31 | Signup handles high concurrency                         | Performance             | Medium   |        |
| 32 | Password reset email arrives quickly                    | Performance             | Medium   |        |
| 33 | Rate limiting does not block valid users                | Performance             | Medium   |        |
| 34 | Login performs well under peak load                     | Performance             | Medium   |        |

> 🔹 **Type:** Functional, UI/UX, Negative & Edge Case, Performance, Security & Access  
> 🔸 **Priority:** High, Medium, Low  
> 🔘 **Status:** To be filled during testing (e.g. Pass, Fail, Blocked)