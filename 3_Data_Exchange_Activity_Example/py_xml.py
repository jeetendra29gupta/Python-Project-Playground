from typing import Any, Dict

import xmltodict
from dicttoxml import dicttoxml

from database import dummy_data as data  # Assuming this is the same dictionary used before


def dict_to_xml(data: Dict[str, Any]) -> bytes:
    """
    Step 2: Convert a Python dictionary to XML.

    Uses `dicttoxml` to convert a dictionary into an XML byte string.

    Args:
        data (Dict[str, Any]): The Python dictionary to convert.

    Returns:
        bytes: XML data in bytes.
    """
    return dicttoxml(data, custom_root='root', attr_type=False)


def xml_to_dict(xml_string: str) -> Dict[str, Any]:
    """
    Step 3: Convert an XML string back into a Python dictionary.

    Uses `xmltodict` to parse XML string into a dictionary.

    Args:
        xml_string (str): The XML string to parse.

    Returns:
        Dict[str, Any]: A Python dictionary representation of the XML.
    """
    return xmltodict.parse(xml_string)['root']


def write_xml_file(filename: str, xml_data: bytes) -> str:
    """
    Step 4: Write XML data to a file.

    Args:
        filename (str): Name/path of the XML file to be created.
        xml_data (bytes): XML data in bytes to write to the file.

    Returns:
        str: Success message.
    """
    with open(filename, 'wb') as file:
        file.write(xml_data)
    return f"✅ XML file '{filename}' created successfully."


def read_xml_file(filename: str) -> str:
    """
    Step 5: Read XML content from a file.

    Args:
        filename (str): Path to the XML file.

    Returns:
        str: The XML content as a string.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()


def separator():
    """
    Print a visual separator line in the console output.
    Useful for better readability when printing different steps.
    """
    print("===" * 99 + "===\n")


if __name__ == '__main__':
    # Step 1: Show sample data
    print("📦 Step 1: Sample Data:\n", data)
    print("Data Type:", type(data))
    separator()

    # Step 2: Convert dictionary to XML
    xml_data_bytes = dict_to_xml(data)
    xml_data_str = xml_data_bytes.decode('utf-8')  # For displaying
    print("🧾 Step 2: XML Data:\n", xml_data_str)
    print("XML Data Type:", type(xml_data_bytes))
    separator()

    # Step 3: Convert XML string back to dictionary
    parsed_dict = xml_to_dict(xml_data_str)
    print("🔁 Step 3: Parsed from XML:\n", parsed_dict)
    print("Parsed Data Type:", type(parsed_dict))
    separator()

    # Step 4: Write XML to file
    xml_filename = "person_data.xml"
    print("💾 Step 4:", write_xml_file(xml_filename, xml_data_bytes))
    separator()

    # Step 5: Read XML from file
    xml_content = read_xml_file(xml_filename)
    print("📂 Step 5: Content read from XML file:\n", xml_content)
    print("XML Content Type:", type(xml_content))
    separator()

    # Step 6: Validate round-trip data
    round_trip_dict = xml_to_dict(xml_content)
    assert parsed_dict == round_trip_dict, "❌ Mismatch in round-trip XML conversion"
    print("✅ Step 6: XML data integrity check passed!")
