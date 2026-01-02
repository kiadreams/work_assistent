from typing import Protocol

from ...core.interfaces.services import EmployeeServiceProtocol
from ...core.models.division_domain import DivisionDomain


class DivisionViewModelProtocol(Protocol):

    @property
    def current_service(self) -> str: ...

    @property
    def divisions(self) -> list[str]: ...

    def show_all_divisions(self) -> None: ...

    def add_new_division(self, service_data: tuple[str, str]) -> None: ...

    @property
    def first_division(self) -> DivisionDomain | None: ...

    @property
    def is_current_division_deleted(self) -> bool: ...

    def change_current_division(self, division_name: str) -> None: ...

    def delete_current_division(self) -> None: ...
