from dataclasses import dataclass

from src.packages.models.work import WorkOrder, Work
from src.packages.models.work_processes import EmployeeEvent


@dataclass
class StatementOfWork:
    work: Work
    order: WorkOrder
    events: list[EmployeeEvent]