from dataclasses import dataclass
from datetime import timedelta
from enum import StrEnum

from src.packages.device import Device


class TypeOfWork(StrEnum):
    SETTING_UP = 'наладка'
    FIRST_CONTROL = 'первый профилактический контроль'
    RESTORATION = 'восстановление'
    CONTROL = 'профилактический контроль'
    TESTING = 'опробование'


@dataclass
class Work:
    name: str
    device: Device
    type_of_work: TypeOfWork


@dataclass
class WorkOrder:
    numbers: int
    dedicated_hours: timedelta
