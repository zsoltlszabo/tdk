#!/usr/bin/python3

from math import sqrt

# Let's start by defining the function. We will request the list of states, their respective populations as tuples, and the number of representatives to assign as an integer.
def assign(list_of_states: tuple, list_of_populations: tuple, number_of_reps: int):
    # We will store the number of states in a variable.
    NUMBER_OF_STATES = len(list_of_states)
    # We will be working with indexes of states instead of the names. To do this, we will create a dictionary that will map the indexes to the names.
    STATE_KEYS = {i: list_of_states[i] for i in range(NUMBER_OF_STATES)}
    # We will be working with the states list. It contains the following data for each state: [0] population, [1] assigned representatives (every state starts with one)
    states = [[list_of_populations[i], 1] for i in range(NUMBER_OF_STATES)]
    # We will create a for loop which will be executed until all the representatives are assigned. As every state is assigned one representative at the start, we will only need to assign the remaining ones.
    for i in range(number_of_reps - NUMBER_OF_STATES):
        # We will create a list which will contain the populations multiplied with the correct values for the current iteration.
        current_multiplied_values = []
        # Next, we will create a for loop that multiplies every state with the correct multiplier.
        for k in states:
            current_multiplied_values.append(k[0] * (1 / sqrt(k[1] * (k[1] + 1))))
        # We will store the index of the state with the largest value after multiplication in a variable.
        current_max = current_multiplied_values.index(max(current_multiplied_values))
        # We will increase the number of representatives of the state with the largest value after multiplication by one.
        states[current_max][1] += 1 
    # We will create a dictionary, where we will store the solution.
    solution = {}
    # We will create a for loop that will be executed for every state.
    for i in range(NUMBER_OF_STATES):
        # We will add the state to the solution dictionary, with the number of representatives as the value.
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
    READ_LOCATION = 'input/eeach2011'
    # name (and location) of the file where we want to output the
    # apportionment (this will overwrite the file)
    WRITE_LOCATION = 'output/eea2011ch_huntington'
    NUMBER_OF_REPS = 705  # number of representatives to be assigned
    list_of_states, list_of_populations = read_data(READ_LOCATION)
    solution = assign(list_of_states, list_of_populations, NUMBER_OF_REPS)
    write_data(WRITE_LOCATION, solution)
    for k, v in solution.items():
        print(k, v)


if __name__ == '__main__':
    main()
