from sqlalchemy.orm import Session
from models import Group, Participant
from schemas import GroupCreate, GroupUpdate, ParticipantCreate
from fastapi import HTTPException
import random


def create_group(db: Session, group: GroupCreate):
    db_group = Group(name=group.name, description=group.description)
    db.add(db_group)
    db.commit()
    db.refresh(db_group)
    return db_group


def get_groups(db: Session):
    return db.query(Group).all()


def get_group(db: Session, group_id: int):
    return db.query(Group).filter(Group.id == group_id).first()


def update_group(db: Session, group_id: int, group: GroupUpdate):
    db_group = db.query(Group).filter(Group.id == group_id).first()
    if not db_group:
        raise HTTPException(status_code=404, detail="Group not found")
    db_group.name = group.name
    db_group.description = group.description
    db.commit()
    db.refresh(db_group)
    return db_group


def delete_group(db: Session, group_id: int):
    db_group = db.query(Group).filter(Group.id == group_id).first()
    if not db_group:
        raise HTTPException(status_code=404, detail="Group not found")
    db.delete(db_group)
    db.commit()


def create_participant(db: Session, group_id: int, participant: ParticipantCreate):
    db_participant = Participant(**participant.dict(), group_id=group_id)
    db.add(db_participant)
    db.commit()
    db.refresh(db_participant)
    return db_participant


def toss_participants(db: Session, group_id: int):
    participants = db.query(Participant).filter(Participant.group_id == group_id).all()
    if len(participants) < 3:
        raise HTTPException(status_code=409, detail="Not enough participants for a draw")

    random.shuffle(participants)

    # Assign recipients
    for i in range(len(participants)):
        recipient_index = (i + 1) % len(participants)
        participants[i].recipient_id = participants[recipient_index].id

    db.commit()
    return participants


def get_recipient_for_participant(db: Session, group_id: int, participant_id: int):
    participant = db.query(Participant).filter(Participant.id == participant_id, Participant.group_id == group_id).first()
    if not participant:
        raise HTTPException(status_code=404, detail="Participant not found")
    if not participant.recipient_id:
        raise HTTPException(status_code=404, detail="Recipient not assigned")
    recipient = db.query(Participant).filter(Participant.id == participant.recipient_id).first()
    return recipient
