from fastapi import HTTPException, Request, Response, status
from sqlalchemy.orm import Session

from .. import schemas
from ..models import Death, Person


def get_patient_info(db: Session):
    patient_info = schemas.PatientInfo

    patient_info.total_patient_number = db.query(Person).count()
    patient_info.male_patient_number = (
        db.query(Person.gender_concept_id)
        .filter(Person.gender_concept_id == 8507)
        .count()
    )
    patient_info.female_patient_number = (
        db.query(Person.gender_concept_id)
        .filter(Person.gender_concept_id == 8532)
        .count()
    )
    patient_info.asian_patient_number = (
        db.query(Person.race_concept_id).filter(Person.race_concept_id == 8515).count()
    )
    patient_info.white_patient_number = (
        db.query(Person.race_concept_id).filter(Person.race_concept_id == 8527).count()
    )
    patient_info.black_patient_number = (
        db.query(Person.race_concept_id).filter(Person.race_concept_id == 8516).count()
    )
    patient_info.hispanic_patient_number = (
        db.query(Person.ethnicity_source_value)
        .filter(Person.ethnicity_source_value == "hispanic")
        .count()
    )
    patient_info.nonhispanic_patient_number = (
        db.query(Person.ethnicity_source_value)
        .filter(Person.ethnicity_source_value == "nonhispanic")
        .count()
    )
    patient_info.death_patient_number = db.query(Death).count()

    return patient_info
