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
pathway          KEGG Pathway Database
path             Release 113.0+/01-15, Jan 25
                 Kanehisa Laboratories
                 1,309,284 entries

linked db        module
                 ko
                 <org>
                 genome
                 compound
                 glycan
                 reaction
                 rclass
                 enzyme
                 network
                 disease
                 drug
                 pubmed
"""


def test_info_genes():
    result = runner.invoke(app, ["info", "genes"])
    assert result.exit_code == 0
    assert expected_result_1.strip() in result.output.strip()


def test_info_kegg():
    result = runner.invoke(app, ["info", "pathway"])
    assert result.exit_code == 0
    assert expected_result_2.strip() in result.output.strip()
