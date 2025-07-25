"""
Module containing the FreetubeSearchHistory class.
"""

from pathlib import Path

from freetubedb.models import FreetubeSearchEntry, Exportable


__all__ = ["FreetubeSearchHistory"]


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
