from typing import List, Optional
from pydantic import BaseModel


class ParticipantBase(BaseModel):
    name: str
    wish: Optional[str] = None


class ParticipantCreate(ParticipantBase):
    pass


class ParticipantUpdate(BaseModel):
    name: Optional[str] = None
    wish: Optional[str] = None


class ParticipantInDBBase(ParticipantBase):
    id: int
    group_id: int

    class Config:
        orm_mode = True


class Participant(ParticipantInDBBase):
    pass


class ParticipantWithRecipient(ParticipantInDBBase):
    recipient: Optional[Participant] = None


class GroupBase(BaseModel):
    name: str
    description: Optional[str] = None


class GroupCreate(GroupBase):
    pass


class GroupUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None


class GroupInDBBase(GroupBase):
    id: int

    class Config:
        orm_mode = True


class Group(GroupInDBBase):
    pass


class GroupDetail(GroupInDBBase):
    participants: List[Participant] = []
