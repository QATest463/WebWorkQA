def delete_time_entry(page, start_time="09:00", project="Project 1", task="Task"):
    print("➡️ Navigating to Timesheets > Time Editor")
    page.get_by_role("link", name="Timesheets").click()
    page.get_by_role("link", name="Time Editor").click()

    print("➡️ Locating the added time entry row")
    entry_row = page.get_by_role("row", name=re.compile(fr"{start_time}.*{project}.*{task}"))
    entry_row.get_by_role("img").click()

    print("➡️ Confirming Delete")
    page.locator("div").filter(has_text=re.compile(r"^Delete$")).click()
    page.get_by_role("button", name="Yes").click()
    print("✅ Entry deleted")