import time
import random
from datetime import datetime

def add_manual_break(page, user_name, break_policy, base_duration):
    print("➡️ Switching to Add Break tab")
    page.get_by_role("tab", name="Add Break").click()
    time.sleep(1)

    today_str = datetime.now().strftime("%b %d, %Y")
    page.get_by_label("Date").fill(today_str)
    print(f"✅ Filled Date: {today_str}")

    print(f"➡️ Selecting User: {user_name}")
    page.locator("input.selected-input").nth(0).click()
    time.sleep(1)
    page.locator(".options-item", has_text=user_name).click()
    time.sleep(1)

    print(f"➡️ Selecting Break Policy: {break_policy}")
    page.get_by_placeholder("Select break policy").click()
    page.locator(".options-item", has_text=break_policy).click()
    time.sleep(1)

    start_minute = random.randint(0, 55)
    interval_minutes = random.randint(1, 5)
    end_minute = start_minute + interval_minutes
    if end_minute >= 60:
        end_minute -= 60

    start_time = f"12:{start_minute:02d}"
    end_time = f"12:{end_minute:02d}"
    print(f"➡️ Start Time: {start_time}, End Time: {end_time}")

    page.get_by_role("textbox", name="hh:mm").first.fill(start_time)
    page.get_by_role("textbox", name="hh:mm").nth(1).fill(end_time)
    time.sleep(1)

    print("➡️ Clicking Add button")
    page.get_by_role("button", name="Add").click()
    time.sleep(3)

    h, m = map(int, base_duration.split(":"))
    total = h * 60 + m + interval_minutes
    break_duration = f"{total // 60}:{total % 60:02d}"
    print(f"✅ Break duration Date: {break_duration}")
    time.sleep(5)

    return break_duration, today_str