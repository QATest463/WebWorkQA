import random
import re
import time


def start_break(page):
    print("➡️ Clicking Break icon to open modal")
    page.get_by_role("button").filter(has_text=re.compile(r"^$")).nth(1).click()
    print("✅ Break modal opened")

    print("➡️ Finding all available Break options")
    radios = page.get_by_role("radio").all()

    if not radios:
        raise Exception("❌ No break options found in modal")

    options = []
    for radio in radios:
        label = radio.locator("..").locator("span").inner_text().strip()
        options.append(label)
    print(f"✅ Found break policy")

    break_policy = random.choice(options)
    print(f"➡️ Randomly selected Break type: {break_policy}")

    page.get_by_role("radio", name=break_policy).check()

    print("➡️ Clicking Start Break")
    page.get_by_role("button", name="Start break").click()
    print("✅ Break started")
    time.sleep(61)
    print("⏳ Waiting 61 seconds")
    raw_timer_value = page.locator("#webwork-tracker-widget p").first.inner_text().strip()
    parts = raw_timer_value.split(":")
    hours = str(int(parts[0]))
    minutes = parts[1].zfill(2)
    break_duration = f"{int(hours)}:{minutes}"
    print(f"✅ Captured expected duration: {break_duration}")

    return break_policy, break_duration