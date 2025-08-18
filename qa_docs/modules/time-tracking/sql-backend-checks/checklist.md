# 🧩 SQL / Backend Validation Checklist – Time Tracking Module

| №  | Check Item                                                                 | Type             | Priority | Status |
|----|----------------------------------------------------------------------------|------------------|----------|--------|
| 1  | Verify new time entry is stored correctly in `time_entries` table          | Data Integrity   | High     |        |
| 2  | Ensure `user_id`, `project_id`, `task_id`, and `duration` are accurate     | Data Mapping     | High     |        |
| 3  | Confirm timestamp format is UTC-based or correctly localized               | Timezone/Format  | High     |        |
| 4  | Verify no overlap in time entries for same user/date                       | Constraint Check | Medium   |        |
| 5  | Manual time entries are flagged as `is_manual = true`                      | Flag Validation  | High     |        |
| 6  | Tracker time entries are flagged as `is_manual = false`                    | Flag Validation  | High     |        |
| 7  | Verify break time entries inserted into `break_entries` or equivalent      | Data Integrity   | High     |        |
| 8  | Check break policy ID is linked to existing policy in break table          | Foreign Key      | High     |        |
| 9  | Ensure end time > start time for every entry                               | Logical Check    | High     |        |
| 10 | Validate that submitted entries are marked with `is_submitted = true`      | Submission Flag  | Medium   |        |
| 11 | Test that deleted entries are soft-deleted (e.g., `is_deleted = true`)     | Soft Delete      | Medium   |        |
| 12 | Confirm audit logs exist for all changes (create/update/delete)            | Audit/Trace      | Medium   |        |
| 13 | Validate accurate total daily/weekly summary calculations (via query)      | Aggregation      | Medium   |        |
| 14 | Check whether break durations are included/excluded from total time        | Logic Rule       | Medium   |        |
| 15 | Cross-validate frontend report with raw SQL count for same user/date       | Sync Consistency | Medium   |        |
| 16 | Ensure foreign keys (user_id, project_id, task_id) exist in related tables | Relational Check | High     |        |
| 17 | Break entries must not exceed policy duration in backend                   | Business Rule    | High     |        |
| 18 | Test concurrent insert does not create duplicate overlapping entries       | Concurrency      | High     |        |
| 19 | Ensure indexes exist on key fields (`user_id`, `date`, `project_id`)       | Performance      | Medium   |        |
| 20 | Confirm correct timezone offset stored or applied in queries               | Localization     | Medium   |        |