"""
Module containing the "search-history.json" file parser.
"""

import json
from datetime import datetime
from pathlib import Path
from typing import Any, Iterable, Union
from freetubedb import FreetubeSearchEntry

__all__ = ["yt_parse_search_history_file"]


def yt_parse_search_history_entry(
    entry: dict[str, Union[str, int]],
) -> FreetubeSearchEntry:
    dt = datetime.fromisoformat(str(entry["time"]).replace("Z", "+00:00"))
    unix_timestamp: int = int(dt.timestamp())

    return FreetubeSearchEntry(id=str(entry["title"]), lastUpdatedAt=unix_timestamp)


def yt_parse_search_history_file(
    search_history_file: Path,
) -> list[FreetubeSearchEntry]:
    if not search_history_file.exists():
        raise FileNotFoundError(f"File does not exist: {search_history_file}")

    with search_history_file.open("r", encoding="utf-8") as f:
        data: Iterable[Any] = json.load(f)

        if not isinstance(data, list):
            raise ValueError("[YT: search_history] Improper data format")
        else:
            return list(map(yt_parse_search_history_entry, data))
