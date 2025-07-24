"""
Module containing the "search-history.json" file parser.
"""

from pathlib import Path
from freetubedb import FreetubePlaylist, FreetubeVideo, FreetubeSearchEntry

__all__ = ["parse_search_history_file"]


def parse_search_history() -> FreetubePlaylist:
    pass


def parse_search_history_file(search_history_file: Path) -> list[FreetubeVideo]:
    pass
