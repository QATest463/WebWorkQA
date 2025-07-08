import re

def go_to_timeline(page, user_name, selected_project, stop_time_hm):
    print("➡️ Going to Timeline")
    page.get_by_role("link", name="Reports").click()
    page.get_by_role("link", name="Timeline").click()
    page.wait_for_url(re.compile(r".*/reports/timeline.*"))
    page.wait_for_selector("div[role='row']")
    print("✅ Timeline loaded")
    rows = page.locator("div[role='row']").filter(has_text=user_name)

    assert rows.count() > 0, f"❌ No rows with User '{user_name}' found!"

    found_valid = False
    for i in range(rows.count()):
        row = rows.nth(i)
        actual_user = row.locator("div[role='gridcell'][col-id='member']").inner_text().strip()
        actual_project = row.locator("div[role='gridcell'][col-id='project']").inner_text().strip()
        raw_time = page.locator("#webwork-tracker-widget p").first.inner_text().strip()
        parts = raw_time.split(":")
        hours = str(int(parts[0]))
        minutes = parts[1].zfill(2)
        actual_time = f"{hours}:{minutes}"

        if actual_project != selected_project:
            continue

        print(f"🔎 Row {i + 1}: User='{actual_user}', Project='{actual_project}', Time='{actual_time}'")

        if actual_user == user_name and actual_project == selected_project and actual_time == stop_time_hm:
            found_valid = True
            print("✅ Found matching row!")
            break

    assert found_valid, f"❌ No matching entry found for User with project='{selected_project}' and time='{stop_time_hm}'!"
    print("✅ All Timeline checks passed!")