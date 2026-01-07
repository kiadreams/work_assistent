from dishka import Provider, Scope, provide

from src.di.interfaces import AppFactoryProtocol
from src.gui.coordinators import (
    AppCoordinator,
    ProtocolsCoordinator,
    ReportsCoordinator,
)
from src.gui.interfaces.coordinators import (
    AppCoordinatorProtocol,
    ProtocolsCoordinatorProtocol,
    ReportsCoordinatorProtocol,
)
from src.gui.interfaces.views import (
    DivisionViewProtocol,
    OrderViewProtocol,
    ReportsWindowProtocol,
    StaffViewProtocol,
    WorkEventViewProtocol,
    WorksViewProtocol,
    WorkTypeViewProtocol,
)


class CoordinatorsProvider(Provider):
    @provide(scope=Scope.APP)
    def app_coordinator(
        self,
        window_factory: AppFactoryProtocol,
    ) -> AppCoordinatorProtocol:
        return AppCoordinator(window_factory=window_factory)

    @provide(scope=Scope.SESSION)
    def reports_coordinator(
        self,
        reports_window: ReportsWindowProtocol,
        divisions_view: DivisionViewProtocol,
        staff_view: StaffViewProtocol,
        work_types_view: WorkTypeViewProtocol,
        work_event_view: WorkEventViewProtocol,
        works_view: WorksViewProtocol,
        order_view: OrderViewProtocol,
    ) -> ReportsCoordinatorProtocol:
        return ReportsCoordinator(
            reports_window,
            divisions_view=divisions_view,
            staff_view=staff_view,
            works_view=works_view,
            order_view=order_view,
            work_types_view=work_types_view,
            work_event_view=work_event_view,
        )

    @provide(scope=Scope.SESSION)
    def protocols_coordinator(
        self,
    ) -> ProtocolsCoordinatorProtocol:
        return ProtocolsCoordinator()
