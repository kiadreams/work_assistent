from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import MappedAsDataclass, Mapped, mapped_column, relationship

from . import association_tables
from . import works
from ..databases.database import Base


class DeviceLocation(MappedAsDataclass, Base):
    __tablename__ = 'device_locations'

    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    name: Mapped[str] = mapped_column(String(50))

    devices: Mapped[list['Device']] = relationship(back_populates='location')
    works: Mapped[list['works.Work']] = relationship(secondary=association_tables.devices_in_works,
                                                     back_populates='devices')

    inventory_number: Mapped[str | None] = mapped_column(String(20), nullable=True, default=None)


class Device(MappedAsDataclass, Base):
    __tablename__ = 'devices'

    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    name: Mapped[str] = mapped_column(String(50))
    device_location_id: Mapped[int] = mapped_column(ForeignKey('device_locations.id'))

    location: Mapped[DeviceLocation] = relationship(back_populates='devices')

    inventory_number: Mapped[str | None] = mapped_column(String(20), nullable=True, default=None)
