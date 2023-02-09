"""Model the PopChange.csv file
"""


class PopChange:
    """Model for tracking population changes
    """

    def __init__(self, id: str, geography: str,
                 target_geo_id1: str, target_geo_id2: int,
                 april_1_pop: int, july_1_pop: int) -> None:
        self.id: str = id
        self.geography: str = geography
        self.target_geo_id1: str = target_geo_id1
        self.target_geo_id2: int = target_geo_id2
        self.april_1_pop: int = april_1_pop
        self.july_1_pop: int = july_1_pop
