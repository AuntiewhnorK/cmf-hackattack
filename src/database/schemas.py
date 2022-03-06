from typing import List, Optional

from pydantic import BaseModel


class OrgBase(BaseModel):
    title: str
    description: Optional[str] = None


class OrgCreate(OrgBase):
    pass


class Organization(OrgBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class EventBase(BaseModel):
    title = str
    email: str
    description: Optional[str] = None

class Event(EventBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class AdminBase(BaseModel):
    email: str

class AdminCreate(AdminBase):
    password: str


class EventCreate(EventBase):
    pass

class Admin(AdminBase):
    id: int
    events: List[Event] = []

    class Config:
        orm_mode = True