from PySide6.QtCore import QObject
from dishka import Container

from ..gui.views import MainWindowView


class AppCoordinator(QObject):
    def __init__(self, container: Container) -> None:
        super().__init__()
        self.container = container

    # def _init_app_windows(self) -> None:
    #     main_window = self.container.get(MainWindowView)
    #     main_window.show()
