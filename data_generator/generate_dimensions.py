"""
=====================================================
Hospital Emergency Department Analytics
Generate Dimension Tables
=====================================================
"""

import random
import pandas as pd
from faker import Faker

from config import (
    RANDOM_SEED,
    NUM_PATIENTS,
    NUM_DOCTORS,
    DEPARTMENTS,
    SHIFTS,
    INSURANCE_TYPES,
    GENDERS,
    RACES,
    RAW_DATA_PATH
)

fake = Faker()

random.seed(RANDOM_SEED)
Faker.seed(RANDOM_SEED)

def generate_departments():

    departments = pd.DataFrame({
        "DepartmentID": range(1, len(DEPARTMENTS) + 1),
        "DepartmentName": DEPARTMENTS,
        "Floor": [1,2,2,3,3,4,4,5,5,1]
    })

    departments.to_csv(
        RAW_DATA_PATH / "Dim_Department.csv",
        index=False
    )

    return departments

def generate_shifts():

    rows = []

    shift_id = 1

    for shift_name, times in SHIFTS.items():

        rows.append({
            "ShiftID": shift_id,
            "ShiftName": shift_name,
            "StartTime": times[0],
            "EndTime": times[1]
        })

        shift_id += 1

    shifts = pd.DataFrame(rows)

    shifts.to_csv(
        RAW_DATA_PATH / "Dim_Shift.csv",
        index=False
    )

    return shifts

DIAGNOSES = [
("Chest Pain","Cardiology","High"),
("Heart Attack","Cardiology","Critical"),
("Stroke","Neurology","Critical"),
("Migraine","Neurology","Medium"),
("Fracture","Orthopedics","Medium"),
("Sprain","Orthopedics","Low"),
("Asthma","Emergency","High"),
("Pneumonia","General Medicine","High"),
("Diabetes","General Medicine","Medium"),
("Appendicitis","General Surgery","High"),
("Burn","Emergency","High"),
("Fever","General Medicine","Low"),
("Food Poisoning","General Medicine","Medium"),
("Ear Infection","ENT","Low"),
("Sinusitis","ENT","Low"),
("Head Injury","Emergency","Critical"),
("Kidney Stone","General Medicine","High"),
("Sepsis","ICU","Critical"),
("COVID-19","General Medicine","High"),
("Flu","General Medicine","Low"),
("Hypertension","Cardiology","Medium"),
("Arrhythmia","Cardiology","High"),
("Epilepsy","Neurology","High"),
("Back Pain","Orthopedics","Low"),
("Arthritis","Orthopedics","Low"),
("Bronchitis","General Medicine","Medium"),
("Tonsillitis","ENT","Low"),
("Gallstones","General Surgery","Medium"),
("Trauma","Emergency","Critical"),
("Dehydration","General Medicine","Medium"),
("Allergic Reaction","Emergency","High"),
("Concussion","Neurology","Medium"),
("Fractured Arm","Orthopedics","Medium"),
("Fractured Leg","Orthopedics","High"),
("Appendix Rupture","General Surgery","Critical"),
("Eye Injury","Emergency","Medium"),
("Child Fever","Pediatrics","Low"),
("Child Asthma","Pediatrics","Medium"),
("Neonatal Infection","Pediatrics","Critical"),
("Internal Bleeding","ICU","Critical")
]
def generate_diagnosis():

    rows = []

    for i, diagnosis in enumerate(DIAGNOSES, start=1):

        rows.append({
            "DiagnosisID": i,
            "DiagnosisName": diagnosis[0],
            "Category": diagnosis[1],
            "Severity": diagnosis[2]
        })

    diagnosis_df = pd.DataFrame(rows)

    diagnosis_df.to_csv(
        RAW_DATA_PATH / "Dim_Diagnosis.csv",
        index=False
    )

    return diagnosis_df


DOCTOR_DISTRIBUTION = {
    "Emergency Medicine": 20,
    "Cardiology": 12,
    "Neurology": 10,
    "Orthopedics": 14,
    "Pediatrics": 12,
    "General Medicine": 18,
    "General Surgery": 12,
    "ICU": 8,
    "ENT": 6,
    "Radiology": 8
}

def generate_doctors():

    rows = []

    doctor_id = 1

    for department_id, department_name in enumerate(DEPARTMENTS, start=1):

        num_doctors = DOCTOR_DISTRIBUTION[department_name]

        for _ in range(num_doctors):

            rows.append({
                "DoctorID": doctor_id,
                "DoctorName": fake.name(),
                "DepartmentID": department_id,
                "ExperienceYears": random.randint(1, 30)
            })

            doctor_id += 1

    doctors = pd.DataFrame(rows)

    doctors.to_csv(
        RAW_DATA_PATH / "Dim_Doctor.csv",
        index=False
    )

    return doctors

def generate_patients():

    rows = []

    cities = [
        "Chennai",
        "Coimbatore",
        "Madurai",
        "Salem",
        "Trichy",
        "Vellore"
    ]

    for patient_id in range(1, NUM_PATIENTS + 1):

        dob = fake.date_of_birth(
            minimum_age=1,
            maximum_age=90
        )

        rows.append({

            "PatientID": patient_id,

            "DateOfBirth": dob,

            "Gender": random.choice(GENDERS),

            "Race": random.choice(RACES),

            "InsuranceType": random.choice(INSURANCE_TYPES),

            "City": random.choice(cities)

        })

    patients = pd.DataFrame(rows)

    patients.to_csv(
        RAW_DATA_PATH / "Dim_Patient.csv",
        index=False
    )

    return patients

def main():

    print("Generating Department Dimension...")
    generate_departments()

    print("Generating Shift Dimension...")
    generate_shifts()

    print("Generating Diagnosis Dimension...")
    generate_diagnosis()

    print("Generating Doctor Dimension...")
    generate_doctors()

    print("Generating Patient Dimension...")
    generate_patients()

    print("\nAll Dimension Tables Generated Successfully!")


if __name__ == "__main__":
    main()