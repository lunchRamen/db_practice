import sqlalchemy
from sqlalchemy import (
    DATE,
    DATETIME,
    TEXT,
    TIMESTAMP,
    Boolean,
    Column,
    ForeignKey,
    Integer,
    Numeric,
    String,
    Table,
)
from sqlalchemy.orm import backref, relationship

from database import Base


class Concept(Base):
    __tablename__ = "concept"
    concept_id = Column(Integer, primary_key=True, index=True)
    concept_name = Column(String(255))
    domain_id = Column(String(20))
    vocabulary_id = Column(String(20))
    concept_class_id = Column(String(20))
    standard_concept = Column(String(1))
    concept_code = Column(String(50))
    valid_start_date = Column(DATE)
    valid_end_date = Column(DATE)
    invalid_reason = Column(String(1))


class Person(Base):
    __tablename__ = "person"

    person_id = Column(Integer, primary_key=True, index=True)
    gender_concept_id = Column(Integer, ForeignKey("concept.concept_id"))
    year_of_birth = Column(Integer)
    month_of_birth = Column(Integer)
    day_of_birth = Column(Integer)
    birth_datetime = Column(TIMESTAMP)
    race_concept_id = Column(Integer, ForeignKey("concept.concept_id"))
    ethnicity_concept_id = Column(Integer)
    location_id = Column(Integer)
    provider_id = Column(Integer)
    care_site_id = Column(Integer)
    person_source_value = Column(String(50))
    gender_source_value = Column(String(50))
    gender_source_concept_id = Column(Integer)
    race_source_value = Column(String(50))
    race_source_concept_id = Column(Integer)
    ethnicity_source_value = Column(String(50))
    ethnicity_source_concept_id = Column(Integer)

    gender_concept = relationship("Concept", foreign_keys=[gender_concept_id])
    race_concept = relationship("Concept", foreign_keys=[race_concept_id])


class VisitOccurrence(Base):
    __tablename__ = "visit_occurrence"

    visit_occurrence_id = Column(Integer, primary_key=True, index=True)
    person_id = Column(Integer, ForeignKey("person.person_id"))
    visit_concept_id = Column(Integer, ForeignKey("concept.concept_id"))
    visit_start_date = Column(DATE)
    visit_start_datetime = Column(TIMESTAMP)
    visit_end_date = Column(DATE)
    visit_end_datetime = Column(TIMESTAMP)
    visit_type_concept_id = Column(Integer, ForeignKey("concept.concept_id"))
    provider_id = Column(Integer)
    care_site_id = Column(Integer)
    visit_source_value = Column(String(50))
    visit_source_concept_id = Column(Integer, ForeignKey("concept.concept_id"))
    admitted_from_concept_id = Column(Integer)
    admitted_from_source_value = Column(String(50))
    discharge_to_source_value = Column(String(50))
    discharge_to_concept_id = Column(Integer, ForeignKey("concept.concept_id"))
    preceding_visit_occurrence_id = Column(
        Integer, ForeignKey("visit_occurrence.visit_occurrence_id")
    )

    person = relationship("Person", foreign_keys=[person_id])
    visit_concept = relationship("Concept", foreign_keys=[visit_concept_id])
    visit_type_concept = relationship("Concept", foreign_keys=[visit_type_concept_id])
    visit_source_concept = relationship(
        "Concept", foreign_keys=[visit_source_concept_id]
    )
    discharge_to_concept = relationship(
        "Concept", foreign_keys=[discharge_to_concept_id]
    )


class ConditionOccurrence(Base):
    __tablename__ = "condition_occurrence"
    condition_occurrence_id = Column(Integer, primary_key=True, index=True)
    person_id = Column(Integer, ForeignKey("person.person_id"))
    condition_concept_id = Column(Integer, ForeignKey("concept.concept_id"))
    condition_start_date = Column(DATE)
    condition_start_datetime = Column(TIMESTAMP)
    condition_end_date = Column(DATE)
    condition_end_datetime = Column(TIMESTAMP)
    condition_type_concept_id = Column(Integer, ForeignKey("concept.concept_id"))
    condition_status_concept_id = Column(Integer, ForeignKey("concept.concept_id"))
    stop_reason = Column(String(20))
    provider_id = Column(Integer)
    visit_occurrence_id = Column(
        Integer, ForeignKey("visit_occurrence.visit_occurrence_id")
    )
    visit_detail_id = Column(Integer)
    condition_source_value = Column(String(50))
    condition_source_concept_id = Column(Integer, ForeignKey("concept.concept_id"))
    condition_status_source_value = Column(String(50))

    person = relationship("Person", foreign_keys=[person_id])
    condition_concept = relationship("Concept", foreign_keys=[condition_concept_id])
    condition_type_concept = relationship(
        "Concept", foreign_keys=[condition_type_concept_id]
    )
    condition_status_concept = relationship(
        "Concept", foreign_keys=[condition_status_concept_id]
    )
    visit_occurrence = relationship(
        "VisitOccurrence", foreign_keys=[visit_occurrence_id]
    )
    condition_source_concept = relationship(
        "Concept", foreign_keys=[condition_source_concept_id]
    )


class DrugExposure(Base):
    __tablename__ = "drug_exposure"
    drug_exposure_id = Column(Integer, primary_key=True, index=True)
    person_id = Column(Integer, ForeignKey("person.person_id"))
    drug_concept_id = Column(Integer, ForeignKey("concept.concept_id"))
    drug_exposure_start_date = Column(DATE)
    drug_exposure_start_datetime = Column(TIMESTAMP)
    drug_exposure_end_date = Column(DATE)
    drug_exposure_end_datetime = Column(TIMESTAMP)
    verbatim_end_date = Column(DATE)
    drug_type_concept_id = Column(Integer, ForeignKey("concept.concept_id"))
    stop_reason = Column(String(20))
    refills = Column(Integer)
    quantity = Column(Numeric)
    days_supply = Column(Integer)
    sig = Column(TEXT)
    route_concept_id = Column(Integer, ForeignKey("concept.concept_id"))
    lot_number = Column(String(50))
    provider_id = Column(Integer)
    visit_occurrence_id = Column(
        Integer, ForeignKey("visit_occurrence.visit_occurrence_id")
    )
    visit_detail_id = Column(Integer)
    drug_source_value = Column(String(50))
    drug_source_concept_id = Column(Integer, ForeignKey("concept.concept_id"))
    route_source_value = Column(String(50))
    dose_unit_source_value = Column(String(50))

    person = relationship("Person", foreign_keys=[person_id])
    drug_concept = relationship("Concept", foreign_keys=[drug_concept_id])
    drug_type_concept = relationship("Concept", foreign_keys=[drug_type_concept_id])
    route_concept = relationship("Concept", foreign_keys=[route_concept_id])
    visit_occurrence = relationship(
        "VisitOccurrence", foreign_keys=[visit_occurrence_id]
    )
    drug_source_concept = relationship("Concept", foreign_keys=[drug_source_concept_id])


class Death(Base):
    __tablename__ = "death"
    person_id = Column(Integer, ForeignKey("person.person_id"), primary_key=True)
    death_date = Column(DATE)
    death_datetime = Column(TIMESTAMP)
    death_type_concept_id = Column(Integer)
    cause_concept_id = Column(Integer, ForeignKey("concept.concept_id"))
    cause_source_value = Column(Integer)
    cause_source_concept_id = Column(Integer, ForeignKey("concept.concept_id"))

    person = relationship("Person", foreign_keys=[person_id])
    cause_concept = relationship("Concept", foreign_keys=[cause_concept_id])
    cause_source_concept = relationship(
        "Concept", foreign_keys=[cause_source_concept_id]
    )
