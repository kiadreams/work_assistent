import datetime

from sqlalchemy import String, ForeignKey, SmallInteger, Date, Time, extract, func
from sqlalchemy.orm import MappedAsDataclass, Mapped, mapped_column, relationship

from . import employee_db_tables
from . import device_db_tables
from src.packages.databases.database import Base
from . import association_db_tables


class TypeOfMaintenance(MappedAsDataclass, Base):
    __tablename__ = 'types_of_maintenance'

    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    name: Mapped[str] = mapped_column(String(30), nullable=False)

    works: Mapped[list['Work']] = relationship(back_populates='type_of_maintenance')

    abbreviation: Mapped[str | None] = mapped_column(String(20), nullable=True, default=None)


class WorkOrder(MappedAsDataclass, Base):
    __tablename__ = 'work_orders'

    id: Mapped[int] = mapped_column(primary_key=True, init=False)

    works: Mapped[list['Work']] = relationship(back_populates='work_order')

    number: Mapped[str] = mapped_column(String(20), nullable=False, default='V05110______')


class Work(MappedAsDataclass, Base):
    __tablename__ = 'list_of_works'

    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    name: Mapped[str] = mapped_column(String(50), nullable=False)

    type_of_maintenance: Mapped['TypeOfMaintenance'] = relationship(back_populates='works')
    work_order: Mapped['WorkOrder'] = relationship(back_populates='works')
    events: Mapped['WorkEvent'] = relationship(back_populates='work')
    devices: Mapped[list['device_db_tables.Device']] = relationship(secondary=association_db_tables.devices_in_works,
                                                           back_populates='works')

    year: Mapped[int] = mapped_column(SmallInteger,
                                      nullable=False,
                                      server_default=extract('year', func.now()))
    month: Mapped[int | None] = mapped_column(SmallInteger, nullable=True, default=None)
    type_of_maintenance_id: Mapped[int | None] = mapped_column(ForeignKey('types_of_maintenance.id'),
                                                               nullable=True,
                                                               default=None)
    work_order_id: Mapped[int | None] = mapped_column(ForeignKey('work_orders.id'), nullable=True, default=None)
    device_id: Mapped[int | None] = mapped_column(ForeignKey('devices.id'), nullable=True, default=None)


class WorkEvent(MappedAsDataclass, Base):
    __tablename__ = 'work_events'

    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    employee_service_number: Mapped[int] = mapped_column(ForeignKey('employees.service_number'), nullable=False)
    work_id: Mapped[int] = mapped_column(ForeignKey('list_of_works.id'), nullable=False)
    date: Mapped[datetime.date] = mapped_column(Date, nullable=False, server_default=func.now())

    work: Mapped[Work] = relationship(back_populates='events')
    employee: Mapped['employee_db_tables.Employee'] = relationship(back_populates='work_events')

    start_time: Mapped[datetime.time] = mapped_column(Time, nullable=False, default=datetime.time(8, 30, 0))
    end_time: Mapped[datetime.time] = mapped_column(Time, nullable=False, default=datetime.time(16, 30, 0))
