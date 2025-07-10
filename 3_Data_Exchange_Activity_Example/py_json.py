import json
from typing import Any, Dict

from database import dummy_data as data  # Import dummy data from a local module


def convert_to_json(data: Dict[str, Any]) -> str:
    """
    Step 2: Convert a Python dictionary to a formatted JSON string.

    This function takes a dictionary and returns a JSON-formatted string with indentation
    for better readability.

    Args:
        data (Dict[str, Any]): The Python dictionary to convert.

    Returns:
        str: A pretty-formatted JSON string.
    """
    return json.dumps(data, indent=4)


def parse_json_to_dict(json_string: str) -> Dict[str, Any]:
    """
    Step 3: Parse a JSON string back into a Python dictionary.

    Converts a JSON-formatted string back into its equivalent Python dictionary.

    Args:
        json_string (str): The JSON string to parse.

    Returns:
        Dict[str, Any]: A Python dictionary representing the JSON data.
    """
    return json.loads(json_string)


def create_json_file(filename: str, data: Dict[str, Any]) -> str:
    """
    Step 4: Write a Python dictionary to a JSON file.

    Saves a dictionary to a file in JSON format using UTF-8 encoding.

    Args:
        filename (str): The path and name of the file to write.
        data (Dict[str, Any]): The dictionary to serialize and write.

    Returns:
        str: A success message indicating the file has been created.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)
    return f"✅ JSON file '{filename}' created successfully."


def read_json_file(filename: str) -> Dict[str, Any]:
    """
    Step 5: Read a JSON file and return its contents as a Python dictionary.

    Opens and reads a JSON file and converts its contents back to a Python dictionary.

    Args:
        filename (str): The path of the JSON file to read.

    Returns:
        Dict[str, Any]: The deserialized dictionary from the file.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)


def separator():
    """
    Print a visual separator line in the console output.
    Useful for better readability when printing different steps.
    """
    print("===" * 99 + "===\n")


if __name__ == '__main__':
    # Step 1: Display sample data and its type
    print("📦 Step 1: Sample Data:\n", data)
    print("Data Type:", type(data))
    separator()

    # Step 2: Convert dictionary to JSON string
    json_data = convert_to_json(data)
    print("🧾 Step 2: JSON Data:\n", json_data)
    print("JSON Data Type:", type(json_data))
    separator()

    # Step 3: Parse JSON string back into a dictionary
    parsed_dict = parse_json_to_dict(json_data)
    print("🔁 Step 3: Parsed Data:\n", parsed_dict)
    print("Parsed Data Type:", type(parsed_dict))
    separator()

    # Step 4: Save dictionary to a JSON file
    filename = "person_data.json"
    print("💾 Step 4:", create_json_file(filename, data))
    separator()

    # Step 5: Read data back from the JSON file
    file_data = read_json_file(filename)
    print("📂 Step 5: Data from JSON file:\n", file_data)
    print("Data Type from file:", type(file_data))
    separator()

    # Step 6: Validate round-trip conversion (original → file → dict)
    assert data == file_data, "❌ Mismatch between original and file data"
    print("✅ Step 6: Data integrity check passed!")
