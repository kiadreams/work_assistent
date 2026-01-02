from ..gui.views import MainWindowView


class AppCoordinator:
    def __init__(self, main_window: MainWindowView) -> None:
        super().__init__()
        self.main_window = main_window
        self.start_app()

    def start_app(self) -> None:
        self.main_window.show()

    def open_create_report_window(self) -> None:
        pass

    def open_create_protocol_window(self) -> None:
        pass

    def close_app(self) -> None:
        pass
