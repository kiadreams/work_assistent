import datetime

from sqlalchemy import String, ForeignKey, Date, CheckConstraint
from sqlalchemy.orm import MappedAsDataclass, Mapped, mapped_column, relationship

from src.packages.databases.database import Base
from . import work_db_tables


class Service(MappedAsDataclass, Base):
    __tablename__ = 'services'

    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)

    departments: Mapped[list['Department']] = relationship(
        back_populates='service',
        default_factory=list
    )
    employee_positions: Mapped[list['EmployeePosition']] = relationship(
        back_populates='service',
        default_factory=list
    )

    full_name: Mapped[str | None] = mapped_column(String(20), nullable=True, default=None)


class Department(MappedAsDataclass, Base):
    __tablename__ = 'departments'

    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    service_id: Mapped[int] = mapped_column(ForeignKey('services.id'))

    service: Mapped['Service'] = relationship(back_populates='departments')
    employee_positions: Mapped[list['EmployeePosition']] = relationship(
        back_populates='department',
        default_factory=list
    )
    full_name: Mapped[str | None] = mapped_column(String(20), nullable=True, default=None)


class EmployeePosition(MappedAsDataclass, Base):
    __tablename__ = 'employee_positions'

    __table_args__ = (
        CheckConstraint(
            sqltext='(service_id IS NOT NULL AND department_id IS NULL) '
                    'OR (service_id IS NULL AND department_id IS NOT NULL)',
            name='chk_single_department'),
    )

    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    service_id: Mapped[int] = mapped_column(ForeignKey('services.id'))
    department_id: Mapped[int] = mapped_column(ForeignKey('departments.id'))

    service: Mapped['Service'] = relationship(back_populates='employee_positions', default=None)
    department: Mapped['Department'] = relationship(back_populates='employee_positions', default=None)
    employees: Mapped[list['Employee']] = relationship(back_populates='employee_position', default_factory=list)

    abbreviation: Mapped[str | None] = mapped_column(String(20), nullable=True, default=None)


class Employee(MappedAsDataclass, Base):
    __tablename__ = 'employees'

    service_number: Mapped[int] = mapped_column(primary_key=True, autoincrement=False)
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    last_name: Mapped[str] = mapped_column(String(30), nullable=False)
    middle_name: Mapped[str] = mapped_column(String(30), nullable=False)
    employee_position_id: Mapped[int] = mapped_column(ForeignKey('employee_positions.id'))

    employee_position: Mapped['EmployeePosition'] = relationship(back_populates='employees')
    work_events: Mapped[list['work_db_tables.WorkEvent']] = relationship(back_populates='employee')

    date_of_birth: Mapped[datetime.date | None] = mapped_column(Date, nullable=True, default=None)
