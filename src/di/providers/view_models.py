from dishka import Provider, Scope, provide

from src.di.interfaces import OperationInvokerProtocol
from src.viewmodels import DivisionViewModel
from src.viewmodels.interfaces import DivisionViewModelProtocol


class ViewmodelProvider(Provider):
    @provide(scope=Scope.APP)
    def division_viewmodel(
        self,
        operation_invokers: OperationInvokerProtocol,
    ) -> DivisionViewModelProtocol:
        return DivisionViewModel(operation_invoker=operation_invokers)
