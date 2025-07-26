"""
Module containing the FreetubeSearchHistory and FreetubeSearchEntry classes.
"""

from pathlib import Path
from dataclasses import dataclass

from freetubedb.models import Exportable


__all__ = ["FreetubeSearchHistory", "FreetubeSearchEntry"]


@dataclass(frozen=True)
class FreetubeSearchEntry:
    """
    FreetubeSearchEntry class. Contains all the information stored about a search entry.
    """

    id: str
    lastUpdatedAt: int  # unix timestamp

    @property
    def search(self) -> str:
        """
        The string that was searched.
        """

        # note: in FreeTube's database, the "_id" of each entry is the search query itself
        return self.id


class FreetubeSearchHistory(list[FreetubeSearchEntry], Exportable):
    """
    FreetubeSearchHistory class. Contains all the information stored about search history.
    Wrapper around `list[FreetubeSearchHistory]`
    """

    def export_to_file(self, export_file: Path = Path("search-history.db")) -> None:
        with export_file.open("w", encoding="utf-8") as f:
            for search_entry in self:
                f.write(
                    f'{{"_id":"{search_entry.id}","lastUpdatedAt":{search_entry.lastUpdatedAt}}}\n'
                )
