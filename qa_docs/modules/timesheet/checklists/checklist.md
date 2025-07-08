# Timesheet Module Checklist

| №  | Check Item                                              | Type                   | Priority | Status |
|----|----------------------------------------------------------|------------------------|----------|--------|
| 1  | View personal timesheet                                  | Functional             | High     |        |
| 2  | View team timesheets (for managers)                      | Functional             | High     |        |
| 3  | Filter by date range, user, project                      | Functional             | High     |        |
| 4  | Add manual time entry                                    | Functional             | High     |        |
| 5  | Edit manual time entry                                   | Functional             | High     |        |
| 6  | Delete manual time entry                                 | Functional             | High     |        |
| 7  | Approve timesheet entry (Manager)                        | Functional             | High     |        |
| 8  | Reject timesheet entry (Manager)                         | Functional             | High     |        |
| 9  | Export timesheet to CSV                                  | Functional             | Medium   |        |
| 10 | Export timesheet to PDF                                  | Functional             | Medium   |        |
| 11 | Unauthorized access blocked                              | Security & Access      | High     |        |
| 12 | Role-based access enforced                               | Security & Access      | High     |        |
| 13 | Validation against tampered IDs                          | Security & Access      | High     |        |
| 14 | Secure export/download links require authentication      | Security & Access      | High     |        |
| 15 | Enforce HTTPS-only connections                           | Security & Access      | High     |        |
| 16 | Empty timesheet period handled gracefully                | Negative & Edge Case   | Medium   |        |
| 17 | Invalid form submissions blocked                         | Negative & Edge Case   | Medium   |        |
| 18 | Overlapping time entries blocked                         | Edge Case              | Medium   |        |
| 19 | Concurrent edits handled gracefully                      | Edge Case              | Medium   |        |
| 20 | Very large number of entries handled correctly           | Edge Case              | Medium   |        |
| 21 | Bulk approval works correctly                            | Edge Case              | Medium   |        |
| 22 | Rapid repeated filter changes handled gracefully         | Edge Case              | Medium   |        |
| 23 | Clear, readable timesheet table                          | UI/UX                  | Medium   |        |
| 24 | Responsive design on mobile devices                      | UI/UX                  | Medium   |        |
| 25 | Filter controls easy to use and accessible               | UI/UX                  | Medium   |        |
| 26 | Intuitive forms for adding/editing entries               | UI/UX                  | Medium   |        |
| 27 | Confirmation dialogs for deletion/approval               | UI/UX                  | High     |        |
| 28 | Loading indicators during operations                     | UI/UX                  | Medium   |        |
| 29 | Error messages for validation failures                    | UI/UX                  | High     |        |
| 30 | Accessibility for keyboard navigation                    | UI/UX                  | Medium   |        |
| 31 | Consistent styling across browsers                       | UI/UX                  | Medium   |        |
| 32 | Timesheet page load time acceptable                      | Performance            | Medium   |        |
| 33 | Filtered search response time acceptable                 | Performance            | Medium   |        |
| 34 | Pagination performance acceptable                        | Performance            | Medium   |        |
| 35 | Add/edit/delete manual entry operation time acceptable   | Performance            | Medium   |        |
| 36 | Approve/reject entry operation time acceptable           | Performance            | Medium   |        |
| 37 | Bulk approval performance acceptable                     | Performance            | Medium   |        |
| 38 | Export large timesheet performance acceptable            | Performance            | Medium   |        |
| 39 | Rapid repeated filter/pagination changes performance     | Performance            | Medium   |        |

> 🔹 **Type:** Functional, Negative & Edge Case, UI/UX, Security & Access, Performance  
> 🔸 **Priority:** High, Medium, Low  
> 🔘 **Status:** To be filled during testing