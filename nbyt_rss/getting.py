# -*- coding: utf-8 -*-
import httpx
from parsel import Selector
from yarl import URL

# TODO: Lots of repeated code. Create a class so parameters like yt_url is defined once and used and accessed by methods within the class.
# TODO: Think up another name for the class and functions as well.
# TODO: URL to define and delegate each part for each method.
# TODO: URL view the docs due to their may be a cache: https://tinyurl.com/2ctm95fo


class Getting:
    """
    Basing fucntions to collect YouTube urls.
    """

    def __init__(self, yt_url):
        self.yt_url: URL = URL(yt_url)

    def getting_link(self):
        """
        This function will pull out the YouTube RSS link.
        """
        # TODO: Create a check that a valid YouTube url has been passed
        # TODO: if 'videos' not in

        if self.yt_url.name != "videos":
            # TODO: Remove this error and just add /videos to the YouTube url passed in.
            # TODO: You can join path of videos like: self.yt_url / 'videos'
            raise ValueError(
                """
                    YouTube url must have videos at the end of the url to get the RSS
                    feed.
                    Make sure to go to the creators page and click on their videos tab.
                    Copy/Paste that into getting_link to avoid this error.
                    """,
            )

        response = httpx.get(self.yt_url.human_repr())

        txt = response.text

        select = Selector(text=txt)

        return select.xpath('//link[@title="RSS"]/@href').get()

    def getting_name(self):
        """
        Getting channel name.
        """

        return self.yt_url.path.split("/")[1]

    def channel_name(self):
        """
        This function returns the name of the YouTube name to attach.
        """

        return self.yt_url.parts[1].replace("@", "")
