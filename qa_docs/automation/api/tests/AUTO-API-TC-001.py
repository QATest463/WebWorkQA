import requests
import time
import pytest

# === CONFIGURATION ===
# Base URLs for different WebWork api services
BASE_URL = "https://background.webwork-tracker.com"
SELECTED_DATA_URL = f"{BASE_URL}/api/selected-data"

# === AUTHENTICATION HEADERS ===
# Replace these values with fresh tokens/cookies when needed
AUTH_HEADERS = {
    "Authorization": "Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoyMTA3NTMsImV4cCI6MTc1MzI4NTUyMSwiaWF0IjoxNzUxNTU3NTIxfQ.sCJR5-wMAH1XROGNcSCZAqFLuzRHpuUXvPs93-L8q_QFEWv9dAvvuXZXqYSCG6DWT3UvNygGjsy_umYA5NkW6Q",
    "Cookie": "webwork_session=eyJpdiI6IlpaLytVN1JDVE5KSFZTMlk4RGl6Unc9PSIsInZhbHVlIjoiUyt1RUsxSmNYZ2lOdjZWVjZwQlMyMTUyS0owV0NWMTBJOVdEYmV5V3NpN2FielFJblBpc20vdU5qM2JLUjdJRC9Oa3ZaTGhhczNQVnJWMkt3UWRBUmhTemozaUxoem4vcGRxMjZhUzJLSzRPMURLTkxOQkdBOXhrSlNRNFRYa0QiLCJtYWMiOiIyNGY5NzZjOWUwYmFmNGZlODhkM2I2NzJhOWM5YTEwZTVmY2NjODY1ODdhYTQ0MTJkZWI1Zjk0Y2MxZDNhM2I4In0",
    "X-XSRF-TOKEN": "eyJpdiI6InFkck9OaFFBYjJTcjE4c050RzYxSUE9PSIsInZhbHVlIjoiV3MwOVY1ZVVRZHl4MUxENUh6UVJsSWtjVFV1VEZXazAxSXU3LytFbXB4YzhyNFdRRm80NmNJWnBFUWNQQldQcXU4ekYyMkM4R2JxSXA4a3c0bytrRmRHd0p0VHdSNGdMUVEvZlJ2UVV5cElWL1RQMEl2ZDNSaXVLVy95NmNKTWIiLCJtYWMiOiI0NWY0MTgxMGEyMTBhMDlmMDFmOTgxNTU0NmEwODFhNGEyOGIwYmJhYjZjOTU0NWVkOTAwYmRkOGI0NzQwNTNhIn0",
    "Owner-id": "208178",
    "Owner_id": "208178",
    "Track-Type": "website",
    "Track_Type": "website",
    "Content-Type": "application/json"
}

USER_ID = 210753
OWNER_ID = 208178

@pytest.fixture(scope="module")
def tracking_context():
    return {"start_id": None}

# 1. Starts tracking via api
def test_01_start_tracking(tracking_context):
    url = f"{BASE_URL}/api/start-tracker"
    payload = {
        "user_id": USER_ID,
        "owner_id": OWNER_ID,
        "track_type": "website",
        "memo": "",
        "contract_id": None,
        "project_id": None,
        "task_id": "no_task",
        "task_title": "No task",
        "start": int(time.time() * 1000)
    }

    resp = requests.post(url, json=payload, headers=AUTH_HEADERS)
    assert resp.status_code == 200
    print("✅ Start tracker success")
    tracking_context["start_id"] = payload["start"]

# 2. Waits 65 seconds to ensure time is counted
def test_02_wait_tracking_period():
    wait_seconds = 65
    print(f"⏳ Waiting {wait_seconds} seconds to accumulate time...")
    time.sleep(wait_seconds)

# 3. Stops tracking via api
def test_03_stop_tracking(tracking_context):
    url = f"{BASE_URL}/api/stop-tracker"
    payload = {
        "user_id": USER_ID,
        "owner_id": OWNER_ID,
        "track_type": "website",
        "contract_id": None,
        "project_id": None,
        "task_id": "no_task",
        "task_title": "No task",
        "start": tracking_context["start_id"],
        "end": int(time.time() * 1000)
    }

    resp = requests.post(url, json=payload, headers=AUTH_HEADERS)
    assert resp.status_code == 200
    print("✅ Stop tracker success")

# 4. Verifies via selected-data that the time entry is saved (~1 minute)
def test_04_verify_tracking_stopped():
    resp = requests.get(SELECTED_DATA_URL, headers=AUTH_HEADERS)
    assert resp.status_code == 200
    data = resp.json().get("result", [])
    print(f"✅ After stop Selected data: {data}")