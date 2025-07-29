# Time Tracking Module – API Checklist

| №  | Check Item                                           | Type        | Priority | Status |
|----|------------------------------------------------------|-------------|----------|--------|
| 1  | Start time tracking                                  | Positive    | High     |        |
| 2  | Stop time tracking                                   | Positive    | High     |        |
| 3  | Pause/resume time tracking                           | Positive    | High     |        |
| 4  | Switch between projects/tasks while tracking         | Positive    | High     |        |
| 5  | Retrieve live tracked time                           | Positive    | High     |        |
| 6  | Add manual time entry                                | Positive    | High     |        |
| 7  | Edit manual time entry                               | Positive    | High     |        |
| 8  | Delete manual time entry                             | Positive    | High     |        |
| 9  | Retrieve time entries with filters and pagination    | Positive    | High     |        |
| 10 | Unauthorized access to endpoints returns 401         | Security    | High     |        |
| 11 | Role-based permissions enforced for manual entries   | Security    | High     |        |
| 12 | Validation against tampered time entry IDs           | Security    | High     |        |
| 13 | Enforce HTTPS-only connections                       | Security    | High     |        |
| 14 | Invalid request body returns validation error        | Negative    | Medium   |        |
| 15 | Attempt to start timer without project/task          | Negative    | Medium   |        |
| 16 | Attempt to edit/delete non-existent entry            | Negative    | Medium   |        |
| 17 | Retrieve large data set with pagination              | Performance | Medium   |        |
| 18 | Rapid repeated start/stop actions handled well       | Performance | Medium   |        |
| 19 | Switch projects/tasks during tracking acceptable     | Performance | Medium   |        |

> 🔹 **Type:** Functional, Security, Negative, Performance  
> 🔸 **Priority:** High, Medium, Low  
> 🔘 **Status:** To be filled during testing