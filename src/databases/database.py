from typing import Any, Generator
from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Session
from sqlalchemy.orm.session import Session


class Base(DeclarativeBase):
    pass


DATABASE_URL = "sqlite:///instance/work_database.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autoflush=False, bind=engine)


class DatabaseManager:
    def __init__(self, db_url: str) -> None:
        self.engine = create_engine(db_url)
        self.SessionLocal = sessionmaker(autoflush=False, bind=engine)


    def create_db_tables(self) -> None:
        print(f"Подключение к базе данных {self.engine.url} и создание таблиц...")
            # --- ЭТА КОМАНДА СОЗДАЕТ ТАБЛИЦЫ ---
        # Она проверяет все импортированные классы, наследуемые от Base,
        # и создает таблицы, если они еще не существуют.
        Base.metadata.create_all(engine)
        print("Таблицы успешно созданы.")

    @contextmanager
    def get_db_session(self) -> Generator[Session, Any, None]:
        """Предоставляет сессию и гарантирует ее закрытие."""
        session = self.SessionLocal()
        try:
            yield session
            session.commit()  # Автоматический коммит при выходе из 'with'
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()
