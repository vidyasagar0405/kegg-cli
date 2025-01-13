import os
import time

import typer
from Bio.KEGG.REST import (
    kegg_get,
)
from rich import print

from kegg_cli._utils import combine_ids, file_to_list, get_random_file_name_current
from kegg_cli.conventional_cmds import info, get, list, find, conv, link
from kegg_cli.arg_enums import SeqType

app = typer.Typer()

app.command()(info)
app.command()(get)
app.command()(list)
app.command()(find)
app.command()(conv)
app.command()(link)

@app.command()
def get_seq(input: str = typer.Argument(..., help="Input file or list of gene IDs"), 
             seq_type: SeqType = typer.Option(SeqType.ntseq, "--seq-type", help="Type of sequence to retrieve"), 
             output: str = typer.Option(get_random_file_name_current("fasta"), "-o", "--output", help="Output file to save concatenated sequences")):
    if os.path.exists(input):
        gene_ids = file_to_list(input)
    elif type(input) is str:
        gene_ids = input.split(" ")

    try:
        total_genes = len(gene_ids)
        print(f"[green]Found {total_genes} gene IDs[/green]")

        combined_list = combine_ids(gene_ids)

        for index, gene_id in enumerate(combined_list, start=1):
            try:
                response = kegg_get(gene_id, seq_type.value).read()
                with open(f"{gene_id}.fa", 'w') as gene_file:
                    gene_file.write(response)
                print(f"[green][{index}/{len(combined_list)}] Retrieved {gene_id.replace('+', ',')} gene {seq_type.value}[/green]")
                time.sleep(0.4)  # To avoid overwhelming the server
            except Exception as e:
                print(f"[red][{index}/{len(combined_list)}] Failed to retrieve {gene_id}: {e}[/red]")

    except FileNotFoundError:
        print(f"[red]{input} not found. Cannot proceed with gene sequence retrieval.[/red]")
        exit(1)

    concatenate_sequences(combined_list, output)

def concatenate_sequences(combined_ids, output_file):
    print("[green]Concatenating retrieved gene sequences[/green]")

    with open(output_file, 'w') as out_file:
        for gene_id in combined_ids:
            gene_file = f"{gene_id}.fa"
            if os.path.exists(gene_file):
                with open(gene_file, 'r') as gf:
                    out_file.write(gf.read())
                os.remove(gene_file)
            else:
                print(f"[red]File {gene_file} not found, skipping...[/red]")

    print(f"[green]All gene sequences saved to {output_file}[/green]")

def main():
    app()

if __name__ == "__main__":
    main()
