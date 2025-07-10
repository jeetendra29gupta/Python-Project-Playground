# MongoDB Tutorial - Class 1

Welcome to the first class in learning MongoDB! This tutorial will introduce you to MongoDB concepts step-by-step,
starting from the basics of data formats and moving toward understanding how MongoDB differs from traditional databases.

---

## What is MongoDB?

MongoDB is a **document database** that stores data in a flexible, JSON-like format called **BSON**. Unlike traditional
relational databases, MongoDB uses documents instead of tables.

---

## 1. Understanding Data Formats: JSON vs BSON

### JSON (JavaScript Object Notation)

* **Format:** Text-based and human-readable.
* **Use:** Commonly used to exchange data between systems (like APIs).
* **Data Types:** Strings, numbers, arrays, booleans, null, and nested objects.
* **Limitations:** Cannot directly store binary data or dates.

**Example JSON document:**

```json
{
  "name": "Alice",
  "age": 30,
  "isMember": true,
  "hobbies": [
    "reading",
    "hiking"
  ]
}
```

---

### BSON (Binary JSON)

* **Format:** Binary-encoded version of JSON used internally by MongoDB.
* **Advantages:** Supports additional data types, including:

    * Dates
    * Binary data
    * 32-bit and 64-bit integers
    * Floating points and high-precision decimals (Decimal128)
    * Embedded documents and arrays
* **Tradeoff:** Not human-readable because it is in binary format.
* **Benefit:** Faster parsing and smaller storage size compared to JSON.

---

### Summary: JSON vs BSON

| Feature      | JSON                  | BSON                                 |
|--------------|-----------------------|--------------------------------------|
| Format       | Text (human-readable) | Binary (compact & fast)              |
| Data Types   | Limited               | Extended (dates, binary, etc.)       |
| Readability  | Easy                  | Not human-readable                   |
| Size & Speed | Larger, slower        | Smaller, faster                      |
| Usage        | Data interchange      | Internal MongoDB storage & transport |

---

## 2. MongoDB Document Structure

A MongoDB **record** is called a **document**. It stores data in key-value pairs, similar to JSON objects.

**Example Document:**

```json
{
  "title": "Post Title 1",
  "body": "Body of post.",
  "category": "News",
  "likes": 1,
  "tags": [
    "news",
    "events"
  ],
  "date": ISODate(
  "2025-07-10T00:00:00Z"
  )
}
```

* `title` (string): The title of the post.
* `body` (string): The content of the post.
* `category` (string): Category name.
* `likes` (integer): Number of likes.
* `tags` (array of strings): Tags related to the post.
* `date` (ISODate): Date when the post was created.

---

## 3. SQL vs Document Databases (MongoDB)

| Aspect         | SQL Databases                                              | MongoDB (Document Database)                   |
|----------------|------------------------------------------------------------|-----------------------------------------------|
| Data Model     | Relational, tables and rows                                | Document-based, flexible JSON-like docs       |
| Schema         | Fixed schema                                               | Flexible schema (dynamic documents)           |
| Data Relations | Related data stored in separate tables, joined via queries | Related data stored together inside documents |
| Query Speed    | Joins can slow queries                                     | Fast reads with embedded data                 |
| Collections    | Tables                                                     | Collections (groups of documents)             |

MongoDB stores data in **collections**, which are analogous to tables but without fixed schemas, enabling fast and
flexible data access.

---

# MongoDB Tutorial - Class 2

Welcome to the second class in learning MongoDB! This session continues from Class 1, focusing on practical operations
like creating databases, inserting data, querying collections, updating documents, and deleting records. These
operations form the foundation of working with MongoDB in real-world applications.

---

## Create Database

### Change or Create a Database

To switch to or create a new database, use the `use` command followed by the database name:

```js
use blog
```

> **Note:** A database is not actually created until it contains some data.

---

## Create Collection and Insert Documents

### Insert a Single Document

To create a collection (if it doesn’t exist) and insert one document:

```js
db.posts.insertOne({
  title: "Post Title 1",
  body: "Body of post.",
  category: "News",
  likes: 1,
  tags: ["news", "events"],
  date: new Date()
})
```

### Insert Multiple Documents

To insert several documents at once:

```js
db.posts.insertMany([
  {
    title: "Post Title 2",
    body: "Body of post.",
    category: "Event",
    likes: 2,
    tags: ["news", "events"],
    date: Date()
  },
  {
    title: "Post Title 3",
    body: "Body of post.",
    category: "Technology",
    likes: 3,
    tags: ["news", "events"],
    date: Date()
  },
  {
    title: "Post Title 4",
    body: "Body of post.",
    category: "Event",
    likes: 4,
    tags: ["news", "events"],
    date: Date()
  }
])
```

---

## Find Data

### `find()`

To retrieve all documents in a collection:

```js
db.posts.find({})
```

### `findOne()`

To retrieve only the first matching document:

```js
db.posts.findOne({})
```

---

## Querying Data

### Filtering with Conditions

Use a query object to filter documents:

```js
db.posts.find({ category: "News" })
db.posts.find({ category: "Event" })
db.posts.findOne({ category: "Event" })
```

---

## Projection

Projection allows you to control which fields appear in the result.

### Include Specific Fields

```js
db.posts.find({}, { title: 1, date: 1 })
```

### Exclude `_id` and Include Others

```js
db.posts.find({}, { _id: 0, title: 1, date: 1 })
```

> ⚠️ You cannot mix inclusion (`1`) and exclusion (`0`) in the same projection (except for `_id`).

Examples:

```js
db.posts.find({}, { title: 1, date: 0 }) // ❌ Error
db.posts.find({}, { title: 1, date: 1 }) // ✅ Works
db.posts.find({}, { title: 0, date: 0 }) // ✅ Works
```

---

## Update Documents

To modify existing documents, use `updateOne()` or `updateMany()`.

### `updateOne()`

Updates the first document that matches the condition:

```js
db.posts.updateOne(
  { title: "Post Title 1" },
  { $set: { likes: 2 } }
)
```

### `updateMany()`

Updates all documents that match the condition:

```js
db.posts.updateMany(
  {},
  { $inc: { likes: 1 } } // Increment likes by 1
)
```

---

## Delete Documents

Use `deleteOne()` and `deleteMany()` to remove data.

### `deleteOne()`

Deletes the first matching document:

```js
db.posts.deleteOne({ title: "Post Title 5" })
```

### `deleteMany()`

Deletes all documents that match the condition:

```js
db.posts.deleteMany({ category: "Technology" })
```

---

# MongoDB Tutorial - Class 3

Welcome to the third class in our MongoDB tutorial series! In this class, we will explore **MongoDB Query Operators**and
**Update Operators**. These tools let you search and manipulate documents with power and precision.

---

## MongoDB Query Operators

Query operators let you filter and match documents based on comparisons, logic, and evaluation.

---

### 📘 Comparison Operators

| Operator | Description                   | Example                                                   |
|----------|-------------------------------|-----------------------------------------------------------|
| `$eq`    | Equal to                      | `db.posts.find({ likes: { $eq: 2 } })`                    |
| `$ne`    | Not equal to                  | `db.posts.find({ category: { $ne: "News" } })`            |
| `$gt`    | Greater than                  | `db.posts.find({ likes: { $gt: 2 } })`                    |
| `$gte`   | Greater than or equal         | `db.posts.find({ likes: { $gte: 3 } })`                   |
| `$lt`    | Less than                     | `db.posts.find({ likes: { $lt: 4 } })`                    |
| `$lte`   | Less than or equal            | `db.posts.find({ likes: { $lte: 2 } })`                   |
| `$in`    | Matches any value in an array | `db.posts.find({ category: { $in: ["News", "Event"] } })` |

---

### 🔗 Logical Operators

| Operator | Description                  | Example                                                                    |
|----------|------------------------------|----------------------------------------------------------------------------|
| `$and`   | Match all conditions         | `db.posts.find({ $and: [ { category: "News" }, { likes: { $gt: 1 } } ] })` |
| `$or`    | Match any condition          | `db.posts.find({ $or: [ { category: "News" }, { likes: { $gt: 3 } } ] })`  |
| `$nor`   | Match none of the conditions | `db.posts.find({ $nor: [ { category: "News" }, { likes: { $gt: 3 } } ] })` |
| `$not`   | Negate a condition           | `db.posts.find({ likes: { $not: { $gt: 2 } } })`                           |

---

### 🧪 Evaluation Operators

| Operator | Description                               | Example                                          |
|----------|-------------------------------------------|--------------------------------------------------|
| `$regex` | Match strings using regular expressions   | `db.posts.find({ title: { $regex: /post/i } })`  |
| `$text`  | Perform text search (requires text index) | `db.posts.find({ $text: { $search: "event" } })` |
| `$where` | Use JavaScript expressions for matching   | `db.posts.find({ $where: "this.likes > 2" })`    |

> 🔍 **Note:** `$text` requires a text index:
> `db.posts.createIndex({ title: "text", body: "text" })`

---

## MongoDB Update Operators

Update operators are used with `updateOne()` and `updateMany()` to change document values.

---

### ✏️ Field Update Operators

| Operator       | Description               | Example                                                                                   |
|----------------|---------------------------|-------------------------------------------------------------------------------------------|
| `$currentDate` | Set field to current date | `db.posts.updateOne({ title: "Post Title 1" }, { $currentDate: { lastModified: true } })` |
| `$inc`         | Increment value           | `db.posts.updateOne({ title: "Post Title 2" }, { $inc: { likes: 1 } })`                   |
| `$rename`      | Rename a field            | `db.posts.updateMany({}, { $rename: { "body": "content" } })`                             |
| `$set`         | Set a field value         | `db.posts.updateOne({ title: "Post Title 3" }, { $set: { category: "Updated" } })`        |
| `$unset`       | Remove a field            | `db.posts.updateOne({ title: "Post Title 4" }, { $unset: { tags: "" } })`                 |

---

### 📚 Array Update Operators

| Operator    | Description                             | Example                                                                              |
|-------------|-----------------------------------------|--------------------------------------------------------------------------------------|
| `$addToSet` | Add a value only if it doesn't exist    | `db.posts.updateOne({ title: "Post Title 1" }, { $addToSet: { tags: "featured" } })` |
| `$pop`      | Remove first or last item (`-1` or `1`) | `db.posts.updateOne({ title: "Post Title 2" }, { $pop: { tags: 1 } })`               |
| `$pull`     | Remove all matching values              | `db.posts.updateOne({ title: "Post Title 3" }, { $pull: { tags: "events" } })`       |
| `$push`     | Add value to array                      | `db.posts.updateOne({ title: "Post Title 4" }, { $push: { tags: "mongodb" } })`      |

---