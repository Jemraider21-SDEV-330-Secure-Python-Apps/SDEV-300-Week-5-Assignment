"""Functionality to display the menu for population changes
"""
from Utils.Functions.statistics import data_statistics
from Utils.Validation.validation import validate_is_int
from Utils.Models.popchanges import PopChange


def population_menu(pop_changes: list[PopChange]):
    """Menu function for population analysis.
    Captures user input and displays information based on selection
    """
    menu_looper: bool = True
    april_population: list = []
    july_population: list = []
    change_population: list = []
    for pop_data in pop_changes:
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
                data_statistics(april_population, titles[0])
            case 2:
                data_statistics(july_population, titles[1])
            case 3: data_statistics(change_population, titles[2])
            case 4: menu_looper = False
    print("Leaving the Population Menu\n")
