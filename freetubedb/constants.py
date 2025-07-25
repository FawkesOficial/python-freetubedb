"""
Module holding freetubedb's constants
"""

from pathlib import Path
import platform
import os

from freetubedb.custom_types import Parser
from freetubedb.parsers.youtube import yt_parse_search_history_file


__all__ = ["FREETUBE_DEFAULT_DB_PATH", "YT_FILE_TO_PARSER"]


def get_freetube_default_db_path() -> Path:
    # https://docs.freetubeapp.io/usage/data-location/

    match platform.system():
        case "Windows":
            return Path(os.getenv("APPDATA", "")) / "FreeTube"
        case "Darwin":
            return Path("~/Library/Application Support/FreeTube").expanduser()
        case _:  # Linux, Unix, etc.
            return Path("~/.config/FreeTube").expanduser()


FREETUBE_DEFAULT_DB_PATH: Path = get_freetube_default_db_path()

YT_FILE_TO_PARSER: dict[
    str,
    Parser,
] = {"search-history.json": yt_parse_search_history_file}

# TODO: YT_TO_FREETUBE_FILENAME dict
