import pytest
from typer.testing import CliRunner
from kegg_cli.main import app

runner = CliRunner()

expected_result_1 = """
osa:4327069\tprotein RALF-like 33
osa:4326020\tprotein RALF-like 33
osa:107278572\tprotein RALF-like 33
osa:107278442\tprotein RALF-like 33
osa:4338064\tprotein RALF-like 33
osa:112937380\tprotein RALF-like 1
dosa:Os01g0357900\tSimilar to RALF
dosa:Os11g0456000\tSimilar to RALF
"""

expected_result_2 = """
cpd:C00493\tC7H10O5
cpd:C04236\tC7H10O5
cpd:C16588\tC7H10O5
cpd:C17696\tC7H10O5
cpd:C18307\tC7H10O5
cpd:C18312\tC7H10O5
cpd:C20961\tC7H10N2O5
cpd:C21281\tC7H10O5
"""

expected_result_3 = """
path:map00966\tGlucosinolate biosynthesis
"""

def test_find_no_arg():
    result = runner.invoke(app, ["find", "ralf osa"])
    assert result.exit_code == 0
    assert expected_result_1.strip() in result.output.strip()

def test_find_all_arg():
    result = runner.invoke(app, [ "find", "C7H10O5", "-db", "compound", "-op", "formula" ])
    assert result.exit_code == 0
    assert expected_result_2.strip() in result.output.strip()

def test_find_only_db():
    result = runner.invoke(app, [ "find", "glucosi", "-db", "pathway" ])
    assert result.exit_code == 0
    assert expected_result_3.strip() in result.output.strip()
