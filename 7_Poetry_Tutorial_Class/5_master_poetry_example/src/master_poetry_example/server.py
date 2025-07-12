from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello from Flask!"


def main():
    app.run(host="0.0.0.0", port=8181, debug=True)


if __name__ == "__main__":
    main()
