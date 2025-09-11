from dataclasses import dataclass
from datetime import datetime, timedelta

from src.package.work import Work
from src.package.employee import Employee


@dataclass
class EmployeeEvent:
    work: Work
    employee: Employee
    start_date: datetime
    end_date: datetime

