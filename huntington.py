#!/usr/bin/python3

from math import sqrt


def assign(list_of_states: tuple, list_of_populations: tuple, number_of_reps: int):
    # Declaring variables
    NUMBER_OF_STATES = len(list_of_states)
    # contains the indexes belonging to each state
    STATE_KEYS = {i: list_of_states[i] for i in range(NUMBER_OF_STATES)}
    # We will be working with the states list. It contains the following data for each state:
    # [0] population
    # [1] assigned representatives (every state starts with one)
    states = [[list_of_populations[i], 1] for i in range(NUMBER_OF_STATES)]
    for i in range(number_of_reps - NUMBER_OF_STATES):
        current_multiplied_values = [] # contains the populations multiplied with the correct values for the current iteration
        for k in states:  # multiplying each state's population with the correct number
            current_multiplied_values.append(k[0] * (1 / sqrt(k[1] * (k[1] + 1))))
        current_max = current_multiplied_values.index(max(current_multiplied_values)) # the index of the greatest value after multiplication
        states[current_max][1] += 1  # increment the number of representatives
    solution = {}
    for i in range(NUMBER_OF_STATES):
        solution.update({STATE_KEYS.get(i): states[i][1]})
    return solution


# Function importing the data from a text file
def read_data(location: str):
    f = open(location, 'r')
    list_of_states, list_of_populations = [], []
    for i in f:
        current = list(i.split())
        list_of_states.append(current[0])
        list_of_populations.append(int(current[1]))
    f.close()
    return tuple(list_of_states), tuple(list_of_populations)


# Function writing the data to a text file
def write_data(location: str, data: dict):
    f = open(location, 'w')
    for k, v in data.items():
        print(k, v, file=f)
    f.close()


def main():
    # name (and location) of the file containing the states and the populations
    READ_LOCATION = 'census2010'
    # name (and location) of the file where we want to output the
    # apportionment (this will overwrite the file)
    WRITE_LOCATION = '2010house'
    NUMBER_OF_REPS = 435  # number of representatives to be assigned
    list_of_states, list_of_populations = read_data(READ_LOCATION)
    solution = assign(list_of_states, list_of_populations, NUMBER_OF_REPS)
    write_data(WRITE_LOCATION, solution)
    for k, v in solution.items():
        print(k, v)


if __name__ == '__main__':
    main()
