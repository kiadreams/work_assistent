from sqlalchemy.orm import Session

from ...core.interfaces.repositories import IDivisionRepository


class DivisionRepository(IDivisionRepository):
    def __init__(self, session: Session):
        self.session = session

