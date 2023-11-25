# Overview

The purpose of this document is describe the functional and nonfunctional requirements of the system to be developed. These requirements at this stage are final.

# Functional Requirements

1. Query Processing
    1. The system shall accept text-based queries from the user.
    2. The system shall utilize a LLM to process and analyze the queries.
    3. The system shall only utilize content from PDF documents to answer user queries.
    4. The system shall return the most accurate and relevant answer to the user.
    5. The system shall provide user-friendly error messages for invalid queries or no results found.

2. PDF Management
    1. The system shall allow new PDF uploads.
    2. The system shall allow any uploaded PDF to be deleted.
    3. The system shall validate uploaded documents are in PDF format.
    4. The system shall convert each PDF to an embedding.
    5. The system shall persist each converted PDF embedding.

3. User Authentication and Authorization
    1. The system shall support two user roles: admin and user.
    2. The system shall persist user information, including username, hashed password, and role.
    3. The system shall only allow admins to process PDFs.
    4. The system shall allow any user to register.
    5. The system shall allow admins to manage user roles and permissions.

4. Chat
    1. The system shall provide a question/answer chat interface.
    2. The system shall persist the user's last chat history.
    3. The system shall allow user to reset chat history.
    4. Upon the user's next login, the system shall resume the chat from where the user left off.
    5.

5. User Feedback
    1. The system shall allow users to leave feedback at any point.
    2. The system shall persist user feedback for admin review.
    3. The system shall allow admins to review user feedback.
    4. The system shall allow admins to archive reviewed user feedback.
    5. The system shall allow admins to review archived user feedback.

# Non-Functional Requirements

1. Section 1
    1.
    2.
    3.
    4.
    5.

2. Section 2
    1.
    2.
    3.
    4.
    5.

3. Section 3
    1.
    2.
    3.
    4.
    5.

4. Section 4
    1.
    2.
    3.
    4.
    5.

5. Section 5
    1.
    2.
    3.
    4.
    5.
