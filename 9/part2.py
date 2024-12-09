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

    def __str__(self):
        return f"FILE: {self.id=}, {self.len=}, {self.Moved=}"

class EmptyBlock:
    def __init__(self, Length):
        self.len = Length
    def __str__(self):
        return f"BLOCK: {self.len=}"

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
        if empty_space_len != 0:
            res.append(EmptyBlock(empty_space_len))  

        id += 1

    # Must account for final file that does not have space after it
    fileLen = int(map[len(map) - 1])
    res.append(File(id, fileLen))

    return res 

def disk_map_to_str(map, sep=""):
    map_str = ""
    for i in map:
        if isinstance(i, File):
            for j in range(i.len):
                map_str += str(i.id)
        if isinstance(i, EmptyBlock):
            for k in range(i.len):
                map_str += "."
            
        map_str += sep
        
    return map_str
    
def print_disk_map(map, sep=""):
    print(disk_map_to_str(map, sep))

@line_profiler.profile
def find_in_list(l, val):
    try:
        return l.index(val)
    except:
        return -1


@line_profiler.profile
def calculate_checksum(map):
    sum = 0
    pos = 0

    for i in map:
        if isinstance(i, File):
            for j in range(i.len):
                sum += (i.id * pos)
                pos += 1
        if isinstance(i, EmptyBlock):
            pos += i.len

    return sum

def swap_block_and_file(l, block: EmptyBlock, file: File):
    if isinstance(block, EmptyBlock) is False:
        raise Exception("Wtf are you doing")
    if isinstance(file, File) is False:
        raise Exception("Wtf are you doing")

    blockIndex = l.index(block)
    fileIndex = l.index(file)

    l[blockIndex], l[fileIndex] = l[fileIndex], EmptyBlock(file.len)

    if block.len > file.len:
        l.insert(blockIndex+1, EmptyBlock(block.len - file.len))
        return True

    return False

def find_empty_block(l, len, end_index):
    for i in range(0, end_index):
        val = l[i]
        if isinstance(val, EmptyBlock):
            if val.len >= len:
                return val
    
    return None

def move_blocks(map):
    l = map.copy()

    i = len(l) - 1
    while i != 0:
        val = l[i]
        # print(f"index: {i}, {val}")
        if isinstance(val, File):
           if val.Moved is False:
            block = find_empty_block(l, val.len, i)
            if block != None:
                res = swap_block_and_file(l, block, val)
                if res is True: 
                    i += 1
                val.Moved = True
        # print_disk_map(l)

        i -= 1
        
    return l

# Logic
def main():

    s = get_remote(9)
    # s = get_local()
    # s = "12345"
    # s = "1010101010101010101010"
    # s = "2333133121414131402"
    f = expand_disk_map(s)
    print_disk_map(f)
    b = move_blocks(f)
    print_disk_map(b)
    # get_last_block(f)
    # b = move_blocks(f) 
    # b = move_block2(f)
    c = calculate_checksum(b) 

    print("\n\nOriginal:", s)
    print("Expanded: ", end="")
    print_disk_map(f)
    print("Blocks Moved: ", end="")
    print_disk_map(b)
    print(f"Code: {c}")


main()
