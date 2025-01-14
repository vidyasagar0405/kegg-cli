from typer.testing import CliRunner
from kegg_cli.main import app

runner = CliRunner()

expected_result_1 = """
rsz:19816419\tncbi-proteinid:YP_009046967
rsz:19816420\tncbi-proteinid:YP_009046968
rsz:19816421\tncbi-proteinid:YP_009046969
rsz:19816422\tncbi-proteinid:YP_009046970
"""


expected_result_2 = """
rsz:19816419\tncbi-geneid:19816419
rsz:19816420\tncbi-geneid:19816420
rsz:19816421\tncbi-geneid:19816421
rsz:19816422\tncbi-geneid:19816422
"""

expected_result_3 = """
ncbi-geneid:19816419\trsz:19816419
ncbi-geneid:19816420\trsz:19816420
ncbi-geneid:19816421\trsz:19816421
ncbi-geneid:19816422\trsz:19816422
"""

expected_result_4 = """
ncbi-proteinid:YP_009046967\trsz:19816419
ncbi-proteinid:YP_009046968\trsz:19816420
ncbi-proteinid:YP_009046969\trsz:19816421
ncbi-proteinid:YP_009046970\trsz:19816422
"""

def test_conv_protein():
    result = runner.invoke(app, ["conv", "ncbi-proteinid", "rsz:19816419 rsz:19816420 rsz:19816421 rsz:19816422"])
    assert result.exit_code == 0
    assert expected_result_1.strip() in result.output.strip()

def test_conv_gene():
    result = runner.invoke(app, ["conv", "ncbi-geneid", "rsz:19816419 rsz:19816420 rsz:19816421 rsz:19816422"])
    assert result.exit_code == 0
    assert expected_result_2.strip() in result.output.strip()

def test_conv_ncbigene():
    result = runner.invoke(app, ["conv", "genes", "ncbi-geneid:19816419 ncbi-geneid:19816420 ncbi-geneid:19816421 ncbi-geneid:19816422" ])
    assert result.exit_code == 0
    assert expected_result_3.strip() in result.output.strip()

def test_conv_ncbiprotein():
    result = runner.invoke(app, ["conv", "genes", "ncbi-proteinid:YP_009046967 ncbi-proteinid:YP_009046968 ncbi-proteinid:YP_009046969 ncbi-proteinid:YP_009046970" ])
    assert result.exit_code == 0
    assert expected_result_4 .strip() in result.output.strip()

