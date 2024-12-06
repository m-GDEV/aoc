# Part 1
import math

def num_before_num(list, num1, num2):
    n1_index = -55
    n2_index = -55
    for i in range(len(list)):
        if list[i] == num1:
            n1_index = i
        if list[i] == num2:
            n2_index = i

    if n1_index == -55 or n2_index == -55:
        raise Exception("One of the numbers is not in the list")

    if n1_index < n2_index:
        return True
    else:
        return False
    
def nums_in_list(list, n1, n2):
    n1_f = False
    n2_f = False

    for num in list:
        if num == n1:
            n1_f = True
        if num == n2:
            n2_f = True
        
    return n1_f and n2_f


def is_update_valid(rules, update):
    checked_rules = []

    for r in rules:
        exists = nums_in_list(up, r[0], r[1])
        
        if exists is True:
            valid = num_before_num(up, r[0], r[1])
            checked_rules.append(valid)

    if not False in checked_rules:
        valid_rules.append(up)


def get_local():
    return """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

def get_remote():
    f = open("C:\\Users\\musa\\Downloads\\input5", "r")
    return f.read()

f = get_local()
s = f.split("\n\n")

ss = s[0].split("\n")

rules = []

for i in range(len(ss)):
    rules_found = ss[i].split("|")
    f = (rules_found[0], rules_found[1])
    rules.append(f)

u = s[1].split("\n")

updates = []

for i in range(len(u)):
    ups = u[i].split(",")
    updates.append(ups)
# del updates[-1]

print("RULES:")
for i in rules:
    print(i)

print("\n\nUPDATES:")
for i in updates:
    print(i)

valid_rules = []

for up in updates:
    valid = is_update_valid(rules, up);
    if valid is True: 
        valid_rules.append(up)


print("\n\nVALID RULES:")
for i in valid_rules:
    print(i)


middles = []
total_sum = 0

for i in valid_rules:
    middles.append(i[math.floor(len(i)/2)])

for n in middles:
    total_sum += int(n)

print("\n\nMIDDLEs:")
print(middles)

print("\n\nTOTAL SUM:")
print(total_sum)