"""
Country Info SOAP Client using Zeep.

This script lists all available SOAP operations and fetches a list of countries
with their ISO codes from the CountryInfoService.

Dependencies:
    - zeep

Install:
    pip install zeep
"""

import logging

from zeep import Client

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class CountryInfoSOAPClient:
    """
    SOAP client for interacting with the CountryInfoService WSDL.
    """

    def __init__(self, wsdl_url: str):
        """
        Initialize the client with the given WSDL URL.

        :param wsdl_url: URL to the WSDL endpoint.
        """
        self.client = Client(wsdl_url)

    def list_available_operations(self):
        """
        Print all available service operations provided by the WSDL.
        """
        logger.info("Listing all available operations in the WSDL...")
        operations = self.client.wsdl.services.values()
        for service in operations:
            for port in service.ports.values():
                methods = sorted(port.binding._operations.keys())
                for method in methods:
                    print(f"Operation: {method}")

    def list_country_codes(self):
        """
        Retrieve and print all country names and their ISO codes.
        """
        logger.info("Fetching list of country codes...")
        try:
            countries = self.client.service.ListOfCountryNamesByCode()
            for country in countries:
                code = country['sISOCode']
                name = country['sName']
                print(f"Country Code: {code}, Country Name: {name}")
        except Exception:
            logger.exception("Failed to retrieve country codes.")


def main():
    """
    Main function to demonstrate fetching services and country codes.
    """
    wsdl = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL"
    client = CountryInfoSOAPClient(wsdl)

    # Print available service operations
    client.list_available_operations()

    # Print country ISO codes and names
    client.list_country_codes()


if __name__ == '__main__':
    main()
