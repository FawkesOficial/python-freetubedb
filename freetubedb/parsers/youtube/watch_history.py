"""
Module containing the "watch-history.json" file parser.
"""

import json
from datetime import datetime
from pathlib import Path
from typing import Any, Iterable

from freetubedb.utils import generate_freetube_id
from freetubedb.models import FreetubeWatchHistory, FreetubeHistoryEntry


__all__ = ["yt_parse_watch_history_file"]


def yt_parse_watch_history_entry(
    entry: dict[str, Any],
) -> FreetubeHistoryEntry:
    video_id: str = (
        str(entry["titleUrl"])
        .split("watch?v=")[1]
        .encode("utf-8")
        .decode("unicode_escape")
    )

    video_author_name = (
        str(entry["subtitles"][0]["name"]) if "subtitles" in entry else ""
    )
    video_author_id = (
        str(entry["subtitles"][0]["url"]).removeprefix(
            "https://www.youtube.com/channel/"
        )
        if "subtitles" in entry
        else ""
    )

    dt = datetime.fromisoformat(str(entry["time"]).replace("Z", "+00:00"))
    unix_timestamp: int = int(dt.timestamp())

    return FreetubeHistoryEntry(
        id=generate_freetube_id(),
        video_id=video_id,
        video_title=str(entry["title"]).removeprefix("Watched "),
        video_author_name=video_author_name,
        video_author_id=video_author_id,
        watch_progress=0.1,
        watch_ts=unix_timestamp,
    )


def yt_parse_watch_history_file(
    watch_history_file: Path,
) -> FreetubeWatchHistory:
    if not watch_history_file.exists():
        raise FileNotFoundError(f"File does not exist: {watch_history_file}")

    with watch_history_file.open("r", encoding="utf-8") as f:
        data: Iterable[Any] = json.load(f)

        if not isinstance(data, list):
            raise ValueError("[YT: watch_history] Improper data format")
        else:
            return FreetubeWatchHistory(
                sorted(
                    map(
                        yt_parse_watch_history_entry,
                        filter(
                            lambda entry: "titleUrl" in entry
                            and "watch?v=" in entry["titleUrl"],
                            data,
                        ),
                    ),
                    key=lambda watch_entry: watch_entry.watch_ts,
                )
            )
