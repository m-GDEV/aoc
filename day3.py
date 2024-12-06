# Part 2
import math
import itertools

# Helper functions
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
        exists = nums_in_list(update, r[0], r[1])
        
        if exists is True:
            valid = num_before_num(update, r[0], r[1])
            checked_rules.append((valid, r))

    for cr in checked_rules:
        if cr[0] is False:
            return [cr for cr in checked_rules if cr[0] == False]
    
    return True

def put_n1_before_n2_in_list(list, n1, n2):
    # throws exception is not found, good
    n1_index = list.index(n1)    
    n2_index = list.index(n2)

    if (n1 == '55' and n2 == '29'):
        pass

    list.pop(n1_index)

    if n2_index -1 < 0:
        list.insert(0, n1)
    else:
        list.insert(n2_index, n1)
    print(f"Rule: {n1, n2}: {list}")

def make_invalid_update_valid(rules, update: list[str]):
    valid_version = sorted(update.copy())
    for r in rules:
        exists = nums_in_list(valid_version, r[0], r[1])
        if exists:
            num_before = num_before_num(valid_version, r[0], r[1])
            if num_before is not True:
                put_n1_before_n2_in_list(valid_version, r[0], r[1])
            else:
                print(f"Rule: {r[0], r[1]}, skipping...")

    return valid_version


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

f = get_remote()

# Parse Input
s = f.split("\n\n")

ss = s[0].split("\n")

rules = []

for i in range(len(ss)):
    rules_found = ss[i].split("|")
    f = (rules_found[0], rules_found[1])
    rules.append(f)

rules.sort(key=lambda rule: rule[0])  

u = s[1].split("\n")

updates = []

for i in range(len(u)):
    ups = u[i].split(",")
    updates.append(ups)
del updates[-1] # remove newline at EOF


# Operations 
valid_updates = []
invalid_updates = []
invalid_made_valid = []

for up in updates:
    valid = is_update_valid(rules, up)

    if valid is True: 
        valid_updates.append(up)
    else:
        invalid_updates.append(up)

        valid_v = make_invalid_update_valid(rules, up)
        invalid_made_valid.append(valid_v)

        if is_update_valid(rules,valid_v) is False:
            raise Exception("fml")


middles = []
total_sum = 0

for i in invalid_made_valid:
    middles.append(i[math.floor(len(i)/2)])

for n in middles:
    total_sum += int(n)

print("\n\nMIDDLEs:")
print(middles)

print("\n\nTOTAL SUM:")
print(total_sum)