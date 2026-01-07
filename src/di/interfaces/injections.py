from typing import ContextManager, Protocol

from dishka import Container
from dishka.container import ContextWrapper

from src.gui.interfaces.views import (
    MainMenuWindowProtocol,
    MainWindowProtocol,
)


class AppFactoryProtocol(Protocol):
    """
    Протокол фабрики для создания окон и вспомогательных координаторов.
    """

    _root_container: Container

    @property
    def main_window(self) -> MainWindowProtocol: ...

    @property
    def main_menu(self) -> MainMenuWindowProtocol: ...

    @property
    def reports_session(self) -> ContextWrapper: ...


class OperationInvokerProtocol(Protocol):
    """
    Протокол для выполнения операций в коротком Scope.REQUEST.
    """

    _root_container: Container

    def request_container(self) -> ContextManager[Container]: ...
