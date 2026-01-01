from __future__ import annotations

from typing import Protocol

from src.core.models.division_domain import DivisionDomain


class EmployeeServiceProtocol(Protocol):
    def is_division_deleted(self, division: DivisionDomain) -> bool: ...

    def load_all_divisions(self) -> list[DivisionDomain]: ...

    def save_division(self, division: DivisionDomain) -> None: ...

    def delete_division(self, division: DivisionDomain) -> None: ...
