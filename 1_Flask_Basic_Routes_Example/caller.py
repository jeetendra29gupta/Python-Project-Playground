import requests


def get_home_message(base_url):
    """
    Sends a GET request to the home endpoint ("/") of the Flask app
    and prints the response or error message.

    Parameters:
        base_url (str): The base URL of the Flask app, e.g., "http://127.0.0.1:8181".
    """
    url = f"{base_url}/"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            # Since the Flask home route returns plain text, use response.text
            print(f"GET Home: Response from '{response.url}': {response.text}")
        else:
            print(f"Failed to access '{response.url}'. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"GET Home Error: {e}")


def get_example_message(base_url):
    """
    Sends a GET request to the '/api/get_example' endpoint of the Flask app
    and prints the JSON response or error message.

    Parameters:
        base_url (str): The base URL of the Flask app, e.g., "http://127.0.0.1:8181".
    """
    url = f"{base_url}/api/get_example"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"GET Example: Response from '{response.url}': {response.json()}")
        else:
            print(f"GET Example Failed: Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"GET Example Error: {e}")


def get_query_example_message(base_url, name="Guest"):
    """
    Sends a GET request to the '/api/query_example' endpoint with a 'name' query parameter
    and prints the JSON response or error message.

    Parameters:
        base_url (str): The base URL of the Flask app, e.g., "http://127.0.0.1:8181".
        name (str): The 'name' query parameter to send in the request. Default is 'Guest'.
    """
    url = f"{base_url}/api/query_example"
    params = {'name': name}

    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            print(f"GET Query: Response from '{response.url}': {response.json()}")
        else:
            print(f"GET Query Failed: Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"GET Query Error: {e}")


def get_multi_query_example(base_url, name="Guest", age="unknown"):
    """
    Sends a GET request to the '/api/multi_query_example' endpoint with 'name' and 'age'
    as query parameters and prints the JSON response or error message.

    Parameters:
        base_url (str): The base URL of the Flask app, e.g., "http://127.0.0.1:8181".
        name (str): The 'name' query parameter. Default is 'Guest'.
        age (str or int): The 'age' query parameter. Default is 'unknown'.
    """
    url = f"{base_url}/api/multi_query_example"
    params = {'name': name, 'age': age}

    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            print(f"GET Multi Query: Response from '{response.url}': {response.json()}")
        else:
            print(f"GET Multi Query Failed: Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"GET Multi Query Error: {e}")


def get_default_query_example(base_url, name=None, age=None):
    """
    Sends a GET request to the '/api/default_query_example' endpoint with optional query parameters.
    Prints the full URL and the JSON response or an error message.

    Parameters:
        base_url (str): The base URL of the Flask app, e.g., "http://127.0.0.1:8181".
        name (str, optional): Optional name to include as a query parameter.
        age (str or int, optional): Optional age to include as a query parameter.
    """
    url = f"{base_url}/api/default_query_example"
    params = {}
    if name is not None:
        params['name'] = name
    if age is not None:
        params['age'] = age

    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            print(f"GET Default Query: Response from '{response.url}': {response.json()}")
        else:
            print(f"GET Default Query Failed: Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"GET Default Query Error: {e}")


def get_url_example_message(base_url, name, age):
    """
    Sends a GET request to the '/api/url_example/<name>/<age>' endpoint,
    passing 'name' and 'age' as URL parameters, and prints the JSON response or error message.

    Parameters:
        base_url (str): The base URL of the Flask app, e.g., "http://127.0.0.1:8181".
        name (str): The 'name' URL parameter.
        age (int): The 'age' URL parameter.
    """
    url = f"{base_url}/api/url_example/{name}/{age}"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"GET URL Example: Response from '{response.url}': {response.json()}")
        else:
            print(f"GET URL Example Failed: Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"GET URL Example Error: {e}")


def get_other_url_example(base_url, ids, score):
    """
    Sends a GET request to the '/api/other_url_example/<ids>/<score>' endpoint,
    passing an integer and a float as URL parameters, and prints the JSON response or error.

    Parameters:
        base_url (str): The base URL of the Flask app, e.g., "http://127.0.0.1:8181".
        ids (int): The integer ID to include in the URL.
        score (float): The float score to include in the URL.
    """
    url = f"{base_url}/api/other_url_example/{ids}/{score}"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"GET Other URL Example: Response from '{response.url}': {response.json()}")
        else:
            print(f"GET Other URL Example Failed: Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"GET Other URL Example Error: {e}")


def post_example(base_url, name="Guest", age="unknown"):
    """
    Sends a POST request to the '/api/post_example' endpoint with 'name' and 'age' in the request body,
    and prints the JSON response or error message.

    Parameters:
        base_url (str): The base URL of the Flask app, e.g., "http://127.0.0.1:8181".
        name (str): The 'name' to include in the request body. Default is 'Guest'.
        age (str or int): The 'age' to include in the request body. Default is 'unknown'.
    """
    url = f"{base_url}/api/post_example"
    payload = {"name": name, "age": age}

    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print(f"POST Example: Response from '{response.url}': {response.json()}")
        else:
            print(f"POST Example Failed: Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"POST Example Error: {e}")


def put_example(base_url, name="Guest", age="unknown"):
    """
    Sends a PUT request to the '/api/put_example' endpoint with 'name' and 'age' in the request body,
    and prints the JSON response or error message.

    Parameters:
        base_url (str): The base URL of the Flask app, e.g., "http://127.0.0.1:8181".
        name (str): The 'name' to include in the request body. Default is 'Guest'.
        age (str or int): The 'age' to include in the request body. Default is 'unknown'.
    """
    url = f"{base_url}/api/put_example"
    payload = {"name": name, "age": age}

    try:
        response = requests.put(url, json=payload)
        if response.status_code == 200:
            print(f"PUT Example: Response from '{response.url}': {response.json()}")
        else:
            print(f"PUT Example Failed: Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"PUT Example Error: {e}")


def delete_example(base_url, name="Guest", age="unknown"):
    """
    Sends a DELETE request to the '/api/delete_example' endpoint with 'name' and 'age' in the request body,
    and prints the JSON response or error message.

    Parameters:
        base_url (str): The base URL of the Flask app, e.g., "http://127.0.0.1:8181".
        name (str): The 'name' to include in the request body. Default is 'Guest'.
        age (str or int): The 'age' to include in the request body. Default is 'unknown'.
    """
    url = f"{base_url}/api/delete_example"
    payload = {"name": name, "age": age}

    try:
        response = requests.delete(url, json=payload)
        if response.status_code == 200:
            print(f"DELETE Example: Response from '{response.url}': {response.json()}")
        else:
            print(f"DELETE Example Failed: Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"DELETE Example Error: {e}")


def patch_example(base_url, name="Guest", age="unknown"):
    """
    Sends a PATCH request to the '/api/patch_example' endpoint with 'name' and 'age' in the request body,
    and prints the JSON response or error message.

    Parameters:
        base_url (str): The base URL of the Flask app, e.g., "http://127.0.0.1:8181".
        name (str): The 'name' to include in the request body. Default is 'Guest'.
        age (str or int): The 'age' to include in the request body. Default is 'unknown'.
    """
    url = f"{base_url}/api/patch_example"
    payload = {"name": name, "age": age}

    try:
        response = requests.patch(url, json=payload)
        if response.status_code == 200:
            print(f"PATCH Example: Response from '{response.url}': {response.json()}")
        else:
            print(f"PATCH Example Failed: Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"PATCH Example Error: {e}")


def dynamic_get(base_url, ids):
    """
    Sends a GET request to the '/api/dynamic_example/<ids>' endpoint with the 'ids' parameter,
    and prints the JSON response or error message.

    Parameters:
        base_url (str): The base URL of the Flask app, e.g., "http://127.0.0.1:8181".
        ids (int): The 'ids' URL parameter to include in the request.
    """
    url = f"{base_url}/api/dynamic_example/{ids}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"GET Dynamic: Response from '{response.url}': {response.json()}")
        else:
            print(f"GET Dynamic Failed: Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"GET Dynamic Error: {e}")


def dynamic_post(base_url, ids, data):
    """
    Sends a POST request to the '/api/dynamic_example/<ids>' endpoint with the 'ids' parameter
    and a JSON payload, and prints the JSON response or error message.

    Parameters:
        base_url (str): The base URL of the Flask app, e.g., "http://127.0.0.1:8181".
        ids (int): The 'ids' URL parameter to include in the request.
        data (dict): The JSON payload to include in the request body.
    """
    url = f"{base_url}/api/dynamic_example/{ids}"
    try:
        response = requests.post(url, json=data)
        if response.status_code == 200:
            print(f"POST Dynamic: Response from '{response.url}': {response.json()}")
        else:
            print(f"POST Dynamic Failed: Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"POST Dynamic Error: {e}")


def dynamic_put(base_url, ids, data):
    """
    Sends a PUT request to the '/api/dynamic_example/<ids>' endpoint with the 'ids' parameter
    and a JSON payload, and prints the JSON response or error message.

    Parameters:
        base_url (str): The base URL of the Flask app, e.g., "http://127.0.0.1:8181".
        ids (int): The 'ids' URL parameter to include in the request.
        data (dict): The JSON payload to include in the request body.
    """
    url = f"{base_url}/api/dynamic_example/{ids}"
    try:
        response = requests.put(url, json=data)
        if response.status_code == 200:
            print(f"PUT Dynamic: Response from '{response.url}': {response.json()}")
        else:
            print(f"PUT Dynamic Failed: Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"PUT Dynamic Error: {e}")


def dynamic_delete(base_url, ids):
    """
    Sends a DELETE request to the '/api/dynamic_example/<ids>' endpoint with the 'ids' parameter,
    and prints the JSON response or error message.

    Parameters:
        base_url (str): The base URL of the Flask app, e.g., "http://127.0.0.1:8181".
        ids (int): The 'ids' URL parameter to include in the request.
    """
    url = f"{base_url}/api/dynamic_example/{ids}"
    try:
        response = requests.delete(url)
        if response.status_code == 200:
            print(f"DELETE Dynamic: Response from '{response.url}': {response.json()}")
        else:
            print(f"DELETE Dynamic Failed: Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"DELETE Dynamic Error: {e}")


def dynamic_patch(base_url, ids, data):
    """
    Sends a PATCH request to the '/api/dynamic_example/<ids>' endpoint with the 'ids' parameter
    and a JSON payload, and prints the JSON response or error message.

    Parameters:
        base_url (str): The base URL of the Flask app, e.g., "http://127.0.0.1:8181".
        ids (int): The 'ids' URL parameter to include in the request.
        data (dict): The JSON payload to include in the request body.
    """
    url = f"{base_url}/api/dynamic_example/{ids}"
    try:
        response = requests.patch(url, json=data)
        if response.status_code == 200:
            print(f"PATCH Dynamic: Response from '{response.url}': {response.json()}")
        else:
            print(f"PATCH Dynamic Failed: Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"PATCH Dynamic Error: {e}")


def requests_caller():
    """
    Calls each of the endpoint functions defined above in sequence
    to demonstrate the expected behavior of each HTTP method.
    """
    base_url = "http://127.0.0.1:8181"
    name = "Sameer"
    age = 30
    ids = 1
    score = 92.5

    payload = {"name": name, "age": age}

    get_home_message(base_url)
    get_example_message(base_url)
    get_query_example_message(base_url, name)
    get_multi_query_example(base_url, name, age)

    # == Without query params (defaults) ==
    get_default_query_example(base_url)
    # == With query params ==
    get_default_query_example(base_url, name="Sameer", age=30)

    get_url_example_message(base_url, name, age)
    get_other_url_example(base_url, ids, score)

    # == POST Example ==
    post_example(base_url, name, age)
    # == PUT Example ==
    put_example(base_url, name, age)
    # == DELETE Example ==
    delete_example(base_url, name, age)
    # == PATCH Example ==
    patch_example(base_url, name, age)

    # == DYNAMIC GET ==
    dynamic_get(base_url, ids)
    # == DYNAMIC POST ==
    dynamic_post(base_url, ids, payload)
    # == DYNAMIC PUT ==
    dynamic_put(base_url, ids, payload)
    # == DYNAMIC DELETE ==
    dynamic_delete(base_url, ids)
    # == DYNAMIC PATCH ==
    dynamic_patch(base_url, ids, payload)


if __name__ == '__main__':
    requests_caller()

"""
GET Home: Response from 'http://127.0.0.1:8181/': Welcome to the Flask app!
GET Example: Response from 'http://127.0.0.1:8181/api/get_example': {'message': 'This is a GET response'}
GET Query: Response from 'http://127.0.0.1:8181/api/query_example?name=Sameer': {'message': 'Hello, Sameer!'}
GET Multi Query: Response from 'http://127.0.0.1:8181/api/multi_query_example?name=Sameer&age=30': {'message': 'Hello, Sameer! You are 30 years old.'}
GET Default Query: Response from 'http://127.0.0.1:8181/api/default_query_example': {'message': 'Hello, Guest! You are unknown years old.'}
GET Default Query: Response from 'http://127.0.0.1:8181/api/default_query_example?name=Sameer&age=30': {'message': 'Hello, Sameer! You are 30 years old.'}
GET URL Example: Response from 'http://127.0.0.1:8181/api/url_example/Sameer/30': {'message': 'Hello, Sameer! You are 30 years old.'}
GET Other URL Example: Response from 'http://127.0.0.1:8181/api/other_url_example/1/92.5': {'message': 'ID: 1, Score: 92.5'}
POST Example: Response from 'http://127.0.0.1:8181/api/post_example': {'message': 'Hello, Sameer! You are 30 years old.'}
PUT Example: Response from 'http://127.0.0.1:8181/api/put_example': {'message': 'Updated: Hello, Sameer! You are 30 years old.'}
DELETE Example: Response from 'http://127.0.0.1:8181/api/delete_example': {'message': 'Deleted: Hello, Sameer! You were 30 years old.'}
PATCH Example: Response from 'http://127.0.0.1:8181/api/patch_example': {'message': 'Patched: Hello, Sameer! You are 30 years old.'}
GET Dynamic: Response from 'http://127.0.0.1:8181/api/dynamic_example/1': {'message': 'GET request for ID: 1'}
POST Dynamic: Response from 'http://127.0.0.1:8181/api/dynamic_example/1': {'message': "POST request for ID: 1, Data: {'name': 'Sameer', 'age': 30}"}
PUT Dynamic: Response from 'http://127.0.0.1:8181/api/dynamic_example/1': {'message': "PUT request for ID: 1, Data: {'name': 'Sameer', 'age': 30}"}
DELETE Dynamic: Response from 'http://127.0.0.1:8181/api/dynamic_example/1': {'message': 'DELETE request for ID: 1'}
PATCH Dynamic: Response from 'http://127.0.0.1:8181/api/dynamic_example/1': {'message': "PATCH request for ID: 1, Data: {'name': 'Sameer', 'age': 30}"}
"""
