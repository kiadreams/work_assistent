from PySide6 import QtWidgets

from .base_app_widget import BaseAppWidget
from ..resource_loader import QtStyleResources
from ..forms.ui_orders_report_widget import Ui_OrderReportsWidget


class OrderReport(QtWidgets.QWidget, Ui_OrderReportsWidget, BaseAppWidget):

    def __init__(self) -> None:
        super().__init__()
        self.__init_content_widget()
        self.__setup_connections()

    def __init_content_widget(self) -> None:
        self._init_widget_style(QtStyleResources.MAIN_MENU_STYLE)

    def __setup_connections(self) -> None:
        pass

