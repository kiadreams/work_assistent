from typing import Any, Protocol

from PySide6.QtCore import SignalInstance

from src.core.constants import PageStructure


class BaseViewProtocol(Protocol):
    def init_content_view(self) -> None: ...


class SessionWindowProtocol(BaseViewProtocol, Protocol):
    back_main_menu_signal: SignalInstance


class MainWindowProtocol(BaseViewProtocol, Protocol):
    def show(self) -> None: ...

    def close(self) -> bool: ...

    def add_window(self, index: PageStructure, window: Any) -> None: ...

    def change_window(self, index: PageStructure) -> None: ...


class MainMenuWindowProtocol(BaseViewProtocol, Protocol):
    open_reports_window_signal: SignalInstance
    open_protocols_window_signal: SignalInstance
    close_app_signal: SignalInstance


class ReportsWindowProtocol(SessionWindowProtocol, Protocol):
    open_divisions_view_signal: SignalInstance
    open_staff_view_signal: SignalInstance
    open_work_types_view_signal: SignalInstance
    open_orders_view_signal: SignalInstance
    open_works_view_signal: SignalInstance
    open_work_events_view_signal: SignalInstance

    def add_view(self, index: PageStructure, view: Any) -> None: ...

    def change_view(self, index: PageStructure) -> None: ...


class DivisionViewProtocol(BaseViewProtocol, Protocol):
    pass


class StaffViewProtocol(BaseViewProtocol, Protocol):
    pass


class WorkTypeViewProtocol(BaseViewProtocol, Protocol):
    pass


class WorksViewProtocol(BaseViewProtocol, Protocol):
    pass


class WorkEventViewProtocol(BaseViewProtocol, Protocol):
    pass


class OrderViewProtocol(BaseViewProtocol, Protocol):
    pass
