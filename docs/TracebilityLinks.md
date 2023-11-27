# Traceability Links

This document depicts the links between requirements and artifacts (use case diagrams, class diagrams, and activity diagrams).

## User Interactions Use Case Diagram Traceability

| Artifact ID | Artifact Name | Requirement ID |
| :---------: | :-----------: | :------------: |
| UseCase1 | Submit Query | FR1, |
| UseCase2 | Generate Response | NFR10 |
| UseCase3 | Create New User | NFR11 |
| UseCase4 | Update Custom Instruction | |
| UseCase5 | Login/Logout | NFR11 |
| UseCase6 | Take User Feedback | FR21 |

## Admin Interaction Use Case Diagram Traceability

| Artifact ID | Artifact Name | Requirement ID |
| :---------: | :-----------: | :------------: |
| UseCase7  | Train AI Model | FR3, FR4, FR13, FR17 |
| UseCase8  | Update User Role | FR15 |
| UseCase9  | Archive User Feedback | FR24 |
| UseCase10 | Review User Feedback | FR23, FR25, NFR19 |

## Overall Class Diagram Traceability

| Artifact Name | Requirement ID |
| :-----------: | :------------: |
| pdf_processor | FR3, FR8, NFR7 |
| store_manager | FR3 |
| user_handler | FR14, NFR17, NFR18, NFR20 |
| chat_chain | FR2, NFR4 |
| chroma | FR10 |

## Persistance Layer Class Diagram Traceability

| Artifact Name | Requirement ID |
| :-----------: | :------------: |
| Database | NFR13, NFR14 |
| User | FR12 |
| Role | FR11 |
| UserFeedback | FR21 |
| UploadedDoc | FR6, FR7 |
