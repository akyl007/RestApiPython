from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Activity(Base):
    __tablename__ = "activities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    parent_id = Column(Integer, ForeignKey("activities.id"))
    level = Column(Integer, default=1)
    
    # Отношения
    children = relationship("Activity", 
                          backref=relationship("Activity", remote_side=[id]),
                          cascade="all, delete-orphan") 