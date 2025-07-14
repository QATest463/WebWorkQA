# ✅ UI Automation – Test Flow Cases

This document describes the **TestFlow Cases** implemented in UI automation using Playwright.  
Each TestFlow represents a realistic user scenario that automates a complete flow from login to verification.

> ✅ Notes:
> - All cases use Python + Playwright
> - Headless=False for visible debugging
> - Test data and credentials are managed in the helpers

---

## 📋 TestFlow Cases

| ID             | Title                                      | Steps Summary                                                                                                                                                             | Verification / Expected Result                                                 |
|----------------|--------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| AUTO-UI-PS-001 | Start/Stop Web Tracker with Task Selection | - Login <br> - Select Project and Task <br> - Start Tracker <br> - Stop Tracker <br> - Navigate to Timeline                                                             | Timeline shows new entry with correct project/task and time                    |
| AUTO-UI-PS-002 | Add, Edit, Delete Manual Time Entry        | - Login <br> - Quick Add Time Entry (Project/Task/Time/Description) <br> - Navigate to Timeline <br> - Edit Time in Timesheets <br> - Delete Entry <br> - Recheck Timeline | Timeline updates correctly after add/edit/delete                               |
| AUTO-UI-PS-003 | Start/Stop Break from Tracker              | - Login <br> - Start Break with Random Policy <br> - Stop Break <br> - Stop Web Tracker                                                                                   | Break Report shows new break duration for selected policy and date             |
| AUTO-UI-PS-004 | Add Manual Break via Quick Add Modal       | - Login <br> - Navigate to Reports > Breaks <br> - Select Break Policy from Filter <br> - Open Quick Add > Time Entry > Add Break Tab <br> - Enter Date/User/Policy/Time | Break Report shows new manual break entry with correct user/policy/date/duration |

---

## ✅ ⚠️ Notes about Break Reports

- The Breaks report aggregates **total duration per user, policy, date**.
- Adding overlapping or repeated intervals may merge in the report.
- Automation check verifies presence of today's Break entry with expected policy.
- Exact duration increase is not guaranteed if pre-existing entries exist.