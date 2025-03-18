from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from app.db.base import Base

# Таблица для связи many-to-many между организациями и телефонами
organization_phones = Table(
    'organization_phones',
    Base.metadata,
    Column('organization_id', Integer, ForeignKey('organizations.id')),
    Column('phone_id', Integer, ForeignKey('phones.id'))
)

# Таблица для связи many-to-many между организациями и видами деятельности
organization_activities = Table(
    'organization_activities',
    Base.metadata,
    Column('organization_id', Integer, ForeignKey('organizations.id')),
    Column('activity_id', Integer, ForeignKey('activities.id'))
)

class Phone(Base):
    __tablename__ = "phones"
    
    id = Column(Integer, primary_key=True, index=True)
    number = Column(String, unique=True, index=True)

class Organization(Base):
    __tablename__ = "organizations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    building_id = Column(Integer, ForeignKey("buildings.id"))
    
    # Отношения
    building = relationship("Building", back_populates="organizations")
    phones = relationship("Phone", secondary=organization_phones)
    activities = relationship("Activity", secondary=organization_activities) 