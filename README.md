# Endee - Vector Search Engine (C++)

## Overview

Endee is a C++ based REST API for managing vector indexes and performing vector similarity search.

The project uses:
- Crow (C++ web framework)
- RESTful API design
- Bearer token authentication
- Vector index management

---

## Features Implemented

### 1. Health Check
GET /api/v1/health

Returns server status and timestamp.

---

### 2. Authentication Middleware
- Uses Bearer token authentication
- Protects all API routes
- Extracts username context from token

---

### 3. Process
1) Create Index
POST /api/v1/index/create

Creates a vector index with:
- index_name
- dimension
- space_type (e.g., cosine)

Example:

curl -X POST http://localhost:8080/api/v1/index/create \
-H "Content-Type: application/json" \
-H "Authorization: Bearer my-secret-token" \
-d '{"index_name":"my_index","dim":128,"space_type":"cosine"}'

2) Insert Vectors
   curl -X POST http://localhost:8080/api/v1/index/my_index/vector/insert \
-H "Authorization: Bearer my-secret-token" \
-H "Content-Type: application/json" \
-d '{
  "id": "vec1",
  "vector": [0.1, 0.2, 0.3, 0.4, 0.5]
}'


3) Search Vectors
4) curl -X POST http://localhost:8080/api/v1/index/my_index/search \
-H "Authorization: Bearer my-secret-token" \
-H "Content-Type: application/json" \
-d '{
  "vector": [0.1, 0.2, 0.3, 0.4, 0.5],
  "k": 2,
  "format": "json"
}'

---


### 4. List Indexes
GET /api/v1/index/list

Returns all indexes for authenticated user.

---

## Output
Further can be viewed in cat output.json 
<img width="1854" height="977" alt="Screenshot From 2026-03-02 00-45-25" src="https://github.com/user-attachments/assets/8c6ec058-127f-4106-8b39-71a2f805c650" />


## Architecture

- Multi-tenant design (username/index_name)
- Middleware-based authentication
- JSON request/response handling
- Modular route registration

---

## How to Run

./run.sh

Server runs at:

http://localhost:8080

Swagger UI available for API testing.

---

## Current Status

- Index creation: Working
- Index listing: Working
- Authentication: Working
- Vector insertion: Working
- Vector search: Working

---

## Future Work

- Add persistence
- Add better error handling
- Improve documentation
