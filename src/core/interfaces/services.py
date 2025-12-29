from __future__ import annotations

from typing import (
    Protocol,
    TYPE_CHECKING,
)


if TYPE_CHECKING:
    from src.database.entities.division import Division


class EmployeeServiceProtocol(Protocol):
    pass