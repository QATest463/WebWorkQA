import time

def login(page, email, password):
    page.goto("https://www.webwork-tracker.com/login")
    page.fill("#email", email)
    page.fill("#password", password)
    page.get_by_role("button", name="Log in").click()
    page.wait_for_url("**/app/dashboard")
    user_name = page.locator(".tooltip-text-user-name").inner_text().strip()
    print("✅ Logged in")
    time.sleep(3)

    return user_name