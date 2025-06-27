# Activity and Productivity Module

## 📌 Overview

This module covers the **Activity and Productivity** feature in WebWork.  
It enables users to **track activity levels, idle time, app/website usage, and productivity categorization**.  
Managers and users can review detailed productivity reports to optimize time management and efficiency.

---

## 🔍 What is tested

### Functional Scenarios:
- Start/stop activity tracking
- Record active/idle time
- Track app/website usage
- Categorize apps/websites as productive/unproductive
- View productivity summary
- Export productivity data

---

### Security and Access:
- Only authenticated users can track/view activity
- Role-based access for managers
- Validation of ownership for viewing/editing productivity categories
- Secure storage and transfer of activity logs

---

### Edge Cases:
- Very long tracking sessions
- Simultaneous tracking on multiple devices
- Sudden network disconnect/reconnect
- High-frequency app/website switching

---

### UI/UX:
- Responsive dashboard
- Clear display of productivity categories
- Easy-to-use start/stop controls
- Filtering and searching activity logs
- Loading indicators during data fetch
- Accessible design for keyboard and screen readers

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
Accurate activity tracking and productivity categorization is essential for billing, performance management, and user trust.

---

## 📎 Notes

- Verify idle detection accuracy.
- Validate app/website categorization features.
- Ensure secure transmission of activity data.
- Check for GDPR compliance in activity logs.