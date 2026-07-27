"""
=====================================================
Hospital Emergency Department Analytics
Configuration File
=====================================================

This file stores all project-level configuration values.
Modify this file instead of hardcoding values in other scripts.
"""

from pathlib import Path

# =====================================================
# PROJECT PATHS
# =====================================================

# Project Root Folder
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Data Folders
RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw"
CLEANED_DATA_PATH = PROJECT_ROOT / "data" / "cleaned"

# Create folders automatically if they don't exist
RAW_DATA_PATH.mkdir(parents=True, exist_ok=True)
CLEANED_DATA_PATH.mkdir(parents=True, exist_ok=True)

# =====================================================
# RANDOMNESS
# =====================================================

# Ensures the dataset is reproducible
RANDOM_SEED = 42

# =====================================================
# DATE RANGE
# =====================================================

START_DATE = "2024-01-01"
END_DATE = "2025-12-31"

# =====================================================
# DATASET SIZE
# =====================================================

NUM_PATIENTS = 6000
NUM_DOCTORS = 120
NUM_VISITS = 15000

NUM_DEPARTMENTS = 10
NUM_DIAGNOSES = 40
NUM_SHIFTS = 3

# =====================================================
# DEPARTMENTS
# =====================================================

DEPARTMENTS = [
    "Emergency Medicine",
    "Cardiology",
    "Neurology",
    "Orthopedics",
    "Pediatrics",
    "General Medicine",
    "General Surgery",
    "ICU",
    "ENT",
    "Radiology"
]

# =====================================================
# SHIFTS
# =====================================================

SHIFTS = {
    "Morning": ("06:00", "14:00"),
    "Evening": ("14:00", "22:00"),
    "Night": ("22:00", "06:00")
}

# =====================================================
# ARRIVAL MODES
# =====================================================

ARRIVAL_MODES = [
    "Walk-in",
    "Ambulance",
    "Referral"
]

# =====================================================
# TRIAGE LEVELS
# =====================================================

TRIAGE_LEVELS = [
    "Level 1",
    "Level 2",
    "Level 3",
    "Level 4",
    "Level 5"
]

# =====================================================
# INSURANCE TYPES
# =====================================================

INSURANCE_TYPES = [
    "Private",
    "Government",
    "Self-Pay"
]

# =====================================================
# GENDER VALUES
# =====================================================

GENDERS = [
    "Male",
    "Female"
]

# =====================================================
# RACE / ETHNICITY
# =====================================================

RACES = [
    "Asian",
    "Black",
    "White",
    "Hispanic",
    "Other"
]