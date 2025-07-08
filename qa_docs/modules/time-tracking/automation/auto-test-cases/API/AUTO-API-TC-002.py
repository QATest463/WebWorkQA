import pytest
import requests

# === CONFIGURATION ===
# Base URLs for different WebWork API services
BASE_URL = "https://realtime.webwork-tracker.com"
SELECTED_DATA_URL = "https://background.webwork-tracker.com/api/selected-data"

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


# === FIXTURES ===
# Shared storage for timelineId between tests in one session
@pytest.fixture(scope="module")
def timeline_id():
    return {"id": None}

# === TESTS ===
# Add Manual Time
def test_01_add_manual_time_entry(timeline_id):
    url = f"{BASE_URL}/api/add-time/create"
    payload = {
        "user_id": USER_ID,
        "contract_id": 599327,
        "task_id": 0,
        "date": "2025-06-30",
        "time_interval": [
            {
                "start": "10:00",
                "end": "11:00",
                "errors": {},
                "index": 1
            }
        ],
        "notes": "1011",
        "isManual": True,
        "returnTimeline": True,
        "filter": {
            "projectsId": [],
            "tasksId": [],
            "startDate": "2025-06-30",
            "endDate": None
        }
    }

    resp = requests.post(url, json=payload, headers=AUTH_HEADERS)
    assert resp.status_code == 200

    # You should extract timelineId from resp.json() in real usage
    timeline_id["id"] = 359480933

    print(f"Added timelineId: {timeline_id['id']}")

# Edit Time
def test_02_edit_manual_time_entry(timeline_id):
    url = f"{BASE_URL}/api/edit-timesheet/time-range"
    payload = {
        "timelineId": timeline_id["id"],
        "date": "2025-06-30",
        "start": "10:00",
        "end": "12:00",
        "user_id": USER_ID,
        "tasksId": [],
        "projectsId": []
    }

    resp = requests.patch(url, json=payload, headers=AUTH_HEADERS)
    assert resp.status_code == 200
    print("Edited timeline successfully")

# Delete time
def test_03_delete_manual_time_entry(timeline_id):
    url = f"{BASE_URL}/api/edit-timesheet/delete-timeline"
    payload = {
        "timelineId": timeline_id["id"],
        "timelineFilter": {
            "user_id": USER_ID,
            "timezone": None,
            "tasksId": [],
            "projectsId": [],
            "startDate": "2025-06-30",
            "endDate": None
        }
    }

    resp = requests.delete(url, json=payload, headers=AUTH_HEADERS)
    assert resp.status_code == 200
    print("Deleted timeline successfully")


def test_04_verify_deleted_from_selected_data(timeline_id):
    url = SELECTED_DATA_URL
    resp = requests.get(url, headers=AUTH_HEADERS)
    assert resp.status_code == 200
    data = resp.json().get("result", [])

    ids = [item["_id"] for item in data if "_id" in item]
    assert timeline_id["id"] not in ids
    print(f"Verified timelineId deleted: {timeline_id['id']}")