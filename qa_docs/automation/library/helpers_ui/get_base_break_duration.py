import time
import random

def get_base_break_duration(page, user_name):
    print("➡️ Navigating to Reports/Breaks")
    page.get_by_role("link", name="Reports").click()
    page.get_by_role("link", name="Breaks").click()
    page.wait_for_url("**/reports/breaks")
    time.sleep(3)

    print("➡️ Opening Break Policy filter")
    page.wait_for_selector(".multipleSelection")
    page.locator(".multipleSelection", has_text="Break Policy").click()
    time.sleep(2)

    print("➡️ Collecting available Break Policies")
    options = page.locator("label:has(input[type='checkbox'])")
    option_count = options.count()

    available_policies = []
    for i in range(option_count):
        label_text = options.nth(i).inner_text().strip()
        if label_text and label_text.lower() not in ["all", "none", "break policy"]:
            available_policies.append(label_text)

    if not available_policies:
        raise Exception("❌ No Break Policies found!")

    print(f"✅ Found Policies: {available_policies}")

    break_policy = random.choice(available_policies)
    print(f"✅ Randomly selected Break Policy: {break_policy}")

    break_policy = random.choice(available_policies)
    print(f"✅ Randomly selected Break Policy: {break_policy}")

    options.get_by_text(break_policy, exact=True).click()
    time.sleep(2)

    print("➡️ Checking existing durations")
    base_duration = "0:00"
    rows = page.locator("div[role='row']").filter(has_text=user_name)
    if rows.count() > 0:
        for i in range(rows.count()):
            row = rows.nth(i)
            policy_text = row.locator("div[role='gridcell'][col-id='break_policy']").inner_text().strip()
            if policy_text == break_policy:
                base_duration = row.locator("div[role='gridcell'][col-id='duration']").inner_text().strip()
                break
    print(f"✅ Base duration: {base_duration}")

    return break_policy, base_duration