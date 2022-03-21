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


class VisitInfo(BaseModel):
    visit_hospital_number: int
    visit_outpatient_number: int
    visit_emergency_number: int
    visit_male_number: int
    visit_female_number: int
    visit_asian_number: int
    visit_white_number: int
    visit_black_number: int
    visit_hispanic_number: int
    visit_nonhispanic_number: int
    # visit_10s_number: int
    # visit_20s_number: int
    # visit_30s_number: int
    # visit_40s_number: int
    # visit_over50s_number: int

    class Config:
        orm_mode = True
