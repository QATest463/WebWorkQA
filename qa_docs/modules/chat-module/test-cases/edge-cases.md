# Edge Cases – Chat Module

| ID          | Title                                       | Precondition                        | Steps                                                         | Expected Result                           | Actual Result | Status |
|-------------|---------------------------------------------|-------------------------------------|---------------------------------------------------------------|-------------------------------------------|---------------|--------|
| CH-EC-001   | Very large message                          | User logged in                      | 1. Compose very large text message <br> 2. Send | App handles gracefully or enforces limits |               |        |
| CH-EC-002   | Poor network conditions                     | User logged in                      | 1. Throttle network <br> 2. Send/receive message | Messages queued or delayed but delivered |               |        |
| CH-EC-003   | Switch network (Wi-Fi to mobile data)       | User logged in                      | 1. Start on Wi-Fi <br> 2. Switch to mobile data during chat | Connection maintained without logout |               |        |
| CH-EC-004   | App in background while message received    | User logged in                      | 1. Minimize app <br> 2. Send message from other device | Notification or badge shown |               |        |
| CH-EC-005   | Multiple devices logged in simultaneously   | User logged in on web and mobile    | 1. Send message from web <br> 2. Observe mobile | Both devices sync and display message |               |        |