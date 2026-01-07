from src.gui.constants import ReportsViews
from src.gui.interfaces.coordinators import ReportsCoordinatorProtocol
from src.gui.interfaces.views import (
    DivisionViewProtocol,
    OrderViewProtocol,
    ReportsWindowProtocol,
    StaffViewProtocol,
    WorkEventViewProtocol,
    WorksViewProtocol,
    WorkTypeViewProtocol,
)


class ReportsCoordinator(ReportsCoordinatorProtocol):
    def __init__(
        self,
        reports_window: ReportsWindowProtocol,
        divisions_view: DivisionViewProtocol,
        staff_view: StaffViewProtocol,
        work_types_view: WorkTypeViewProtocol,
        work_event_view: WorkEventViewProtocol,
        works_view: WorksViewProtocol,
        order_view: OrderViewProtocol,
    ) -> None:
        self._reports_window = reports_window
        self.divisions_view = divisions_view
        self.staff_view = staff_view
        self.work_types_view = work_types_view
        self.work_events_view = work_event_view
        self.works_view = works_view
        self.orders_view = order_view

    @property
    def reports_window(self) -> ReportsWindowProtocol:
        return self._reports_window

    def start_session(self) -> None:
        self.reports_window.add_view(ReportsViews.DIVISIONS, self.divisions_view)
        self.reports_window.add_view(ReportsViews.STAFF, self.staff_view)
        self.reports_window.add_view(ReportsViews.WORK_TYPES, self.work_types_view)
        self.reports_window.add_view(ReportsViews.WORKS, self.works_view)
        self.reports_window.add_view(ReportsViews.ORDERS, self.orders_view)
        self.reports_window.add_view(ReportsViews.WORK_EVENTS, self.work_events_view)
        self.reports_window.change_view(ReportsViews.DIVISIONS)
        self._connect_signals()

    def _connect_signals(self) -> None:
        # self.reports_window.back_main_menu_signal.connect(self.open_main_menu_window)
        self.reports_window.open_divisions_view_signal.connect(self.open_divisions_view)
        self.reports_window.open_staff_view_signal.connect(self.open_staff_view)
        self.reports_window.open_works_view_signal.connect(self.open_works_view)
        self.reports_window.open_work_events_view_signal.connect(self.open_work_events_view)
        self.reports_window.open_work_types_view_signal.connect(self.open_work_types_view)
        self.reports_window.open_orders_view_signal.connect(self.open_orders_view)

    def open_main_menu_window(self) -> None:
        print('возвращаемся в главное меню')

    def open_divisions_view(self) -> None:
        self.reports_window.change_view(ReportsViews.DIVISIONS)

    def open_staff_view(self) -> None:
        self.reports_window.change_view(ReportsViews.STAFF)

    def open_work_types_view(self) -> None:
        self.reports_window.change_view(ReportsViews.WORK_TYPES)

    def open_works_view(self) -> None:
        self.reports_window.change_view(ReportsViews.WORKS)

    def open_orders_view(self) -> None:
        self.reports_window.change_view(ReportsViews.ORDERS)

    def open_work_events_view(self) -> None:
        self.reports_window.change_view(ReportsViews.WORK_EVENTS)
