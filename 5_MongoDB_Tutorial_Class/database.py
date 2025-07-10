from typing import Tuple
from urllib.parse import quote_plus

from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database


class Config:
    """
    MongoDB configuration settings.

    Update these values to match your MongoDB environment.
    """
    MONGODB_USERNAME: str = "Admin"
    MONGODB_PASSWORD: str = "Admin@1814"
    MONGODB_HOST: str = "192.168.18.44"
    MONGODB_PORT: int = 27017
    MONGODB_AUTH_DB: str = "admin"
    MONGODB_TIMEOUT: int = 5000  # Timeout in milliseconds


def get_mongodb_client() -> MongoClient:
    """
    Create and return an authenticated MongoDB client using settings from Config.

    Returns:
        MongoClient: Connected MongoDB client instance.

    Raises:
        pymongo.errors.PyMongoError: If connection fails or URI is malformed.
    """
    # Encode special characters in password (e.g., @, :)
    encoded_password = quote_plus(Config.MONGODB_PASSWORD)

    # Construct MongoDB URI
    uri = (
        f"mongodb://{Config.MONGODB_USERNAME}:{encoded_password}"
        f"@{Config.MONGODB_HOST}:{Config.MONGODB_PORT}"
        f"/?authSource={Config.MONGODB_AUTH_DB}"
    )

    # Return MongoDB client
    return MongoClient(uri, serverSelectionTimeoutMS=Config.MONGODB_TIMEOUT)


def get_mongodb_database(client: MongoClient, db_name: str) -> Database:
    """
    Retrieve the specified MongoDB database from the client.

    Args:
        client (MongoClient): Connected MongoDB client.
        db_name (str): Name of the database.

    Returns:
        Database: MongoDB Database object.
    """
    return client[db_name]


def get_mongodb_collection(database: Database, collection_name: str) -> Collection:
    """
    Retrieve the specified collection from a MongoDB database.

    Args:
        database (Database): MongoDB Database object.
        collection_name (str): Name of the collection.

    Returns:
        Collection: MongoDB Collection object.
    """
    return database[collection_name]


def get_mongodb_connection(db_name: str, collection_name: str) -> Tuple[MongoClient, Database, Collection]:
    """
    Establish a full MongoDB connection and return client, database, and collection.

    Args:
        db_name (str): Name of the database to connect to.
        collection_name (str): Name of the collection to access.

    Returns:
        tuple: (MongoClient, Database, Collection)

    Example:
        client, db, collection = get_mongodb_connection("blog", "posts")
    """
    client = get_mongodb_client()
    database = get_mongodb_database(client, db_name)
    collection = get_mongodb_collection(database, collection_name)
    return client, database, collection
