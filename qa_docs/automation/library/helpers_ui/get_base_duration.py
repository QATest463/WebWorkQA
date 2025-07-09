import re

def get_base_duration_from_beak(page, user_name, break_policy):
    print("➡️ Navigating to Reports/Breaks")
    page.get_by_role("link", name="Reports").click()
    page.get_by_role("link", name="Breaks").click()
    page.wait_for_url(re.compile(r".*/reports/breaks.*"))
    page.wait_for_selector("div[role='row']")

    rows = page.locator("div[role='row']").filter(has_text=user_name)
    for i in range(rows.count()):
        row = rows.nth(i)
        policy = row.locator("div[role='gridcell'][col-id='break_policy']").inner_text().strip()
        if policy == break_policy:
            duration = row.locator("div[role='gridcell'][col-id='duration']").inner_text().strip()
            print(f"✅ Found existing duration for policy '{break_policy}': {duration}")
            return duration

    print(f"⚠️ No existing entries found for policy '{break_policy}'. Using 0:00")
    return "0:00"