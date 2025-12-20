from PySide6 import QtWidgets
from PySide6.QtCore import Signal

from .base_app_widget import BaseAppWidget
from .order_reports import OrderReport
from .service_reports import ServiceReport
from .staff_reports import StaffReport
from .work_event_reports import WorkEventReport
from .work_reports import WorkReport
from .work_type_reports import WorkTypeReport
from ..resource_loader import QtStyleResources
from ..views_structure import MainWindowPages, ReportGenerationPages
from ..forms.ui_report_generation_widget import Ui_ReportGenerationWidget


class ReportGenerator(QtWidgets.QWidget, Ui_ReportGenerationWidget, BaseAppWidget):

    change_page_signal = Signal(int)

    def __init__(self) -> None:
        super().__init__()
        self.services = ServiceReport()
        self.staff = StaffReport()
        self.work_types = WorkTypeReport()
        self.works = WorkReport()
        self.orders = OrderReport()
        self.work_events = WorkEventReport()
        self.__init_content_widget()
        self.__setup_connections()

    def __init_content_widget(self) -> None:
        self._init_widget_style(QtStyleResources.MAIN_MENU_STYLE)
        self.stackedWidget_types_of_reports.insertWidget(ReportGenerationPages.SERVICES_AND_GROUPS,
                                                         self.get_widget_to_insert(self.services))
        self.stackedWidget_types_of_reports.insertWidget(ReportGenerationPages.STAFF,
                                                         self.get_widget_to_insert(self.staff))
        self.stackedWidget_types_of_reports.insertWidget(ReportGenerationPages.TYPES_OF_WORK,
                                                         self.get_widget_to_insert(self.work_types))
        self.stackedWidget_types_of_reports.insertWidget(ReportGenerationPages.WORKS,
                                                         self.get_widget_to_insert(self.works))
        self.stackedWidget_types_of_reports.insertWidget(ReportGenerationPages.ORDERS,
                                                         self.get_widget_to_insert(self.orders))
        self.stackedWidget_types_of_reports.insertWidget(ReportGenerationPages.WORK_EVENTS,
                                                         self.get_widget_to_insert(self.work_events))

        self.stackedWidget_types_of_reports.setCurrentIndex(ReportGenerationPages.SERVICES_AND_GROUPS)

    def __setup_connections(self):
        self.pushButton_go_to_main_menu.clicked.connect(self.go_to_main_menu)
        self.buttonGroup.idClicked.connect(self.change_report_page)

    def change_report_page(self, id: int) -> None:
        id = abs(id + 2)
        print(id)
        self.stackedWidget_types_of_reports.setCurrentIndex(abs(id) + 2)

    def go_to_main_menu(self) -> None:
        self.change_page_signal.emit(MainWindowPages.MAIN_MENU)

