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
    f = open("./7/input", "r")
    return f.read()


def eval_left_to_right(s):
    n1 = re.match('(\\d+)', s)
    n1 = n1.groups()[0]
    total = int(n1)
    s = s.removeprefix(str(n1))

    op = "x"

    while op != None:

        op = re.match("(\\*|\\+|\\>)", s)
        if op is None:
            continue
        op = op.groups()[0]
        s = s.removeprefix(str(op))

        n2 = re.match('(\\d+)', s)
        n2 = n2.groups()[0]
        s = s.removeprefix(str(n2))

        if op == ">":
            total = int(str(total) + n2)
        else:
            total = eval(str(total) + op + n2) 

    return total

# Logic
def main():

    f = get_remote()

    s = f.split("\n")
    del s[-1]

    # Gather Info
    info = []
    for i in s:
        sp = i.split(":")
        target = sp[0]
        nums = sp[1].split(" ")
        nums.pop(0)
        info.append((target, nums))


    # Main stuff
    final = 0
    final_count = 0

    # Iterate through all lines in input
    for i in info:
        completed = False 

        target = int(i[0])
        nums = i[1]
        l = len(nums) - 1

        # thrid operator is meant to be '||' but i use > 
        combs = itertools.product('+*>', repeat=l)
        ll = list(combs)

        # Iterate through all combinations of operators placed in between nums
        for comb in ll:
            if completed is True:
                break
            eval_str = ""

            # Create string that inserts operators into numbers
            for k in range(len(nums)):
                eval_str += nums[k]
                if k != len(nums) - 1:
                    eval_str += comb[k]

            # Evaluate expression left to right
            res = eval_left_to_right(eval_str)
            if res == target:
                final += res
                completed = True
                final_count += 1
                # print(f"Result is True: {target=} | {res=} = {eval_str}")
                print(f"{final_count} True Expressions")
            else:
                pass
                # print(f"Result is False: {target=} | {res=} = {eval_str}")
    
    print(final)

main()
