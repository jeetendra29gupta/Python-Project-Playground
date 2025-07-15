# 🚀 Lambda Hello – AWS SAM Local API Example

This project demonstrates a **simple AWS Lambda function** deployed using **AWS SAM (Serverless Application Model)**
with **Python 3.11**, and tested locally using Docker.

---

## 📘 What is AWS SAM?

**AWS SAM** is an open-source framework for building serverless applications. It simplifies the setup, build, and
deployment of AWS Lambda functions and other serverless resources using concise YAML syntax.

SAM lets you:

- Define infrastructure as code (`template.yaml`)
- Run & debug Lambda functions locally using Docker
- Deploy applications with `sam deploy`

---

## 🟨 Create Your First SAM App (This Project)

### 🧱 Project Structure

```

lambda-hello/
├── hello_world/
│   └── app.py              # Lambda function code
├── main.py                 # Optional entry file (not used in this example)
├── requirements.txt        # Python dependencies (empty or optional)
└── template.yaml           # SAM template to define Lambda + API Gateway

````

---

## 🖥️ Setup & Run Locally

### ✅ Prerequisites

- Python 3.11+
- Docker (running)
- AWS CLI configured (`aws configure`)
- AWS SAM CLI installed

### 📥 Install Dependencies

No external Python packages used in this example, so `requirements.txt` is optional. If needed:

```bash
pip install -r requirements.txt
````

---

### 🛠️ Build the Project

```bash
sam build
```

---

### ▶️ Run the API Locally

```bash
sam local start-api
```

Open your browser or use curl:

```bash
curl http://localhost:3000/hello
```

✅ Output:

```json
"Hello from Local Lambda Function!"
```

---

## 🧠 How It Works

### 🔧 `template.yaml`

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31
Resources:
  HelloWorldFunction:
    Type: AWS::Serverless::Function
    Properties:
      CodeUri: hello_world/
      Handler: app.lambda_handler
      Runtime: python3.11
      Events:
        HelloWorld:
          Type: Api
          Properties:
            Path: /hello
            Method: get
```

This configures:

* A Lambda function in `hello_world/app.py`
* API Gateway to route `GET /hello` to that function

---

### 📂 `hello_world/app.py`

```python
import json


def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps("Hello from Local Lambda Function!")
    }
```

---

## ✅ Docker Status

Ensure Docker is running:

```bash
sudo systemctl status docker
```

If not running, start it with:

```bash
sudo systemctl start docker
```

---

## 📦 Package and Deploy to AWS

When you're ready to deploy:

```bash
sam deploy --guided
```

Follow prompts to deploy to your AWS account.

---

## 🧪 Testing Locally with `sam local invoke`

Create an `event.json` file:

```json
{
  "httpMethod": "GET",
  "path": "/hello"
}
```

Run:

```bash
sam local invoke HelloWorldFunction -e event.json
```

---

## Local Build and Run it:

```bash
sudo sam local invoke && sudo sam local start-api
```

---

