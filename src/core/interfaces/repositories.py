from __future__ import annotations

from typing import (
    Any,
    ContextManager,
    Generator,
    Protocol,
    TYPE_CHECKING,
)

from sqlalchemy.orm import Session

if TYPE_CHECKING:
    from src.core.models.division_domain import DivisionDomain


class DatabaseManagerProtocol(Protocol):
    def create_db_tables(self) -> None: ...

    def create_session(self) -> Session: ...


class DivisionRepositoryProtocol(Protocol):
    def get_division_by_name(self, name: str) -> DivisionDomain | None: ...

    @property
    def all_divisions(self) -> list[DivisionDomain]: ...

    def add_new_division(self, division: DivisionDomain) -> None: ...
