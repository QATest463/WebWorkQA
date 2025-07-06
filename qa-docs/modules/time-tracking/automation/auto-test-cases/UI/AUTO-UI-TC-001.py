import time
import re
from playwright.sync_api import Playwright, sync_playwright

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # === Login ===
    print("➡️ Logging in")
    page.goto("https://www.webwork-tracker.com/login")
    page.fill("#email", "imperiya.prazdnika71017@mail.ru")
    page.fill("#password", "Prazdnik71017")
    page.get_by_role("button", name="Log in").click()
    page.wait_for_url("**/app/dashboard")
    print("✅ Logged in")

    # === Select Project and Task from dropdown ===
    page.get_by_role("button").filter(has_text=re.compile(r"^$")).nth(2).click()
    time.sleep(3)
    print("➡️ Selecting project")
    page.locator(".css-9z0tdp").first.click()
    selected_project_option = page.locator("#react-select-2-option-1")
    selected_project = selected_project_option.inner_text().strip()
    selected_project_option.click()
    print(f"✅ Selected Project: {selected_project}")
    print("➡️ Selecting task")
    page.locator(".css-1d3ue9b-control > .css-1bgdfwe > .css-9z0tdp").click()
    page.locator("#react-select-3-option-1").click()

    # === Start the tracker ===
    print("✅ Clicking START")
    page.locator("#webwork-tracker-widget").get_by_role("button").first.click()
    print("⏳ Waiting 65 seconds to accumulate time...")
    time.sleep(65)

    # === Capture stop time from tracker widget (only hours and minutes) ===
    raw_stop_time = page.locator("#webwork-tracker-widget p").first.inner_text().strip()
    stop_time_hm = ":".join(raw_stop_time.split(":")[0:2]).lstrip("0")
    print(f"✅ Tracker stop time (hours:minutes): {stop_time_hm}")

    # === Stop the tracker ===
    print("✅ Clicking STOP")
    page.locator("#webwork-tracker-widget").get_by_role("button").first.click()

    # === Verify Timeline entries for User ===
    print("➡️ Going to Timeline")
    page.get_by_role("link", name="Reports").click()
    page.get_by_role("link", name="Timeline").click()
    page.wait_for_url(re.compile(r".*/reports/timeline.*"))
    print("✅ Timeline loaded")
    print("➡️ Checking Timeline for User")
    page.wait_for_selector("div[role='row']")
    rows = page.locator("div[role='row']").filter(has_text="User")
    assert rows.count() > 0, "❌ No rows with User found!"

    found_valid = False
    for i in range(rows.count()):
        row = rows.nth(i)
        project_name = row.locator("div[role='gridcell'][col-id='project']").inner_text().strip()
        time_value = row.locator("div[role='gridcell'][col-id='time'] span").inner_text().strip().lstrip("0")

        print(f"🔎 Row {i+1}: Project='{project_name}', Time='{time_value}'")

        if project_name == selected_project and time_value == stop_time_hm:
            found_valid = True
            print(f"✅ Match found! Project: {project_name}, Time: {time_value}")
            break

    assert found_valid, f"❌ No matching entry found for User with project='{selected_project}' and time='{stop_time_hm}'!"
    print("✅ All Timeline checks passed!")

    # === Close browser context ===
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)