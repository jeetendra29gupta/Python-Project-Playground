from flask import Flask, jsonify, request

app = Flask(__name__)


# Basic route to return a welcome message.
# Access the route by visiting: http://127.0.0.1:8181/
@app.route('/')
def home():
    """
    Home route to provide a basic welcome message.
    Returns:
        str: A welcome message.
    """
    return "Welcome to the Flask app!"


# Simple API route (GET request).
# Access the route by visiting: http://127.0.0.1:8181/api/get_example
@app.route('/api/get_example', methods=['GET'])
def get_example():
    """
    A simple GET API endpoint returning a basic message.
    Returns:
        json: A JSON response with a message.
    """
    return jsonify({"message": "This is a GET response"})


# Simple API route (GET request) with a single query parameter.
# Access the route by visiting: http://127.0.0.1:8181/api/query_example?name=Sameer
@app.route('/api/query_example', methods=['GET'])
def query_example():
    """
    A GET endpoint that accepts a 'name' query parameter and responds with a message.

    Parameters:
        name (str): The name passed via query string. Defaults to 'Guest'.

    Returns:
        json: A JSON response with a personalized greeting.
    """
    name = request.args.get('name', 'Guest')  # Retrieve 'name' query parameter, default to 'Guest'
    return jsonify({"message": f"Hello, {name}!"})


# Simple API route (GET request) with multiple query parameters.
# Access the route by visiting: http://127.0.0.1:8181/api/multi_query_example?name=Sameer&age=30
@app.route('/api/multi_query_example', methods=['GET'])
def multi_query_example():
    """
    A GET endpoint that accepts multiple query parameters ('name' and 'age') and returns a message.

    Parameters:
        name (str): The name passed via query string. Defaults to 'Guest'.
        age (str): The age passed via query string. Defaults to 'unknown'.

    Returns:
        json: A JSON response with a personalized message containing the name and age.
    """
    name = request.args.get('name', 'Guest')  # Retrieve 'name' query parameter, default to 'Guest'
    age = request.args.get('age', 'unknown')  # Retrieve 'age' query parameter, default to 'unknown'
    return jsonify({"message": f"Hello, {name}! You are {age} years old."})


# Simple API route (GET request) with default query parameters.
# Access the route by visiting: http://127.0.0.1:8181/api/default_query_example
@app.route('/api/default_query_example', methods=['GET'])
def default_query_example():
    """
    A GET endpoint that returns a message with the default query parameters (name and age).
    Defaults are 'Guest' for name and 'unknown' for age.

    Parameters:
        name (str): The name passed via query string. Defaults to 'Guest'.
        age (str): The age passed via query string. Defaults to 'unknown'.

    Returns:
        json: A JSON response with a personalized message containing the name and age.
    """
    name = request.args.get('name', 'Guest')
    age = request.args.get('age', 'unknown')
    return jsonify({"message": f"Hello, {name}! You are {age} years old."})


# Simple API route (GET request) with URL parameters.
# Access the route by visiting: http://127.0.0.1:8181/api/url_example/Sameer/30
@app.route('/api/url_example/<name>/<int:age>', methods=['GET'])
def url_example(name, age):
    """
    A GET endpoint that takes 'name' and 'age' as URL parameters and returns a personalized message.

    Parameters:
        name (str): The name passed as part of the URL.
        age (int): The age passed as part of the URL.

    Returns:
        json: A JSON response with a personalized message containing the name and age.
    """
    # Debugging to check types (optional)
    print("name", type(name), "age", type(age))  # For debugging purpose
    return jsonify({"message": f"Hello, {name}! You are {age} years old."})


# Simple API route (GET request) with other types of URL parameters.
# Access the route by visiting: http://127.0.0.1:8181/api/other_url_example/1/2.5
@app.route('/api/other_url_example/<int:ids>/<float:score>', methods=['GET'])
def other_url_example(ids, score):
    """
    A GET endpoint that accepts two types of URL parameters: an integer 'ids' and a float 'score'.

    Parameters:
        ids (int): An integer passed as part of the URL.
        score (float): A float passed as part of the URL.

    Returns:
        json: A JSON response with the provided 'ids' and 'score'.
    """
    # Debugging to check types (optional)
    print(type(ids), type(score))  # For debugging purpose
    return jsonify({"message": f"ID: {ids}, Score: {score}"})


# Simple API route (POST request).
@app.route('/api/post_example', methods=['POST'])
def post_example():
    """
    A POST endpoint that accepts JSON data in the request body and returns a personalized message.

    Request Body (JSON):
        {
            "name": "string",
            "age": "int"
        }

    Returns:
        json: A JSON response with a personalized message based on the provided data.
    """
    data = request.get_json()  # Get the incoming JSON data
    if not data:
        return jsonify({"error": "No data provided"}), 400  # Bad request if no data is provided
    name = data.get('name', 'Guest')
    age = data.get('age', 'unknown')
    return jsonify({"message": f"Hello, {name}! You are {age} years old."})


# Simple API route (PUT request).
@app.route('/api/put_example', methods=['PUT'])
def put_example():
    """
    A PUT endpoint that accepts JSON data in the request body and returns an updated message.

    Request Body (JSON):
        {
            "name": "string",
            "age": "int"
        }

    Returns:
        json: A JSON response with the updated message based on the provided data.
    """
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400
    name = data.get('name', 'Guest')
    age = data.get('age', 'unknown')
    return jsonify({"message": f"Updated: Hello, {name}! You are {age} years old."})


# Simple API route (DELETE request).
@app.route('/api/delete_example', methods=['DELETE'])
def delete_example():
    """
    A DELETE endpoint that accepts JSON data and returns a message indicating that the data has been deleted.

    Request Body (JSON):
        {
            "name": "string",
            "age": "int"
        }

    Returns:
        json: A JSON response indicating the deletion of the provided data.
    """
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400
    name = data.get('name', 'Guest')
    age = data.get('age', 'unknown')
    return jsonify({"message": f"Deleted: Hello, {name}! You were {age} years old."})


# Simple API route (PATCH request).
@app.route('/api/patch_example', methods=['PATCH'])
def patch_example():
    """
    A PATCH endpoint that accepts JSON data and returns a message indicating the data has been patched.

    Request Body (JSON):
        {
            "name": "string",
            "age": "int"
        }

    Returns:
        json: A JSON response indicating the data has been patched.
    """
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400
    name = data.get('name', 'Guest')
    age = data.get('age', 'unknown')
    return jsonify({"message": f"Patched: Hello, {name}! You are {age} years old."})


# Dynamic Route with Multiple Methods (GET, POST, PUT, DELETE, PATCH)
@app.route('/api/dynamic_example/<int:ids>', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
def dynamic_example(ids):
    """
    A dynamic route that accepts different HTTP methods (GET, POST, PUT, DELETE, PATCH)
    and responds accordingly based on the method.
    # Other methods: Head, Options, Trace, Connect

    Parameters:
        ids (int): The ID passed as part of the URL.

    Returns:
        json: A JSON response depending on the HTTP method used.
    """
    if request.method == 'GET':
        return jsonify({"message": f"GET request for ID: {ids}"})
    elif request.method == 'POST':
        data = request.get_json()
        return jsonify({"message": f"POST request for ID: {ids}, Data: {data}"})
    elif request.method == 'PUT':
        data = request.get_json()
        return jsonify({"message": f"PUT request for ID: {ids}, Data: {data}"})
    elif request.method == 'DELETE':
        return jsonify({"message": f"DELETE request for ID: {ids}"})
    elif request.method == 'PATCH':
        data = request.get_json()
        return jsonify({"message": f"PATCH request for ID: {ids}, Data: {data}"})
    else:
        return jsonify({"error": "Method not allowed"}), 405


# Start the Flask app
if __name__ == '__main__':
    # Run the app with the specified host and port, enabling debug mode for development
    app.run(host="0.0.0.0", port=8181, debug=True)
