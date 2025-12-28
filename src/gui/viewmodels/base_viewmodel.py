from typing import Type
from sqlalchemy import select
from sqlalchemy.orm import Session

from ..database.database import Base, SessionLocal


class BaseViewModel:
    def __init__(self) -> None:
        self.session: Session = SessionLocal()
