from dishka import Provider, Scope, provide
from sqlalchemy.orm import Session

from src.core.interfaces.repositories import DivisionRepositoryProtocol, DatabaseManagerProtocol
from src.core.interfaces.services import EmployeeServiceProtocol
from src.database.db_manager import DatabaseManager
from src.database.repositories.division_repository import DivisionRepository
from src.gui.views import MainWindowView
from src.services.EmployeeService import EmployeeService


class DatabaseProvider(Provider):
    @provide(scope=Scope.APP)
    def db_manager(self) -> DatabaseManagerProtocol:
        return DatabaseManager()

    @provide(scope=Scope.REQUEST)
    def db_session(self, manager: DatabaseManagerProtocol) -> Session:
        with manager.get_db_session() as session:
            return session

    @provide(scope=Scope.REQUEST)
    def division_repository(self, session: Session) -> DivisionRepositoryProtocol:
        return DivisionRepository(session=session)


class ServiceProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def employee_service(self, session: Session) -> EmployeeServiceProtocol:
        return EmployeeService(session=session)


# class UIWindowsProvider(Provider):
#     @provide(scope=Scope.APP)
#     def main_window(self) -> MainWindowView:
#         return MainWindowView()
