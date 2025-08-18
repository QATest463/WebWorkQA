# 🕵️‍♂️ Exploratory Session Notes – Time Tracking Module

This folder contains **session-based exploratory testing notes** for the **Time Tracking** module of WebWork.

Exploratory testing complements scripted test cases by uncovering **unexpected behaviors, edge cases, and usability issues** in a flexible, unscripted way.

---

## ✅ What is covered here

- Session-based notes with **charters, observations, and issues found**
- Ad hoc test ideas and paths explored
- Bugs or UX feedback discovered during free exploration
- Test environment, build version, and context
- Ideas for future structured test cases

---

## 🗂️ Folder Structure

| File                           | Description                                       |
|--------------------------------|---------------------------------------------------|
| `session-nomber-YYYY-MM-DD.md` | Notes from specific exploratory testing session   |
| `charters.md`                  | Planned exploratory charters and test ideas       |
| `issues-found.md`              | Bugs or observations raised during exploration    |
| `ideas-for-next-session.md`    | Ideas and questions to investigate next time      |

---

## 📌 Recommended structure for a single session note

Example template for **session-001-2025-07-10.md**:

# Exploratory Session Notes #001 – 2025-07-10

## 🎯 Charter
Test adding and editing manual Break entries in Time Tracking.

## 🧭 Setup / Environment
- WebWork Staging URL
- Build: v3.12.0
- Logged in as: QA Tester (Team Manager role)

## 🔎 Test Ideas
- Add Break with valid data
- Add Break with missing policy
- Edit Break to overlap with other time
- Switch between Add Time and Add Break tabs

## ✅ Observations
- Break modal opens quickly
- Can select policy from dropdown
- Validation error for missing fields shown clearly

## 🐞 Issues Found
- Placeholder text for Break Policy sometimes missing
- Switching tabs resets entered data unexpectedly

## 💡 Suggestions
- Improve placeholder consistency
- Add confirmation dialog on Close button

## ➡️ Notes for Next Session
- Test on mobile view
- Check performance with large number of Break Policies


---

## 🌟 How to use this folder

✅ Create one file per session with date in the filename.<br>
✅ Capture both planned charters and unexpected findings.<br>
✅ Include bugs found even if they’ll go to separate bug report files.<br>
✅ Add ideas for future sessions.

---

## 🧪 Benefits of Exploratory Notes

- Finds real-world usage problems
- Documents tester thinking
- Supplements scripted test cases
- Supports learning about the system
- Helps QA teams see coverage gaps

---

🧑‍💻 Author

"Name" QA Engineer