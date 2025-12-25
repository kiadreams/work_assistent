from typing import Protocol

from src.entities import Division


class IDivisionRepository(Protocol):
    def get_division_by_name(self, name: str) -> Division: