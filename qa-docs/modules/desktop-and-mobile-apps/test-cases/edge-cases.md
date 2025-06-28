# Edge Cases – Desktop and Mobile Apps Module

| ID          | Title                                       | Precondition                        | Steps                                                         | Expected Result                           | Actual Result | Status |
|-------------|---------------------------------------------|-------------------------------------|---------------------------------------------------------------|-------------------------------------------|---------------|--------|
| DMA-EC-001  | Switch network from Wi-Fi to mobile data    | User tracking time                  | 1. Start tracking on Wi-Fi <br> 2. Switch to mobile data | Sync continues without error |               |        |
| DMA-EC-002  | App resumes from background                 | User tracking time                  | 1. Start tracking <br> 2. Minimize app <br> 3. Reopen | Timer and state preserved correctly |               |        |
| DMA-EC-003  | Logging out during sync                     | User tracking time                  | 1. Start sync <br> 2. Log out mid-sync | Sync cancels gracefully, user logged out |               |        |
| DMA-EC-004  | Lost connection during tracking             | User tracking time                  | 1. Start tracking <br> 2. Disconnect internet | App saves locally and retries sync |               |        |
| DMA-EC-005  | Device sleep or low battery                 | User tracking time                  | 1. Start tracking <br> 2. Let device sleep or low battery mode | Tracking resumes or handles appropriately |               |        |