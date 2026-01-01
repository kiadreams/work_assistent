from typing import Protocol


class MainWindowProtocol(Protocol):
    def change_page(self, page: int) -> None: ...