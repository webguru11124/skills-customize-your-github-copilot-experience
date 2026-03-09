# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn the fundamentals of building REST APIs using the FastAPI framework in Python. Students will create API endpoints, handle HTTP requests and responses, and use Pydantic for data validation.

## 📝 Tasks

### 🛠️ Set Up FastAPI Application

#### Description
Install FastAPI and create a basic application with a root endpoint that returns a welcome message.

#### Requirements
Completed program should:

- Install FastAPI and Uvicorn using pip
- Create a FastAPI app instance
- Define a GET endpoint at "/" that returns a JSON response with a welcome message
- Run the server using Uvicorn and verify the endpoint works

### 🛠️ Create CRUD Endpoints for Items

#### Description
Implement Create, Read, Update, and Delete (CRUD) operations for a simple "item" resource using FastAPI endpoints.

#### Requirements
Completed program should:

- Define Pydantic models for Item (with id, name, description)
- Create a POST endpoint to add new items
- Create a GET endpoint to retrieve all items or a specific item by ID
- Create a PUT endpoint to update an existing item
- Create a DELETE endpoint to remove an item
- Use an in-memory list to store items (no database required)

### 🛠️ Add Path and Query Parameters

#### Description
Enhance the API by adding path parameters for item IDs and query parameters for filtering results.

#### Requirements
Completed program should:

- Modify GET endpoint to accept an optional item ID as a path parameter
- Add query parameters to filter items by name or description
- Ensure proper error handling for non-existent items
- Test all endpoints with different parameter combinations