from PySide6.QtCore import QObject
# from


class AppCoordinator(QObject):
    def __init__(self, container) -> None:
        super().__init__()
        self.container = container
