# Desktop and Mobile Apps Module

## 📌 Overview

This module covers the **Desktop and Mobile Apps** of the WebWork system.  
It ensures that the cross-platform applications function correctly, deliver a good user experience, maintain security, and perform reliably.

---

## 🔍 What is tested

### Functional Scenarios:
- User login and logout
- Time tracking features
- Manual time entry
- Screenshot and activity capture
- Notifications
- Offline/online sync
- App settings

---

### Security and Access:
- User authentication
- Secure storage of credentials
- Authorization for accessing features
- Prevent unauthorized time editing
- Enforce HTTPS connections

---

### Edge Cases:
- Switching networks
- App resuming from background
- Logging out during sync
- Handling lost or interrupted connections
- Low battery or device sleep

---

### UI/UX:
- Responsive layouts
- Accessible design
- Consistent theming
- Intuitive navigation
- Feedback during loading/sync

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
The desktop and mobile apps are primary tools for time tracking and productivity monitoring.

---

## 📎 Notes

- Test on multiple OS versions (Windows, macOS, iOS, Android).  
- Ensure sync works across devices.  
- Validate offline functionality and data integrity.  
- Prioritize security of user data.