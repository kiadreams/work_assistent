from sqlalchemy import select
from sqlalchemy.exc import MultipleResultsFound
from sqlalchemy.orm import Session

from ..entities import Division
from ...core.interfaces.repositories import DivisionRepositoryProtocol


class DivisionRepository(DivisionRepositoryProtocol):
    def __init__(self, session: Session):
        self.session = session

    def get_division_by_name(self, name: str) -> Division | None:
        stmt = select(Division).where(Division.name == name)
        try:
            division = self.session.scalar(stmt)
            return division
        except MultipleResultsFound:
            print(f"Найдено более одного значения division")
        return None

    @property
    def all_divisions(self) -> list[Division]:
        stmt = select(Division).order_by(Division.name.asc())
        try:
            divisions = self.session.scalars(stmt).all()
            return list(divisions)
        except Exception as e:
            print(f"Произошла ошибка при запросе всех служб: {e}")
            return []

    def add_new_division(self, division: Division) -> None:
        self.session.add(division)
