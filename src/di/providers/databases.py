from dishka import Provider, Scope, provide
from sqlalchemy.orm import Session

from src.database.db_manager import DatabaseManager
from src.database.interfaces.repositories import DatabaseManagerProtocol, DivisionRepositoryProtocol
from src.database.repositories import DivisionRepository


class DatabaseProvider(Provider):
    @provide(scope=Scope.APP)
    def db_manager(self) -> DatabaseManagerProtocol:
        return DatabaseManager()

    @provide(scope=Scope.REQUEST)
    def db_session(self, manager: DatabaseManagerProtocol) -> Session:
        return manager.create_session()

    @provide(scope=Scope.REQUEST)
    def division_repository(self, curr_session: Session) -> DivisionRepositoryProtocol:
        return DivisionRepository(session=curr_session)
