# -*- coding: utf-8 -*-
from pathlib import Path
from typing import List

import typer

from .getting import channel_name, getting_link

app = typer.Typer()


@app.command()
def main(urls: List[str]):
    """
    Pass in a YouTube videos url and it will add the correct RSS feed to
    newsboat.
    """

    for url in urls:

        link = getting_link(url)

        newsboat = Path("/Users/evanbaird/.newsboat/urls")

        with newsboat.open(mode="a", encoding="utf-8") as wr:
            wr.write(f'\n{link} "~{channel_name(url_name=url)}"')
