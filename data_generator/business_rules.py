"""
=====================================================
Hospital Emergency Department Analytics
Business Rules
=====================================================

Contains all business logic used for synthetic
data generation.
"""

# =====================================================
# PATIENT ARRIVAL DISTRIBUTION
# =====================================================

SHIFT_PROBABILITY = {
    "Morning": 0.30,
    "Evening": 0.50,
    "Night": 0.20
}

# =====================================================
# ARRIVAL MODE DISTRIBUTION
# =====================================================

ARRIVAL_MODE_PROBABILITY = {
    "Walk-in": 0.70,
    "Ambulance": 0.20,
    "Referral": 0.10
}

# =====================================================
# TRIAGE DISTRIBUTION
# =====================================================

TRIAGE_PROBABILITY = {
    "Level 1": 0.05,
    "Level 2": 0.15,
    "Level 3": 0.35,
    "Level 4": 0.30,
    "Level 5": 0.15
}

# =====================================================
# WAIT TIME (Minutes)
# =====================================================

WAIT_TIME = {
    "Level 1": (0, 10),
    "Level 2": (10, 20),
    "Level 3": (20, 45),
    "Level 4": (45, 90),
    "Level 5": (60, 150)
}

# =====================================================
# TREATMENT TIME (Minutes)
# =====================================================

TREATMENT_TIME = {
    "Emergency Medicine": (20, 60),
    "Cardiology": (60, 180),
    "Neurology": (120, 300),
    "Orthopedics": (90, 240),
    "Pediatrics": (30, 90),
    "General Medicine": (30, 120),
    "General Surgery": (90, 240),
    "ICU": (180, 720),
    "ENT": (20, 60),
    "Radiology": (15, 45)
}

# =====================================================
# ADMISSION PROBABILITY
# =====================================================

ADMISSION_PROBABILITY = {
    "Level 1": 0.95,
    "Level 2": 0.80,
    "Level 3": 0.50,
    "Level 4": 0.20,
    "Level 5": 0.05
}

# =====================================================
# SATISFACTION SCORE
# =====================================================

SATISFACTION_SCORE = {
    "Excellent": (4.5, 5.0),
    "Good": (3.5, 4.4),
    "Average": (2.5, 3.4),
    "Poor": (1.0, 2.4)
}