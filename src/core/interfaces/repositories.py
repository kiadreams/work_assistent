from __future__ import annotations

from typing import Protocol, TYPE_CHECKING


if TYPE_CHECKING:
    from src.database.entities.division import Division


class IDivisionRepository(Protocol):
    def get_division_by_name(self, name: str) -> Division: ...

    @property
    def all_divisions(self) -> list[Division]: ...
