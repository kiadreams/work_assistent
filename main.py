import sys

from PySide6.QtWidgets import QApplication

from src.core.interfaces.coordinators import AppCoordinatorProtocol
from src.core.interfaces.repositories import DatabaseManagerProtocol
from src.di.container import get_container


if __name__ == "__main__":
    container = get_container()
    db_manager = container.get(DatabaseManagerProtocol)
    db_manager.create_db_tables()

    app = QApplication(sys.argv)
    coordinator = container.get(AppCoordinatorProtocol)
    sys.exit(app.exec())
