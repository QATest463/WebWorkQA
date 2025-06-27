# Timesheet Module – API Checklist

| №  | Check Item                                             | Type        | Priority | Status |
|----|---------------------------------------------------------|-------------|----------|--------|
| 1  | Retrieve personal timesheet entries                     | Functional  | High     |        |
| 2  | Retrieve team timesheet entries (Manager)                | Functional  | High     |        |
| 3  | Filter entries by date range, project, user              | Functional  | High     |        |
| 4  | Add manual time entry                                    | Functional  | High     |        |
| 5  | Edit manual time entry                                   | Functional  | High     |        |
| 6  | Delete manual time entry                                 | Functional  | High     |        |
| 7  | Approve timesheet entry (Manager)                        | Functional  | High     |        |
| 8  | Reject timesheet entry (Manager)                         | Functional  | High     |        |
| 9  | Export timesheet to CSV/PDF                              | Functional  | Medium   |        |
| 10 | Unauthorized access to endpoints returns 401             | Security    | High     |        |
| 11 | Role-based permissions enforced for viewing/approvals    | Security    | High     |        |
| 12 | Validation against tampered time entry IDs               | Security    | High     |        |
| 13 | Secure export/download links require authentication      | Security    | High     |        |
| 14 | Enforce HTTPS-only connections                           | Security    | High     |        |
| 15 | Invalid request body returns validation error            | Negative    | Medium   |        |
| 16 | Attempt to edit/delete non-existent entry                | Negative    | Medium   |        |
| 17 | Attempt to approve/reject without permissions            | Negative    | Medium   |        |
| 18 | Retrieve large data set with pagination                  | Performance | Medium   |        |
| 19 | Bulk approval operation performance acceptable           | Performance | Medium   |        |
| 20 | Rapid repeated filter/pagination changes handled well    | Performance | Medium   |        |

> 🔹 **Type:** Functional, Security, Negative, Performance  
> 🔸 **Priority:** High, Medium, Low  
> 🔘 **Status:** To be filled during testing