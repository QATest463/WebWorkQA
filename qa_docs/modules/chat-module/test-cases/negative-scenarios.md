# Negative Test Cases – Chat Module

| ID          | Title                                       | Precondition                        | Steps                                                         | Expected Result                           | Actual Result | Status |
|-------------|---------------------------------------------|-------------------------------------|---------------------------------------------------------------|-------------------------------------------|---------------|--------|
| CH-NT-001   | Send empty message                          | User logged in                      | 1. Open chat <br> 2. Leave message box empty <br> 3. Tap send | Send button disabled or error shown |               |        |
| CH-NT-002   | Send message with unsupported file type     | User logged in                      | 1. Tap attach <br> 2. Select unsupported file <br> 3. Send | Error message displayed |               |        |
| CH-NT-003   | Extremely long message                      | User logged in                      | 1. Paste very long text <br> 2. Tap send | Error or truncation handled gracefully |               |        |
| CH-NT-004   | Sending without network connection          | User offline                        | 1. Disable network <br> 2. Tap send | Error or queued for later sending |               |        |
| CH-NT-005   | Deleting message not owned by user          | User logged in in group chat        | 1. Attempt to delete other user's message | Action blocked with error |               |        |