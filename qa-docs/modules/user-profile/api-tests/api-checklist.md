# User Profile Module – API Checklist

| №  | Check Item                                             | Type        | Priority | Status |
|----|---------------------------------------------------------|-------------|----------|--------|
| 1  | Retrieve user profile details                           | Functional  | High     |        |
| 2  | Update personal information                             | Functional  | High     |        |
| 3  | Upload/change profile picture                           | Functional  | High     |        |
| 4  | Change user password                                    | Functional  | High     |        |
| 5  | Retrieve assigned role and permissions                  | Functional  | Medium   |        |
| 6  | Update notification preferences                         | Functional  | Medium   |        |
| 7  | Update language preferences                             | Functional  | Medium   |        |
| 8  | Retrieve activity log                                   | Functional  | Medium   |        |
| 9  | Unauthorized access to endpoints returns 401            | Security    | High     |        |
| 10 | Role-based permissions enforced for Admin editing       | Security    | High     |        |
| 11 | Validation against tampered user IDs                    | Security    | High     |        |
| 12 | Secure password update process                          | Security    | High     |        |
| 13 | Enforce HTTPS-only connections                          | Security    | High     |        |
| 14 | Invalid request body returns validation error           | Negative    | Medium   |        |
| 15 | Attempt to update another user's profile                | Negative    | Medium   |        |
| 16 | Attempt to upload unsupported image format              | Negative    | Medium   |        |
| 17 | Attempt to update with invalid email/password           | Negative    | Medium   |        |
| 18 | Large activity log retrieval with pagination            | Performance | Medium   |        |
| 19 | Profile update save response time acceptable            | Performance | Medium   |        |
| 20 | Upload profile picture operation time acceptable        | Performance | Medium   |        |

> 🔹 **Type:** Functional, Security, Negative, Performance  
> 🔸 **Priority:** High, Medium, Low  
> 🔘 **Status:** To be filled during testing