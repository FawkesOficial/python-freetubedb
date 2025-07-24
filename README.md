# freetubedb

[![PyPI - Version](https://img.shields.io/pypi/v/freetubedb.svg)](https://pypi.org/project/freetubedb)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/freetubedb.svg)](https://pypi.org/project/freetubedb)

Python library for interacting with [FreeTube](https://freetubeapp.io/)'s database files and importing YouTube's data export

-----

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Installation

```console
pip install freetubedb
```

## Usage

### `FreetubePlaylist`
```python
@dataclass(frozen=True)
class FreetubePlaylist:
    """
    FreetubePlaylist class. Contains all the information stored about a playlist.
    """

    id: str
    name: str
    description: str
    protected: bool
    videos: list[FreetubeVideo] = field(default_factory=list[FreetubeVideo])
```

### `FreetubeVideo`
```python
@dataclass(frozen=True)
class FreetubeVideo:
    """
    FreetubeVideo class. Contains all the information stored about a video in a FreetubePlaylist.
    """

    id: str
    title: str

    author_id: str
    author_name: str

    length: int  # seconds
    date_published: int  # unix timestamp
    date_added: int  # unix timestamp

    playlist_item_id: str
```

### `FreetubeSearchEntry`
```python
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
```

### Example
```python
from pathlib import Path
from freetubedb import ft_parse_playlists_file, FreetubePlaylist

# uses default FreeTube path based on operating system
playlists: list[FreetubePlaylist] = ft_parse_playlists_file()

# alternatively, you can supply your own custom path:
# playlists: list[FreetubePlaylist] = ft_parse_playlists_file(Path("./playlists.db"))


for playlist in playlists:
    print(f"Playlist: {playlist.name} (ID: {playlist.id})")
    print(f"Description: {playlist.description}")
    print(f"Number of videos: {len(playlist.videos)}")

    for video in playlist.videos:
        print(f"  - {video.title} by {video.author_name}")
        print(f"    Video ID: {video.id}")
        print(f"    Length: {video.length} seconds")
        print(f"    Published: {video.date_published} (unix timestamp)")
        print(f"    Added to playlist: {video.date_added} (unix timestamp)")
```

## License

`freetubedb` is distributed under the terms of the [GPL-3.0](https://spdx.org/licenses/GPL-3.0.html) license.
