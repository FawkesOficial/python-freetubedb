"""
Exportable protocol/trait/"interface"
"""

from typing import Protocol, runtime_checkable
from pathlib import Path


__all__ = ["Exportable"]


@runtime_checkable
class Exportable(Protocol):
    def export_to_file(self, export_file: Path) -> None: ...
