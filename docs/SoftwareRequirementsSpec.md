# Overview

The purpose of this document is describe the functional and nonfunctional requirements of the system to be developed. These requirements at this stage are not final and are open for additional edits.

# Functional Requirements

1. Query Processing
    1. The system shall accept text-based queries from the  user.
    2. The system shall utilize AI to process and analyze the queries.
    3. The system shall scan available PDF documents to find relavent information.
    4. The system shall return the most accurate and relevant answer to the user.

2. PDF Management
    1. The system shall allow the admin to upload new PDF documents.
    2. The system shall validate the uploaded documents to ensure they are in PDF format.
    3. The system shall securely store the uploadded PDF documents.
    4. The system shall update the databsae after every new PDF upload.

3. Log In
    1. Allow a user and a admin role.
    2. The system shall only allow admin's can process PDFs.
    3. The system shall have users and admins query.
    4. They system shall allow users to register.

4. Chat
    1. The system shall have a question/answer chat.
    2. The system shall persist last user chat.
    3. On next login, the system shall start user off where they left off.

# Non-Functional Requirements

1. The system shall be reachable over the internet.
2. The system shall responsive to user queries within a seconds.