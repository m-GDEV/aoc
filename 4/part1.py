# Part 1 - holy shit why was this so hard
import re

def transpose(s):
    t = {}
    
    for i in range(len(s)):
        for j in range(len(s[i])):
            t[str(j)] = t.get(str(j), "") + s[i][j]

    return t

def find_horizontal_forward(f):
    return len(re.findall("XMAS", f))
    
def find_horizontal_backward(f):
    return len(re.findall("SAMX", f))

def find_horizontal(f):
    return find_horizontal_forward(f) + find_horizontal_backward(f)


# Use hash map and transform each column into a string 
# Then search that string for XMAS or SAMX
def find_vertical(s):
    down_count = 0
    t = transpose(s)
    
    for key in t:
        down_count += find_horizontal(t[key])
    
    return down_count


def find_diagonal_left(s):
    diag_count = 0
    l = []

    # Start at first row and first col
    for i in range(len(s)):
        for j in range(len(s[i])):
            if i + 3 >= len(s) or j + 3 >= len(s[i]):
                continue
            else:
                substr = ""
                substr += s[i][j]
                substr += s[i+1][j+1]
                substr += s[i+2][j+2]
                substr += s[i+3][j+3]
                l.append(substr)

                diag_count += find_horizontal(substr)

    # print(f"left diagonal substrs: {l}")
    return diag_count

def find_diagonal_right(s):
    diag_count = 0
    l = []

    # Start at first row and last col
    for i in range(len(s)):
        for j in range(len(s[i]) - 1, 0, -1):
            if i + 3 >= len(s) or j - 3 < 0:
                continue
            else:
                substr = ""
                substr += s[i][j]
                substr += s[i+1][j-1]
                substr += s[i+2][j-2]
                substr += s[i+3][j-3]
                l.append(substr)

                diag_count += find_horizontal(substr)

    # print(f"right diagonal substrs: {l}")
    return diag_count

def find_diagonal(s):
    l = find_diagonal_left(s)
    r = find_diagonal_right(s)
    print(f"diag | left: {l}, right: {r}")
    return find_diagonal_left(s) + find_diagonal_right(s)


def get_local():
    return """....XXMAS.
.SAMXMS...
...S..A...
..A.A.MS.X
XMASAMX.MM
X.....XA.A
S.S.S.S.SS
.A.A.A.A.A
..M.M.M.MM
.X.X.XMASX"""

def get_remote():
    f = open("/home/user/aoc-day-4-input", "r")
    f = f.read()
    return f

f = get_remote()
s = f.split("\n")
# remove extra newline at end
del s[-1]

h = find_horizontal(f)
v = find_vertical(s)
d = find_diagonal(s)


print(f"{h=}, {v=}, {d=} = {h+v+d}")
# print(v)

# for line in s:
#     print(line)