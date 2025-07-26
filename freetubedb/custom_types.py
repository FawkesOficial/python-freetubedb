"""
Module holding freetube's custom type aliases
"""

from pathlib import Path
from typing import TypeAlias, Callable, Union

from freetubedb.models import (
    FreetubeVideo,
    FreetubePlaylist,
    FreetubeSearchHistory,
    FreetubeWatchHistory,
)

ParserOutput: TypeAlias = Union[
    FreetubeVideo, FreetubePlaylist, FreetubeSearchHistory, FreetubeWatchHistory
]  # TODO: propper typing for the Union here

Parser: TypeAlias = Callable[[Path], ParserOutput]
