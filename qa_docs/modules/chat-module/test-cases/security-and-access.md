# Security and Access Test Cases – Chat Module

| ID          | Title                                       | Precondition                        | Steps                                                         | Expected Result                           | Actual Result | Status |
|-------------|---------------------------------------------|-------------------------------------|---------------------------------------------------------------|-------------------------------------------|---------------|--------|
| CH-SA-001   | Authentication required to access chat      | None                                | 1. Open app without login <br> 2. Try to access chat | Redirected to login screen |               |        |
| CH-SA-002   | Secure transmission (HTTPS)                 | User logged in                      | 1. Send/receive message <br> 2. Inspect network traffic | Data sent over HTTPS only |               |        |
| CH-SA-003   | Access control for team members only        | User logged in                      | 1. Attempt to access chat outside team <br> 2. Observe behavior | Access denied with error |               |        |
| CH-SA-004   | Message content sanitized                   | User logged in                      | 1. Send message with HTML/JS code <br> 2. Observe rendering | Content displayed safely, no XSS |               |        |
| CH-SA-005   | Rate limiting to prevent spam               | User logged in                      | 1. Send many messages rapidly <br> 2. Observe system | Rate limit enforced or warning shown |               |        |