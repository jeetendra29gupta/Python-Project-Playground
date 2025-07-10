# SOAP WSDL Client Example

This example demonstrates how to create a SOAP client in Python using the `zeep` library to consume a WSDL service. The
example uses the `zeep` library to interact with a SOAP service defined by a WSDL file.

## Requirements

- Python 3.x
- zeep
- lxml

## Installation

You can install the `zeep` & `lxml` library using pip:

```bash
pip install zeep lxml
```

## What is SOAP and WSDL?

- SOAP (Simple Object Access Protocol) is a protocol for exchanging structured information in the implementation of web
  services. It relies on XML as its message format and typically uses HTTP or SMTP for message transmission.
- WSDL (Web Services Description Language) is an XML-based language for describing the functionality offered by a web
  service. It provides a machine-readable description of how the service can be called, what parameters it expects, and
  what data structures it returns.