def quick_add_modal(page):
    print("➡️ Clicking Quick Add")
    page.locator(".dropdown.d-flex.align-items-center").click()

    print("➡️ Selecting 'Time entry'")
    page.get_by_text("Time entry", exact=True).click()

    print("➡️ Waiting for modal")
    page.wait_for_selector("[role='dialog']:not(.d-none)")
    print("✅ Modal opened")