def stop_web_tracker(page):
    page.locator("#webwork-tracker-widget").get_by_role("button").first.click()
    print("✅ Clicking STOP")
    raw_time = page.locator("#webwork-tracker-widget p").first.inner_text().strip()
    parts = raw_time.split(":")
    hours = str(int(parts[0]))
    minutes = parts[1].zfill(2)
    stop_time_hm = f"{hours}:{minutes}"

    print(f"✅ Tracker stop time: {stop_time_hm}")

    return stop_time_hm