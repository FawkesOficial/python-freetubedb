"""
Module holding freetube's custom type aliases
"""

from pathlib import Path
from typing import TypeAlias, Callable, Union

from freetubedb.models import FreetubeSearchHistory

ParserOutput: TypeAlias = Union[
    FreetubeSearchHistory, int
]  # TODO: propper typing for the Union here

Parser: TypeAlias = Callable[[Path], ParserOutput]
