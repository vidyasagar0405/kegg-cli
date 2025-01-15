import os
import sys
import time

import typer
from Bio.KEGG.REST import kegg_get
from rich import print

from kegg_cli._utils import (
    combine_ids,
    concatenate_sequences,
    file_to_list,
    get_random_file_name_current,
    module_to_list,
    pathway_to_list,
)
from kegg_cli.arg_enums import SeqType

app = typer.Typer()


@app.command()
def get_seq(
            input: str = typer.Argument(..., help="Pathway code (path:hsa00010) or Module (md:rsz_M00005) or Input file or args ('id1 id2') of gene IDs"),
            delimiter: str = typer.Option("\t", "--delimiter", help="file delimiter"),
            field: int = typer.Option(0, "--field", help="geneID cloumn/field in file"),
            seq_type: SeqType = typer.Option(SeqType.ntseq, "--seq-type", help="Type of sequence to retrieve"),
            output: str = typer.Option(get_random_file_name_current("fasta"), "-o", "--output", help="Output file to save concatenated sequences"),
            ):
    """ Fetches the nucleotide/amino acid sequence of given IDs (Arg or File) / Pathway / Module

    This function provides multiple ways to retrieve sequences:
    1. From a KEGG pathway
    2. From a KEGG module
    3. From a file containing gene IDs
    4. From direct input of space-separated gene IDs

    The function handles rate limiting and batch processing automatically:
    - Retrieves sequences in batches of 10 genes
    - Includes a 1/3 second delay between requests
    - Concatenates all sequences into a single FASTA file

    Args:
        input (str): Source of gene IDs. Can be one of:
            - KEGG pathway (e.g., "path:hsa00010" for human glycolysis pathway)
            - KEGG module (e.g., "md:M00001" for glycolysis module)
            - File path (e.g., "genes.txt" containing one gene ID per line)
            - Space-separated IDs (e.g., "hsa:10458 hsa:10460")
        delimiter (str, optional): Delimiter used in input file. Defaults to tab ("\t").
            Use different delimiters for files with other formats:
            - "\t" for TSV files
            - "," for CSV files
            - " " for space-separated files
        field (int, optional): Zero-based index of column containing gene IDs in input file.
            Defaults to 0 (first column). Examples:
            - 0 for first column
            - 1 for second column
            - 2 for third column
        seq_type (SeqType, optional): Type of sequence to retrieve. Defaults to "ntseq".
            Options:
            - "ntseq" for nucleotide sequences
            - "aaseq" for amino acid sequences
        output (str, optional): Path for output FASTA file. Defaults to timestamp-based filename.

    Raises:
        FileNotFoundError: If the specified input file doesn't exist
        Exception: If sequence retrieval fails for any gene ID

    Notes:
        - Temporary .fa files are created during processing and automatically cleaned up
        - Rate limiting is implemented to avoid overwhelming the KEGG server
        - Large sets of genes are automatically processed in batches of 10
    """

    if os.path.exists(input):
        gene_ids = file_to_list(input, field, delimiter)
    elif "path:" in input:
        gene_ids = pathway_to_list(input)
    elif "md:" in input:
        gene_ids = module_to_list(input)
    elif type(input) is str:
        gene_ids = input.split(" ")

    try:
        total_genes = len(gene_ids)
        print(f"[green]Found {total_genes} gene IDs[/green]")

        combined_list = combine_ids(gene_ids)

        for index, gene_id in enumerate(combined_list, start=1):
            try:
                response = kegg_get(gene_id, seq_type.value).read()
                with open(f"{gene_id}.fa", "w") as gene_file:
                    gene_file.write(response)
                print(
                    f"[green][{index}/{len(combined_list)}] Retrieved {gene_id.replace('+', ',')} gene {seq_type.value}[/green]"
                )
                time.sleep(0.3333333333)  # To avoid overwhelming the server
            except Exception as e:
                print(f"[red][{index}/{len(combined_list)}] Failed to retrieve {gene_id}: {e}[/red]")

    except FileNotFoundError:
        print(f"[red]{input} not found. Cannot proceed with gene sequence retrieval.[/red]")
        sys.exit(1)

    concatenate_sequences(combined_list, output)
