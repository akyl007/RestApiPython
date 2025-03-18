from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from app.db.base import Base

class Building(Base):
    __tablename__ = "buildings"

    id = Column(Integer, primary_key=True, index=True)
    address = Column(String, index=True)
    latitude = Column(Float)
    longitude = Column(Float)
    
    # Отношения
    organizations = relationship("Organization", back_populates="building") 