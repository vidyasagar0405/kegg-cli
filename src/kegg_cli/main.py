import os
import time

import typer
from Bio.KEGG.REST import (
    kegg_conv,
    kegg_find,
    kegg_get,
    kegg_info,
    kegg_link,
    kegg_list,
)
from rich import print

from kegg_cli._utils import combine_ids, file_to_list, get_random_file_name_current

app = typer.Typer()

@app.command()
def info(query: str):
    print(kegg_info(query).read())

@app.command()
def get(query: str):
    print(kegg_get(query).read())

@app.command()
def list(query: str):
    print(kegg_list(query).read())

@app.command()
def find(query: str, db: str = typer.Option("-db")):
    print(kegg_find(db,query).read())

@app.command()
def conv(to_db :str, from_db: str):
    print(kegg_conv(to_db, from_db).read())

@app.command()
def link(query: str, db: str = typer.Option("-db")):
    print(kegg_link(db,query).read())

@app.command()
# Step 2: Download each gene's nucleotide sequence
def get_seq(input:str, seq_type="ntseq", output:str = typer.Option(get_random_file_name_current("fasta"), "-o", "--output")):
    
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
                response = kegg_get(gene_id, seq_type).read()
                with open(f"{gene_id}.fa", 'w') as gene_file:
                    gene_file.write(response)
                print(f"[green][{index}/{len( combined_list )}] Retrieved {gene_id.replace("+", ",")} gene ntseq[/green]")
                time.sleep(0.4)  # To avoid overwhelming the server
            except:
                print(f"[red][{index}/{len( combined_list )}] Failed to retrieve {gene_id}[/red]")

    except FileNotFoundError:
        print(f"[red]{input} not found. Cannot proceed with gene sequence retrieval.[/red]")
        exit(1)
    concatenate_sequences(combined_list, output)

# Step 3: Concatenate all .fa files into a single file and clean up
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
