"""Model the PopChange.csv file
"""
from dataclasses import dataclass


@dataclass
class PopChange:
    """Model for tracking population changes
    """
    pop_id: str
    geography: str
    target_geo_id1: str
    target_geo_id2: int
    april_1_pop: int
    july_1_pop: int
