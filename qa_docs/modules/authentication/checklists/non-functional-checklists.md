# 🧪 Non-Functional Checklist – Authentication Module

| №  | Check Item                                                                    | Type           | Priority | Status |
|----|-------------------------------------------------------------------------------|----------------|----------|--------|
| 1  | Login, registration, and reset pages are mobile responsive                    | UI/UX          | Medium   |        |
| 2  | Login and reset forms are accessible via keyboard                             | Accessibility  | Medium   |        |
| 3  | Registration and login forms support screen reader labels                     | Accessibility  | Medium   |        |
| 4  | Helpful error messages are shown for invalid input                            | Usability      | High     |        |
| 5  | Password input field has show/hide toggle                                     | Usability      | Low      |        |
| 6  | Registration/login pages use HTTPS only                                       | Security       | High     |        |
| 7  | Password is stored using hashing (e.g., bcrypt, SHA)                          | Security       | High     |        |
| 8  | Token expiration is handled gracefully (user logged out, session expired msg) | Security       | Medium   |        |
| 9  | Login page load time is under 2 seconds                                       | Performance    | Medium   |        |
| 10 | Mail delivery for password reset takes less than 5 seconds                    | Performance    | Low      |        |
| 11 | Registration/login forms handle slow network without breaking                 | Performance    | Medium   |        |
| 12 | Rate limiting is enforced on login attempts                                   | Security       | High     |        |
| 13 | CAPTCHA or bot protection (if any) is working correctly                       | Security       | Medium   |        |