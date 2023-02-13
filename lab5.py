"""Main file for the program. Displays statistics for certain subject
"""

from Utils.Functions.housing_functions import housing_menu
from Utils.Functions.popchange_functions import population_menu
from Utils.Models.housing import Housing
from Utils.Models.popchanges import PopChange
from Utils.Validation.validation import validate_is_int

HOUSES: list[Housing] = []
POPULATION_CHANGES: list[PopChange] = []


def create_arrays():
    """Read the files from the InputFiles directory and create models for these files.
    Store them in the necessary array for use.
    """
    housing_url = "./InputFiles/Housing.csv"
    popchanges_url = "./InputFiles/PopChange.csv"

    with open(housing_url, "r", encoding="utf-8") as file:
        for line in file.readlines()[1:]:
            line_contents: list[str] = line.split(",")
            HOUSES.append(Housing(
                int(line_contents[0]),  # age
                int(line_contents[1]),  # bedrooms
                int(line_contents[2]),  # year_build
                int(line_contents[3]),  # num_units
                int(line_contents[4]),  # rooms
                float(line_contents[5]),  # weight
                float(line_contents[6]),  # utility
            ))

    with open(popchanges_url, "r", encoding="utf-8") as file:
        for line in file.readlines()[1:]:
            line_contents: list[str] = line.split(",")
            POPULATION_CHANGES.append(PopChange(
                line_contents[0],  # pop_id
                line_contents[1],  # geography
                line_contents[2],  # target_geo_id1
                int(line_contents[3]),  # target_geo_id2
                int(line_contents[4]),  # april_1_pop
                int(line_contents[5])  # july_1_pop
            ))


def main_menu() -> int:
    """Generate the main menu and collect user choice

    Returns:
        int: User choice for main menu selection
    """
    print("Select the file you want to analyze:")
    print("1. Population Data")
    print("2. Housing Data")
    print("3. Exit the Program")
    looper: bool = True
    choice: int = 0
    while looper:
        choice = validate_is_int("Main Menu Choice")
        if choice not in range(1, 4):
            print("Wrong main menu input. Please try again")
        else:
            looper = False
    return choice


def main():
    """Main menu of the project.
    Prompt the user for selection and either display a menu or exit the program
    """
    create_arrays()
    looper: bool = True
    while looper:
        choice: int = main_menu()
        match choice:
            case 1:
                population_menu(POPULATION_CHANGES)
            case 2:
                housing_menu(HOUSES)
            case 3: looper = False
    print("\nGoodbye!")


if __name__ == "__main__":
    main()
