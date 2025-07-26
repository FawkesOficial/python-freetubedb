"""
Module containing the FreetubeVideo class.
"""

import datetime
from dataclasses import dataclass
from typing import Optional


__all__ = ["FreetubeVideo"]


@dataclass(frozen=True)
class FreetubeVideo:
    """
    FreetubeVideo class. Contains all the information stored about a video in a FreetubePlaylist.
    """

    id: str
    title: str

    author_id: str
    author_name: str

    length: int  # seconds
    published_ts: int  # unix timestamp (ms)

    playlist_item_id: str

    added_to_playlist: Optional[int] = None  # unix timestamp (ms)

    @property
    def date_published(self) -> datetime.datetime:
        """
        The date the video was published.
        """

        return datetime.datetime.fromtimestamp(self.published_ts / 1000)

    @property
    def date_added_to_playlist(self) -> Optional[datetime.datetime]:
        """
        The date the video was added to the playlist, when in a FreetubePlaylist context.
        """

        return (
            datetime.datetime.fromtimestamp(self.added_to_playlist / 1000)
            if self.added_to_playlist
            else None
        )
