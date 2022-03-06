from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Organization(Base):
    __tablename__ = "organizations"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    #owner_id = Column(Integer, ForeignKey("admin.id"))
    description = Column(String, index=True)
    title = Column(String, index=True)
    events = relationship("Event", back_populates="organizer")

class Admin(Base):
    __tablename__ = "admins"
    
    name = Column(String, index=True)
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    events = relationship("Event", back_populates="organizer")
    organizations = relationship("Organization", back_populates="owner")


class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    #owner_id = Column(Integer, ForeignKey("admin.id"))

    organizer = relationship("Admin", back_populates="events")
