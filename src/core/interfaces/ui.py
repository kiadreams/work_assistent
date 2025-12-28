from typing import Protocol


class MainWindow(Protocol):
    def change_page(self, page: int) -> None: ...