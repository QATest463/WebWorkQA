# 🚀 Performance API Test Cases – Time Tracking Module

| ID            | Title                                 | Precondition   | Steps                                                          | Expected Result                      | Actual Result | Status |
|---------------|---------------------------------------|----------------|----------------------------------------------------------------|--------------------------------------|---------------|--------|
| TT-API-PF-001 | Retrieve large dataset                | User logged in | GET /time/entries with pagination                              | 200 OK with acceptable response time |               |        |
| TT-API-PF-002 | Rapid repeated start/stop actions     | User logged in | Multiple POST to /api/start-tracker and /api/stop-tracker      | 200 OK each time                     |               |        |
| TT-API-PF-003 | Switch projects/tasks during tracking | Timer running  | POST /api/selected-data rapidly                                | 200 OK updates without error         |               |        |
| TT-API-PF-004 | Bulk retrieval with complex filters   | User logged in | GET /time/entries with filters                                 | 200 OK, correct results              |               |        |
| TT-API-PF-005 | Simultaneous manual/break additions   | User logged in | Multiple POST /api/add-time and /api/add-break simultaneously  | 200 OK, no duplicates                |               |        |