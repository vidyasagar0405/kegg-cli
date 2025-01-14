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
    """Retrieve information about KEGG databases.

    Displays current statistics and release information about the specified KEGG database.
    """
    print(kegg_info(database).read())

@app.command()
def get(query: str = typer.Argument(..., help="The KEGG query string"), 
        option: str = typer.Option("", "--option", "-op", help="Additional options for the query")):
    """Retrieve entries from KEGG databases.

    Gets detailed information about specific entries in KEGG databases.
    Supports various options like sequence retrieval (ntseq, aaseq).
    """
    query = query.replace(' ', '+')
    print(kegg_get(query, option=option).read())

@app.command()
def list(query: str = typer.Argument(..., help="The KEGG query(s) to list"), 
         org: str = typer.Option("", "--organism", "-org", help="Organism code to filter the list")):
    """List entries in KEGG databases.

    Lists entries in specified KEGG databases, optionally filtered by organism.
    """
    query = query.replace(' ', '+')
    print(kegg_list(query, org=org).read())

@app.command()
def find(query: str = typer.Argument(..., help="The search query"),
         db: str = typer.Option("genes", "--database", "-db", help="The database to query"),
         option: str = typer.Option(None, "--option", "-op", help="Additional query option, optional")):
    """Find entries in KEGG databases by keyword search.

    Performs keyword searches in KEGG databases and returns matching entries.
    """
    query = query.replace(' ', '+')
    print(kegg_find(database=db, query=query, option=option).read())

@app.command()
def conv(to_db: str = typer.Argument(..., help="The target database for conversion"), 
         from_db: str = typer.Argument(..., help="The source database for conversion"),
         option: str = typer.Option(None, "--option", "-op", help="Additional query option, optional")):
    """
    Converts identifiers between KEGG databases and external databases.
    """
    to_db = to_db .replace(' ', '+')
    from_db = from_db .replace(' ', '+')
    print(kegg_conv(to_db, from_db, option=option).read())

@app.command()
def link(target_db: str = typer.Argument(..., help="The target database for query"), 
         source_db: str = typer.Argument(..., help="The target database/entry for query"), 
         option: str = typer.Option("", "--option", "-op", help="Additional query option, optional")):
    """
    Finds related entries between different KEGG databases.
    """
    target_db = target_db.replace(' ', '+')
    source_db = source_db.replace(' ', '+')
    print(kegg_link(target_db=target_db, source_db=source_db, option=option).read())
