# Authentication Module – API Checklist

| №  | Check Item                                     | Type        | Priority | Status |
|----|-------------------------------------------------|-------------|----------|--------|
| 1  | Login endpoint returns 200 with valid credentials | Functional  | High     |        |
| 2  | Login endpoint returns 401 with invalid credentials | Functional  | High     |        |
| 3  | Registration endpoint creates user with valid data | Functional  | High     |        |
| 4  | Registration endpoint rejects duplicate email   | Functional  | High     |        |
| 5  | Password reset request returns 200 with valid email | Functional  | High     |        |
| 6  | Password reset link invalid after use            | Security    | High     |        |
| 7  | Login endpoint enforces rate limiting            | Security    | High     |        |
| 8  | All sensitive data sent over HTTPS               | Security    | High     |        |
| 9  | SQL injection attempts in payload are blocked    | Security    | High     |        |
| 10 | Registration with invalid email format fails     | Negative    | Medium   |        |
| 11 | Login with empty fields returns 400              | Negative    | Medium   |        |
| 12 | Password reset with invalid token returns 400/401 | Negative    | Medium   |        |
| 13 | Rate limiting doesn't block valid requests       | Performance | Medium   |        |
| 14 | Login endpoint responds <1s under normal load    | Performance | Medium   |        |
| 15 | Registration handles high concurrency            | Performance | Medium   |        |

> 🔹 **Type:** Functional, Security, Negative, Performance  
> 🔸 **Priority:** High, Medium, Low  
> 🔘 **Status:** To be filled during testing