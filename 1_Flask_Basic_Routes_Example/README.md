# RESTful API Overview

## 📘 Introduction

A **RESTful API (Representational State Transfer)** is a web service that allows communication between client and server
through standard HTTP methods. REST APIs use predictable, stateless operations and are widely used in modern web and
mobile applications.

### Predictable Operations

RESTful APIs follow standard conventions for how resources are accessed and manipulated, making behavior easy to
understand and expect.
Key principle: Use HTTP methods consistently and clearly:

GET — retrieve data (should not change state)
POST — create a new resource
PUT — update a resource entirely
PATCH — update a part of the resource
DELETE — delete a resource

### Stateless Operations

Each request from a client to a server must contain all the information needed to understand and process the request.
The server does not store any client context between requests.

This API demonstrates the principles of REST using various HTTP methods and URL patterns to handle data in a simple and
structured way.

---

## 🌐 Base URL

```
http://127.0.0.1:8181
```

All API requests should be made relative to this base URL.

---

## 🧭 RESTful Principles

* **Stateless**: Each request contains all the information needed to process it.
* **Resources**: Represented using URIs (e.g., `/api/users/1`)
* **HTTP Methods**: Indicate the desired action:

    * `GET` → Retrieve data
    * `POST` → Create new data
    * `PUT` → Replace data
    * `PATCH` → Modify data
    * `DELETE` → Remove data

---

## 🚀 Available Endpoints

### 🔹 Basic Test

| Method | Endpoint           | Description                      |
|--------|--------------------|----------------------------------|
| GET    | `/`                | Returns a simple welcome message |
| GET    | `/api/get_example` | Returns a sample JSON message    |

---

### 🔸 Query Parameters

| Method | Endpoint                                    | Description                                           |
|--------|---------------------------------------------|-------------------------------------------------------|
| GET    | `/api/query_example?name=John`              | Returns a greeting using a query parameter            |
| GET    | `/api/multi_query_example?name=John&age=25` | Returns a greeting with name and age                  |
| GET    | `/api/default_query_example`                | Same as above but with default values if not provided |

---

### 🔸 URL Parameters

| Method | Endpoint                               | Example                         | Description                       |
|--------|----------------------------------------|---------------------------------|-----------------------------------|
| GET    | `/api/url_example/<name>/<age>`        | `/api/url_example/Alice/30`     | Uses name and age in the URL      |
| GET    | `/api/other_url_example/<ids>/<score>` | `/api/other_url_example/1/95.5` | Uses integer and float in the URL |

---

### 🔸 Request Body (JSON)

| Method | Endpoint              | Description                           |
|--------|-----------------------|---------------------------------------|
| POST   | `/api/post_example`   | Accepts JSON to create or submit data |
| PUT    | `/api/put_example`    | Accepts JSON to replace/update data   |
| DELETE | `/api/delete_example` | Accepts JSON to delete specific data  |
| PATCH  | `/api/patch_example`  | Accepts JSON to partially update data |

**Example Request Body (JSON):**

```json
{
  "name": "John",
  "age": 30
}
```

---

### 🔸 Dynamic Route with Multiple Methods

| Method                    | Endpoint                     | Description                                                         |
|---------------------------|------------------------------|---------------------------------------------------------------------|
| GET/POST/PUT/DELETE/PATCH | `/api/dynamic_example/<ids>` | Handles different operations based on HTTP method for a resource ID |

---

### What Does Idempotent Mean in RESTful APIs?

In RESTful APIs, an operation is considered **idempotent** if performing it multiple times has the same effect as
performing it once. For example:

- `GET` requests are idempotent because they retrieve data without changing it.
- `PUT` requests are idempotent because updating a resource with the same data multiple times does not change the
  outcome.
- `POST` requests are not idempotent because creating a new resource each time results in different outcomes.
- `DELETE` requests are idempotent because deleting a resource multiple times has the same effect as deleting it once (
  the resource is gone).
- `PATCH` requests can be idempotent or not, depending on whether they modify the resource in a way that results in the
  same state each time.

Do it once or do it 100 times — the result will be the same.

🧪 Which HTTP Methods Are Idempotent?

| Method  | Idempotent  | Description                                                              |
|---------|-------------|--------------------------------------------------------------------------|
| GET     | ✅ Yes       | Fetches data without changing server state — same result every time.     |
| PUT     | ✅ Yes       | Replaces a resource — doing it multiple times gives the same result.     |
| DELETE  | ✅ Yes       | Deleting the same item repeatedly has no new effect after the first.     |
| HEAD    | ✅ Yes       | Like GET, but without the body — no state change.                        |
| OPTIONS | ✅ Yes       | Just returns allowed methods — no change to server state.                |
| POST    | ❌ No        | Creates new resources — sending it multiple times may create duplicates. |
| PATCH   | ❌ Sometimes | Depends on implementation — may or may not be idempotent.                |

---

