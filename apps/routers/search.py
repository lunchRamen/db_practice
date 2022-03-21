from typing import List

from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session

from database import get_db

from .. import schemas
from ..repository import search

router = APIRouter(
    prefix="/search",
    tags=["searches"],
)


@router.get("/patient", response_model=schemas.PatientInfo)
def search_patient(db: Session = Depends(get_db)):
    return search.get_patient_info(db)
