import time
import re
from playwright.sync_api import Playwright, sync_playwright

from qa_docs.automation.library.helpers_ui.login import login
from qa_docs.automation.library.helpers_ui.start_web_tracker import start_web_tracker
from qa_docs.automation.library.helpers_ui.stop_web_tracker import stop_web_tracker
from qa_docs.automation.library.helpers_ui.go_to_timeline import go_to_timeline

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # === SCENARIO ===
    user_name = login(page, "imperiya.prazdnika71017@mail.ru", "Prazdnik71017")

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

    start_web_tracker(page)
    stop_time_hm = stop_web_tracker(page)

    go_to_timeline(page, user_name, selected_project, stop_time_hm)

    # === Close browser context ===
    context.close()
    browser.close()

if __name__ == "__main__":
    with sync_playwright() as playwright:
        run(playwright)