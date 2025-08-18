# 🗄️ SQL / Backend Checks – Time Tracking Module

This folder documents **backend data validation checks** for the **Time Tracking** module in WebWork.

QA engineers must verify not only UI behavior but also **database consistency, correctness of stored data, and integrity of business rules** on the backend.

---

## ✅ What is covered here

- SQL queries to verify time entries, breaks, manual additions
- Steps to validate consistency between UI and DB
- Sample backend test cases
- Notes on API / DB interactions

---

## 🗂️ Folder Structure

| File                               | Description                                      |
|------------------------------------|--------------------------------------------------|
| `queries.md`                       | Useful SQL queries for validation                |
| `checks-manual-time.md`            | Checks for Add/Edit/Delete of manual time        |
| `checks-break-entries.md`          | Checks for Break policy time tracking entries    |
| `api-db-consistency.md`            | Notes on verifying API responses vs DB state     |
| `issues-found.md`                  | Any discrepancies or bugs found in data checks   |

---

## 🔎 Examples of checks

✅ Verify that **time entry added via UI** exists in DB:

```sql
SELECT * FROM time_entries
WHERE user_id = {{userId}}
  AND date = '2025-07-10'
  AND start_time = '09:00'
  AND end_time = '10:00';
```

✅ Confirm Break policy entry is stored with correct policy ID:

```sql
SELECT * FROM break_entries
WHERE user_id = {{userId}}
  AND break_policy_id = {{policyId}}
  AND start_time >= '2025-07-10 12:00:00';
```

✅ Ensure deleted entry is soft-deleted / removed:

```sql
SELECT * FROM time_entries
WHERE id = {{entryId}};
-- Should return 0 rows or is_deleted = true
```

✅ Compare API response to DB:

- Step 1: Call GET /api/timetracking/{id}
- Step 2: Query DB for same entry
- Step 3: Verify all fields match

---

## 📌 Recommended file template

Example checks-manual-time.md:

# Manual Time Entry DB Checks

## 🎯 Purpose
Ensure that manual time entries created/edited/deleted via UI or API are correctly reflected in the database.

## 🧭 Setup
- Connect to staging DB
- Have user account with appropriate permissions

## ✅ Checks
- Verify new entry exists with correct user_id, project_id, task_id
- Check start_time, end_time match input
- Validate is_manual flag = true
- Ensure deletion sets is_deleted = true or removes row

## 🐞 Issues Found
- [ ] None yet

---

🌟 Why add SQL / Backend Checks?
	•	Ensures data integrity
	•	Finds issues not visible in UI
	•	Validates API / DB consistency
	•	Shows professional, thorough QA approach

---

🧑‍💻 Author

Name QA Engineer