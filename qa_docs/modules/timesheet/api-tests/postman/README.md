# Postman Collection – Timesheet Module

This folder contains the exported Postman collection for testing the **Timesheet** API endpoints.

---

## 📌 File Included
- `postman_collection.json` – Complete set of Timesheet API requests

---

## ✅ What It Covers
- Retrieve personal timesheet entries
- Retrieve team timesheet entries (for Managers)
- Filter by date range, project, user
- Add, edit, delete manual time entries
- Approve/reject timesheet entries (Manager)
- Export timesheet to CSV/PDF
- Negative scenarios (invalid data, unauthorized access, non-existent IDs)
- Security tests (role-based access, authentication, HTTPS enforcement)
- Performance checks for bulk operations and large datasets

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