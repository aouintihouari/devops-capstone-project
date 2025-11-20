**As a** API consumer
**I need** to retrieve customer account details via REST API
**So that** I can display user information in the frontend

**Details and Assumptions**
* The microservice uses Flask and Python 3.9+
* Database is PostgreSQL with SQLAlchemy ORM
* Authentication uses JWT tokens
* API follows REST conventions
* Response format is JSON

**Acceptance Criteria**

**Scenario 1: Successfully retrieve account**
Given I have a valid customer ID and authentication token
When I send a GET request to `/api/accounts/{customer_id}`
Then I receive a 200 response with the customer's account details in JSON format

**Scenario 2: Account not found**
Given I have an invalid customer ID
When I send a GET request to `/api/accounts/invalid_id`
Then I receive a 404 response with error message "Account not found"

**Scenario 3: Unauthorized access**
Given I have no valid authentication token
When I send a GET request to `/api/accounts/123`
Then I receive a 401 response with "Unauthorized" message