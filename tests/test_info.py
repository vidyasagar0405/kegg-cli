import pytest
from typer.testing import CliRunner
from kegg_cli.main import app

runner = CliRunner()

expected_result_1 = """
genes            KEGG Genes Database
genes            Release 113.0+/01-14, Jan 25
                 Kanehisa Laboratories
                 57,888,170 entries

"""

expected_result_2 = """
kegg             Kyoto Encyclopedia of Genes and Genomes
kegg             Release 113.0+/01-14, Jan 25
                 Kanehisa Laboratories
                 pathway   1,309,284 entries
                 brite       411,448 entries
                 module          576 entries
                 orthology    27,345 entries
                 genome       25,263 entries
                 genes     57,888,170 entries
                 compound     19,437 entries
                 glycan       11,232 entries
                 reaction     12,209 entries
                 rclass        3,202 entries
                 enzyme        8,235 entries
                 network       1,589 entries
                 variant       1,528 entries
                 disease       2,832 entries
                 drug         12,564 entries
                 dgroup        2,491 entries
"""

def test_info_genes():
    result = runner.invoke(app, ["info", "genes"])
    assert result.exit_code == 0
    assert expected_result_1.strip() in result.output.strip()

def test_info_kegg():
    result = runner.invoke(app, ["info", "kegg"])
    assert result.exit_code == 0
    assert expected_result_2.strip() in result.output.strip()
