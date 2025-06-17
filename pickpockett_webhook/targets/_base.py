import os
from abc import ABC, abstractmethod


class Target(ABC):
    URL_BASE_PATH = ""

    def __init__(self) -> None:
        self.env_prefix = self.__class__.__name__.upper()
        self.url = self._get_var("url")

    def _get_var(self, name: str) -> str:
        return os.environ.get(f"{self.env_prefix}_{name.upper()}")

    def _get_url(self, path: str) -> str:
        return os.path.join(self.url, self.URL_BASE_PATH, path)

    @abstractmethod
    def hook(self, old: str, new: str) -> None: ...
