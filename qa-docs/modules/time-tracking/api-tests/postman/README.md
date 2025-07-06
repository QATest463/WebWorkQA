# 🗂️ Postman Collection – Time Tracking Module

This folder contains the exported Postman collection for testing **WebWork Time Tracking API** endpoints.  
It is structured to help you test:

✅ Functional scenarios  
✅ Negative cases  
✅ Security requirements  
✅ Performance aspects  

---

## 📌 Quick Start

1️⃣ Open **Postman**.  
2️⃣ Click **Import** and choose `postman_collection.json` from this folder.  
3️⃣ The full folder structure with all requests and tests will appear.  
4️⃣ Make sure you're **already logged in** to WebWork in your browser.  
5️⃣ Configure environment variables (like `baseUrl` and `authToken`).  
6️⃣ Run individual requests or use **Collection Runner** to execute entire suites.

---

## 📂 Recommended Folder Structure in Postman

- **Time Entries**
  - Start Time Entry
  - Stop Time Entry
  - Pause/Resume Tracking
  - Manual Time Entry (Add, Edit, Delete)
  - Retrieve Entries (with filters/pagination)
  - Live Tracked Time
- **Validation and Security**
  - Unauthorized Access
  - Invalid Payload
  - Role-Based Access Control
  - HTTPS Enforcement
  - Rate Limit Checks
- **Performance / Bulk Testing**
  - Bulk Start/Stop
  - Multiple Entries Listing
  - Rapid Actions
- **Negative / Edge Cases**
  - Missing Required Fields
  - Malformed JSON
  - Large Payload
  - Offline / Queued Entries

---

## 🌐 Environment Variables Example

```json
{
  "baseUrl": "https://background.webwork-tracker.com",
  "authToken": ""
}
```
- **baseUrl** – The actual base API URL for WebWork's time tracking endpoints.
- **authToken** – Bearer token obtained manually from an active session if required.

---

## ⚠️ Note on Authentication

WebWork does not provide a public REST API for email/password login.  
Authentication is performed via the browser UI at `/sign-in`, which sets a session cookie.  

✅ This means:
- You can't perform login via Postman as a raw API request.
- You must already be logged in via browser and have a valid session cookie or token.
- Postman requests in this collection assume that session is valid.

---

## ⚠️ Negative and Security Tests

### ⚠️ Notes on Limitations

❗️Some time-tracking flows (Start, Stop, Resume) require a logged-in user session and real UI interaction. These cannot be fully tested via Postman as raw API calls.

✅ These cases are moved to UI Automation using Playwright + Pytest, where user login and interactions are simulated.

#### ✅ Expected Result:
- Server returns **HTTP 422 Unprocessable Entity** with an error like "Invalid track type".

#### ✅ How to Test:
- Send these requests in Postman.
- Confirm the **422 response** in the Tests tab.

#### ✅ Notes:
- Ensures the endpoint cannot be bypassed via raw API calls.
- Documented in both **Negative** and **Security** test sections.

---

## ✅ Recommended Practices

- Organize requests logically into folders and scenarios.
- Use Pre-request Scripts to automate token injection and setup.
- Store and share Environment Variables securely.
- Maintain separate environments for Dev, Staging, and Production.
- Add clear, consistent naming and descriptions to each request.
- Include automated tests in Postman's **Post-response** tab for validation.

---
