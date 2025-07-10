"""
SOAP Client using Zeep for CountryInfoService.

Performs operations like retrieving capital cities by country ISO code.

Dependencies:
    - zeep

To install:
    pip install zeep
"""

import logging

from zeep import Client

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class CountryInfoSOAPClient:
    """
    SOAP client using Zeep to interact with CountryInfoService.
    """

    def __init__(self, wsdl_url: str):
        """
        Initialize the SOAP client with the WSDL URL.

        :param wsdl_url: URL to the WSDL endpoint.
        """
        self.client = Client(wsdl_url)

    def get_capital_city(self, country_code: str) -> str:
        """
        Get the capital city of a country by ISO code.

        :param country_code: Country ISO code (e.g., "IN", "US").
        :return: Capital city name.
        """
        logger.info(f"Fetching capital city for: {country_code}")
        try:
            capital = self.client.service.CapitalCity(country_code)
            logger.info(f"Capital of {country_code}: {capital}")
            return capital
        except Exception:
            logger.exception(f"Failed to fetch capital for {country_code}")
            raise


def main():
    wsdl = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL"
    client = CountryInfoSOAPClient(wsdl)

    for code in ["IN", "US"]:
        try:
            capital = client.get_capital_city(code)
            print(f"Capital of {code}: {capital}")
        except Exception:
            print(f"Could not retrieve capital for {code}")


if __name__ == '__main__':
    main()
