"""
SOAP WSDL Client Example using Zeep.

This module demonstrates how to interact with a SOAP web service
to convert temperature values between Celsius and Fahrenheit.

Requirements:
- zeep
- lxml

To install dependencies:
    pip install zeep lxml
"""

from lxml import etree
from zeep import Client
from zeep.plugins import HistoryPlugin


class TemperatureConverterSOAPClient:
    """
    A SOAP client for converting temperatures using W3Schools TempConvert SOAP Service.
    """

    def __init__(self, wsdl_url: str):
        """
        Initialize the SOAP client with the given WSDL URL.

        :param wsdl_url: The URL to the WSDL describing the SOAP service.
        """
        self.history = HistoryPlugin()
        self.client = Client(wsdl=wsdl_url, plugins=[self.history])

    def celsius_to_fahrenheit(self, celsius: str) -> str:
        """
        Convert Celsius to Fahrenheit.

        :param celsius: Temperature in Celsius (string format).
        :return: Temperature in Fahrenheit.
        """
        return self.client.service.CelsiusToFahrenheit(Celsius=celsius)

    def fahrenheit_to_celsius(self, fahrenheit: str) -> str:
        """
        Convert Fahrenheit to Celsius.

        :param fahrenheit: Temperature in Fahrenheit (string format).
        :return: Temperature in Celsius.
        """
        return self.client.service.FahrenheitToCelsius(Fahrenheit=fahrenheit)

    def print_last_request_response(self):
        """
        Pretty-print the last SOAP request and response XML.
        """
        request_xml = etree.tostring(self.history.last_sent['envelope'], pretty_print=True).decode()
        response_xml = etree.tostring(self.history.last_received['envelope'], pretty_print=True).decode()

        print("\n--- Last SOAP Request ---")
        print(request_xml)

        print("\n--- Last SOAP Response ---")
        print(response_xml)


def main():
    """
    Main execution function to demonstrate SOAP requests.
    """
    # Define WSDL endpoint
    wsdl_url = 'https://www.w3schools.com/xml/tempconvert.asmx?WSDL'

    # Instantiate the SOAP client
    soap_client = TemperatureConverterSOAPClient(wsdl_url)

    # Celsius → Fahrenheit
    celsius = "20"
    fahrenheit_result = soap_client.celsius_to_fahrenheit(celsius)
    print(f"Convert Celsius:{celsius} → Fahrenheit: {fahrenheit_result}")
    soap_client.print_last_request_response()

    # Fahrenheit → Celsius
    fahrenheit = "68"
    celsius_result = soap_client.fahrenheit_to_celsius(fahrenheit)
    print(f"\nConvert Fahrenheit:{fahrenheit} → Celsius: {celsius_result}")
    soap_client.print_last_request_response()


if __name__ == '__main__':
    main()
