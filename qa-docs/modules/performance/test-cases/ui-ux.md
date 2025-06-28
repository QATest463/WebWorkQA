# UI/UX Test Cases – Performance Module

| ID          | Title                                       | Precondition                        | Steps                                                         | Expected Result                           | Actual Result | Status |
|-------------|---------------------------------------------|-------------------------------------|---------------------------------------------------------------|-------------------------------------------|---------------|--------|
| PF-UX-001   | Progress indicators for long operations      | User logged in                      | 1. Trigger report generation <br> 2. Observe UI | Shows progress/loading indicator |               |        |
| PF-UX-002   | Feedback for loading states                  | User logged in                      | 1. Navigate between slow-loading pages | Clear loading messages displayed |               |        |
| PF-UX-003   | Avoid UI freezes during heavy operations     | User logged in                      | 1. Generate large report <br> 2. Interact with UI | UI remains responsive |               |        |
| PF-UX-004   | Accessible performance feedback              | User with accessibility needs       | 1. Trigger slow operation <br> 2. Use screen reader | Loading state announced clearly |               |        |
| PF-UX-005   | Responsive design during slow network        | User on mobile device               | 1. Simulate slow network <br> 2. Navigate app | Layout adapts well, no unstyled breaks |               |        |