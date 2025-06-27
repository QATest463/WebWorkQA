# Billing and Payments Module Checklist

| №  | Check Item                                              | Type                   | Priority | Status |
|----|----------------------------------------------------------|------------------------|----------|--------|
| 1  | View available plans and pricing                         | Functional             | High     |        |
| 2  | Upgrade subscription plan                                | Functional             | High     |        |
| 3  | Downgrade subscription plan                              | Functional             | High     |        |
| 4  | Add new payment method                                   | Functional             | High     |        |
| 5  | Update existing payment method                           | Functional             | High     |        |
| 6  | Process payment successfully                             | Functional             | High     |        |
| 7  | Cancel subscription                                      | Functional             | High     |        |
| 8  | Refund processing                                        | Functional             | High     |        |
| 9  | View and download invoices                               | Functional             | Medium   |        |
| 10 | Registration with invalid card number is blocked         | Negative & Edge Case   | High     |        |
| 11 | Expired card is rejected                                 | Negative & Edge Case   | High     |        |
| 12 | Payment with insufficient funds shows error              | Negative & Edge Case   | High     |        |
| 13 | Duplicate payment attempts are blocked                   | Negative & Edge Case   | High     |        |
| 14 | Invalid promo codes are rejected                         | Negative & Edge Case   | Medium   |        |
| 15 | Refunds are blocked for non-refundable items             | Negative & Edge Case   | Medium   |        |
| 16 | Payment with maximum allowed amount                      | Edge Case              | Medium   |        |
| 17 | Payment gateway timeout is handled                       | Edge Case              | Medium   |        |
| 18 | Rapid multiple plan changes handled safely               | Edge Case              | Medium   |        |
| 19 | Responsive design on mobile devices                      | UI/UX                  | Medium   |        |
| 20 | Clear error messages for failed payments                 | UI/UX                  | High     |        |
| 21 | Confirmation dialogs for billing changes                 | UI/UX                  | High     |        |
| 22 | Pricing info is clear and readable                       | UI/UX                  | High     |        |
| 23 | Consistent styling across browsers                       | UI/UX                  | Medium   |        |
| 24 | Accessibility for input fields and buttons               | UI/UX                  | Medium   |        |
| 25 | Secure transmission of payment data (HTTPS)              | Security & Access      | High     |        |
| 26 | PCI compliance enforced                                   | Security & Access      | High     |        |
| 27 | Tokenization of credit card data                          | Security & Access      | High     |        |
| 28 | Rate limiting on payment attempts                         | Security & Access      | High     |        |
| 29 | Prevention of duplicate charges                           | Security & Access      | High     |        |
| 30 | Access control enforced for billing routes                | Security & Access      | High     |        |
| 31 | Protection against tampered payment requests              | Security & Access      | High     |        |
| 32 | Payment processing response time is acceptable            | Performance            | Medium   |        |
| 33 | High concurrency is handled during checkout               | Performance            | Medium   |        |
| 34 | Billing history loads within performance threshold        | Performance            | Medium   |        |
| 35 | Payment gateway latency handled gracefully                | Performance            | Medium   |        |
| 36 | Rate limiting effective under simulated attack            | Performance            | Medium   |        |

> 🔹 **Type:** Functional, Negative & Edge Case, UI/UX, Security & Access, Performance  
> 🔸 **Priority:** High, Medium, Low  
> 🔘 **Status:** To be filled during testing