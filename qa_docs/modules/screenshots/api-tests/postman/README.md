# Postman Collection – Screenshots Module

This folder contains the exported Postman collection for testing the **Screenshots** API endpoints.

---

## 📌 File Included
- `postman_collection.json` – Complete set of Screenshots API requests

---

## ✅ What It Covers
- Retrieve screenshots list with filters (project, user, date range)
- Retrieve single screenshot details
- Download single screenshot
- Download multiple screenshots as ZIP
- Delete single screenshot
- Delete multiple screenshots in one request
- Negative scenarios (invalid filters, unauthorized access, non-existent IDs)
- Security tests (role-based access, authentication, HTTPS enforcement)
- Performance checks for bulk operations

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