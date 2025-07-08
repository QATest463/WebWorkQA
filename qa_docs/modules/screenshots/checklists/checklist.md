# Screenshots Module Checklist

| №  | Check Item                                              | Type                   | Priority | Status |
|----|----------------------------------------------------------|------------------------|----------|--------|
| 1  | View screenshots by user                                | Functional             | High     |        |
| 2  | Filter by project                                        | Functional             | High     |        |
| 3  | Filter by date range                                     | Functional             | High     |        |
| 4  | Paginate through screenshots                             | Functional             | Medium   |        |
| 5  | Download single screenshot                               | Functional             | High     |        |
| 6  | Download multiple screenshots                            | Functional             | High     |        |
| 7  | Delete single screenshot                                 | Functional             | High     |        |
| 8  | Delete multiple screenshots                              | Functional             | High     |        |
| 9  | Verify time data columns                                 | Functional             | High     |        |
| 10 | Refresh screenshots list                                 | Functional             | Medium   |        |
| 11 | Unauthorized access blocked                              | Security & Access      | High     |        |
| 12 | Role-based access enforced                               | Security & Access      | High     |        |
| 13 | Secure download links require auth                       | Security & Access      | High     |        |
| 14 | Validation against tampered delete requests              | Security & Access      | High     |        |
| 15 | Enforce HTTPS-only connections                           | Security & Access      | High     |        |
| 16 | Empty data range returns no screenshots                  | Negative & Edge Case   | Medium   |        |
| 17 | Invalid date format rejected                             | Negative & Edge Case   | Medium   |        |
| 18 | No matching filters shows "No data available" message    | Negative & Edge Case   | Medium   |        |
| 19 | Prevent delete without selecting screenshots             | Negative & Edge Case   | Medium   |        |
| 20 | Prevent download without selecting screenshots           | Negative & Edge Case   | Medium   |        |
| 21 | Large number of screenshots handled with pagination      | Edge Case              | Medium   |        |
| 22 | Rapid filter changes handled gracefully                  | Edge Case              | Medium   |        |
| 23 | Concurrent download and deletion requests supported      | Edge Case              | Medium   |        |
| 24 | Filter with multiple overlapping projects works correctly | Edge Case              | Medium   |        |
| 25 | Filter by multiple users simultaneously works correctly  | Edge Case              | Medium   |        |
| 26 | Bulk delete operation on large selection works           | Edge Case              | Medium   |        |
| 27 | Clear, readable grid/list layout                          | UI/UX                  | Medium   |        |
| 28 | Responsive design on mobile devices                       | UI/UX                  | Medium   |        |
| 29 | Filter controls easy to use and accessible                | UI/UX                  | Medium   |        |
| 30 | Download and Delete buttons visible and accessible        | UI/UX                  | High     |        |
| 31 | Loading indicators during heavy operations                | UI/UX                  | Medium   |        |
| 32 | Error messages for invalid filters                        | UI/UX                  | High     |        |
| 33 | Accessibility for keyboard navigation                     | UI/UX                  | Medium   |        |
| 34 | Consistent styling across browsers                        | UI/UX                  | Medium   |        |
| 35 | Screenshots page load time acceptable                     | Performance            | Medium   |        |
| 36 | Filtered search response time acceptable                  | Performance            | Medium   |        |
| 37 | Pagination performance with large dataset acceptable      | Performance            | Medium   |        |
| 38 | Bulk download operation time acceptable                   | Performance            | Medium   |        |
| 39 | Bulk delete operation time acceptable                     | Performance            | Medium   |        |
| 40 | Concurrent filter and pagination requests handled well    | Performance            | Medium   |        |

> 🔹 **Type:** Functional, Negative & Edge Case, UI/UX, Security & Access, Performance  
> 🔸 **Priority:** High, Medium, Low  
> 🔘 **Status:** To be filled during testing