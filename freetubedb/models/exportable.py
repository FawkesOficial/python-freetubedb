"""
Exportable protocol/trait/"interface"
"""

import json
from typing import Protocol, ClassVar, runtime_checkable

from freetubedb.utils import rename_dict_keys

__all__ = ["Exportable"]


@runtime_checkable
class Exportable(Protocol):
    RENAME_MAP: ClassVar[dict[str, str]] = {}  # freetube name -> custom freetubedb name

    def export(self) -> str:
        return json.dumps(
            rename_dict_keys(self.__dict__, self.RENAME_MAP), separators=(",", ":")
        )
