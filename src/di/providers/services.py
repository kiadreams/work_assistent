from dishka import Provider, Scope, provide

from src.database.interfaces.repositories import DivisionRepositoryProtocol
from src.services.EmployeeService import EmployeeService
from src.services.interfaces.services import EmployeeServiceProtocol


class ServiceProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def employee_service(
        self, divisions_repository: DivisionRepositoryProtocol
    ) -> EmployeeServiceProtocol:
        return EmployeeService(division_repository=divisions_repository)
