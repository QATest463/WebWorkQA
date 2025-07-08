import time
from playwright.sync_api import sync_playwright
from qa_docs.automation.library.helpers_ui.login import login
from qa_docs.automation.library.helpers_ui.start_break import start_break
from qa_docs.automation.library.helpers_ui.stop_break import stop_break
from qa_docs.automation.library.helpers_ui.stop_web_tracker import stop_web_tracker
from qa_docs.automation.library.helpers_ui.verify_break_report import verify_break_report

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # === SCENARIO ===
    user_name = login(page, "imperiya.prazdnika71017@mail.ru", "Prazdnik71017")

    break_policy, break_duration = start_break(page)
    stop_break(page)
    stop_web_tracker(page)

    verify_break_report(
        page,
        user_name=user_name,
        break_policy=break_policy,
        break_duration=break_duration
    )

    context.close()
    browser.close()

if __name__ == "__main__":
    with sync_playwright() as playwright:
        run(playwright)