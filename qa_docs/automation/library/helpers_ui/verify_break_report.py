import re
from datetime import datetime
from qa_docs.automation.library.helpers_ui import start_web_tracker
from qa_docs.automation.library.helpers_ui import login


def verify_break_report(page, user_name, break_policy, break_duration):

    print("➡️ Navigating to Reports > Breaks")
    page.get_by_role("link", name="Reports").click()
    page.get_by_role("link", name="Breaks").click()
    page.wait_for_url(re.compile(r".*/reports/breaks.*"))
    print("✅ Breaks page loaded")

    today_str = datetime.now().strftime("%b %d, %Y")
    print(f"Expecting date: {today_str}")

    page.wait_for_selector("div[role='row']")
    rows = page.locator("div[role='row']").filter(has_text=user_name)
    assert rows.count() > 0, "❌ No rows for user found!"

    found_valid = False
    for i in range(rows.count()):
        row = rows.nth(i)
        user = row.locator("div[role='gridcell'][col-id='member']").inner_text().strip()
        policy = row.locator("div[role='gridcell'][col-id='break_policy']").inner_text().strip()
        date = row.locator("div[role='gridcell'][col-id='date']").inner_text().strip()
        duration = row.locator("div[role='gridcell'][col-id='duration']").inner_text().strip()

        print(f"🔎 Row {i+1}: User='{user}', Policy='{policy}', Date='{date}', Duration='{duration}'")

        if (user == user_name and
            policy == break_policy and
            date == today_str and
            duration.startswith(break_duration)):
            found_valid = True
            print("✅ Break entry matches expected values!")
            break

    assert found_valid, "❌ No matching break entry found!"