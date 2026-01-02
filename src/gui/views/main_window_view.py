from PySide6 import QtWidgets

from src.utils.qt_recource_loader import ResourceLoader
from .main_menu_view import MainMenuView
from .report_generator_view import ReportGeneratorView
from src.gui.constants import QtStyleResources
from src.gui.generated import Ui_MainWindow
from src.gui.constants import MainWindowPages


class MainWindowView(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, views: ReportGeneratorView, main_menu: MainMenuView) -> None:
        super().__init__()
        self.menu = main_menu
        self.report_views = views
        self.__init_content_widget()
        self.__setup_connections()

    def __init_content_widget(self) -> None:
        self.setupUi(self)  # type: ignore[no-untyped-call]
        self.setStyleSheet(ResourceLoader(QtStyleResources.MAIN_WINDOW_STYLE).load_style())
        self.stackedWidget_windows.insertWidget(
            MainWindowPages.MAIN_MENU, self.get_widget_to_insert(self.menu)
        )
        self.stackedWidget_windows.insertWidget(
            MainWindowPages.REPORT_CREATION, self.get_widget_to_insert(self.report_views)
        )
        self.stackedWidget_windows.setCurrentIndex(MainWindowPages.MAIN_MENU)
        self.resize(1280, 800)

    def __setup_connections(self) -> None:
        self.menu.close_app_signal.connect(self.close)
        self.menu.change_page_signal.connect(self.change_page)
        self.report_views.change_page_signal.connect(self.change_page)

    def change_page(self, index: int) -> None:
        self.stackedWidget_windows.setCurrentIndex(index)

    @staticmethod
    def get_widget_to_insert(widget: QtWidgets.QWidget) -> QtWidgets.QWidget:
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(widget)
        widget.setLayout(layout)
        return widget