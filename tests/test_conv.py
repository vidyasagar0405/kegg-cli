import pytest
from typer.testing import CliRunner
from kegg_cli.main import app

runner = CliRunner()

expected_result_1 = """

"""

def test_conv():
    result = runner.invoke(app, ["conv", "ncbi-geneid", "genes"])
    assert result.exit_code == 0
    assert expected_result_1.strip() in result.output.strip()
