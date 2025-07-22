import time
import re
from playwright.sync_api import Playwright, sync_playwright


def login(page):
    print("➡️ Logging in")
    page.goto("https://www.webwork-tracker.com/login")
    page.fill("#email", "imperiya.prazdnika71017@mail.ru")
    page.fill("#password", "Prazdnik71017")
    page.get_by_role("button", name="Log in").click()
    page.wait_for_url("**/app/dashboard")
    print("✅ Logged in")
    time.sleep(5)


def add_time_entry(page):
    print("➡️ Clicking Quick Add")
    page.locator(".dropdown.d-flex.align-items-center").click()
    print("➡️ Selecting 'Time entry'")
    page.get_by_text("Time entry", exact=True).click()
    print("➡️ Waiting for Time Entry modal/dialog")
    page.wait_for_selector("[role='dialog']:not(.d-none)")
    print("✅ Time Entry modal opened!")

    print("➡️ Selecting Project")
    page.get_by_role("dialog", name="Add Time close icon").locator("img").nth(3).click()
    page.locator("#simple-popover").get_by_text("Project 1").click()
    print("➡️ Selecting Task")
    page.locator("[role='dialog']").locator("img").nth(4).click()
    page.locator("#simple-popover").get_by_text("Task").click()
    print("➡️ Setting start and end time")
    page.get_by_role("textbox", name="hh:mm").first.fill("09:00")
    page.get_by_role("textbox", name="hh:mm").nth(1).fill("10:00")
    print("➡️ Adding activity description")
    description_input = page.get_by_placeholder("Activity description")
    description_input.fill("text1")
    description_input.press("Enter")
    print("✅ Saving new time entry")
    page.get_by_role("button", name="Add").click()


def go_to_timeline(page, context_msg=""):
    print(f"➡️ Navigating to Timeline {context_msg}")
    page.get_by_role("link", name="Reports").click()
    page.get_by_role("link", name="Timeline").click()
    page.wait_for_url(re.compile(r".*/reports/timeline.*"))
    print(f"✅ Timeline loaded {context_msg}")


def edit_time_entry(page):
    print("➡️ Navigating to Timesheets > Time Editor")
    page.get_by_role("link", name="Timesheets").click()
    page.get_by_role("link", name="Time Editor").click()
    print("➡️ Editing end time to 10:30")
    page.get_by_placeholder("hh:mm").nth(1).click()
    page.get_by_placeholder("hh:mm").nth(1).fill("10:30")
    page.locator(".page-content").click()
    print("✅ Edited time")


def delete_time_entry(page):
    print("➡️ Navigating to Timesheets > Time Editor")
    page.get_by_role("link", name="Timesheets").click()
    page.get_by_role("link", name="Time Editor").click()

    print("➡️ Locating the added time entry row")
    entry_row = page.get_by_role("row", name=re.compile(r"09:00.*Project 1.*Task"))
    entry_row.get_by_role("img").click()

    print("➡️ Confirming Delete")
    page.locator("div").filter(has_text=re.compile(r"^Delete$")).click()
    page.get_by_role("button", name="Yes").click()
    print("✅ Entry deleted")


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # === Scenario ===
    login(page)
    add_time_entry(page)
    go_to_timeline(page, "(after add)")

    edit_time_entry(page)
    go_to_timeline(page, "(after edit)")

    delete_time_entry(page)
    go_to_timeline(page, "(after delete)")

    # === Close browser
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)