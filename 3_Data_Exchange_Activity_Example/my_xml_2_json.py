import json
import xml.etree.ElementTree as ET


def get_xml_data() -> str:
    """
    Step 1: Return a sample XML string representing flight search response.

    Returns:
        str: Multiline string containing flight data in XML format.
    """
    xml_data = """
    <FlightSearchResponse>
      <Flights>
        <Flight>
          <FlightNumber>WN123</FlightNumber>
          <Origin>DAL</Origin>
          <Destination>HOU</Destination>
          <DepartureTime>2025-07-20T08:00:00</DepartureTime>
          <ArrivalTime>2025-07-20T09:30:00</ArrivalTime>
          <Fare>150.00</Fare>
        </Flight>
        <Flight>
          <FlightNumber>WN456</FlightNumber>
          <Origin>DAL</Origin>
          <Destination>HOU</Destination>
          <DepartureTime>2025-07-20T10:00:00</DepartureTime>
          <ArrivalTime>2025-07-20T11:30:00</ArrivalTime>
          <Fare>170.00</Fare>
        </Flight>
      </Flights>
    </FlightSearchResponse>
    """
    return xml_data


def xml_to_json(xml_data: str) -> str:
    """
    Step 2–4: Convert XML flight data into JSON format.

    Parses the input XML string, extracts flight information,
    converts it to a dictionary, and then serializes it to a JSON string.

    Args:
        xml_data (str): XML string representing flights.

    Returns:
        str: JSON-formatted string of flights data.
    """
    # Step 2: Parse XML
    root = ET.fromstring(xml_data)
    print("📥 Step 2: XML parsed successfully.")

    # Step 3: Extract data
    flights = []
    for flight in root.find('Flights'):
        flights.append({
            "FlightNumber": flight.find('FlightNumber').text,
            "Origin": flight.find('Origin').text,
            "Destination": flight.find('Destination').text,
            "DepartureTime": flight.find('DepartureTime').text,
            "ArrivalTime": flight.find('ArrivalTime').text,
            "Fare": float(flight.find('Fare').text)
        })
    print("🔄 Step 3: XML data converted to Python dictionary.")

    # Step 4: Convert to JSON
    json_data = json.dumps({"flights": flights}, indent=2)
    print("🧾 Step 4: Python dictionary converted to JSON.")
    print(json_data)

    return json_data


def write_to_file(filename: str, content: str, mode: str = 'w') -> str:
    """
    Common function to write content to a file.

    Args:
        filename (str): Path to the file.
        content (str): Text content to write.
        mode (str): File open mode ('w' for text, 'wb' for binary). Default is 'w'.

    Returns:
        str: Success message.
    """
    with open(filename, mode, encoding='utf-8') as file:
        file.write(content)
    return f"✅ File '{filename}' written successfully."


def separator():
    """
    Print a visual separator line in the console output.
    Useful for better readability between steps.
    """
    print("===" * 33 + "===\n")


if __name__ == '__main__':
    # Step 1: Get XML data
    print("📦 Step 1: Getting sample XML data...")
    sample_xml = get_xml_data()
    separator()

    # Write XML to file
    xml_filename = "flight_search.xml"
    print("💾 Writing XML to file...")
    print(write_to_file(xml_filename, sample_xml))
    separator()

    # Steps 2–4: Convert to JSON
    json_result = xml_to_json(sample_xml)
    separator()

    # Write JSON to file
    json_filename = "flight_search.json"
    print("💾 Writing JSON to file...")
    print(write_to_file(json_filename, json_result))
    separator()
