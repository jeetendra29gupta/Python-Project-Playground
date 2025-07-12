import pytest

from src.my_poetry_project_flask.app import app

def test_hello_world():
    with app.test_client() as client:
        response = client.get('/')
        assert response.data == b'Hello, Poetry & Flask!'

if __name__ == '__main__':
    pytest.main()