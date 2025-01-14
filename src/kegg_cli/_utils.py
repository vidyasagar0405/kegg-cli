from __future__ import annotations

import os
import re
import sys
from datetime import datetime

from Bio.KEGG.REST import kegg_link
from rich import print


def get_random_file_name_current(ext: str) -> str:
    """Generate a random file name with the given extension in the current working directory.

    Args:
        ext (str): The file extension (without the dot)

    Returns:
        str: A file path string in the format '{current_path}/{timestamp}.{ext}'
    """
    now = datetime.now()
    date_time = now.strftime("%H%M_%d%m%Y")
    path = os.getcwd()
    return f"{path}/{date_time}.{ext}"


def combine_ids(ids: list[str]) -> list[str]:
    """Combine a list of IDs into groups of 10, joined by '+'.

    Args:
        ids (list[str]): List of IDs to combine

    Returns:
        list[str]: List of combined ID strings, each containing up to 10 IDs joined by '+'
    """
    return ["+".join(ids[i : i + 10]) for i in range(0, len(ids), 10)]


def file_to_list(file: str, field: int, delimiter: str = "\t") -> list[str]:
    """Read a delimited file and extract values from a specific field/column.

    Args:
        file (str): Path to the input file
        field (int): Zero-based index of the field to extract
        delimiter (str, optional): Field delimiter. Defaults to tab.

    Returns:
        list[str]: List of values extracted from the specified field

    Raises:
        FileNotFoundError: If the input file doesn't exist
    """
    try:
        with open(file) as f:
            return [line.split(delimiter)[field].strip() for line in f]
    except FileNotFoundError:
        print(f"[red]{file} not found. Cannot proceed with gene sequence retrieval.[/red]")
        sys.exit(1)


def get_org(text: str) -> str:
    """Extract organism code from a KEGG identifier string.

    Args:
        text (str): KEGG identifier string (e.g., 'path:hsa00010')

    Returns:
        str: Organism code (e.g., 'hsa')
    """
    # Regular expression to find organism
    pattern = r":(\w+?)(?:_|(?=\d))"
    org = re.findall(pattern, text)
    return org[0]


def pathway_to_list(pathway: str) -> list[str]:
    """Get list of gene IDs associated with a KEGG pathway.

    Args:
        pathway (str): KEGG pathway identifier (e.g., 'path:hsa00010')

    Returns:
        list[str]: List of gene IDs in the pathway
    """
    org = get_org(pathway)
    response = kegg_link(org, pathway).read()

    return [line.split("\t")[1] for line in response.strip().split("\n")]


def module_to_list(module: str) -> list[str]:
    """Get list of gene IDs associated with a KEGG module.

    Args:
        module (str): KEGG module identifier (e.g., 'md:hsa_M00001')

    Returns:
        list[str]: List of gene IDs in the module
    """
    org = get_org(module)
    response = kegg_link(org, module).read()

    return [
        line.split("\t")[1]
        for line in response.strip().split("\n")
        # if module in line.split('\t')[1]
    ]


def concatenate_sequences(combined_ids: list[str], output_file: str) -> None:
    """Concatenate individual sequence files into a single output file.

    Args:
        combined_ids (list[str]): List of combined gene IDs
        output_file (str): Path to the output file

    Note:
        - Reads individual .fa files for each gene ID
        - Concatenates their contents into the output file
        - Deletes individual .fa files after concatenation
    """
    print("[green]Concatenating retrieved gene sequences[/green]")

    with open(output_file, "w") as out_file:
        for gene_id in combined_ids:
            gene_file = f"{gene_id}.fa"
            if os.path.exists(gene_file):
                with open(gene_file) as gf:
                    out_file.write(gf.read())
                os.remove(gene_file)
            else:
                print(f"[red]File {gene_file} not found, skipping...[/red]")

    print(f"[green]All gene sequences saved to {output_file}[/green]")
