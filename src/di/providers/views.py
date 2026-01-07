from dishka import Provider, Scope, provide

from src.gui.interfaces.views import (
    DivisionViewProtocol,
    MainMenuWindowProtocol,
    MainWindowProtocol,
    OrderViewProtocol,
    ReportsWindowProtocol,
    StaffViewProtocol,
    WorkEventViewProtocol,
    WorksViewProtocol,
    WorkTypeViewProtocol,
)
from src.gui.views import (
    DivisionReportView,
    MainMenuWindow,
    MainWindow,
    OrderReportView,
    ReportsWindow,
    StaffReportView,
    WorkEventReportView,
    WorkReportView,
    WorkTypeReportView,
)
from src.viewmodels.interfaces import DivisionViewModelProtocol


class UIWindowsProvider(Provider):
    @provide(scope=Scope.APP)
    def main_window(self) -> MainWindowProtocol:
        return MainWindow()

    @provide(scope=Scope.APP)
    def main_menu_ui(self) -> MainMenuWindowProtocol:
        return MainMenuWindow()

    @provide(scope=Scope.SESSION)
    def reports_window_ui(self) -> ReportsWindowProtocol:
        return ReportsWindow()

    @provide(scope=Scope.SESSION)
    def division_report_ui(self, viewmodel: DivisionViewModelProtocol) -> DivisionViewProtocol:
        return DivisionReportView(viewmodel=viewmodel)

    @provide(scope=Scope.SESSION)
    def order_report_ui(self) -> OrderViewProtocol:
        return OrderReportView()

    @provide(scope=Scope.SESSION)
    def staff_report_ui(self) -> StaffViewProtocol:
        return StaffReportView()

    @provide(scope=Scope.SESSION)
    def work_event_report_ui(self) -> WorkEventViewProtocol:
        return WorkEventReportView()

    @provide(scope=Scope.SESSION)
    def work_report_ui(self) -> WorksViewProtocol:
        return WorkReportView()

    @provide(scope=Scope.SESSION)
    def work_type_report_ui(self) -> WorkTypeViewProtocol:
        return WorkTypeReportView()
