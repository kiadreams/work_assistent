from __future__ import annotations

from typing import (
    Protocol,
    TYPE_CHECKING,
)


if TYPE_CHECKING:
    from src.core.models.division_domain import DivisionDomain


class DivisionRepositoryProtocol(Protocol):

    def get_division_by_name(self, name: str) -> DivisionDomain | None: ...

    @property
    def all_divisions(self) -> list[DivisionDomain]: ...

    def add_new_division(self, division: DivisionDomain) -> None: ...
