# ✅ Functional Checklist – Authentication Module

| №  | Check Item                                                                                 | Type        | Priority | Status |
|----|--------------------------------------------------------------------------------------------|-------------|----------|--------|
| 1  | User can register with valid details (First Name, Last Name, Email, Password)              | Functional  | High     |        |
| 2  | First and last name fields enforce 1–36 characters limit                                   | Functional  | High     |        |
| 3  | Email field validates proper email format                                                  | Functional  | High     |        |
| 4  | Password field validates: 8–36 chars, upper & lowercase, at least one number               | Functional  | High     |        |
| 5  | Password and confirm password must match                                                   | Functional  | High     |        |
| 6  | User can register via Google                                                               | Functional  | High     |        |
| 7  | User can register via Slack                                                                | Functional  | Medium   |        |
| 8  | Owner is redirected to onboarding after registration                                       | Functional  | Medium   |        |
| 9  | Member can register via email invitation                                                   | Functional  | High     |        |
| 10 | Member can register via direct invite link                                                 | Functional  | High     |        |
| 11 | Member can register via Slack integration                                                  | Functional  | Medium   |        |
| 12 | User can log in with valid email and password                                              | Functional  | High     |        |
| 13 | User is redirected to dashboard after successful login                                     | Functional  | High     |        |
| 14 | System prevents login with incorrect credentials                                           | Functional  | High     |        |
| 15 | System prompts for two-factor authentication if workspace requires it                      | Functional  | High     |        |
| 16 | Login works for all roles (Owner, Executive Manager, etc.)                                 | Functional  | Medium   |        |
| 17 | “Remember Me” checkbox retains session after browser/tab close (if checked)                | Functional  | Medium   |        |
| 18 | User is logged out after browser close if “Remember Me” is unchecked                       | Functional  | Medium   |        |
| 19 | User is automatically logged out when token expires                                        | Functional  | Medium   |        |
| 20 | “Forgot Password?” link navigates to password recovery page                                | Functional  | Medium   |        |
| 21 | System sends password reset email after entering valid email                               | Functional  | Medium   |        |
| 22 | User receives and opens valid password reset link                                          | Functional  | Medium   |        |
| 23 | User can reset password using reset link                                                   | Functional  | High     |        |
| 24 | Login with new password works after reset                                                  | Functional  | High     |        |
| 25 | Login/register pages are accessible by all browsers                                        | Functional  | Medium   |        |
| 26 | System blocks duplicate email registrations                                                | Functional  | High     |        |
| 27 | System shows validation error for missing or invalid required fields                       | Functional  | High     |        |
| 28 | All successful form submissions result in success messages or page redirects               | Functional  | Medium   |        |
| 29 | Registration/login/logout flows work consistently across roles and methods                 | Functional  | High     |        |
| 30 | User sessions persist until logout or token expiration                                     | Functional  | Medium   |        |