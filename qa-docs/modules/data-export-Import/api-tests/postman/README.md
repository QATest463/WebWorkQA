# Postman Collection – Data Export / Import Module

This folder contains the exported Postman collection for testing the **Data Export / Import** API endpoints.

---

## 📌 File Included
- `postman_collection.json` – Complete set of Data Export / Import API requests

---

## ✅ What It Covers
- Export user activity logs
- Export timesheets
- Export reports
- Choose file formats (CSV, XLSX)
- Import users in bulk
- Import projects/tasks data
- Validate imported data
- View import/export history logs
- Negative scenarios (invalid data, unauthorized access)
- Security tests (authentication, role-based access, HTTPS enforcement)
- Performance checks for large files and simultaneous requests

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