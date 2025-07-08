# Postman Collection – Reports Module

This folder contains the exported Postman collection for testing the **Reports** API endpoints.

---

## 📌 File Included
- `postman_collection.json` – Complete set of Reports API requests

---

## ✅ What It Covers
- Retrieve available report types
- Generate time tracking reports with filters
- Generate billing reports with filters
- Apply date range and advanced filters
- Export reports to PDF/CSV
- Schedule automated reports
- Negative scenarios (invalid filters, empty ranges)
- Security tests (unauthorized access, role-based access, HTTPS enforcement)
- Performance checks for response times and concurrency

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

---

✅ Recommended Practices
- Add example responses to Postman documentation.
- Use the **Tests** tab in Postman to automate assertions.
- Organize requests into folders for clarity.