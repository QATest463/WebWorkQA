# UI/UX Test Cases – Chat Module

| ID          | Title                                       | Precondition                        | Steps                                                         | Expected Result                           | Actual Result | Status |
|-------------|---------------------------------------------|-------------------------------------|---------------------------------------------------------------|-------------------------------------------|---------------|--------|
| CH-UX-001   | Message input usability                     | User logged in                      | 1. Open chat <br> 2. Tap input box <br> 3. Type message | Input responds smoothly, keyboard appears |               |        |
| CH-UX-002   | Message bubble design consistency           | User logged in                      | 1. Send/receive messages <br> 2. Observe chat screen | Bubbles styled consistently |               |        |
| CH-UX-003   | Timestamp visibility                        | User logged in                      | 1. Send/receive message <br> 2. Check timestamp | Timestamp displayed clearly |               |        |
| CH-UX-004   | Readability on mobile and desktop           | User logged in                      | 1. Open chat on different devices <br> 2. Observe UI | Text and layout readable everywhere |               |        |
| CH-UX-005   | Notifications for new messages              | User logged in                      | 1. Minimize app <br> 2. Receive message | Notification/banner displayed |               |        |
| CH-UX-006   | Error states (failed to send)               | User offline                        | 1. Send message without network | Error icon or message shown |               |        |