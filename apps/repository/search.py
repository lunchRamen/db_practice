from fastapi import HTTPException, Request, Response, status
from sqlalchemy.orm import Session

from .. import schemas
from ..models import Death, Person, VisitOccurrence


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


def get_visit_info(db: Session):
    visit_info = schemas.VisitInfo

    visit_info.visit_hospital_number = (
        db.query(VisitOccurrence.visit_concept_id)
        .filter(VisitOccurrence.visit_concept_id == 9201)
        .count()
    )
    visit_info.visit_outpatient_number = (
        db.query(VisitOccurrence.visit_concept_id)
        .filter(VisitOccurrence.visit_concept_id == 9202)
        .count()
    )
    visit_info.visit_emergency_number = (
        db.query(VisitOccurrence.visit_concept_id)
        .filter(VisitOccurrence.visit_concept_id == 9203)
        .count()
    )
    visit_info.visit_male_number = (
        db.query(Person.gender_concept_id)
        .join(Person, VisitOccurrence.person)
        .filter(
            (VisitOccurrence.person_id == Person.person_id)
            & (Person.gender_concept_id == 8507)
        )
        .count()
    )
    visit_info.visit_female_number = (
        db.query(Person.gender_concept_id)
        .join(Person, VisitOccurrence.person)
        .filter(
            (VisitOccurrence.person_id == Person.person_id)
            & (Person.gender_concept_id == 8532)
        )
        .count()
    )
    visit_info.visit_asian_number = (
        db.query(Person.race_concept_id)
        .join(Person, VisitOccurrence.person)
        .filter(
            (VisitOccurrence.person_id == Person.person_id)
            & (Person.race_concept_id == 8515)
        )
        .count()
    )
    visit_info.visit_white_number = (
        db.query(Person.race_concept_id)
        .join(Person, VisitOccurrence.person)
        .filter(
            (VisitOccurrence.person_id == Person.person_id)
            & (Person.race_concept_id == 8527)
        )
        .count()
    )
    visit_info.visit_black_number = (
        db.query(Person.race_concept_id)
        .join(Person, VisitOccurrence.person)
        .filter(
            (VisitOccurrence.person_id == Person.person_id)
            & (Person.race_concept_id == 8516)
        )
        .count()
    )
    visit_info.visit_hispanic_number = (
        db.query(Person.ethnicity_source_value)
        .join(Person, VisitOccurrence.person)
        .filter(
            (VisitOccurrence.person_id == Person.person_id)
            & (Person.ethnicity_source_value == "hispanic")
        )
        .count()
    )
    visit_info.visit_nonhispanic_number = (
        db.query(Person.ethnicity_source_value)
        .join(Person, VisitOccurrence.person)
        .filter(
            (VisitOccurrence.person_id == Person.person_id)
            & (Person.ethnicity_source_value == "nonhispanic")
        )
        .count()
    )

    return visit_info
