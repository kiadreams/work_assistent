from contextlib import contextmanager
from typing import Iterator

from dishka import Provider, Scope, provide
from sqlalchemy.orm import Session

from src.database.db_manager import DatabaseManager
from src.database.repositories.division_repository import DivisionRepository
from src.services.EmployeeService import EmployeeService


class DatabaseProvider(Provider):
    @provide(scope=Scope.APP)
    def get_db_manager(self) -> DatabaseManager:
        return DatabaseManager()

    @provide(scope=Scope.REQUEST)
    @contextmanager
    def get_db_session(self, manager: DatabaseManager) -> Iterator[Session]:
        with manager.get_db_session() as session:
            yield session

    @provide(scope=Scope.REQUEST)
    def get_division_repository(self, session: Session) -> DivisionRepository:
        return DivisionRepository(session=session)


class ServiceProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def get_employee_service(self, session: Session) -> EmployeeService:
        return EmployeeService(session=session)
