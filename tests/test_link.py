import pytest
from typer.testing import CliRunner
from kegg_cli.main import app

runner = CliRunner()

expected_result_1 = """
path:rsz00966\trsz:108805860
path:rsz00966\trsz:108806231
path:rsz00966\trsz:108806403
path:rsz00966\trsz:108812420
path:rsz00966\trsz:108812530
path:rsz00966\trsz:108813098
path:rsz00966\trsz:108813271
path:rsz00966\trsz:108813467
path:rsz00966\trsz:108814109
path:rsz00966\trsz:108814391
path:rsz00966\trsz:108814527
path:rsz00966\trsz:108815254
path:rsz00966\trsz:108818790
path:rsz00966\trsz:108819835
path:rsz00966\trsz:108820205
path:rsz00966\trsz:108821294
path:rsz00966\trsz:108822883
path:rsz00966\trsz:108829823
path:rsz00966\trsz:108830725
path:rsz00966\trsz:108832830
path:rsz00966\trsz:108835158
path:rsz00966\trsz:108840698
path:rsz00966\trsz:108843574
path:rsz00966\trsz:108846410
path:rsz00966\trsz:108848454
path:rsz00966\trsz:108853095
path:rsz00966\trsz:108854183
path:rsz00966\trsz:108855362
path:rsz00966\trsz:108855674
path:rsz00966\trsz:108857098
path:rsz00966\trsz:108862402
path:rsz00966\trsz:130494332
path:rsz00966\trsz:130497108
path:rsz00966\trsz:130507033
path:rsz00966\trsz:130507293
path:rsz00966\trsz:130507531
path:rsz00966\trsz:130507697
path:rsz00966\trsz:130507828
path:rsz00966\trsz:130511890
"""

expected_result_2 = """
hsa:10458\tpath:hsa04520
hsa:10458\tpath:hsa04810
hsa:10458\tpath:hsa05130
hsa:10458\tpath:hsa05135
ece:Z5100\tpath:ece05130
"""

expected_result_3 = """
path:map00010\tcpd:C00022
path:map00010\tcpd:C00024
path:map00010\tcpd:C00031
path:map00010\tcpd:C00033
path:map00010\tcpd:C00036
path:map00010\tcpd:C00068
path:map00010\tcpd:C00074
path:map00010\tcpd:C00084
path:map00010\tcpd:C00085
path:map00010\tcpd:C00103
path:map00010\tcpd:C00111
path:map00010\tcpd:C00118
path:map00010\tcpd:C00186
path:map00010\tcpd:C00197
path:map00010\tcpd:C00221
path:map00010\tcpd:C00236
path:map00010\tcpd:C00267
path:map00010\tcpd:C00354
path:map00010\tcpd:C00469
path:map00010\tcpd:C00631
path:map00010\tcpd:C00668
path:map00010\tcpd:C01159
path:map00010\tcpd:C01172
path:map00010\tcpd:C01451
path:map00010\tcpd:C05125
path:map00010\tcpd:C06186
path:map00010\tcpd:C06187
path:map00010\tcpd:C06188
path:map00010\tcpd:C15972
path:map00010\tcpd:C15973
path:map00010\tcpd:C16255
"""

def test_conv_1():
    result = runner.invoke(app, ["link", "rsz", "rsz00966"])
    assert result.exit_code == 0
    assert expected_result_1.strip() in result.output.strip()

def test_conv_2():
    result = runner.invoke(app, ["link", "pathway", "hsa:10458 ece:Z5100"])
    assert result.exit_code == 0
    assert expected_result_2.strip() in result.output.strip()

def test_conv_3():
    result = runner.invoke(app, ["link", "cpd", "map00010"])
    assert result.exit_code == 0
    assert expected_result_3.strip() in result.output.strip()
