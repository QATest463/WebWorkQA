import time

def start_web_tracker(page):
    page.locator("#webwork-tracker-widget").get_by_role("button").first.click()
    print("✅ Pressed START, Waiting 61 seconds")
    time.sleep(3)