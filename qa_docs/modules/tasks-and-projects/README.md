# Tasks and Projects Module

## 📌 Overview

This module covers the **Tasks and Projects** feature in WebWork.  
It is designed to help teams manage, assign, and track tasks within projects, supporting time tracking and reporting integration.

---

## 🔍 What is tested

### Functional Scenarios:
- Create a new project
- Edit project details
- Delete project
- View project list with pagination
- Create a new task
- Assign task to users
- Set task deadlines and priorities
- Edit and update tasks
- Delete tasks
- View task list filtered by project, user, date
- Mark task as complete/incomplete
- Integration with time tracking

---

### Security and Access:
- Only authorized users can create/edit/delete projects
- Role-based permissions (Admin, Manager, User)
- Data access restricted to team
- Validation against tampered requests

---

### Edge Cases:
- Empty project/task lists
- Bulk deletion or editing
- Very large number of tasks in a project
- Concurrent edits

---

### UI/UX:
- Responsive design
- Easy-to-use forms for project/task creation
- Filter and sort functionality
- Confirmation dialogs for deletions
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
Managing tasks and projects is critical for productivity and reporting accuracy.  
Proper role-based access and data integrity must be enforced.

---

## 📎 Notes

- Verify correct integration with time tracking.
- Check role restrictions for creating, editing, and deleting.
- Validate all form fields thoroughly.
- Test error handling for API and UI.