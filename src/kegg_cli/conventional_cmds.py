import typer
from Bio.KEGG.REST import (
    kegg_conv,
    kegg_find,
    kegg_get,
    kegg_info,
    kegg_link,
    kegg_list,
)

from kegg_cli.main import app


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
