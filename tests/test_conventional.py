import pytest
from typer.testing import CliRunner
from kegg_cli.main import app, SeqType

runner = CliRunner()

def test_list():
    result = runner.invoke(app, ["list", "genes"])
    assert result.exit_code == 0
    assert "gene" in result.output  # Replace with actual expected response

def test_get_seq_ntseq():
    input_ids = "eco:b0001 eco:b0002"
    with runner.isolated_filesystem():
        input_file = "input.txt"
        with open(input_file, "w") as f:
            f.write(input_ids)

        result = runner.invoke(app, ["get-seq", input_file, "--seq-type", SeqType.ntseq.value])
        assert result.exit_code == 0
        assert "Retrieved" in result.output

def test_get_seq_aaseq():
    input_ids = "eco:b0001 eco:b0002"
    with runner.isolated_filesystem():
        input_file = "input.txt"
        with open(input_file, "w") as f:
            f.write(input_ids)

        result = runner.invoke(app, ["get-seq", input_file, "--seq-type", SeqType.aaseq.value])
        assert result.exit_code == 0
        assert "Retrieved" in result.output

