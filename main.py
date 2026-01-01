from src.core.app_coordinator import AppCoordinator
from src.core.interfaces.repositories import DatabaseManagerProtocol
from src.database.db_manager import DatabaseManager
from src.di.container import get_container


if __name__ == "__main__":
    container = get_container()
    db_manager = container.get(DatabaseManagerProtocol)
    db_manager.create_db_tables()

    print(container)
    coordinator = AppCoordinator(container)
