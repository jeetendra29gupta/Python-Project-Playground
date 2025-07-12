import pytest
from src.master_poetry_example.server import app
from src.master_poetry_example.client import main as cli_main
from click.testing import CliRunner


def test_root():
    client = app.test_client()
    res = client.get("/")
    assert res.data == b"Hello from Flask!"


def test_click_cli():
    runner = CliRunner()
    result = runner.invoke(cli_main, ["--name", "Jeetendra"])
    assert result.exit_code == 0
    assert "Hello, Jeetendra from Click + Poetry!" in result.output


if __name__ == "__main__":
    pytest.main(["-v", __file__])
