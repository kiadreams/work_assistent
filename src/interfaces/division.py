from typing import Protocol

from ..entities.division import Division


class IDivisionRepository(Protocol):
    def get_division_by_name(self, name: str) -> Division: ...
