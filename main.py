from src.database.db_manager import DatabaseManager
from src.di.container import get_container


if __name__ == "__main__":
    container = get_container()
    db_manager = container.get(DatabaseManager)
    db_manager.create_db_tables()

