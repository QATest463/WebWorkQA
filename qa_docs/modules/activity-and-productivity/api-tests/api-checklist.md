# Activity and Productivity Module – API Checklist

| №  | Check Item                                             | Type        | Priority | Status |
|----|---------------------------------------------------------|-------------|----------|--------|
| 1  | Start activity tracking                                 | Functional  | High     |        |
| 2  | Stop activity tracking                                  | Functional  | High     |        |
| 3  | Retrieve activity logs                                  | Functional  | High     |        |
| 4  | Record active and idle time                             | Functional  | High     |        |
| 5  | Track app usage                                         | Functional  | High     |        |
| 6  | Track website usage                                     | Functional  | High     |        |
| 7  | Categorize apps/websites                                | Functional  | Medium   |        |
| 8  | Retrieve productivity summary                           | Functional  | Medium   |        |
| 9  | Export productivity data                                | Functional  | Medium   |        |
| 10 | Unauthorized access to endpoints returns 401            | Security    | High     |        |
| 11 | Role-based permissions enforced for managers            | Security    | High     |        |
| 12 | Validation against tampered activity IDs                | Security    | High     |        |
| 13 | Secure storage and transmission of activity logs        | Security    | High     |        |
| 14 | Enforce HTTPS-only connections                          | Security    | High     |        |
| 15 | Invalid request body returns validation error           | Negative    | Medium   |        |
| 16 | Attempt to modify another user's activity data          | Negative    | Medium   |        |
| 17 | Upload unsupported file format for categorization       | Negative    | Medium   |        |
| 18 | Large activity log retrieval with pagination            | Performance | Medium   |        |
| 19 | Start/stop tracking response time acceptable            | Performance | Medium   |        |
| 20 | Export large productivity data performance acceptable   | Performance | Medium   |        |

> 🔹 **Type:** Functional, Security, Negative, Performance  
> 🔸 **Priority:** High, Medium, Low  
> 🔘 **Status:** To be filled during testing