"""
TODO
"""

from pathlib import Path
import platform
import os


__all__ = ["FREETUBE_DEFAULT_DB_PATH"]


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
