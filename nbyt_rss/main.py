# -*- coding: utf-8 -*-
from pathlib import Path
from typing import List, Optional

import typer
from rich import print
from typing_extensions import Annotated

from .__init__ import __version__
from .getting import channel_name, getting_link

app = typer.Typer(rich_markup_mode="rich")


def version_callback(value: bool):
    if value:
        print(
            f":sparkle:[bold]Awesome CLI Version:[/] [green]{__version__}[/]",
        )
        raise typer.Exit()


@app.command(epilog="[bold red]Made with desperation[/] :sweat:")
def main(
    urls: List[str],
    version: Annotated[
        Optional[bool],
        typer.Option(
            "--version",
            "-v",
            callback=version_callback,
            is_eager=True,
        ),
    ] = None,
):
    """
    Pass in a YouTube videos url and it will add the correct RSS feed to
    newsboat.
    """

    for url in urls:

        link = getting_link(url)

        newsboat = Path("/Users/evanbaird/.newsboat/urls")

        with newsboat.open(mode="a", encoding="utf-8") as wr:
            wr.write(f'\n{link} "~{channel_name(url_name=url)}"')
