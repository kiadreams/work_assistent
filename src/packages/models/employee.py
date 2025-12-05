from dataclasses import dataclass
from datetime import date





@dataclass
class Employee:
    name: str
    last_name: str
    middle_name: str
    date_of_birth: date
    post: EmployeePosition
