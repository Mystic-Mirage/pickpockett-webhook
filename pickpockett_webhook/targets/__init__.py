from contextlib import suppress

from ._base import Target
from .qbittorrent import QBittorrent

__all__ = [
    "QBittorrent",
    "get_target",
]


def get_target(name: str) -> Target | None:
    with suppress(StopIteration):
        return next(
            target
            for target in Target.__subclasses__()
            if target.__name__.lower() == name
        )()
