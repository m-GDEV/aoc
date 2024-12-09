# Part 1
import itertools
import re

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

endkey = "\t"

# Generic Methods
def get_local():
    f = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""

    s = f.split("\n")
    return s


def get_remote(path):
    f = open(path, "r")
    s = f.split("\n")
    del s[-1]
    return s

def print_with_color(text, color, endk=endkey):
    print(f"{color}{text}{bcolors.ENDC}", end=endk)

def print_list(list, append_val=""):
    for i in list:
        print(append_val, i)

def print_dict(dict):
    f = dict.items()

    for i in f:
        print(f"key: {i[0]}")
        print_list(i[1], "--> ") 

print

# Grid methods
def make_grid(s):
    g = []

    for i in s:
        mainList = []
        for j in i:
            mainList.append(j)
        
        g.append(mainList)

    return g

def print_grid(s):
    for colnum in range(len(s)):
        print_with_color(f"{colnum}", bcolors.HEADER)

    print()

    for i in range(len(s)):
        print_with_color(i, bcolors.HEADER, endk=" ")
        for j in range(len(s[i])):
            val = s[i][j]
            if val != ".":
                print_with_color(val, bcolors.FAIL)
            else:
                print(val, end=endkey)
        print("\n")

def find_value_in_grid(grid, value):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == value:
                return (i, j)
    
    return None

def find_occurences_of_value_in_grid(grid, value):
    occurences = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == value:
                occurences += 1
    
    return occurences

def find_all_antennas(grid):
    ants = {}

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            val = grid[i][j]
            if val != ".":
                obj = (i, j)

                list_of_ants = ants.get(val)
                if list_of_ants is None:
                    ants[val] = [ obj ]
                else:
                    list_of_ants.append(obj)
    return ants

# Logic
def main():

    s = get_local()
    g = make_grid(s)

    print_grid(g)

    l = find_all_antennas(g)
    print_dict(l)

main()
