import hashlib
import os

from typer.testing import CliRunner

from kegg_cli.arg_enums import SeqType
from kegg_cli.main import app

runner = CliRunner()


def calculate_md5(file_path):
    """Calculate the MD5 hash of a file."""
    hasher = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def test_get_seq_file_ntseq():
    input_ids = """
    rsz:108806876
    rsz:108839148
    rsz:108848881
    rsz:108857319
    """.strip()
    expected_file = f"{os.path.dirname(__file__)}/data/expected_ntseq.fasta"
    output_file = "test_get_seq_ntseq.fasta"

    with runner.isolated_filesystem():
        input_file = "input.txt"
        with open(input_file, "w") as f:
            f.write(input_ids)

        result = runner.invoke(app, ["get-seq", input_file, "--seq-type", SeqType.ntseq.value, "-o", output_file])

        assert result.exit_code == 0
        assert os.path.exists(output_file)
        assert calculate_md5(output_file) == calculate_md5(expected_file)


def test_get_seq_file_aaseq():
    input_ids = """
    rsz:108806876
    rsz:108839148
    rsz:108848881
    rsz:108857319
    """.strip()
    expected_file = f"{os.path.dirname(__file__)}/data/expected_aaseq.fasta"
    output_file = "test_get_seq_aaseq.fasta"

    with runner.isolated_filesystem():
        input_file = "input.txt"
        with open(input_file, "w") as f:
            f.write(input_ids)

        result = runner.invoke(app, ["get-seq", input_file, "--seq-type", SeqType.aaseq.value, "-o", output_file])

        assert result.exit_code == 0
        assert os.path.exists(output_file)
        assert calculate_md5(output_file) == calculate_md5(expected_file)
