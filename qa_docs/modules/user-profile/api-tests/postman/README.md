# Postman Collection – User Profile Module

This folder contains the exported Postman collection for testing the **User Profile** API endpoints.

---

## 📌 File Included
- `postman_collection.json` – Complete set of User Profile API requests

---

## ✅ What It Covers
- Retrieve user profile details
- Update personal information
- Upload/change profile picture
- Change password
- Retrieve assigned role and permissions
- Update notification and language preferences
- Retrieve activity log
- Negative scenarios (invalid data, unauthorized access, unsupported formats)
- Security tests (role-based access, authentication, HTTPS enforcement)
- Performance checks for large logs and save operations

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