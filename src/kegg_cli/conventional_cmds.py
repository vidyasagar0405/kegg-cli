import typer
from Bio.KEGG.REST import (
    kegg_find,
    kegg_get,
    kegg_info,
    kegg_link,
    kegg_list,
)
from kegg_cli.kegg_conv import kegg_conv

app = typer.Typer()

@app.command()
def info(database: str = typer.Argument(..., help="The KEGG database to retrieve information from")):
    print(kegg_info(database).read())

@app.command()
def get(query: str = typer.Argument(..., help="The KEGG query string"), 
        option: str = typer.Option("", "--option", "-op", help="Additional options for the query")):
    query = query.replace(' ', '+')
    print(kegg_get(query, option=option).read())

@app.command()
def list(database: str = typer.Argument(..., help="The KEGG database to list"), 
         org: str = typer.Option("", "--organism", "-org", help="Organism code to filter the list")):
    print(kegg_list(database, org=org).read())

@app.command()
def find(query: str = typer.Argument(..., help="The search query"),
         db: str = typer.Option("genes", "--database", "-db", help="The database to query"),
         option: str = typer.Option(None, "--option", "-op", help="Additional query option, optional")):
    query = query.replace(' ', '+')
    print(kegg_find(database=db, query=query, option=option).read())

@app.command()
def conv(to_db: str = typer.Argument(..., help="The target database for conversion"), 
         from_db: str = typer.Argument(..., help="The source database for conversion")):
    print(kegg_conv(to_db, from_db).read())

@app.command()
def link(target_db : str = typer.Argument(..., help="The target database for query"), 
         source_db: str = typer.Argument(..., help="The target database/entry for query"), 
         option: str = typer.Option("", "--option", "-op", help="Additional query option, optional")):
    target_db = target_db.replace(' ', '+')
    source_db = source_db.replace(' ', '+')
    option= option.replace(' ', '+')
    print(kegg_link(target_db=target_db, source_db=source_db, option=option).read())
