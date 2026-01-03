from functools import wraps
from typing import Any, Callable

from dishka import Container

from src.core.interfaces.invokers import OperationFunc, OperationInvokerProtocol


def invoke_request(func: OperationFunc) -> Callable[..., Any]:
    """
    Декоратор, который выполняет метод внутри OperationInvoker.
    Предполагает наличие self._invoker в декорируемом классе.
    """

    @wraps(func)
    def wrapper(self: Any, *args: Any, **kwargs: Any) -> Any:
        # 1. Получаем экземпляр Invoker из self
        invoker: OperationInvokerProtocol = self._operation_invoker

        # 2. Определяем функцию, которую нужно выполнить внутри Scope.REQUEST
        def operation_logic(container: Container) -> Any:
            # Мы вызываем оригинальную функцию func, передавая ей контейнер и все аргументы
            return func(self, container, *args, **kwargs)  # type: ignore[call-arg]

        # 3. Передаем эту функцию Invoker'у для выполнения в Scope.REQUEST
        return invoker.execute_request(operation_logic)

    return wrapper
