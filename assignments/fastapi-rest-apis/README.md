# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Practice building a REST API using the FastAPI framework to create endpoints, validate request data, and return JSON responses.

## 📝 Tasks

### 🛠️ Create API Endpoints

#### Description

Build the core FastAPI application with endpoints to manage a simple resource collection.

#### Requirements
Completed program should:

- Define a FastAPI application instance
- Create at least three endpoints, such as `GET /items`, `GET /items/{id}`, and `POST /items`
- Use JSON responses for all endpoints
- Include at least one endpoint that accepts request body data

### 🛠️ Add Validation and Query Parameters

#### Description

Add request validation using Pydantic models and support query parameters to filter or limit results.

#### Requirements
Completed program should:

- Use Pydantic models for request validation and response schemas
- Accept query parameters such as `limit` and `search`
- Return filtered or paginated results based on query params
- Handle invalid input with appropriate HTTP error responses
