# Overview

The purpose of this document is describe the functional and nonfunctional requirements of the system to be developed. These requirements at this stage are final.

# Software Requirements

Below are a list of both functional and non-funcational requiremnts for the new system.

## Functional Requirements

### Query Processing

| ID | Requirement |
| ---- | ----------- |
| FR1  | The system shall accept text-based queries from the user. |
| FR2  | The system shall utilize a LLM to process and analyze the queries. |
| FR3  | The system shall only utilize content from PDF documents to answer user queries. |
| FR4  | The system shall return the most accurate and relevant answer to the user. |
| FR5  | The system shall provide user-friendly error messages for invalid queries or no results found. |

### PDF Management

| ID | Requirement |
| ---- | ----------- |
| FR6  | The system shall allow new PDF uploads. |
| FR7  | The system shall allow any uploaded PDF to be deleted. |
| FR8  | The system shall validate uploaded documents are in PDF format. |
| FR9  | The system shall convert each PDF to an embedding. |
| FR10 | The system shall persist each converted PDF embedding. |

### User Authentication and Authorization

| ID | Requirement |
| ---- | ----------- |
| FR11 | The system shall support two user roles: admin and user. |
| FR12 | The system shall persist user information, including username, hashed password, and role. |
| FR13 | The system shall only allow admins to process PDFs. |
| FR14 | The system shall allow any user to register. |
| FR15 | The system shall allow admins to manage user roles and permissions. |

### Chat

| ID | Requirement |
| ---- | ----------- |
| FR16 | The system shall provide a question/answer chat interface. |
| FR17 | The system shall respond with "I am not sure on this" when asked a question outside of its context. |
| FR18 | The system shall persist the user's last chat history. |
| FR19 | The system shall allow user to reset chat history. |
| FR20 | Upon the user's next login, the system shall resume the chat from where the user left off. |

### User Feedback

| ID | Requirement |
| ---- | ----------- |
| FR21 | The system shall allow users to leave feedback at any point. |
| FR22 | The system shall persist user feedback for admin review. |
| FR23 | The system shall allow admins to review user feedback. |
| FR24 | The system shall allow admins to archive reviewed user feedback. |
| FR25 | The system shall allow admins to review archived user feedback. |

## Non-Functional Requirements

### Performance

| ID | Requirement |
| ----- | ----------- |
| NFR1  | The system shall have a response time for user queries of less than 2 seconds. |
| NFR2  | The system shall be capable of handling multiple users concurrently without performance egradation. |
| NFR3  | The system shall be scalable to accommodate future growth in terms of data storage and user base. |
| NFR4  | The system shall stream real-time updates for chat responses. |
| NFR4  | The system shall be tested thoroughly using automated unit tests, integration tests, and user acceptance tests. |
| NFR5  | The system shall have a responsive customer support team available during business hours to address user inquiries and issues. |

### Compatibility and Technology

| ID | Requirement |
| ----- | ----------- |
| NFR6  | The system shall be compatible with Python 3.8 or higher. |
| NFR7  | The system shall use an up-to-date PDF parsing library to ensure compatibility with the latest PDF formats. |
| NFR8  | The system shall adhere to industry best practices for code quality, including code reviews and coding standards. |
| NFR9  | The system shall be designed with accessibility in mind to ensure compliance with accessibility standards. |
| NFR10 | The system shall use the latest version of the LLM framework for query processing. |

### Security and Compliance

| ID | Requirement |
| ----- | ----------- |
| NFR11 | The system shall implement role-based access control for user authentication and authorization. |
| NFR12 | The system shall minimize the use of external dependencies to reduce the risk of third-party service failures. |
| NFR13 | The system shall use encryption to secure store user passwords. |
| NFR14 | The system shall comply with relevant data privacy regulations. |
| NFR15 | The system shall have a robust logging and monitoring system to facilitate debugging and issue resolution. |

### User Experience and Design

| ID | Requirement |
| ----- | ----------- |
| NFR16 | The system's codebase shall be well-documented following industry-standard practices. |
| NFR17 | The system's user interface shall be responsive and compatible with modern web browsers. |
| NFR18 |  |
| NFR19 |  |
| NFR20 |  |

### Maintenance and Operations

| ID | Requirement |
| ----- | ----------- |
| NFR21 | The system shall undergo regular security audits and updates to protect against vulnerabilities. |
| NFR22 | The system shall log and monitor system and application-level metrics for performance analysis. |
| NFR23 | The system shall provide a seamless user experience with minimal downtime during updates and maintenance. |
| NFR24 | The system shall have a mechanism for automated deployment and continuous integration/continuous deployment (CI/CD). |
| NFR25 | The system shall have a well-documented maintenance plan for system administrators. |
