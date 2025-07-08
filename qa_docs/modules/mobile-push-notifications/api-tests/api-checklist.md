# Mobile Push Notifications Module – API Checklist

| №  | Check Item                                             | Type        | Priority | Status |
|----|---------------------------------------------------------|-------------|----------|--------|
| 1  | Send push notification                                | Functional  | High     |        |
| 2  | Retrieve notification delivery status                 | Functional  | Medium   |        |
| 3  | Manage user device tokens                             | Functional  | High     |        |
| 4  | Opt-in/Opt-out endpoints                              | Functional  | High     |        |
| 5  | Unauthorized send attempt blocked                     | Security    | High     |        |
| 6  | Permission enforcement for sending notifications      | Security    | High     |        |
| 7  | Secure transmission of device tokens                  | Security    | High     |        |
| 8  | Enforce HTTPS-only connections                        | Security    | High     |        |
| 9  | Rate limiting on send notification endpoint           | Security    | High     |        |
| 10 | Handle large-scale simultaneous notification sends    | Performance | Medium   |        |
| 11 | Delivery latency under load                           | Performance | Medium   |        |

> 🔹 **Type:** Functional, Security, Performance  
> 🔸 **Priority:** High, Medium, Low  
> 🔘 **Status:** To be filled during testing