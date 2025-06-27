# Screenshots Module – API Checklist

| №  | Check Item                                             | Type        | Priority | Status |
|----|---------------------------------------------------------|-------------|----------|--------|
| 1  | Retrieve screenshots list with valid filters            | Functional  | High     |        |
| 2  | Retrieve single screenshot details                      | Functional  | High     |        |
| 3  | Download single screenshot                              | Functional  | High     |        |
| 4  | Download multiple screenshots as ZIP                    | Functional  | High     |        |
| 5  | Delete single screenshot with valid permissions         | Functional  | High     |        |
| 6  | Delete multiple screenshots in one request              | Functional  | High     |        |
| 7  | Filter by project, user, date range                      | Functional  | High     |        |
| 8  | Unauthorized access to screenshots endpoints returns 401 | Security    | High     |        |
| 9  | Role-based access enforced for viewing/deleting         | Security    | High     |        |
| 10 | Secure download links require authentication            | Security    | High     |        |
| 11 | Enforce HTTPS-only connections                          | Security    | High     |        |
| 12 | Validation against tampered delete requests             | Security    | High     |        |
| 13 | Invalid filters return validation error                 | Negative    | Medium   |        |
| 14 | Empty filter results return "No data available"         | Negative    | Medium   |        |
| 15 | Rate limiting on bulk operations enforced               | Security    | Medium   |        |
| 16 | Retrieve large data set with pagination                 | Performance | Medium   |        |
| 17 | Bulk download performance acceptable                    | Performance | Medium   |        |
| 18 | Bulk delete operation time acceptable                   | Performance | Medium   |        |

> 🔹 **Type:** Functional, Security, Negative, Performance  
> 🔸 **Priority:** High, Medium, Low  
> 🔘 **Status:** To be filled during testing