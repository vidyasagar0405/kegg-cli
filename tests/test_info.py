import pytest
from typer.testing import CliRunner
from kegg_cli.main import app

runner = CliRunner()

expected_result = """
genes            KEGG Genes Database
genes            Release 113.0+/01-14, Jan 25
                 Kanehisa Laboratories
                 57,888,170 entries

"""

def test_info():
    result = runner.invoke(app, ["info", "genes"])
    assert result.exit_code == 0
    assert expected_result.strip() in result.output.strip()
