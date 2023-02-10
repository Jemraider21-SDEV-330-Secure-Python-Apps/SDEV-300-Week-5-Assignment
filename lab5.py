from Utils.Models.housing import Housing
from Utils.Models.popchanges import PopChange
from Utils.Validation.validation import validate_is_int
import numpy as np
import matplotlib.pyplot as plt


HOUSES: list[Housing] = []
POPULATION_CHANGES: list[PopChange] = []


def create_arrays():
    """Read the files from the InputFiles directory and create models for these files.
    Store them in the necessary array for use.
    """
    housing_url = "./InputFiles/Housing.csv"
    popchanges_url = "./InputFiles/PopChange.csv"

    housing_file = open(housing_url, "r", encoding="utf-8")
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

    popchanges_file = open(popchanges_url, "r", encoding="utf-8")
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


def math(data: list, title: str):
    """Calculates the statistics of a data set and displays the histrogram

    Args:
        data (list): dataset to be used
        title (str): Description of dataset (ex: population as of 2020)
    """
    print(f'\nDisplaying information for {title}')
    print("The statistics for this column are:")
    print(f'Count: {len(data)}')
    print(f'Mean: {np.mean(data)}')
    print(f'Standard Deviation: {np.std(data)}')
    print(f'Min: {np.min(data)}')
    print(f'Max: {np.max(data)}')
    plt.hist(np.histogram(data))
    plt.title(title)
    plt.show()


def population_menu():
    """Menu function for population analysis.
    Captures user input and displays information based on selection
    """
    menu_looper: bool = True
    april_population: list = []
    july_population: list = []
    change_population: list = []
    for pop_data in POPULATION_CHANGES:
        april_population.append(pop_data.april_1_pop)
        july_population.append(pop_data.july_1_pop)
        change_population.append(
            abs(pop_data.april_1_pop - pop_data.july_1_pop))
    titles: list = ["Population as of April 1",
                    "Population as of July 1", "Change In Population"]
    while menu_looper:
        print("\nPopulation Menu")
        print("Select the column you want to analyze:")
        for menu_num, title in enumerate(titles):
            print(f'{menu_num + 1}. {title}')
        print("4. Return to Main Menu")
        choice_looper: bool = True
        choice: int = 0
        while choice_looper:
            choice = validate_is_int("Population Menu Choice")
            if choice not in range(1, 5):
                print("Invalid population menu choice. Please try again")
            else:
                choice_looper = False
        match choice:
            case 1:
                math(april_population, titles[0])
            case 2:
                math(july_population, titles[1])
            case 3: math(change_population, titles[2])
            case 4: menu_looper = False
    print("Leaving the Population Menu\n")


def housing_menu():
    """Menu function for housing analysis.
    Captures user input and displays information based on selection
    """
    titles: list = ["House Ages", "Number of Bedrooms",
                    "Year Built", "Number of Rooms", "Utilities"]
    ages: list = []
    bedroom_counts: list = []
    built_year_data: list = []
    rooms_counts: list = []
    utility_data: list = []
    for house in HOUSES:
        ages.append(house.age)
        bedroom_counts.append(house.bedrooms)
        built_year_data.append(house.year_build)
        rooms_counts.append(house.rooms)
        utility_data.append(house.utility)
    menu_looper = True
    while menu_looper:
        print("\nHouses Menu")
        print("Select the column you want to analyze:")
        for menu_num, title in enumerate(titles):
            print(f'{menu_num + 1}. {title}')
        print("6. Return to Main Menu")
        choice: int = 0
        choice_looper: bool = True
        while choice_looper:
            choice = validate_is_int("Houses Menu Choice")
            if choice not in range(1, 7):
                print("Invalid houses menu choice. Please try again")
            else:
                choice_looper = False
        match choice:
            case 1: math(ages, titles[0])
            case 2: math(bedroom_counts, titles[1])
            case 3: math(built_year_data, titles[2])
            case 4: math(rooms_counts, titles[3])
            case 5: math(utility_data, titles[4])
            case 6: menu_looper = False
    print("Leaving the Houses Menu\n")


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
                population_menu()
            case 2:
                housing_menu()
            case 3: looper = False
    print("\nGoodbye!")


if __name__ == "__main__":
    main()
