from PySide6 import QtWidgets

from .. import resources_rc
from ..resource_loader import ResourceLoader, get_version_from_file
from ..views_structure import QtResources


class BaseAppWidget:

    @property
    def app_version(self) -> str:
        return get_version_from_file()

    def _init_widget_style(self, resources: QtResources) -> None:
        self.setupUi(self)
        self.setStyleSheet(ResourceLoader(resources).load_style())

    @staticmethod
    def get_widget_to_insert(widget: QtWidgets.QWidget) -> QtWidgets.QWidget:
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(widget)
        widget.setLayout(layout)
        return widget
