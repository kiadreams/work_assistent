from dataclasses import dataclass

from src.package.work import WorkOrder, Work
from src.package.work_processes import EmployeeEvent


@dataclass
class StatementOfWork:
    work: Work
    order: WorkOrder
    events: list[EmployeeEvent]