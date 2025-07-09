def go_to_dashboard(page):
    print("➡️ Go to Dashboard")
    page.goto("https://www.webwork-tracker.com/app/dashboard")
    page.wait_for_load_state("networkidle")