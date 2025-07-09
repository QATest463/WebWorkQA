# 📦 Functional Postman Collection – Time Tracking Module

This folder contains the **exported Postman collection** for **Functional API tests** of the WebWork Time Tracking module.

---

## ✅ Collection Name
**TT-API-FN**

> "Collection to test all Time Tracking API endpoints for WebWork."

---

## ✅ How to use

1️⃣ Open Postman.  
2️⃣ Click **Import**.  
3️⃣ Select the JSON file in this folder (e.g. `TT-API-FN.postman_collection.json`).  
4️⃣ Use the Collection Runner or manually test individual requests.  

---

## ✅ Requirements

- Set up your Postman **Environment** with these variables:

| Variable     | Example / Notes                           |
| ------------- | ------------------------------------------ |
| `baseUrl`     | e.g. `https://api.webwork-tracker.com`     |
| `auth`        | Bearer token for authenticated requests    |
| `ownerId`     | Your owner ID                             |
| `trackType`   | Tracking type (e.g. `website`)            |
| `manualTime`  | Base URL for manual time endpoints        |
| `userId`      | ID of the user                            |
| `contractId`  | Contract ID                               |
| `date`        | Date for time entry (format: YYYY-MM-DD)  |
| `startTime`   | Start time (HH:mm)                        |
| `endTime`     | End time (HH:mm)                          |
| `Id`          | Saved timeline ID for edits/deletes       |

---

## ✅ Included Requests

| ID            | Name                      | Method | Endpoint                                 | Description                               |
| -------------- | ------------------------ | ------ | ---------------------------------------- | ----------------------------------------- |
| TT-API-FN-001  | Start Tracker            | POST   | `/api/start-tracker`                     | Starts time tracking                      |
| TT-API-FN-002  | Stop Tracker             | POST   | `/api/stop-tracker`                      | Stops time tracking                       |
| TT-API-FN-003  | Get Selected Data        | POST   | `/api/selected-data`                     | Fetch selected time tracking data         |
| TT-API-FN-004  | Add Manual Time          | POST   | `/api/add-time/create`                   | Adds a new manual time entry              |
| TT-API-FN-005-1 | Add Manual Time (for Edit) | POST | `/api/add-time/create/data`              | Creates time entry for editing tests      |
| TT-API-FN-005-2 | Edit Manual Time        | POST   | `/api/edit-timesheet/time-range`         | Edits existing manual time entry          |
| TT-API-FN-006-1 | Add Manual Time (for Delete) | POST | `/api/add-time/create/data`             | Creates time entry for delete tests       |
| TT-API-FN-006-2 | Delete Manual Time      | POST   | `/api/edit-timesheet/delete-timeline`    | Deletes an existing time entry            |

---

## ✅ Test Scripts Included

- Status code assertions (200 / 201)  
- Validation of response structure:
  - Presence of `result`, `data`, `need_update`, etc.
  - Ensures returned JSON contains required fields
- Saving environment variables like `Id` for chaining requests

---

## ✅ Purpose

⭐️ This collection serves as the **source of truth** for all *Functional* API tests in the Time Tracking module.

⭐️ It can be:
- Imported to Postman for manual testing
- Used as a spec for writing automated tests (e.g. PyTest + Requests)
- Shared with teammates and stakeholders

---

> **📌 Note:**  
> All requests are designed to work with the appropriate environment variables.  
> Make sure to configure your environment before running the collection.

---