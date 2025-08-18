# 🔐 Authentication Module

## 📌 Overview

This module covers all authentication flows for WebWork, including login, logout, registration, and password management.

---

## 🔍 What is tested

### Functional Scenarios:
- User login (valid/invalid credentials)
- User registration (if enabled)
- Password reset (forgot password flow)
- Logout behavior
- Session expiration
- Email confirmation (if applicable)

---

### Security and Access:
- Brute-force protection
- Rate limiting
- Enforce HTTPS-only access
- Block access for inactive/unverified accounts
- Session hijacking protection
- CSRF/XSS mitigation

---

### Edge Cases:
- Repeated failed login attempts
- Expired/invalid password reset tokens
- Multiple sessions from different devices
- Login with special characters in credentials

---

### UI/UX:
- Error messages for wrong credentials
- Password visibility toggle
- Clear login/signup form validation
- Mobile responsiveness

---

## 📁 Folder Contents

- `test-cases/` → All manual test cases (positive, negative, etc.)
- `checklists/` → Functional and non-functional checklists
- `api-tests/` → API-level test cases & Postman collections
- `bug-reports/` → Bugs tracked during authentication testing
- `sql-beckend-checks/` → DB queries for verifying account states
- `exploratory-session-notes/` → Session logs from exploratory testing
- `requirements-review-comments/` → Notes on requirement quality

---

## 🧪 Priority

Authentication has **very high priority** due to its impact on user access, system security, and legal compliance.

---

## 📎 Notes

- Ensure login works across multiple browsers
- Validate secure session cookies/tokens
- Test both desktop and mobile versions
- Review error messages for leakage of sensitive info