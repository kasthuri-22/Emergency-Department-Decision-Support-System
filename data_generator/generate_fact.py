"""
=====================================================
Hospital Emergency Department Analytics
Generate Fact Table
=====================================================
"""

import random
from datetime import datetime, timedelta

import numpy as np
import pandas as pd

from config import (
    RANDOM_SEED,
    NUM_VISITS,
    START_DATE,
    END_DATE,
    RAW_DATA_PATH
)

from business_rules import (
    SHIFT_PROBABILITY,
    ARRIVAL_MODE_PROBABILITY,
    TRIAGE_PROBABILITY,
    WAIT_TIME,
    TREATMENT_TIME,
    ADMISSION_PROBABILITY
)

random.seed(RANDOM_SEED)
np.random.seed(RANDOM_SEED)

# Load Dimension Tables

patients = pd.read_csv(RAW_DATA_PATH / "Dim_Patient.csv")

doctors = pd.read_csv(RAW_DATA_PATH / "Dim_Doctor.csv")

departments = pd.read_csv(RAW_DATA_PATH / "Dim_Department.csv")

diagnosis = pd.read_csv(RAW_DATA_PATH / "Dim_Diagnosis.csv")

shifts = pd.read_csv(RAW_DATA_PATH / "Dim_Shift.csv")

def generate_visit_date():

    start = datetime.strptime(START_DATE, "%Y-%m-%d")
    end = datetime.strptime(END_DATE, "%Y-%m-%d")

    random_days = random.randint(
        0,
        (end - start).days
    )

    return start + timedelta(days=random_days)


def generate_shift():

    return random.choices(
        population=list(SHIFT_PROBABILITY.keys()),
        weights=list(SHIFT_PROBABILITY.values()),
        k=1
    )[0]

def generate_arrival_time(visit_date, shift):

    if shift == "Morning":

        hour = random.randint(6, 13)

    elif shift == "Evening":

        hour = random.randint(14, 21)

    else:

        hour = random.choice([22,23,0,1,2,3,4,5])

    minute = random.randint(0,59)

    arrival = visit_date.replace(
        hour=hour,
        minute=minute,
        second=0
    )

    if hour <= 5:
        arrival += timedelta(days=1)

    return arrival

def generate_arrival_mode():

    return random.choices(
        population=list(ARRIVAL_MODE_PROBABILITY.keys()),
        weights=list(ARRIVAL_MODE_PROBABILITY.values()),
        k=1
    )[0]

def generate_triage():

    return random.choices(
        population=list(TRIAGE_PROBABILITY.keys()),
        weights=list(TRIAGE_PROBABILITY.values()),
        k=1
    )[0]

def generate_wait_time(triage):

    min_wait, max_wait = WAIT_TIME[triage]

    return random.randint(min_wait, max_wait)

def generate_treatment_time(department_name):

    min_time, max_time = TREATMENT_TIME[department_name]

    return random.randint(min_time, max_time)

def generate_satisfaction(wait_minutes):

    if wait_minutes <= 15:

        return round(random.uniform(4.5,5.0),1)

    elif wait_minutes <=45:

        return round(random.uniform(3.5,4.4),1)

    elif wait_minutes <=90:

        return round(random.uniform(2.5,3.4),1)

    else:

        return round(random.uniform(1.0,2.4),1)


def generate_admission(triage):

    probability = ADMISSION_PROBABILITY[triage]

    return random.random() < probability

DEPARTMENT_DIAGNOSIS = {
    "Emergency Medicine": [7, 11, 16, 29, 31, 36],
    "Cardiology": [1, 2, 21, 22],
    "Neurology": [3, 4, 23, 32],
    "Orthopedics": [5, 6, 24, 25, 33, 34],
    "Pediatrics": [37, 38, 39],
    "General Medicine": [8, 9, 12, 13, 17, 19, 20, 26, 30],
    "General Surgery": [10, 28, 35],
    "ICU": [18, 40],
    "ENT": [14, 15, 27],
    "Radiology": [36]
}

def generate_visit(visit_id):

    # -----------------------------
    # Random Patient
    # -----------------------------
    patient = patients.sample(1).iloc[0]

    # -----------------------------
    # Random Doctor
    # -----------------------------
    doctor = doctors.sample(1).iloc[0]

    department_id = doctor["DepartmentID"]

    department_name = departments.loc[
        departments["DepartmentID"] == department_id,
        "DepartmentName"
    ].iloc[0]

    # -----------------------------
    # Diagnosis
    # -----------------------------
    diagnosis_id = random.choice(
        DEPARTMENT_DIAGNOSIS[department_name]
    )

    # -----------------------------
    # Date & Time
    # -----------------------------
    visit_date = generate_visit_date()

    shift = generate_shift()

    arrival_time = generate_arrival_time(
        visit_date,
        shift
    )

    shift_id = shifts.loc[
        shifts["ShiftName"] == shift,
        "ShiftID"
    ].iloc[0]

    # -----------------------------
    # Clinical Information
    # -----------------------------
    arrival_mode = generate_arrival_mode()

    triage = generate_triage()

    wait_minutes = generate_wait_time(triage)

    treatment_minutes = generate_treatment_time(
        department_name
    )

    seen_time = arrival_time + timedelta(
        minutes=wait_minutes
    )

    discharge_time = seen_time + timedelta(
        minutes=treatment_minutes
    )

    length_of_stay = wait_minutes + treatment_minutes

    satisfaction = generate_satisfaction(
        wait_minutes
    )

    admitted = generate_admission(
        triage
    )

    return {

        "VisitID": visit_id,

        "PatientID": patient["PatientID"],

        "DoctorID": doctor["DoctorID"],

        "DepartmentID": department_id,

        "DiagnosisID": diagnosis_id,

        "ShiftID": shift_id,

        "VisitDate": visit_date.date(),

        "ArrivalTime": arrival_time,

        "SeenTime": seen_time,

        "DischargeTime": discharge_time,

        "WaitMinutes": wait_minutes,

        "TreatmentMinutes": treatment_minutes,

        "LengthOfStay": length_of_stay,

        "SatisfactionScore": satisfaction,

        "AdmissionFlag": admitted,

        "ArrivalMode": arrival_mode,

        "TriageLevel": triage

    }

def generate_fact_table():

    visits = []

    for visit_id in range(1, NUM_VISITS + 1):

        visits.append(
            generate_visit(visit_id)
        )

    fact = pd.DataFrame(visits)

    fact.to_csv(
        RAW_DATA_PATH / "Fact_EmergencyVisit.csv",
        index=False
    )

    return fact

def main():

    print("Generating Fact Table...")

    generate_fact_table()

    print("\nFact Table Generated Successfully!")

if __name__ == "__main__":
    main()



