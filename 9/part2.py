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

class File:
    def __init__(self, Id, Len):
        self.id = Id
        self.Moved = False
        self.len = Len

class EmptyBlock:
    def __init__(self, Length):
        self.len = Length

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

def print_list(list, append_val="", endk="\n"):
    for i in list:
        print(i, end=endk)
    print()

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
        fileLen = int(map[i])
        empty_space_len = int(map[i+1])

        res.append(File(id, fileLen))

        res.append(EmptyBlock(empty_space_len))  

        id += 1

    # Must account for final file that does not have space after it
    fileLen = int(map[len(map) - 1])
    res.append(File(id, fileLen))

    return res 

def print_disk_map(map):
    for i in map:
        if isinstance(i, File):
            for j in range(i.len):
                print(i.id, end="")
        if isinstance(i, EmptyBlock):
            for k in range(i.len):
                print(".", end="")
    
    print()

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


def get_last_block(l, start_index):
    if len(l) < 1:
        return -1
    
    og_char = l[-1]
    start_index = -1
    size_of_file = 0

    # allows for custom start index so caller can choose not to repeat
    for i in range(start_index, 0, -1):
        if l[i] != og_char:
            break
        else:
            size_of_file += 1
            start_index = i

    # File: (id, size, where this file starts in the list)
    return (og_char, size_of_file, start_index)

def find_x_len_block(l, len):
    block = "." * len
    try:
        l.index(block)
    except:
        return -1

def replace_block_with_file(l, fileChar, fileSize, fileIndex, blockIndex):
    fIndex = fileIndex
    bIndex = blockIndex
    for i in range(fileSize):
        l[bIndex] = fileChar
        bIndex += 1
    
    for i in range(fileSize):
        l[fIndex] = "."
        fIndex += 1

def move_block2(m):
    last_block = get_last_block(m, len(m) - 1)

    while last_block != -1:
        og_char = last_block[0]
        file_size = last_block[1]
        file_start_index = last_block[2]
        li = find_x_len_block(m, file_size)

        if li != -1:
            replace_block_with_file(m, og_char, file_size, file_start_index, li)

        last_block = get_last_block(m, file_start_index)

# Logic
def main():

    # s = get_remote(9)
    # s = get_local()
    # s = "12345"
    # s = "1010101010101010101010"
    s = "2333133121414131402"
    f = expand_disk_map(s)
    print_disk_map(f)
    # get_last_block(f)
    # b = move_blocks(f) 
    # b = move_block2(f)
    # c = calculate_checksum(b) 

    # print("\n\nOriginal:", s)
    # print("Expanded: ", end="")
    # print_list(f, endk="")
    # print("Blocks Moved: ", end="")
    # print_list(b, endk="")
    # print(f"Code: {c}")


main()
