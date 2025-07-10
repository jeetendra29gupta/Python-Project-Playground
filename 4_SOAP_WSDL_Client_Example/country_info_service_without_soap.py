"""
SOAP Client using raw HTTP and XML for CountryInfoService.

Performs the CapitalCity operation by manually constructing the SOAP XML request.

Dependencies:
    - requests
    - xmltodict

To install:
    pip install requests xmltodict
"""

import logging

import requests
import xmltodict

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class CountryInfoRawSOAPClient:
    """
    SOAP client using raw HTTP and XML to interact with CountryInfoService.
    """

    def __init__(self, service_url: str, country_code: str):
        """
        Initialize the client.

        :param service_url: Endpoint of the SOAP service.
        :param country_code: Country ISO code.
        """
        self.url = service_url
        self.country_code = country_code

    def build_request_body(self) -> str:
        """
        Construct the SOAP envelope for the CapitalCity operation.

        :return: SOAP XML string.
        """
        return f"""
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"
               xmlns:web="http://www.oorsprong.org/websamples.countryinfo">
  <soap:Body>
    <web:CapitalCity>
      <web:sCountryISOCode>{self.country_code}</web:sCountryISOCode>
    </web:CapitalCity>
  </soap:Body>
</soap:Envelope>
""".strip()

    def call_capital_city(self) -> str:
        """
        Send the request and parse the capital city response.

        :return: Capital city name.
        """
        headers = {
            "Content-Type": "text/xml; charset=utf-8",
            "SOAPAction": "http://www.oorsprong.org/websamples.countryinfo/CountryInfoService.wso/CapitalCity"
        }

        body = self.build_request_body()
        logger.info("Sending SOAP request:\n%s", body)

        response = requests.post(self.url, data=body.encode("utf-8"), headers=headers)
        logger.info("Received status code: %s", response.status_code)
        response.raise_for_status()

        try:
            data = xmltodict.parse(response.text)
            capital = data['soap:Envelope']['soap:Body']['m:CapitalCityResponse']['m:CapitalCityResult']
            logger.info(f"Capital of {self.country_code}: {capital}")
            return capital
        except Exception:
            logger.exception("Failed to parse SOAP response.")
            raise


def main():
    service_url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"
    for code in ["IN", "US"]:
        client = CountryInfoRawSOAPClient(service_url, code)
        try:
            capital = client.call_capital_city()
            print(f"Capital of {code}: {capital}")
        except Exception:
            print(f"Could not retrieve capital for {code}")


if __name__ == '__main__':
    main()
