# WebWorkQA 📋

**Modular Quality Assurance Documentation for the WebWork Time Tracking Platform**

This repository contains complete, scalable, and modular QA documentation for manual and automated testing of the WebWork platform.
It demonstrates best practices for both individual and collaborative QA work.

---

## 📦 Project Structure

- qa-docs/
  - automation/
    - api/
    - ui/
    - library/
  - assets/
  - modules/
    - time-tracking
      - api-tests/
        - api-test-cases/
          - positive/
          - negative/
          - performance/
          - security/
          - edge-cases/
        - postman_collection/
          - positive/
          - negative/
          - performance/
          - security/
          - edge-cases/
        - api-checklist.md
      - bug-reports/
        - closed/
        - fixed/
        - in-review/
        - open/
      - checklists/
        - functional-checklists.md
        - non-functional-checklists.md
      - exploratory-session-notes/
      - requirements-review-comments/
      - sql-backend-checks/
      - test-cases/
        - positive.md
        - negative-scenarios.md
        - performance.md
        - edge-cases.md
        - security-and-access.md
      - README.md
  - reports/
    - bug-reports/
      - functional/
      - non-functional/
    - sprint-reports/
  - templates/
  - README.md
ROADMAP.md
PROJECT_OVERVIEW.md

---

## 🛠️ In Progress
- `Time Tracking`
  - PyTest API automation
  - Exploratory testing documentation
  - SQL/backend validation checklists

## 🔜 Next Planned Modules

- Authentication 
- User Profile / Account Management
- Projects and Tasks

---

## 🧪 Tools Used

- [✔] **Manual Testing**
- [✔] **Postman** – REST API testing
- [✔] **Swagger** – API inspection and verification
- [✔] **DevTools** – Debugging, inspecting
- [✔] **Playwright (Python)** – UI automation
- [✔] **PyTest** – API automation 
- [✔] **Markdown** – Documentation
- [✔] **Git/GitHub** – Version control

---

## 🔄 Workflow & Guidelines

- All features are documented and tested incrementally by module
- Manual comes first: test cases, checklists, bugs, API
- Then: automation (UI + API)
- All documentation lives in Markdown for portability

---

## 👨‍💻 Author

**Vahe Hunanyan**  
QA Engineer | Manual + Automation  
Email: qatesting463@gmail.com  
Open to feedback and collaboration!