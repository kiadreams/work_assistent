from dataclasses import dataclass
from datetime import timedelta

from src.packages.models.device import Device
from src.packages.databases.types_of_work import TypeOfWork


@dataclass
class Work:
    name: str
    device: Device
    type_of_work: TypeOfWork


@dataclass
class WorkOrder:
    numbers: int
    dedicated_hours: timedelta
