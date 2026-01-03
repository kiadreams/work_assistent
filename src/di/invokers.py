from typing import Any

from dishka import Container, Scope

from src.core.interfaces.invokers import OperationFunc


class OperationInvoker:
    def __init__(self, root_container: Container):
        self._root_container = root_container

    def execute_request(self, func_to_run: OperationFunc) -> Any:
        # Вся магия управления Scope происходит здесь
        with self._root_container(scope=Scope.REQUEST) as request_container:
            # Вызываем переданную функцию, передавая ей короткий контейнер
            return func_to_run(request_container)
