from contextlib import contextmanager
from typing import Generator

from dishka import Container, Scope
from dishka.container import ContextWrapper

from src.gui.interfaces.views import (
    MainMenuWindowProtocol,
    MainWindowProtocol,
)


class AppFactory:
    """
    Фабрика для создания окон и вспомогательных координаторов.
    """

    def __init__(self, root_container: Container) -> None:
        self._root_container = root_container

    @property
    def main_window(self) -> MainWindowProtocol:
        return self._root_container.get(MainWindowProtocol)  # type: ignore[no-any-return]

    @property
    def main_menu(self) -> MainMenuWindowProtocol:
        return self._root_container.get(MainMenuWindowProtocol)  # type: ignore[no-any-return]

    @property
    def reports_session(self) -> ContextWrapper:
        return self._root_container(scope=Scope.SESSION)


class OperationInvoker:
    def __init__(self, root_container: Container):
        self._root_container = root_container

    @contextmanager
    def request_container(self) -> Generator[Container, None, None]:
        with self._root_container(scope=Scope.REQUEST) as request_container:
            yield request_container
