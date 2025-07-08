# Performance Test Cases – Security and Roles Module

| ID          | Title                                       | Precondition                        | Steps                                                         | Expected Result                           | Actual Result | Status |
|-------------|---------------------------------------------|-------------------------------------|---------------------------------------------------------------|-------------------------------------------|---------------|--------|
| SR-PF-001   | Load roles page with many roles              | Admin logged in                     | 1. Navigate to Roles page with large number of roles | Page loads within acceptable time (<2s) |               |        |
| SR-PF-002   | Assign roles to many users                    | Admin logged in                     | 1. Assign role to many users simultaneously | Operation completes without delay |               |        |
| SR-PF-003   | Concurrent role updates                       | Admin logged in                     | 1. Multiple admins edit roles simultaneously | System handles concurrency without errors |               |        |
| SR-PF-004   | Role inheritance processing                   | Admin logged in                     | 1. Define complex inheritance <br> 2. Assign roles | Permissions applied correctly and quickly |               |        |