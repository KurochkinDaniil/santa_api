from typing import List

from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session

import crud
import database
from database import SessionLocal
from models import Participant, Base
from schemas import Group as GroupSchema, GroupCreate, GroupDetail, GroupUpdate, Participant as ParticipantSchema, \
    ParticipantWithRecipient, ParticipantCreate

Base.metadata.create_all(bind=database.engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/group/", response_model=GroupSchema, status_code=status.HTTP_201_CREATED)
def create_group(group: GroupCreate, db: Session = Depends(get_db)):
    return crud.create_group(db=db, group=group)


@app.get("/groups/", response_model=List[GroupSchema])
def read_groups(db: Session = Depends(get_db)):
    return crud.get_groups(db=db)


@app.get("/group/{group_id}", response_model=GroupDetail)
def read_group(group_id: int, db: Session = Depends(get_db)):
    db_group = crud.get_group(db=db, group_id=group_id)
    if db_group is None:
        raise HTTPException(status_code=404, detail="Group not found")
    return db_group


@app.put("/group/{group_id}", response_model=GroupSchema)
def update_group(group_id: int, group: GroupUpdate, db: Session = Depends(get_db)):
    return crud.update_group(db=db, group_id=group_id, group=group)


@app.delete("/group/{group_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_group(group_id: int, db: Session = Depends(get_db)):
    crud.delete_group(db=db, group_id=group_id)
    return {"ok": True}


@app.post("/group/{group_id}/participant", response_model=Participant, status_code=status.HTTP_201_CREATED)
def add_participant(group_id: int, participant: ParticipantCreate, db: Session = Depends(get_db)):
    return crud.create_participant(db=db, group_id=group_id, participant=participant)


@app.post("/group/{group_id}/toss", response_model=List[ParticipantWithRecipient])
def toss(group_id: int, db: Session = Depends(get_db)):
    try:
        return crud.toss_participants(db=db, group_id=group_id)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/group/{group_id}/participant/{participant_id}/recipient", response_model=ParticipantSchema)
def get_recipient(group_id: int, participant_id: int, db: Session = Depends(get_db)):
    return crud.get_recipient_for_participant(db=db, group_id=group_id, participant_id=participant_id)
