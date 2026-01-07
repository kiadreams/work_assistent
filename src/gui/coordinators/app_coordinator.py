import sys

from dishka.container import Container, ContextWrapper

from src.di.interfaces import AppFactoryProtocol
from src.gui.interfaces.views import (
    MainMenuWindowProtocol,
    MainWindowProtocol,
)

from ..constants import MainWindows
from ..interfaces.coordinators import AppCoordinatorProtocol, ReportsCoordinatorProtocol


class AppCoordinator(AppCoordinatorProtocol):
    def __init__(self, window_factory: AppFactoryProtocol) -> None:
        super().__init__()
        self.factory = window_factory
        self.main_window: MainWindowProtocol | None = None
        self.main_menu: MainMenuWindowProtocol | None = None
        self._active_session_scope: ContextWrapper | None = None
        # self._active_session_coordinator: ReportsCoordinatorProtocol | None = None

    def start_app(self) -> None:
        self.main_window = self.factory.main_window
        self.main_menu = self.factory.main_menu
        self.main_window.add_window(
            MainWindows.MAIN_MENU,
            self.main_menu,
        )
        self.main_window.show()
        self._connect_signals()

    def _connect_signals(self) -> None:
        if self.main_menu and self.main_window:
            self.main_menu.open_reports_window_signal.connect(self.open_reports_window)
            self.main_menu.open_protocols_window_signal.connect(self.open_protocols_window)
            self.main_menu.close_app_signal.connect(self.main_window.close)

    def open_main_menu_window(self) -> None:
        if self.main_window:
            self.main_window.change_window(MainWindows.MAIN_MENU)
        if self._active_session_scope:
            self._active_session_scope.__exit__(None, None, None)
            self._active_session_scope = None
            print("удаляем ссылку на сессионный координатор")

    def open_reports_window(self) -> None:
        reports_container: Container | None = None
        self._active_session_scope = self.factory.reports_session
        try:
            reports_container = self._active_session_scope.__enter__()
            reports_coordinator = reports_container.get(ReportsCoordinatorProtocol)
            reports_coordinator.start_session()
            reports_window = reports_coordinator.reports_window
            reports_window.back_main_menu_signal.connect(self.open_main_menu_window)
            if self.main_window:
                self.main_window.add_window(MainWindows.REPORTS_WINDOW, reports_window)
                self.main_window.change_window(MainWindows.REPORTS_WINDOW)
        except Exception:
            if reports_container:
                self._active_session_scope.__exit__(*sys.exc_info())
            raise

    def open_protocols_window(self) -> None:
        if self.main_window:
            self.main_window.change_window(MainWindows.PROTOCOLS_WINDOW)
            print("Нажали кнопку создания протоколов!!!")
