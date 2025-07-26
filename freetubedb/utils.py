"""
General utilities
"""

import secrets
from typing import Any


def rename_dict_keys(d: dict[str, Any], rename_map: dict[str, str]) -> dict[str, Any]:
    result = d
    for freetube_name, custom_name in rename_map.items():
        prev_v = result.pop(custom_name, None)
        result[freetube_name] = prev_v if prev_v else ""

    return result


def generate_freetube_id(length: int = 16) -> str:
    return secrets.token_urlsafe(length)[:length]
