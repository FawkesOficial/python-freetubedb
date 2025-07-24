__productname__ = "freetubedb"
__version__ = "1.0.1"
__description__ = "Python library for interacting with [FreeTube](https://freetubeapp.io/)'s database files and importing YouTube's data export"
__url__ = "https://github.com/FawkesOficial/python-freetubedb"
__author__ = "FawkesOficial"
__author_email__ = "mario.lourenco.morte@gmail.com"
__license__ = "GNU General Public License v3 (GPLv3)"
__bugtracker__ = "https://github.com/FawkesOficial/python-freetubedb/issues"
__ci__ = "https://github.com/FawkesOficial/python-freetubedb/actions"
__changelog__ = "https://github.com/FawkesOficial/python-freetubedb/releases"
__cake__ = "lie"


from freetubedb.models import FreetubePlaylist, FreetubeVideo, FreetubeSearchEntry
from freetubedb.parsers.freetube import ft_parse_playlists_file
from freetubedb.parsers.youtube import parse_search_history


__all__ = [
    "FreetubePlaylist",
    "FreetubeVideo",
    "FreetubeSearchEntry",
    "ft_parse_playlists_file",
    "parse_search_history",
]
