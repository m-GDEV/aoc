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
    f = "2333133121414131402"

    return f

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


# Logic
def main():

    s = get_local()
    g = make_grid(s)

    print_grid(g)

    l = find_all_antennas(g)
    print_dict(l)

main()
