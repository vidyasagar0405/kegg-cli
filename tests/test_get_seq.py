import os
import hashlib
import pytest
from typer.testing import CliRunner
from kegg_cli.main import app, SeqType

runner = CliRunner()

def calculate_md5(file_path):
    """Calculate the MD5 hash of a file."""
    hasher = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hasher.update(chunk)
    return hasher.hexdigest()

def test_get_seq_ntseq():
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

        # Write input IDs to a temporary input file
        with open(input_file, "w") as f:
            f.write(input_ids)

        # Invoke the CLI command
        result = runner.invoke(app, ["get-seq", input_file, "--seq-type", SeqType.ntseq.value, "-o", output_file])

        # Verify the command executed successfully
        assert result.exit_code == 0

        # Verify the output file exists
        assert os.path.exists(output_file)

        # Compare the MD5 hashes of the generated and expected files
        assert calculate_md5(output_file) == calculate_md5(expected_file)

def test_get_seq_aaseq():
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

        # Write input IDs to a temporary input file
        with open(input_file, "w") as f:
            f.write(input_ids)

        # Invoke the CLI command
        result = runner.invoke(app, ["get-seq", input_file, "--seq-type", SeqType.aaseq.value, "-o", output_file])

        # Verify the command executed successfully
        assert result.exit_code == 0

        # Verify the output file exists
        assert os.path.exists(output_file)

        # Compare the MD5 hashes of the generated and expected files
        assert calculate_md5(output_file) == calculate_md5(expected_file)
