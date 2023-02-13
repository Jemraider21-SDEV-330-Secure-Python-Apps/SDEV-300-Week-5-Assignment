"""Functionality to display the statistics of a list
"""
import numpy as np
import matplotlib.pyplot as plt


def data_statistics(data: list, title: str):
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
