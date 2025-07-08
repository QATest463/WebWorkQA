def edit_time_entry(page, new_end_time="10:30"):
    print("➡️ Navigating to Timesheets > Time Editor")
    page.get_by_role("link", name="Timesheets").click()
    page.get_by_role("link", name="Time Editor").click()

    print(f"➡️ Editing end time to {new_end_time}")
    page.get_by_placeholder("hh:mm").nth(1).click()
    page.get_by_placeholder("hh:mm").nth(1).fill(new_end_time)
    page.locator(".page-content").click()
    print("✅ Edited time")