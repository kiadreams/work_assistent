from typing import Protocol, Any, Callable
from dishka import Container  # Приходится импортировать Container сюда

# Определяем тип функции, которую может принять Invoker:
# Функция принимает контейнер и возвращает что угодно (Any)
OperationFunc = Callable[[Container], Any]


class OperationInvokerProtocol(Protocol):
    """
    Протокол для выполнения операций в коротком Scope.REQUEST.
    """

    _root_container: Container

    def execute_request(self, func_to_run: OperationFunc) -> Any: ...
