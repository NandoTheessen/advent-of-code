from sys import argv
from itertools import cycle

def readfile(filename):
    array = []
    file = open(filename, "r")
    for x in file:
        array.append(int(x.strip()))
    return array

def determine_frequency_sum(array):
    cache = {}
    frequency = 0
    for x in array:
        frequency += x
        if frequency in cache:
            return frequency
        else:
            cache[frequency] = 1
    

def main(filename):
    array = readfile(filename)
    print(determine_frequency_sum(array))

if __name__ == '__main__':
    if len(argv) == 2:
        filename = argv[1]
        main(filename)
    else:
        print("Usage: python solution.py [filename]")