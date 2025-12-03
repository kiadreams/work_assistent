from dataclasses import dataclass
from datetime import datetime, timedelta

from src.packages.work import Work
from src.packages.employee import Employee


@dataclass
class EmployeeEvent:
    work: Work
    employee: Employee
    start_date: datetime
    end_date: datetime

