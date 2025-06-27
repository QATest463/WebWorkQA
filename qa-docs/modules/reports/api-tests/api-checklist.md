# Reports Module – API Checklist

| №  | Check Item                                             | Type        | Priority | Status |
|----|---------------------------------------------------------|-------------|----------|--------|
| 1  | Retrieve available report types returns 200             | Functional  | High     |        |
| 2  | Generate time tracking report with valid filters        | Functional  | High     |        |
| 3  | Generate billing report with valid filters              | Functional  | High     |        |
| 4  | Apply date range filters returns correct data           | Functional  | High     |        |
| 5  | Export report to PDF returns valid file                 | Functional  | High     |        |
| 6  | Export report to CSV returns valid file                 | Functional  | High     |        |
| 7  | Schedule automated report is saved correctly            | Functional  | Medium   |        |
| 8  | Invalid filters return validation error                 | Negative    | High     |        |
| 9  | Empty data range returns "No data" message              | Negative    | Medium   |        |
| 10 | Unauthorized access returns 401                         | Security    | High     |        |
| 11 | Role-based access enforced for reports data             | Security    | High     |        |
| 12 | Secure download/export links require auth               | Security    | High     |        |
| 13 | Enforce HTTPS-only connections                          | Security    | High     |        |
| 14 | Rate limiting on report generation endpoint             | Security    | Medium   |        |
| 15 | Report generation response time under threshold         | Performance | Medium   |        |
| 16 | High concurrency generation is supported                | Performance | Medium   |        |
| 17 | Export endpoints respond within acceptable time         | Performance | Medium   |        |

> 🔹 **Type:** Functional, Security, Negative, Performance  
> 🔸 **Priority:** High, Medium, Low  
> 🔘 **Status:** To be filled during testing