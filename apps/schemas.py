from datetime import datetime
from typing import List, Optional

from fastapi import Depends
from pydantic import BaseModel


class PatientInfo(BaseModel):
    total_patient_number: int
    male_patient_number: int
    female_patient_number: int
    asian_patient_number: int
    white_patient_number: int
    black_patient_number: int
    hispanic_patient_number: int
    nonhispanic_patient_number: int
    death_patient_number: int

    class Config:
        orm_mode = True
