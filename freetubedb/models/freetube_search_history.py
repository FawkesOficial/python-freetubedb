"""
Module containing the FreetubeSearchHistory and FreetubeSearchEntry classes.
"""

import datetime
from dataclasses import dataclass
from typing import ClassVar

from freetubedb.models import Exportable


__all__ = ["FreetubeSearchHistory", "FreetubeSearchEntry"]


@dataclass(frozen=True)
class FreetubeSearchEntry(Exportable):
    """
    FreetubeSearchEntry class. Contains all the information stored about a search entry.
    """

    id: str
    last_updated_ts: int  # unix timestamp (ms)

    # freetube name -> custom freetubedb name
    RENAME_MAP: ClassVar[dict[str, str]] = {
        "_id": "id",
        "lastUpdatedAt": "last_updated_ts",
    }

    @property
    def search(self) -> str:
        """
        The string that was searched.
        """

        # note: in FreeTube's database, the "_id" of each entry is the search query itself
        return self.id

    @property
    def date_last_updated(self) -> datetime.datetime:
        """
        The date the query was searched.
        """

        return datetime.datetime.fromtimestamp(self.last_updated_ts / 1000)


class FreetubeSearchHistory(list[FreetubeSearchEntry], Exportable):
    """
    FreetubeSearchHistory class. Contains all the information stored about search history.
    Wrapper around `list[FreetubeSearchHistory]`
    """

    def export(self) -> str:
        return "\n".join(map(lambda _: _.export(), self))
