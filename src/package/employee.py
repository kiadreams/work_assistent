from dataclasses import dataclass
from datetime import date
from enum import StrEnum


class EmployeePosition(StrEnum):
    ENGINEER = 'инженер'
    ENGINEER_2_CATEGORY = 'инженер 2-ой категории'
    ENGINEER_1_CATEGORY = 'инженер 1-ой категории'
    LEAD_ENGINEER = 'ведущий инженер'


@dataclass
class Employee:
    name: str
    last_name: str
    middle_name: str
    date_of_birth: date
    post: EmployeePosition
