"""Functionality to display the menu for population changes
"""
from Utils.Functions.statistics import data_statistics
from Utils.Validation.validation import validate_is_int
from Utils.Models.housing import Housing


def housing_menu(houses: list[Housing]):
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
    for house in houses:
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
            case 1: data_statistics(ages, titles[0])
            case 2: data_statistics(bedroom_counts, titles[1])
            case 3: data_statistics(built_year_data, titles[2])
            case 4: data_statistics(rooms_counts, titles[3])
            case 5: data_statistics(utility_data, titles[4])
            case 6: menu_looper = False
    print("Leaving the Houses Menu\n")
