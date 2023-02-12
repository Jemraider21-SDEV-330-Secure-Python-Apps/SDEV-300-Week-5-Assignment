"""Model for the Housing.csv file
"""
from dataclasses import dataclass


@dataclass
class Housing:
    """Model statistics for a house
    """
    age: int
    bedrooms: int
    year_build: int
    num_units: int
    rooms: int
    weight: float
    utility: float
