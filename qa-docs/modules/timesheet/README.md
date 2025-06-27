# Timesheet Module

## 📌 Overview

This module covers the **Timesheet** feature in WebWork.  
It allows users and managers to **view, edit, approve, and export time entries**.  
Timesheets summarize tracked, manual, idle, and leave times per day or week, supporting payroll and reporting processes.

---

## 🔍 What is tested

### Functional Scenarios:
- View personal timesheet
- View team timesheets (for managers)
- Filter by date range, user, project
- Add manual time entry
- Edit manual time entry
- Delete manual time entry
- Approve/reject timesheet entries (for managers)
- Export timesheet to CSV/PDF

---

### Security and Access:
- Only authorized users can view timesheets
- Role-based access (User vs Manager/Admin)
- Validation of time entry ownership
- Secure export/download links

---

### Edge Cases:
- Empty timesheet period
- Large number of entries
- Overlapping time entries
- Concurrent edits/approvals

---

### UI/UX:
- Responsive design
- Filter and search functionality
- Clear table/grid layout
- Confirmation dialogs for deletion/approval
- Loading indicators during operations
- Error messages for validation failures

---

## 📁 Module Folder Structure
- test-cases/
  - functional.md
  - negative-scenarios.md
  - edge-cases.md
  - ui-ux.md
  - security-and-access.md
  - performance.md
- checklists/
  - checklist.md
- bug-reports/
  - open/
  - fixed/
  - in-review/
  - closed/
- api-tests/
  - api-checklist.md
  - api-test-cases/
    - functional.md
    - security.md
    - negative.md
  - postman/
    - postman_collection.json
- README.md

---

## 🧪 Priority

This module has **High Priority**.  
Accurate timesheets are critical for billing, payroll, and compliance.  
Any errors can lead to incorrect payments or disputes.

---

## 📎 Notes

- Verify data consistency across filters.
- Check role restrictions for editing and approving.
- Validate time overlaps and maximum allowed durations.
- Ensure secure export functionality.