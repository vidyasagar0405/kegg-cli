from __future__ import annotations

import os
import re
import sys
from datetime import datetime

from Bio.KEGG.REST import kegg_link
from rich import print


def get_random_file_name_current(ext: str) -> str:
    """
    generates a file name with the given ext parameter in the current working dir
    """
    now = datetime.now()
    date_time = now.strftime("%H%M_%d%m%Y")
    path = os.getcwd()
    return f"{path}/{date_time}.{ext}"


def combine_ids(ids: list[str]) -> list[str]:
    return ["+".join(ids[i : i + 10]) for i in range(0, len(ids), 10)]


def file_to_list(file: str, field: int, delimiter: str = "\t") -> list[str]:
    try:
        with open(file) as f:
            return [line.split(delimiter)[field].strip() for line in f]
    except FileNotFoundError:
        print(f"[red]{file} not found. Cannot proceed with gene sequence retrieval.[/red]")
        sys.exit(1)


def get_org(text) -> str:
    # Regular expression to find organism
    pattern = r":(\w+?)(?:_|(?=\d))"
    org = re.findall(pattern, text)
    return org[0]


def pathway_to_list(pathway: str) -> list[str]:
    org = get_org(pathway)
    response = kegg_link(org, pathway).read()

    return [line.split("\t")[1] for line in response.strip().split("\n")]


def module_to_list(module: str) -> list[str]:
    org = get_org(module)
    response = kegg_link(org, module).read()

    return [
        line.split("\t")[1]
        for line in response.strip().split("\n")
        # if module in line.split('\t')[1]
    ]


def concatenate_sequences(combined_ids, output_file):
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
