# Postman Collection – Authentication Module

This folder contains the exported Postman collection for testing Authentication API endpoints.

## 📌 File Included
- `postman_collection.json` – Full set of Authentication API requests

## ✅ What It Covers
- User registration
- User login
- Password reset request
- Password reset confirmation
- Social login
- Negative test cases (invalid credentials, invalid tokens, etc.)
- Security tests (rate limiting, SQL injection attempts)

## 🗂️ How to Use
1. Open Postman.
2. Import the `postman_collection.json` file:
   - Click **Import**.
   - Select **File**.
   - Choose `postman_collection.json`.
3. Review the collection in your workspace.
4. Set up any required environment variables (e.g. baseURL, tokens).
5. Run individual requests or use the **Collection Runner** for automated testing.

## ⚠️ Notes
- Make sure you configure the correct environment (e.g. Dev, Staging).
- Sensitive credentials (API keys, tokens) should not be committed to this repo.
- Always verify environment variables before running tests.

---

✅ Recommended Practices
- Keep this collection up to date with any API changes.
- Include example responses in Postman documentation.
- Use Postman Tests tab to automate basic assertions.