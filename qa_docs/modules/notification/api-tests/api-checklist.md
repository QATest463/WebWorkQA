# Notification Module – API Checklist

| №  | Check Item                                             | Type        | Priority | Status |
|----|---------------------------------------------------------|-------------|----------|--------|
| 1  | Retrieve all notifications                             | Functional  | High     |        |
| 2  | Retrieve unread notifications                          | Functional  | High     |        |
| 3  | Mark notification as read/unread                       | Functional  | High     |        |
| 4  | Delete single notification                             | Functional  | High     |        |
| 5  | Bulk delete notifications                              | Functional  | High     |        |
| 6  | Filter notifications by type or status                 | Functional  | Medium   |        |
| 7  | Search notifications                                   | Functional  | Medium   |        |
| 8  | Notification settings/preferences retrieval            | Functional  | Medium   |        |
| 9  | Unauthorized access to endpoints returns 401           | Security    | High     |        |
| 10 | Role-based permissions enforced for certain notifications | Security  | High     |        |
| 11 | Validation against tampered notification IDs           | Security    | High     |        |
| 12 | Enforce HTTPS-only connections                         | Security    | High     |        |
| 13 | Invalid request body returns validation error          | Negative    | Medium   |        |
| 14 | Attempt to delete non-existent notification            | Negative    | Medium   |        |
| 15 | Attempt to mark another user's notification as read    | Negative    | Medium   |        |
| 16 | Retrieve large data set with pagination                | Performance | Medium   |        |
| 17 | Bulk deletion operation performance acceptable         | Performance | Medium   |        |
| 18 | Filter and search response time acceptable             | Performance | Medium   |        |

> 🔹 **Type:** Functional, Security, Negative, Performance  
> 🔸 **Priority:** High, Medium, Low  
> 🔘 **Status:** To be filled during testing