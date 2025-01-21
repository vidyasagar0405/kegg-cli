import os
import typer
from Bio.KEGG.REST import (
    kegg_find,
    kegg_get,
    kegg_info,
    kegg_link,
    kegg_list,
)
from kegg_cli.kegg_conv import kegg_conv
from kegg_cli._utils import combine_ids, file_to_list

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
    if os.path.exists(query):
        query_list = file_to_list(query, delimiter='\t', field=0)
    else:
        query_list = query.split(' ')
    combined_ids = combine_ids(query_list)
    for id in combined_ids:
        print(kegg_get(id, option=option).read())

@app.command()
def list(query: str = typer.Argument(..., help="The KEGG query(s) to list"), 
         org: str = typer.Option("", "--organism", "-org", help="Organism code to filter the list")):
    """List entries in KEGG databases.

    Lists entries in specified KEGG databases, optionally filtered by organism.
    """
    if os.path.exists(query):
        query_list = file_to_list(query, delimiter='\t', field=0)
    else:
        query_list = query.split(' ')
    combined_ids = combine_ids(query_list)
    for id in combined_ids:
        print(kegg_list(id, org=org).read())

@app.command()
def find(query: str = typer.Argument(..., help="The search query"),
         db: str = typer.Option("genes", "--database", "-db", help="The database to query"),
         option: str = typer.Option(None, "--option", "-op", help="Additional query option, optional")):
    """Find entries in KEGG databases by keyword search.

    Performs keyword searches in KEGG databases and returns matching entries.
    """
    if os.path.exists(query):
        query_list = file_to_list(query, delimiter='\t', field=0)
    else:
        query_list = query.split(' ')
    combined_ids = combine_ids(query_list)
    for id in combined_ids:
        print(kegg_find(database=db, query=id, option=option).read())

@app.command()
def conv(to_db: str = typer.Argument(..., help="The target database for conversion"), 
         from_db: str = typer.Argument(..., help="The source database for conversion"),
         option: str = typer.Option(None, "--option", "-op", help="Additional query option, optional")):
    """
    Converts identifiers between KEGG databases and external databases.
    """
    if os.path.exists(from_db):
        query_list = file_to_list(from_db, delimiter='\t', field=0)
    else:
        query_list = from_db.split(' ')
    combined_ids = combine_ids(query_list)
    for id in combined_ids:
        print(kegg_conv(to_db, id, option=option))

@app.command()
def link(target_db: str = typer.Argument(..., help="The target database for query"), 
         source_db: str = typer.Argument(..., help="The target database/entry for query"), 
         option: str = typer.Option("", "--option", "-op", help="Additional query option, optional")):
    """
    Finds related entries between different KEGG databases.
    """
    if os.path.exists(source_db):
        query_list = file_to_list(source_db, delimiter='\t', field=0)
    else:
        query_list = source_db.split(' ')
    combined_ids = combine_ids(query_list)
    for id in combined_ids:
        print(kegg_link(target_db=target_db, source_db=id, option=option).read())
