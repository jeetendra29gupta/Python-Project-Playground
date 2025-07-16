sudo sam build && sudo sam local start-api --host 0.0.0.0 --docker-network host

### Run AWS DynamoDB in locally

```bash
nohup java -Djava.library.path=./DynamoDBLocal_lib -jar DynamoDBLocal.jar -sharedDb -dbPath ./data > dynamodb.log 2>&1 &
```

### Table Operations

* **List all tables**

  ```bash
  aws dynamodb list-tables --endpoint-url http://localhost:8000
  ```

* **Create a table** (example: simple key schema)

  ```bash
  aws dynamodb create-table \
    --table-name MyTable \
    --attribute-definitions AttributeName=Id,AttributeType=S \
    --key-schema AttributeName=Id,KeyType=HASH \
    --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5 \
    --endpoint-url http://localhost:8000
  ```

* **Delete a table**

  ```bash
  aws dynamodb delete-table --table-name MyTable --endpoint-url http://localhost:8000
  ```

* **Describe a table** (get detailed info)

  ```bash
  aws dynamodb describe-table --table-name MyTable --endpoint-url http://localhost:8000
  ```

---

### Item Operations

* **Put (insert/update) an item**

  ```bash
  aws dynamodb put-item \
    --table-name MyTable \
    --item '{"Id": {"S": "123"}, "Name": {"S": "Example: 123"}}' \
    --endpoint-url http://localhost:8000
  ```

* **Get an item by primary key**

  ```bash
  aws dynamodb get-item \
    --table-name MyTable \
    --key '{"Id": {"S": "123"}}' \
    --endpoint-url http://localhost:8000
  ```

* **Delete an item**

  ```bash
  aws dynamodb delete-item \
    --table-name MyTable \
    --key '{"Id": {"S": "123"}}' \
    --endpoint-url http://localhost:8000
  ```
  
---
