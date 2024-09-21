# -*- coding: utf-8 -*-
from pathlib import Path
from typing import List, Optional

import typer
from typing_extensions import Annotated

from .__init__ import __version__
from .getting import channel_name, getting_link

app = typer.Typer()


def version_callback(value: bool):
    if value:
        print(f"Awesome CLI Version: {__version__}")
        raise typer.Exit()


@app.command()
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
