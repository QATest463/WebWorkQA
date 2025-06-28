# Performance Module – API Checklist

| №  | Check Item                                             | Type        | Priority | Status |
|----|---------------------------------------------------------|-------------|----------|--------|
| 1  | Measure API response time under normal load           | Functional  | High     |        |
| 2  | Measure API response time under peak load             | Functional  | High     |        |
| 3  | Handle large payloads gracefully                      | Functional  | Medium   |        |
| 4  | Rate limiting enforced on critical APIs               | Security    | High     |        |
| 5  | Protect against DoS attacks via APIs                  | Security    | High     |        |
| 6  | Secure resource allocation under API stress           | Security    | High     |        |
| 7  | Enforce HTTPS-only connections                        | Security    | High     |        |
| 8  | Handle simultaneous high-volume API requests          | Performance | High     |        |
| 9  | Maintain SLA on critical endpoints                    | Performance | High     |        |
| 10 | Resource usage monitoring during stress tests         | Performance | High     |        |

> 🔹 **Type:** Functional, Security, Performance  
> 🔸 **Priority:** High, Medium, Low  
> 🔘 **Status:** To be filled during testing