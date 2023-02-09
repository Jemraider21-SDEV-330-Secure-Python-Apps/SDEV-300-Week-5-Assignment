"""Model for the Housing.csv file
"""


class Housing:
    """Model statistics for a house
    """

    def __init__(self, age: int, bedrooms: int, year_built: int,
                 num_units: int, rooms: int, weight: float, utility: float) -> None:
        self.age: int = age
        self.bedrooms: int = bedrooms
        self.year_build: int = year_built
        self.num_units: int = num_units
        self.rooms: int = rooms
        self.weight: float = weight
        self.utility: float = utility
