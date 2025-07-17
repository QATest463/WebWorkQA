# ✅ Time Tracking Module – QA Checklist 

### Precondition: At least one Break Policy is available and configured in Settings.

| №  | Check Item                                                                                       | Type                   | Priority | Status |
|----|--------------------------------------------------------------------------------------------------|------------------------|----------|--------|
| 1  | Start and stop time tracking                                                                     | Functional             | High     |        |
| 2  | Pause and resume time tracking                                                                   | Functional             | High     |        |
| 3  | Switch between projects/tasks while tracking                                                     | Functional             | High     |        |
| 4  | Add manual time entry                                                                            | Functional             | High     |        |
| 5  | Edit manual time entry                                                                           | Functional             | High     |        |
| 6  | Delete manual time entry                                                                         | Functional             | High     |        |
| 7  | View daily/weekly/monthly tracked summaries                                                      | Functional             | Medium   |        |
| 8  | Integration with Timesheet module                                                                | Functional             | High     |        |
| 9  | Start and stop Break                                                                             | Functional             | High     |        |
| 10 | Add manual Break entry                                                                           | Functional             | High     |        |
| 11 | Edit manual Break entry                                                                          | Functional             | High     |        |
| 12 | Delete manual Break entry                                                                        | Functional             | High     |        |
| 13 | View Break reports and summaries                                                                 | Functional             | Medium   |        |
| 14 | Only authenticated users can track time and breaks                                               | Security & Access      | High     |        |
| 15 | Unauthorized access is blocked                                                                   | Security & Access      | High     |        |
| 16 | Role-based access for automatic time addition (Executive M., Team M., Project M., Regular User)  | Security & Access      | High     |        |
| 17 | Users can only edit/delete their own entries                                                     | Security & Access      | High     |        |
| 18 | Validation against tampered requests                                                             | Security & Access      | High     |        |
| 19 | Enforce HTTPS-only connections                                                                   | Security & Access      | High     |        |
| 20 | Starting multiple timers or breaks simultaneously is blocked                                     | Negative / Edge Case   | Medium   |        |
| 21 | Overlapping manual and automatic entries are blocked                                             | Negative / Edge Case   | Medium   |        |
| 22 | Rapid switching between projects/tasks is handled                                                | Negative / Edge Case   | Medium   |        |
| 23 | Network disconnect/reconnect during tracking is handled                                          | Negative / Edge Case   | Medium   |        |
| 24 | Long-running timer sessions work correctly                                                       | Negative / Edge Case   | Medium   |        |
| 25 | Bulk deletion of manual entries works as expected                                                | Negative / Edge Case   | Medium   |        |
| 26 | Viewing large number of time or break entries is handled                                         | Negative / Edge Case   | Medium   |        |
| 27 | Clear, readable timer and break widgets                                                          | UI / UX                | Medium   |        |
| 28 | Responsive design on mobile devices                                                              | UI / UX                | Medium   |        |
| 29 | Easy-to-use start/stop/pause/resume/break controls                                               | UI / UX                | Medium   |        |
| 30 | Manual entry form is intuitive                                                                   | UI / UX                | Medium   |        |
| 31 | Confirmation dialogs for deletions                                                               | UI / UX                | High     |        |
| 32 | Loading indicators during operations                                                             | UI / UX                | Medium   |        |
| 33 | Error messages for validation failures                                                           | UI / UX                | High     |        |
| 34 | Accessibility for keyboard navigation                                                            | UI / UX                | Medium   |        |
| 35 | Consistent styling across browsers                                                               | UI / UX                | Medium   |        |