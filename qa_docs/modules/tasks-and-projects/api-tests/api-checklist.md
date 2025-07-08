# Tasks and Projects Module – API Checklist

| №  | Check Item                                             | Type        | Priority | Status |
|----|---------------------------------------------------------|-------------|----------|--------|
| 1  | Create new project                                      | Functional  | High     |        |
| 2  | Edit project details                                    | Functional  | High     |        |
| 3  | Delete project                                          | Functional  | High     |        |
| 4  | Get project list with filters and pagination            | Functional  | High     |        |
| 5  | Create new task in project                              | Functional  | High     |        |
| 6  | Edit task details                                       | Functional  | High     |        |
| 7  | Delete task                                             | Functional  | High     |        |
| 8  | Get task list with filters and pagination               | Functional  | High     |        |
| 9  | Assign task to user                                     | Functional  | High     |        |
| 10 | Set task deadlines and priorities                       | Functional  | High     |        |
| 11 | Unauthorized access to endpoints returns 401            | Security    | High     |        |
| 12 | Role-based permissions enforced for creating/editing    | Security    | High     |        |
| 13 | Role-based permissions enforced for deleting            | Security    | High     |        |
| 14 | Validation against tampered IDs                         | Security    | High     |        |
| 15 | Enforce HTTPS-only connections                          | Security    | High     |        |
| 16 | Invalid request body returns validation error           | Negative    | Medium   |        |
| 17 | Attempt to assign task to non-existent user             | Negative    | Medium   |        |
| 18 | Attempt to delete non-existent project/task             | Negative    | Medium   |        |
| 19 | Retrieve large data set with pagination                 | Performance | Medium   |        |
| 20 | Bulk deletion operation performance acceptable          | Performance | Medium   |        |
| 21 | Rapid repeated create/edit/delete handled gracefully    | Performance | Medium   |        |

> 🔹 **Type:** Functional, Security, Negative, Performance  
> 🔸 **Priority:** High, Medium, Low  
> 🔘 **Status:** To be filled during testing