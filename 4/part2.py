# Part 2 - pretty easy
import re

def pattern_exists(f):
    l = len(re.findall("MAS", f))
    l2 = len(re.findall("SAM", f))
    if l == 1 or l2 == 1:
        return True
    elif l > 1 or l2 > 1:
        raise Exception("wtf is happening?")
    
    return False

def find_xmas(s):
    xmas_count = 0

    # Start at first row and last col
    for i in range(len(s)):
        for j in range(len(s[i])):
            if i + 2 >= len(s) or j + 2 >= len(s[i]):
                continue
            else:
                mas1 = ""
                mas2 = ""
                
                mas1 += s[i][j]
                mas1 += s[i+1][j+1]
                mas1 += s[i+2][j+2]

                mas2 += s[i][j+2]
                mas2 += s[i+1][j+1]
                mas2 += s[i+2][j]

                mas1_exist = pattern_exists(mas1)
                mas2_exist = pattern_exists(mas2)

                if mas1_exist and mas2_exist:
                    xmas_count += 1
                    

    # print(f"right diagonal substrs: {l}")
    return xmas_count

def get_local():
    return """.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
.........."""

def get_remote():
    f = open("C:\\Users\\musa\\Downloads\\input4", "r")
    f = f.read()
    return f

f = get_remote()
s = f.split("\n")
# remove extra newline at end
del s[-1]

x = find_xmas(s)

print(f"{x=}")
# print(v)

# for line in s:
#     print(line)