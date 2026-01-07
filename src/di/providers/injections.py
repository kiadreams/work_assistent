from dishka import Container, Provider, Scope, provide

from src.di.injections import AppFactory, OperationInvoker
from src.di.interfaces import AppFactoryProtocol, OperationInvokerProtocol


class InjectionsProvider(Provider):
    @provide(scope=Scope.APP)
    def operation_invoker(self, root_container: Container) -> OperationInvokerProtocol:
        return OperationInvoker(root_container=root_container)

    @provide(scope=Scope.APP)
    def app_factory(self, root_container: Container) -> AppFactoryProtocol:
        return AppFactory(root_container=root_container)
