# Time Tracking Module

## 📌 Overview

This module covers the **Time Tracking** feature in WebWork.  
It allows users to **start, stop, pause, and manage timers** while working on projects and tasks.  
Tracked time is used for billing, productivity reports, and payroll.

---

## 🔍 What is tested

### Functional Scenarios:
- Start time tracking
- Stop time tracking
- Pause/resume time tracking
- Switch between projects/tasks while tracking
- View live tracked time
- Add manual time entry
- Edit manual time entry
- Delete manual time entry
- View daily/weekly/monthly tracked summaries
- Integration with Timesheet module

---

### Security and Access:
- Only authenticated users can track time
- Role-based access enforced (Admin, Manager, User)
- Validation of time entries and ownership
- Prevent editing other users' tracked entries

---

### Edge Cases:
- Starting multiple timers simultaneously
- Overlapping manual and automatic entries
- Rapidly switching tasks/projects
- Network disconnect/reconnect while tracking

---

### UI/UX:
- Responsive timer widget
- Clear start/stop/pause controls
- Easy-to-use forms for manual time
- Confirmation dialogs for deletions
- Loading indicators during operations
- Validation errors clearly displayed

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
Accurate time tracking is critical for billing, productivity analysis, and employee accountability.  
Errors can lead to incorrect invoices or lost time data.

---

## 📎 Notes

- Validate continuous tracking sessions without gaps.
- Test integration with Timesheet and Reports.
- Ensure security and ownership of entries.
- Test UI for responsiveness and accessibility.