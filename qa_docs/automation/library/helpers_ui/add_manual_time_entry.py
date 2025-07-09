from qa_docs.automation.library.helpers_ui.quick_add_modal import quick_add_modal

def add_manual_time_entry(page, project="Project 1", task="Task", start_time="09:00", end_time="10:00", description="text1"):

    quick_add_modal(page)

    print("➡️ Selecting Project")
    page.get_by_role("dialog", name="Add Time close icon").locator("img").nth(3).click()
    page.locator("#simple-popover").get_by_text(project).click()

    print("➡️ Selecting Task")
    page.locator("[role='dialog']").locator("img").nth(4).click()
    page.locator("#simple-popover").get_by_text(task).click()

    print("➡️ Setting start and end time")
    page.get_by_role("textbox", name="hh:mm").first.fill(start_time)
    page.get_by_role("textbox", name="hh:mm").nth(1).fill(end_time)

    print("➡️ Adding description")
    desc_input = page.get_by_placeholder("Activity description")
    desc_input.fill(description)
    desc_input.press("Enter")

    print("✅ Saving entry")
    page.get_by_role("button", name="Add").click()