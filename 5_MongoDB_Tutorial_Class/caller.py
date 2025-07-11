import sys
from datetime import datetime, timezone
from typing import Any, Dict, List

from database import get_mongodb_connection


def sanity_check(database_name: str, collection_name: str):
    """
    Performs a connection and sanity check on MongoDB.

    Steps:
    - Connect to MongoDB
    - Check if the database exists
    - Check if the collection exists
    - Print all documents in the collection
    """
    print("=" * 100)
    print("📚 MongoDB Connection Test")
    print("This script checks MongoDB connection and verifies database/collection existence.")
    print("=" * 100)

    try:
        # Step 1: Connect
        client, db, collection = get_mongodb_connection(database_name, collection_name)

        # Step 2: Ping server
        client.admin.command('ping')
        print("✅ MongoDB client connected successfully.")

        # Step 3: Check database existence
        if database_name not in client.list_database_names():
            print(f"❌ Database '{database_name}' does not exist.")
            sys.exit(1)
        print(f"✅ Database '{database_name}' exists.")

        # Step 4: Check collection existence
        if collection_name not in db.list_collection_names():
            print(f"❌ Collection '{collection_name}' does not exist.")
            sys.exit(1)
        print(f"✅ Collection '{collection_name}' exists.")

        print("=" * 100)
        # Step 5: Display documents
        print("📄 Documents in collection:")
        documents = list(collection.find({}))
        if not documents:
            print("⚠️  No documents found in the collection.")
        else:
            print(f"📄 Found {len(documents)} document(s):")
            for document in documents:
                print(document)

    except Exception as e:
        print(f"❌ MongoDB operation failed: {e}")
        sys.exit(1)

    print("=" * 100)


# ──────────────────────────────────────────────────────────────
# INSERT OPERATIONS
# ──────────────────────────────────────────────────────────────

def insert_one_document(collection, data: Dict[str, Any]) -> None:
    """
    Insert a single document into the collection.

    Args:
        collection: MongoDB collection object.
        data (Dict[str, Any]): Document to insert.
    """
    result = collection.insert_one(data)
    print(f"✅ Inserted 1 document with _id: {result.inserted_id}")


def insert_many_documents(collection, data_list: List[Dict[str, Any]]) -> None:
    """
    Insert multiple documents into the collection.

    Args:
        collection: MongoDB collection object.
        data_list (List[Dict[str, Any]]): List of documents to insert.
    """
    if not data_list:
        print("⚠️  No documents provided for insertion.")
        return

    result = collection.insert_many(data_list)
    print(f"✅ Inserted {len(result.inserted_ids)} documents.")


# ──────────────────────────────────────────────────────────────
# READ OPERATIONS
# ──────────────────────────────────────────────────────────────

def display_all_documents(collection) -> None:
    """
    Display all documents in the collection.

    Args:
        collection: MongoDB collection object.
    """
    documents = list(collection.find({}))
    if not documents:
        print("⚠️  No documents found.")
        return

    print(f"📄 Found {len(documents)} document(s):")
    for document in documents:
        print(document)


def select_first_document(collection, query: Dict[str, Any], projection: Dict[str, Any] = None) -> None:
    """
    Retrieve and print the first document matching the query.

    Args:
        collection: MongoDB collection object.
        query (Dict[str, Any]): Filter query.
        projection (Dict[str, Any], optional): Fields to include/exclude.
    """
    document = collection.find_one(query, projection)
    if document:
        print("📄 First matching document:")
        print(document)
    else:
        print("⚠️  No matching document found.")


def select_all_document(collection, query: Dict[str, Any], projection: Dict[str, Any] = None) -> None:
    """
    Retrieve and print all documents matching the query.

    Args:
        collection: MongoDB collection object.
        query (Dict[str, Any]): Filter query.
        projection (Dict[str, Any], optional): Fields to include/exclude.
    """
    documents = list(collection.find(query, projection))
    if not documents:
        print("⚠️  No matching documents found.")
        return

    print(f"📄 Found {len(documents)} matching document(s):")
    for document in documents:
        print(document)


# ──────────────────────────────────────────────────────────────
# UPDATE OPERATIONS
# ──────────────────────────────────────────────────────────────

def update_one_document(collection, query: Dict[str, Any], update_fields: Dict[str, Any]) -> None:
    """
    Update a single document that matches the query.

    Args:
        collection: MongoDB collection object.
        query (Dict[str, Any]): Filter query.
        update_fields (Dict[str, Any]): Fields to update.
    """
    result = collection.update_one(query, {'$set': update_fields})
    if result.modified_count:
        print("✅ One document updated successfully.")
    else:
        print("⚠️  No document was updated.")


def update_all_document(collection, query: Dict[str, Any], update_fields: Dict[str, Any]) -> None:
    """
    Update all documents that match the query.

    Args:
        collection: MongoDB collection object.
        query (Dict[str, Any]): Filter query.
        update_fields (Dict[str, Any]): Fields to update.
    """
    result = collection.update_many(query, {'$set': update_fields})
    if result.modified_count:
        print(f"✅ Updated {result.modified_count} document(s) successfully.")
    else:
        print("⚠️  No documents were updated.")


# ──────────────────────────────────────────────────────────────
# DELETE OPERATIONS
# ──────────────────────────────────────────────────────────────

def delete_one_document(collection, query: Dict[str, Any]) -> None:
    """
    Delete a single document matching the query.

    Args:
        collection: MongoDB collection object.
        query (Dict[str, Any]): Filter query.
    """
    result = collection.delete_one(query)
    if result.deleted_count:
        print("🗑️  One document deleted.")
    else:
        print("⚠️  No document matched the query for deletion.")


def delete_many_documents(collection, query: Dict[str, Any]) -> None:
    """
    Delete all documents matching the query.

    Args:
        collection: MongoDB collection object.
        query (Dict[str, Any]): Filter query.
    """
    result = collection.delete_many(query)
    if result.deleted_count:
        print(f"🗑️  Deleted {result.deleted_count} document(s).")
    else:
        print("⚠️  No matching documents found to delete.")


# ──────────────────────────────────────────────────────────────
# MAIN DEMO
# ──────────────────────────────────────────────────────────────

def main(database_name: str, collection_name: str) -> None:
    """
    Demonstrates insert, read, update, and delete operations on a MongoDB collection.

    Args:
        database_name (str): Name of the MongoDB database.
        collection_name (str): Name of the collection.
    """
    client, db, collection = get_mongodb_connection(database_name, collection_name)

    # Insert one
    one_doc = {
        "title": "Post Title 1",
        "body": "Body of post 1.",
        "category": "News",
        "likes": 1,
        "tags": ["news", "events"],
        "date": datetime.now(timezone.utc)
    }
    insert_one_document(collection, one_doc)

    # Insert many
    many_docs = [
        {
            "title": "Post Title 2",
            "body": "Body of post 2.",
            "category": "Event",
            "likes": 2,
            "tags": ["news", "events"],
            "date": datetime.now(timezone.utc),
        },
        {
            "title": "Post Title 3",
            "body": "Body of post 3.",
            "category": "Technology",
            "likes": 3,
            "tags": ["news", "technology"],
            "date": datetime.now(timezone.utc),
        },
        {
            "title": "Post Title 4",
            "body": "Body of post 4.",
            "category": "Event",
            "likes": 4,
            "tags": ["news", "event"],
            "date": datetime.now(timezone.utc),

        },
        {
            "title": "Post Title 5",
            "body": "Body of post 5.",
            "category": "Social",
            "likes": 5,
            "tags": ["news", "social"],
            "date": datetime.now(timezone.utc),

        }
    ]
    insert_many_documents(collection, many_docs)

    # Display documents
    display_all_documents(collection)

    # Read: Select with and without filters/projections
    select_first_document(collection, {})
    select_first_document(collection, {"category": "Event"})
    select_all_document(collection, {})
    select_all_document(collection, {"category": "Event"})
    select_all_document(collection, {"category": "Event"}, {"title": 1, "body": 1, "_id": 0})

    # Update
    update_one_document(collection, {"title": "Post Title 2"}, {"likes": 99})
    update_all_document(collection, {"category": "Event"}, {"likes": 10})

    # Delete
    delete_one_document(collection, {"title": "Post Title 2"})
    delete_many_documents(collection, {"category": "Event"})


def clear_collection(collection):
    """
    Remove all documents from a MongoDB collection without dropping the collection itself.
    """
    result = collection.delete_many({})
    print(f"🧹 Cleared {result.deleted_count} documents from the collection.")


def drop_collection(collection):
    """
    Drop the entire collection from the database.
    """
    collection_name = collection.name
    collection.drop()
    print(f"🗑️ Collection '{collection_name}' dropped successfully.")


def drop_database(client, db_name: str):
    """
    Drop the entire database and all its collections.
    """
    client.drop_database(db_name)
    print(f"🗑️ Database '{db_name}' dropped successfully.")


def clear_reset(database_name: str, collection_name: str) -> None:
    client, database, collection = get_mongodb_connection(database_name, collection_name)

    # Option 1: Clear all documents from 'posts' collection (keep collection)
    clear_collection(collection)

    # Option 2: Drop 'posts' collection completely
    drop_collection(collection)

    # Option 3: Drop entire 'blog' database

    drop_database(client, database_name)


if __name__ == '__main__':
    # To clean or reset a MongoDB database
    # clear_reset(database_name="blog", collection_name="posts")

    # Run connection + sanity check first
    # sanity_check(database_name="blog", collection_name="posts")

    # Then perform insert, update, delete
    main(database_name="blog", collection_name="posts")
