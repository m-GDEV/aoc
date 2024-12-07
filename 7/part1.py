# Part 1

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

# Methods
def print_with_color(text, color, endk=endkey):
    print(f"{color}{text}{bcolors.ENDC}", end=endk)

def get_local():
    return """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""

def get_remote():
    f = open("/home/musa/aoc/6/input", "r")
    return f.read()


# Logic

math_ops = ["+","*"]

def main():
    f = get_local()

    s = f.split("\n")
    #  del s[-1]

    info = []
    for i in s:
        sp = i.split(":")
        target = sp[0]
        nums = sp[1].split(" ")
        nums.pop(0)

        info.append((target, nums))

    for i in info:
        print(i)



    for i in info:
        print(f"Target: {info[0]}")

        if len(info[1]) == 2:
            for m in math_ops:
                left = i[1][0]
                right = i[1][1]
                res = eval(left + m + right)
                print(f"Operator: {m}, {res=}")

main()
