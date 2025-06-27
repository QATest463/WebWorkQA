# Postman Collection – Notification Module

This folder contains the exported Postman collection for testing the **Notification** API endpoints.

---

## 📌 File Included
- `postman_collection.json` – Complete set of Notification API requests

---

## ✅ What It Covers
- Retrieve all notifications
- Retrieve unread notifications
- Mark notifications as read/unread
- Delete single and multiple notifications
- Filter by type or status
- Search notifications
- Retrieve notification settings/preferences
- Negative scenarios (invalid data, unauthorized access, non-existent IDs)
- Security tests (role-based access, authentication, HTTPS enforcement)
- Performance checks for large datasets and bulk operations

---

## 🗂️ How to Use
1. Open **Postman**.
2. Click **Import**.
3. Choose **File** and select `postman_collection.json`.
4. The collection will appear in your workspace.
5. Configure any required environment variables (e.g. baseURL, tokens).
6. Run individual requests or use **Collection Runner** to automate.

---

## ⚠️ Notes
- Ensure correct environment configuration (Dev, Staging, Prod).
- Do not commit sensitive data like API keys or tokens.
- Keep the collection updated with any API changes.
- Include example responses for documentation.
- Use the **Tests** tab in Postman to automate assertions.

---

✅ Recommended Practices
- Organize requests into folders by feature or scenario.
- Add pre-request scripts for authentication tokens.
- Store environment variables securely.