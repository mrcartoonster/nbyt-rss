# -*- coding: utf-8 -*-
import httpx
from parsel import Selector
from yarl import URL


def getting_link(yt_url: str):
    """
    This function will pull out the YouTube RSS link.
    """
    url = URL(yt_url)

    if url.name != "videos":
        raise ValueError(
            """
                YouTube url must have videos at the end of the url to get the RSS
                feed.
                Make sure to go to the creators page and click on their videos tab.
                Copy/Paste that into getting_link to avoid this error.
                """,
        )

    response = httpx.get(yt_url)

    txt = response.text

    select = Selector(text=txt)

    return select.xpath('//link[@title="RSS"]/@href').get()


def channel_name(url_name: str):
    """
    This function returns the name of the YouTube name to attach.
    """
    name = URL(url_name)

    return name.parts[1].replace("@", "")
