# Time Tracking Module Checklist

| №  | Check Item                                              | Type                   | Priority | Status |
|----|----------------------------------------------------------|------------------------|----------|--------|
| 1  | Start time tracking                                      | Functional             | High     |        |
| 2  | Stop time tracking                                       | Functional             | High     |        |
| 3  | Pause/resume time tracking                               | Functional             | High     |        |
| 4  | Switch between projects/tasks while tracking             | Functional             | High     |        |
| 5  | View live tracked time                                   | Functional             | High     |        |
| 6  | Add manual time entry                                    | Functional             | High     |        |
| 7  | Edit manual time entry                                   | Functional             | High     |        |
| 8  | Delete manual time entry                                 | Functional             | High     |        |
| 9  | View daily/weekly/monthly summaries                      | Functional             | Medium   |        |
| 10 | Integration with Timesheet                               | Functional             | High     |        |
| 11 | Unauthorized access blocked                              | Security & Access      | High     |        |
| 12 | Only authenticated users can track time                  | Security & Access      | High     |        |
| 13 | Role-based access enforced for manual entries            | Security & Access      | High     |        |
| 14 | User can only edit/delete own manual entries             | Security & Access      | High     |        |
| 15 | Validation against tampered requests                     | Security & Access      | High     |        |
| 16 | Enforce HTTPS-only connections                           | Security & Access      | High     |        |
| 17 | Starting multiple timers simultaneously blocked          | Negative & Edge Case   | Medium   |        |
| 18 | Overlapping manual and automatic entries blocked         | Negative & Edge Case   | Medium   |        |
| 19 | Rapidly switching projects/tasks handled gracefully      | Edge Case              | Medium   |        |
| 20 | Network disconnect/reconnect while tracking handled      | Edge Case              | Medium   |        |
| 21 | Long-running timer session handled correctly             | Edge Case              | Medium   |        |
| 22 | Bulk deletion of manual entries works correctly          | Edge Case              | Medium   |        |
| 23 | Viewing large number of time entries handled correctly   | Edge Case              | Medium   |        |
| 24 | Clear, readable timer widget                             | UI/UX                  | Medium   |        |
| 25 | Responsive design on mobile devices                      | UI/UX                  | Medium   |        |
| 26 | Easy-to-use start/stop/pause/resume controls             | UI/UX                  | Medium   |        |
| 27 | Manual entry form is intuitive                           | UI/UX                  | Medium   |        |
| 28 | Confirmation dialogs for deletions                       | UI/UX                  | High     |        |
| 29 | Loading indicators during operations                     | UI/UX                  | Medium   |        |
| 30 | Error messages for validation failures                    | UI/UX                  | High     |        |
| 31 | Accessibility for keyboard navigation                    | UI/UX                  | Medium   |        |
| 32 | Consistent styling across browsers                       | UI/UX                  | Medium   |        |
| 33 | Time Tracking page load time acceptable                   | Performance            | Medium   |        |
| 34 | Timer start/stop response time acceptable                 | Performance            | Medium   |        |
| 35 | Pause/resume timer response time acceptable               | Performance            | Medium   |        |
| 36 | Add/edit/delete manual entry operation time acceptable    | Performance            | Medium   |        |
| 37 | View large number of entries without performance issues   | Performance            | Medium   |        |
| 38 | Switch projects/tasks during tracking acceptable          | Performance            | Medium   |        |
| 39 | Rapid repeated start/stop actions handled gracefully      | Performance            | Medium   |        |

> 🔹 **Type:** Functional, Negative & Edge Case, UI/UX, Security & Access, Performance  
> 🔸 **Priority:** High, Medium, Low  
> 🔘 **Status:** To be filled during testing