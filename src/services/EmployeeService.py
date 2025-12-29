from sqlalchemy.orm import Session

from src.core.interfaces.services import EmployeeServiceProtocol


class EmployeeService(EmployeeServiceProtocol):
    def __init__(self, session: Session):
        self.session = session
