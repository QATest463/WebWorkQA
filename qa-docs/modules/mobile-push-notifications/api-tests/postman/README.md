# Postman Collection – Mobile Push Notifications Module

This folder contains the exported Postman collection for testing the **Mobile Push Notifications** API endpoints.

---

## 📌 File Included
- `postman_collection.json` – Complete set of Mobile Push Notifications API requests

---

## ✅ What It Covers
- Sending push notifications
- Retrieving delivery status
- Registering user device tokens
- Managing opt-in/opt-out preferences
- Unauthorized access attempts
- Security tests (HTTPS enforcement, data encryption)
- Rate limiting scenarios
- Negative and edge case validations

---

## 🗂️ How to Use
1. Open **Postman**.
2. Click **Import**.
3. Choose **File** and select `postman_collection.json`.
4. The collection will appear in your workspace.
5. Configure any required environment variables (e.g., baseURL, tokens).
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