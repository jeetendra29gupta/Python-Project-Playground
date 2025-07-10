"""
SOAP Calculator Client using Zeep.

This module demonstrates how to interact with a public SOAP-based calculator
web service to perform basic arithmetic operations like Add, Subtract,
Multiply, and Divide.

Dependencies:
    - zeep
    - lxml

To install:
    pip install zeep lxml
"""

import logging

from lxml import etree
from zeep import Client
from zeep.plugins import HistoryPlugin

# Setup logging to capture HTTP transport and SOAP XML exchanges
logging.basicConfig(level=logging.INFO)
logging.getLogger('zeep.transports').setLevel(logging.DEBUG)


class CalculatorSOAPClient:
    """
    SOAP client for performing arithmetic operations using the public calculator SOAP service.
    """

    def __init__(self, wsdl_url: str):
        """
        Initialize the SOAP client with the WSDL URL.

        :param wsdl_url: The URL of the WSDL describing the SOAP service.
        """
        self.history = HistoryPlugin()
        self.client = Client(wsdl=wsdl_url, plugins=[self.history])

    def add(self, int_a: int, int_b: int) -> int:
        """Perform addition."""
        return self.client.service.Add(intA=int_a, intB=int_b)

    def subtract(self, int_a: int, int_b: int) -> int:
        """Perform subtraction."""
        return self.client.service.Subtract(intA=int_a, intB=int_b)

    def multiply(self, int_a: int, int_b: int) -> int:
        """Perform multiplication."""
        return self.client.service.Multiply(intA=int_a, intB=int_b)

    def divide(self, int_a: int, int_b: int) -> int:
        """Perform division."""
        return self.client.service.Divide(intA=int_a, intB=int_b)

    def print_last_request_response(self):
        """
        Pretty-print the last SOAP request and response XML.
        Useful for debugging and understanding SOAP messages.
        """
        request_xml = etree.tostring(self.history.last_sent['envelope'], pretty_print=True).decode()
        response_xml = etree.tostring(self.history.last_received['envelope'], pretty_print=True).decode()

        print("\n--- Last SOAP Request ---")
        print(request_xml)

        print("\n--- Last SOAP Response ---")
        print(response_xml)


def main():
    """
    Main function demonstrating usage of the calculator SOAP client.
    """
    wsdl_url = 'http://www.dneonline.com/calculator.asmx?wsdl'
    calc_client = CalculatorSOAPClient(wsdl_url)

    # Perform Add
    result_add = calc_client.add(10, 20)
    print(f"Result of Add(10, 20): {result_add}")
    calc_client.print_last_request_response()

    # Perform Subtract
    result_sub = calc_client.subtract(50, 15)
    print(f"\nResult of Subtract(50, 15): {result_sub}")
    calc_client.print_last_request_response()

    # Perform Multiply
    result_mul = calc_client.multiply(5, 9)
    print(f"\nResult of Multiply(5, 9): {result_mul}")
    calc_client.print_last_request_response()

    # Perform Divide
    result_div = calc_client.divide(100, 5)
    print(f"\nResult of Divide(100, 5): {result_div}")
    calc_client.print_last_request_response()


if __name__ == '__main__':
    main()
