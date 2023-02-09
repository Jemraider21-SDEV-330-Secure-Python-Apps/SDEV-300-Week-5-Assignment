from Models.housing import Housing
from Models.popchanges import PopChange


HOUSES: list[Housing] = []
POPULATION_CHANGES: list[PopChange] = []


def create_arrays():
    """Read the files from the InputFiles directory and create models for these files.
    Store them in the necessary array for use.
    Note: This may not be used. The handling of each file might appear in their own function
    """
    housing_url = "./InputFiles/Housing.csv"
    popchanges_url = "./InputFiles/PopChange.csv"

    housing_file = open(housing_url, "r")
    for line in housing_file.readlines()[1:]:
        line_contents: list[str] = line.split(",")
        age: int = int(line_contents[0])
        bedrooms: int = int(line_contents[1])
        year_build: int = int(line_contents[2])
        num_units: int = int(line_contents[3])
        rooms: int = int(line_contents[4])
        weight: float = float(line_contents[5])
        utility: float = float(line_contents[6])
        HOUSES.append(Housing(age, bedrooms, year_build,
                              num_units, rooms, weight, utility))
    housing_file.close()
    print(f'Housing has {len(HOUSES)} entries')

    popchanges_file = open(popchanges_url, "r")
    for line in popchanges_file.readlines()[1:]:
        line_contents: list[str] = line.split(",")
        id: str = line_contents[0]
        geography: str = line_contents[1]
        target_geo_id1: str = line_contents[2]
        target_geo_id2: int = int(line_contents[3])
        april_1_pop: int = int(line_contents[4])
        july_1_pop: int = int(line_contents[5])
        POPULATION_CHANGES.append(PopChange(
            id, geography, target_geo_id1, target_geo_id2, april_1_pop, july_1_pop))
    popchanges_file.close()
    print(f'PopChanges has {len(POPULATION_CHANGES)} entries')


create_arrays()
