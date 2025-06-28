# Negative Test Cases – User Onboarding & Welcome Flow Module

| ID          | Title                                       | Precondition                        | Steps                                                         | Expected Result                           | Actual Result | Status |
|-------------|---------------------------------------------|-------------------------------------|---------------------------------------------------------------|-------------------------------------------|---------------|--------|
| UOWF-NT-001 | Registration with existing email             | None                                | 1. Enter email already in use <br> 2. Submit form | Error message: Email already registered |               |        |
| UOWF-NT-002 | Registration with invalid email format       | None                                | 1. Enter invalid email <br> 2. Submit form | Error message: Invalid email |               |        |
| UOWF-NT-003 | Weak password rejected                       | None                                | 1. Enter weak password <br> 2. Submit form | Error message: Password requirements not met |               |        |
| UOWF-NT-004 | Bypassing email verification                  | User registered but unverified      | 1. Attempt login without verifying email | Login blocked, error message shown |               |        |
| UOWF-NT-005 | Broken verification link                      | User registered                     | 1. Open expired/altered link | Error page or message displayed |               |        |
| UOWF-NT-006 | Registration form submission with empty fields| None                                | 1. Leave required fields blank <br> 2. Submit form | Validation errors shown, submission blocked |               |        |
| UOWF-NT-007 | Multiple rapid registration attempts         | None                                | 1. Submit form multiple times quickly | Rate limiting error or blocking |               |        |