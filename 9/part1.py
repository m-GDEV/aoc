# Part 1
import itertools
import re
import line_profiler

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

@line_profiler.profile
def get_remote(day):
    f = open(f"./{day}/input", "r") 
    f = f.read()
    s = f.split("\n")
    del s[-1]
    return s[0]

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

@line_profiler.profile
def expand_disk_map(map):
    # if len(map) % 2 != 0:
    #     raise Exception("Length of map needs to be divisible by 2")

    res = []

    id = 0 

    for i in range(0, len(map) - 1, 2):
        n1 = int(map[i])
        n2 = int(map[i+1])

        for i in range(n1):
            res.append(id)
        
        for i in range(n2):
            res.append(".")

        id += 1

    n1 = int(map[len(map) - 1])
    for i in range(n1):
        res.append(id)

    return res 

@line_profiler.profile
def find_in_list(l, val):
    try:
        return l.index(val)
    except:
        return -1

@line_profiler.profile
def move_blocks(map):
    m = list(map)
    emptyPlace = find_in_list(m, ".")

    while emptyPlace != -1:
        m[emptyPlace] = m[-1]
        del m[-1]

        emptyPlace = find_in_list(m, ".")
    
    return m

@line_profiler.profile
def calculate_checksum(map):
    id = 0
    sum = 0

    for i in range(len(map)):
        sum += (id * int(map[i]))
        id += 1
    
    return sum

# Logic
def main():

    s = get_remote(9)
    # s = get_local()
    # s = "1010101010101010101010"
    f = expand_disk_map(s)
    b = move_blocks(f) 
    c = calculate_checksum(b) 

    print(f)
    print(b)
    print(f"\n\nCode: {c}")


main()
