## 🧪 4️⃣ Test It

### ✅ Using Query String

* **URL:** `http://localhost:3000/greet?name=Jeetendra`

📬 Response:

```json
"Hello, Jeetendra 👋! (Path: /greet)"
```

---

### ✅ Using Route Parameter

* **URL:** `http://localhost:3000/greet/Jeetendra`

📬 Response:

```json
"Hello, Jeetendra 👋! (Path: /greet/Jeetendra)"
```

---

### ✅ In Postman

* Use `GET` method
* URL:

    * `http://localhost:3000/greet?name=Jeetendra` *(query string)*
    * `http://localhost:3000/greet/Jeetendra` *(route param)*

No headers or body needed.

---

## ✅ Summary

| Feature         | URL                     | Notes                   |
|-----------------|-------------------------|-------------------------|
| Query String    | `/greet?name=Jeetendra` | `queryStringParameters` |
| Route Parameter | `/greet/Jeetendra`      | `pathParameters`        |

---

## 🔥 Bonus: Add Fallback Name

Already done in the code — if no name is passed, it defaults to `"Guest"`.

---