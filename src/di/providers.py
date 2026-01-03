from typing import ContextManager

from dishka import Provider, Scope, provide, Container
from sqlalchemy.orm import Session

from src.core.app_coordinator import AppCoordinator
from src.core.interfaces.coordinators import AppCoordinatorProtocol
from src.core.interfaces.invokers import OperationInvokerProtocol
from src.core.interfaces.repositories import DivisionRepositoryProtocol, DatabaseManagerProtocol
from src.core.interfaces.services import EmployeeServiceProtocol
from src.core.interfaces.viewmodels import DivisionViewModelProtocol
from src.database.db_manager import DatabaseManager
from src.database.repositories.division_repository import DivisionRepository
from src.di.invokers import OperationInvoker
from src.gui.viewmodels import DivisionViewModel
from src.gui.views import (
    MainMenuView,
    MainWindowView,
    DivisionReportView,
    WorkEventReportView,
    WorkReportView,
    WorkTypeReportView,
    OrderReportView,
    StaffReportView,
    ReportGeneratorView,
)
from src.services.EmployeeService import EmployeeService


class DatabaseProvider(Provider):
    @provide(scope=Scope.APP)
    def db_manager(self) -> DatabaseManagerProtocol:
        return DatabaseManager()

    @provide(scope=Scope.REQUEST)
    def db_session(self, manager: DatabaseManagerProtocol) -> Session:
        print("пытаемся создать сессию")
        return manager.create_session()

    @provide(scope=Scope.REQUEST)
    def division_repository(self, curr_session: Session) -> DivisionRepositoryProtocol:
        print("создаем репозиторий")
        return DivisionRepository(session=curr_session)


class InvokersProvider(Provider):
    @provide(scope=Scope.APP)
    def operation_invoker(self, root_container: Container) -> OperationInvokerProtocol:
        return OperationInvoker(root_container=root_container)


class ServiceProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def employee_service(
        self, divisions_repository: DivisionRepositoryProtocol
    ) -> EmployeeServiceProtocol:
        print("создаем сервис")
        return EmployeeService(division_repository=divisions_repository)


class ViewmodelProvider(Provider):
    @provide(scope=Scope.APP)
    def division_viewmodel(
        self,
        operation_invokers: OperationInvokerProtocol,
    ) -> DivisionViewModelProtocol:
        return DivisionViewModel(operation_invoker=operation_invokers)


class UIWindowsProvider(Provider):
    @provide(scope=Scope.APP)
    def main_menu_ui(self) -> MainMenuView:
        return MainMenuView()

    @provide(scope=Scope.APP)
    def division_report_ui(self, viewmodel: DivisionViewModelProtocol) -> DivisionReportView:
        return DivisionReportView(viewmodel=viewmodel)

    @provide(scope=Scope.APP)
    def order_report_ui(self) -> OrderReportView:
        return OrderReportView()

    @provide(scope=Scope.APP)
    def staff_report_ui(self) -> StaffReportView:
        return StaffReportView()

    @provide(scope=Scope.APP)
    def work_event_report_ui(self) -> WorkEventReportView:
        return WorkEventReportView()

    @provide(scope=Scope.APP)
    def work_report_ui(self) -> WorkReportView:
        return WorkReportView()

    @provide(scope=Scope.APP)
    def work_type_report_ui(self) -> WorkTypeReportView:
        return WorkTypeReportView()

    @provide(scope=Scope.APP)
    def report_generator_ui(
        self,
        staff_report: StaffReportView,
        work_event_report: WorkEventReportView,
        work_report: WorkReportView,
        work_type_report: WorkTypeReportView,
        order_report: OrderReportView,
        division_report: DivisionReportView,
    ) -> ReportGeneratorView:
        return ReportGeneratorView(
            staff_view=staff_report,
            works_view=work_report,
            work_events_view=work_event_report,
            work_types_view=work_type_report,
            orders_view=order_report,
            division_view=division_report,
        )

    @provide(scope=Scope.APP)
    def main_window(self, menu: MainMenuView, view: ReportGeneratorView) -> MainWindowView:
        return MainWindowView(main_menu=menu, views=view)


class CoordinatorsProvider(Provider):
    @provide(scope=Scope.APP)
    def app_coordinator(
        self,
        main_window: MainWindowView,
    ) -> AppCoordinatorProtocol:
        print("создаем координатор")
        return AppCoordinator(main_window=main_window)
