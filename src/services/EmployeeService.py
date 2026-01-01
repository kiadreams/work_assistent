from sqlalchemy.orm import Session

from src.core.models.division_domain import DivisionDomain


class EmployeeService:
    def __init__(self, session: Session):
        self.session = session

    def is_division_deleted(self, division: DivisionDomain) -> bool:
        if self.session:
            return False
        return True

    def load_all_divisions(self) -> list[DivisionDomain]:
        if self.session:
            return []
        return []

    def save_division(self, division: DivisionDomain) -> None:
        pass

    def delete_division(self, division: DivisionDomain) -> None:
        pass
