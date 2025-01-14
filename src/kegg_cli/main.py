import typer

from kegg_cli.conventional_cmds import conv, find, get, info, link, list
from kegg_cli.get_seq import get_seq

app = typer.Typer()

app.command()(info)
app.command()(get)
app.command()(list)
app.command()(find)
app.command()(conv)
app.command()(link)
app.command()(get_seq)


def main():
    app()


if __name__ == "__main__":
    main()
