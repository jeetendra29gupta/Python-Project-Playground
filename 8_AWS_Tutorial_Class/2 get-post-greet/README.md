# 🚀 Lambda Greet – Class 2: GET & POST API using AWS SAM

This project demonstrates how to build and test a **serverless API** with both `GET` and `POST` methods using **AWS SAM
CLI**, **Python**, and **Docker** — tested via **Postman** and `event.json`.

---

## 📁 Project Structure

```

lambda-greet/
├── my_module/
│   └── app.py              # Lambda function code
├── event-get.json          # Event for GET /hello
├── event-post.json         # Event for POST /hello
├── requirements.txt        # Python dependencies (optional)
└── template.yaml           # SAM template

````

---

## 📦 Requirements

- Python 3.11+
- AWS CLI (`aws configure`)
- AWS SAM CLI (`sam --version`)
- Docker running (`sudo systemctl start docker`)

---

## 🔧 Setup & Run

### 🛠 Build the SAM Project

```bash
sam build
````

### ▶️ Run the API Locally

```bash
sam local start-api
```

Access the endpoints at: `http://localhost:3000/hello`

---

## 🧪 Test in Postman

### ✅ GET `/hello`

* **Method:** GET
* **URL:** `http://localhost:3000/hello`

#### Response:

```json
"Hello from Lambda via GET!"
```

---

### ✅ POST `/hello`

* **Method:** POST
* **URL:** `http://localhost:3000/hello`
* **Headers:** `Content-Type: application/json`
* **Body:**

```json
{
  "name": "Jeetendra"
}
```

#### Response:

```json
"Hello, Jeetendra from Lambda via POST!"
```

---

## 🔁 Invoke Locally Using event.json

### 📁 event-get.json

```json
{
  "httpMethod": "GET",
  "path": "/hello"
}
```

### 📁 event-post.json

```json
{
  "httpMethod": "POST",
  "path": "/hello",
  "headers": {
    "Content-Type": "application/json"
  },
  "body": "{\"name\": \"Jeetendra\"}"
}
```

### Run from CLI

```bash
sam local invoke GreetFunction -e event-get.json
sam local invoke GreetFunction -e event-post.json
```

---

