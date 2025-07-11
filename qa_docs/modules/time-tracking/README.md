# 📘 Time Tracking Module

This folder contains all QA documentation and assets for the **Time Tracking** feature in WebWork.  
Time Tracking is a critical module for recording user work hours, billing, and productivity reporting.

---

## ✅ Scope of Testing

- Start, stop, and pause timers
- Add, edit, and delete manual time entries
- Break policy handling
- UI/UX checks (modals, forms, responsiveness)
- API endpoints for time tracking
- Role-based access (Admin, Manager, User)

---

## 📂 Folder Structure

- `test-cases/` – detailed functional, negative, and edge test cases
- `checklists/` – execution checklists (e.g., regression, smoke)
- `bug-reports/` – open, fixed, and closed bugs
- `api-tests/` – API test cases, Postman collections
- `automation/` – Playwright and PyTest automated scripts
- `exploratory-sessions/` – session notes and charters
- `traceability-matrix/` – mapping of requirements to test cases
- `requirements-review/` – notes and questions on requirements
- `sql-checks/` – sample queries for backend validation

---

## 🔒 Security & Access
- Only authenticated users can track time
- Role-based permissions:
  - **Admin:** view and edit all entries
  - **Manager:** view team entries
  - **User:** view/edit own entries

---

## 🧪 Priorities
- **High Priority:** billing accuracy, productivity tracking, data integrity
- **Medium Priority:** UI responsiveness, error handling

---

## 📎 Notes
- Integrates with Timesheet and Reports modules
- Includes **manual** test cases and **automated** tests (Playwright UI tests, PyTest API tests)
- Work in progress – additional scenarios and test assets will be added