"""
Module containing the FreetubeSearchEntry class.
"""

from dataclasses import dataclass

__all__ = ["FreetubeSearchEntry"]


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
