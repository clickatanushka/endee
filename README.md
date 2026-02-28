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

### 3. Create Index
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

---

### 4. List Indexes
GET /api/v1/index/list

Returns all indexes for authenticated user.

---

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
- Vector insertion: In progress
- Vector search: In progress

---

## Future Work

- Complete vector add endpoint
- Implement vector search
- Add persistence
- Add better error handling
- Improve documentation
