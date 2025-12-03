from dataclasses import dataclass

from src.packages.work import WorkOrder, Work
from src.packages.work_processes import EmployeeEvent


@dataclass
class StatementOfWork:
    work: Work
    order: WorkOrder
    events: list[EmployeeEvent]