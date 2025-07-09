from playwright.sync_api import sync_playwright
from qa_docs.automation.library.helpers_ui.login import login
from qa_docs.automation.library.helpers_ui.get_base_break_duration import get_base_break_duration
from qa_docs.automation.library.helpers_ui.quick_add_modal import quick_add_modal
from qa_docs.automation.library.helpers_ui.add_manual_break import add_manual_break
from qa_docs.automation.library.helpers_ui.go_to_dashboard import go_to_dashboard
from qa_docs.automation.library.helpers_ui.verify_break_report import verify_break_report

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # === SCENARIO ===
    user_name = login(page, "imperiya.prazdnika71017@mail.ru", "Prazdnik71017")

    break_policy, base_duration = get_base_break_duration(page, user_name)
    quick_add_modal(page)

    break_duration, today_str = add_manual_break(page,user_name, break_policy, base_duration)
    go_to_dashboard(page)

    verify_break_report(
        page,
        user_name=user_name,
        break_policy=break_policy,
        break_duration=break_duration
    )

    print("✅ Test completed successfully!")
    context.close()
    browser.close()

if __name__ == "__main__":
    with sync_playwright() as playwright:
        run(playwright)