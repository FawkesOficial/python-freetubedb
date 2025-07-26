"""
Module containing the FreetubeWatchHistory and FreetubeHistoryEntry classes.
"""

import datetime
from typing import Optional, ClassVar
from dataclasses import dataclass

from freetubedb.models import Exportable


__all__ = ["FreetubeWatchHistory", "FreetubeHistoryEntry"]


@dataclass(frozen=True)
class FreetubeHistoryEntry(Exportable):
    """
    FreetubeHistoryEntry class. Contains all the information stored about a watch history entry.
    """

    id: str

    video_id: str
    video_title: str
    video_author_name: str
    video_author_id: str

    watch_progress: float  # percentage (%)
    watch_ts: int  # unix timestamp (ms)

    playlist_id: Optional[str] = ""
    playlist_item_id: Optional[str] = ""

    # freetube name -> custom freetubedb name
    RENAME_MAP: ClassVar[dict[str, str]] = {
        "videoId": "video_id",
        "title": "video_title",
        "author": "video_author_name",
        "authorId": "video_author_id",
        "watchProgress": "watch_progress",
        "timeWatched": "watch_ts",
        "_id": "id",
        "lastViewedPlaylistId": "playlist_id",
        "lastViewedPlaylistItemId": "playlist_item_id",
    }

    @property
    def date_watched(self) -> datetime.datetime:
        """
        The date the video was watched.
        """

        return datetime.datetime.fromtimestamp(self.watch_ts / 1000)


class FreetubeWatchHistory(list[FreetubeHistoryEntry], Exportable):
    """
    FreetubeWatchHistory class. Contains all the information stored about watch history.
    Wrapper around `list[FreetubeHistoryEntry]`
    """

    def export(self) -> str:
        return "\n".join(map(lambda _: _.export(), self))
