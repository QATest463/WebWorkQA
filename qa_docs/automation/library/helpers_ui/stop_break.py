import time

def stop_break(page):

    page.locator("#webwork-tracker-widget").get_by_role("button").first.click()
    print("✅ Break stopped")
    time.sleep(2)