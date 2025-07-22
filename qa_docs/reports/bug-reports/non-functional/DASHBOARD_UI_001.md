# 🐞 Bug Report

## 🆔 Bug ID
`DASHBOARD_UI_001`

## 📌 Title
**Inconsistent height in dashboard cards due to fixed container and button presence (e.g., Top Members, Today’s Activity)**

## 📝 Description
Dashboard cards such as **"Top Members"** and **"Today’s Activity"** exhibit inconsistent height and visual misalignment when placed in a row layout.
Both cards contain action buttons (e.g., `+ Invite Members`, `Download`), which may contribute to height being locked or incorrectly calculated.

Cards like “Productivity” remain at a fixed height (370px), while “Today’s Activity” and “Top Members” remain at a fixed height (443px), breaking the visual grid.

---

## 🧪 Precondition
- Brand new workspace with no tracked time or member activity
- No productivity or attendance data
- Browser window with standard resolution (e.g., 1440px+)
- Widgets "Top Members", "Productivity", and "Today's Activity" are placed on the same row via dashboard customization

---

## 🔁 Steps to Reproduce
1. Log into WebWork Tracker
2. Navigate to the **Dashboard**
3. Place the following widgets in one row:
   - Top Members
   - Productivity
   - Today’s Activity
4. Observe layout differences
5. Open DevTools → Inspect `.card-body` height
6. Resize browser window — note which cards adjust and which don’t

---

## ✅ Expected Result
- All cards in the same row should have consistent height
- Height should be flexible based on content and screen size

---

## ❌ Actual Result
- “Top Members” and “Today’s Activity” retain fixed height of `443px`
- "Productivity" widget adapts correctly
- Buttons inside cards (e.g., `+ Invite Members`) might influence this behavior

---

## 📸 Attachments
- 📷 Screenshot 1: Visual layout with misaligned heights
- 📷 Screenshot 2: DevTools → computed height 443px

---

## 🧪 Severity
`Minor` — cosmetic UI bug, does not block functionality but affects visual consistency

## 🧭 Priority
`Medium` — important for layout polish

## 🔄 Frequency
`Always`

## 📅 Date
2025-05-15

## 👤 Reported By
Vahe Hunanyan

## 🔁 Reproducibility
- ✅ macOS Chrome 125
- ✅ Safari (macOS Sonoma)
- ✅ Firefox 117

## 👤 Assigned To
—

---

## 🧱 Status
`Open`

## 📆 Deadline (Fix ETA)
—

## 🧩 Resolution Comment
Suggest checking container height styles, flex/grid wrapping logic, and influence of internal buttons.