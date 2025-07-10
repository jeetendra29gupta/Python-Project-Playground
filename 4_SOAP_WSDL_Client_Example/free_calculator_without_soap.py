"""
SOAP Calculator Client using raw HTTP and XML.

This client sends a SOAP request to perform the Add operation using
the public calculator web service and parses the XML response.

Dependencies:
    - requests
    - xmltodict

Install:
    pip install requests xmltodict
"""

import logging

import requests
import xmltodict

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class SOAPCalculatorClient:
    """
    SOAP client that interacts with the calculator web service
    using raw HTTP and XML.
    """

    def __init__(self, service_url: str, int_a: int, int_b: int):
        """
        Initialize the SOAP client.

        :param service_url: The endpoint URL of the SOAP service.
        :param int_a: First integer for the operation.
        :param int_b: Second integer for the operation.
        """
        self.url = service_url
        self.int_a = int_a
        self.int_b = int_b

    def build_request_body(self) -> str:
        """
        Build the SOAP request body for the Add operation.

        :return: SOAP request body as a string.
        """
        return f"""
<soap-env:Envelope xmlns:soap-env="http://schemas.xmlsoap.org/soap/envelope/">
  <soap-env:Body>
    <ns0:Add xmlns:ns0="http://tempuri.org/">
      <ns0:intA>{self.int_a}</ns0:intA>
      <ns0:intB>{self.int_b}</ns0:intB>
    </ns0:Add>
  </soap-env:Body>
</soap-env:Envelope>
""".strip()

    def call_add(self) -> int:
        """
        Call the Add operation of the SOAP service.

        :return: The result of the Add operation as an integer.
        :raises: requests.HTTPError if the request fails.
        """
        headers = {
            "Content-Type": "text/xml; charset=utf-8",
            "SOAPAction": "http://tempuri.org/Add"
        }

        request_body = self.build_request_body()
        logger.info("Sending SOAP request:\n%s", request_body)

        response = requests.post(self.url, data=request_body.encode("utf-8"), headers=headers)
        logger.info("Received response with status code: %s", response.status_code)
        response.raise_for_status()

        logger.debug("Raw Response:\n%s", response.text)

        # Parse the response and extract the result
        parsed_response = xmltodict.parse(response.text)
        try:
            result = parsed_response['soap:Envelope']['soap:Body']['AddResponse']['AddResult']
            return int(result)
        except (KeyError, TypeError, ValueError) as e:
            logger.error("Failed to parse Add result from response.")
            raise e


def main():
    """
    Main function to demonstrate calling the Add operation.
    """
    service_url = "http://www.dneonline.com/calculator.asmx"
    int_a = 10
    int_b = 20

    client = SOAPCalculatorClient(service_url, int_a, int_b)
    try:
        result = client.call_add()
        logger.info("Add(%d, %d) = %d", int_a, int_b, result)
    except Exception:
        logger.exception("An error occurred while calling the SOAP service.")


if __name__ == '__main__':
    main()
