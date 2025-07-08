# Screenshots Module

## 📌 Overview

This module covers the **Screenshots** feature in WebWork.  
It allows team admins and users to **view, filter, download, and manage screenshots** taken during tracked sessions.  
Screenshots are essential for monitoring productivity, verifying work, and supporting billing and reports.

---

## 🔍 What is tested

### Functional Scenarios:
- View screenshots by user
- Filter by project, date range, time period
- Paginate through screenshots
- Download single or multiple screenshots
- Delete single or multiple screenshots
- Verify time data columns (Total, Tracked, Manual Added, Idle, Paid Leave, Break)
- Role-based access control for viewing/editing

---

### Security and Access:
- Only authorized users can view screenshots
- Role-based permissions (Admin, Manager, User)
- Secure download links
- HTTPS enforced for transmission
- Validation against tampered requests

---

### Edge Cases:
- Empty data periods (no screenshots)
- Large number of screenshots (pagination stress)
- Concurrent downloads/deletions
- Filtering by multiple overlapping projects or users

---

### UI/UX:
- Responsive design
- Clear layout of images in grid/list
- Visible download/delete buttons
- Filter panels easy to use
- Loading indicators for images
- Error messages for failed downloads or deletions

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
Screenshots are a critical compliance and monitoring feature for many teams.  
Their accuracy and security are essential for trust in the system.

---

## 📎 Notes

- Always verify images match session data.  
- Check download files for correct resolution and naming.  
- Test filters across projects, users, and dates.  
- Consider accessibility for screen readers and keyboard navigation.