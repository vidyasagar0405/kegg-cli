import pytest
from typer.testing import CliRunner
from kegg_cli.main import app

runner = CliRunner()

expected_result_1 = """
rsz:19816419\tndhE, RadishC_p075; NADH dehydrogenase subunit 4L
rsz:19816420\tndhG, RadishC_p076; NADH dehydrogenase subunit 6
rsz:19816421\tndhI, RadishC_p077; NADH dehydrogenase subunit I
rsz:19816422\tndhA, RadishC_p078; NADH dehydrogenase subunit 1
rsz:19816423\tndhH, RadishC_p079; NADH dehydrogenase subunit 7
rsz:19816424\trps15, RadishC_p080; ribosomal protein S15
rsz:19816425\tycf1, RadishC_p081; Ycf1
rsz:19816435\trps7, RadishC_p082; ribosomal protein S7
rsz:19816436\tndhB, RadishC_p083; NADH dehydrogenase subunit 2
rsz:19816438\tycf15, RadishC_p084; Ycf15
rsz:19816439\tycf2, RadishC_p085; Ycf2
rsz:19816441\trpl23, RadishC_p086; ribosomal protein L23
rsz:19816442\trpl2, RadishC_p087; ribosomal protein L2
rsz:19816443\trps12, RadishC_p045; ribosomal protein S12
"""

expected_result_2 = """
C01290	Lactosylceramide; beta-D-Galactosyl-(1->4)-beta-D-glucosyl-(1<->1)-ceramide; beta-D-Galactosyl-1,4-beta-D-glucosylceramide; Gal-beta1->4Glc-beta1->1'Cer; LacCer; Lactosyl-N-acylsphingosine; D-Galactosyl-1,4-beta-D-glucosylceramide
G00092	Lactosylceramide; LacCer; CD17; (Gal)1 (Glc)1 (Cer)1
"""

def test_list_gene():
    result = runner.invoke(app, ["list", "rsz:19816419 rsz:19816420 rsz:19816421 rsz:19816422 rsz:19816423 rsz:19816424 rsz:19816425 rsz:19816435 rsz:19816436 rsz:19816438 rsz:19816439 rsz:19816441 rsz:19816442 rsz:19816443"])
    assert result.exit_code == 0
    assert expected_result_1.strip() in result.output.strip()

def test_list_cmp():
    result = runner.invoke(app, ["list", "C01290 G00092"])
    assert result.exit_code == 0
    assert expected_result_2.strip() in result.output.strip()
