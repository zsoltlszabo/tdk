#!/usr/bin/python3

from math import sqrt

# Let's start by defining the function. We will request the list of states, their respective populations as tuples, and the number of representatives to assign as an integer.
def assign(list_of_states: tuple, list_of_populations: tuple, number_of_reps: int):
    # We will store the number of states in a variable.
    NUMBER_OF_STATES = len(list_of_states)
    # We will be working with indexes of states instead of the names. To do this, we will create a dictionary that will map the indexes to the names.
    STATE_KEYS = {i: list_of_states[i] for i in range(NUMBER_OF_STATES)}
    # We will be working with the states list. It contains the following data for each state: [0] population, [1] assigned representatives (every state starts with six)
    states = [[list_of_populations[i], 6] for i in range(NUMBER_OF_STATES)]
    # We will create a for loop which will be executed until all the representatives are assigned. As every state is assigned six representative at the start, we will only need to assign the remaining ones.
    for i in range(number_of_reps - NUMBER_OF_STATES * 6):
        # We will create a list which will contain the populations multiplied with the correct values for the current iteration.
        current_multiplied_values = []
        # Next, we will create a for loop that multiplies every state with the correct multiplier.
        for k in states:
            current_multiplied_values.append(k[0] / (k[1] + 1 / 2))
        # This while loop will check if a certain member state has reached the maximum amount of seats.
        while True:
            # We will store the index of the state with the largest value after multiplication in a variable.
            current_max = current_multiplied_values.index(max(current_multiplied_values))
            # If the state with the largest value already has 96 representatives, the value will be decreased to zero, thus putting the state at the end of the list.
            if states[current_max][1] == 96:
                current_multiplied_values[current_max] = 0
            # If the state has fewer than 96 representatives, we will increase the number of representatives by one.
            else:
                states[current_max][1] += 1
                break
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
    f = open('location', 'r')
    for i, v in enumerate(f):
        if i == 0:
            READ_LOCATION = v.strip()
        if i == 1:
            WRITE_LOCATION = v.strip() + '_arithmetic_degressive'
        if i == 2:
            NUMBER_OF_REPS = int(v.strip())
    f.close()
    list_of_states, list_of_populations = read_data(READ_LOCATION)
    solution = assign(list_of_states, list_of_populations, NUMBER_OF_REPS)
    write_data(WRITE_LOCATION, solution)
    for k, v in solution.items():
        print(k, v)


if __name__ == '__main__':
    main()
