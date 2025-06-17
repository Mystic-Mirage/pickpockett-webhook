import requests

from . import Target


class QBittorrent(Target):
    URL_BASE_PATH = "api/v2"

    def __init__(self) -> None:
        super().__init__()
        self.username = self._get_var("username")
        self.password = self._get_var("password")
        self.cookies = None

    def _login(self) -> None:
        if self.username and self.password:
            url = self._get_url("auth/login")
            response = requests.post(
                url,
                data={
                    "username": self.username,
                    "password": self.password,
                },
            )
            response.raise_for_status()
            self.cookies = response.cookies

    def hook(self, old: str, new: str) -> None:
        if not self.cookies:
            self._login()

        url = self._get_url("torrents/delete")
        response = requests.post(
            url,
            data={
                "hashes": old,
                "deleteFiles": False,
            },
            cookies=self.cookies,
        )
        response.raise_for_status()


#
# if __name__ == "__main__":
#     qbittorrent = QBittorrent()
#     qbittorrent.hook("1", "2")
