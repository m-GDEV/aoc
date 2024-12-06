# Part 2 Final

# reports = [[7,6, 4,2,1], [1,2,7,8,9], [9,7,6,2,1], [1,3,2,4,5], [8,6,4,4,1], [1,3,6,7,9]]
# reports = [[1,3,2,4,5], [8,6,4,4,1], [1,3,6,7,9]]


f = open("/home/user/aoc-day-2-input", "r")

reports = []

for line in f:
    reports.append(line.replace("\n", "").split(" "))

def check_increasing(report):
    last = int(report[0]) - 1
    for i in range(len(report)):
        intr = int(report[i])
        dif = intr - last
#         print(f"intr {intr}, dif {dif}, last {last}")
        if dif >= 1 and dif <= 3:
            last = int(report[i])
        else:
            return False

    return True


def check_decreasing(report):
    last = int(report[0]) + 1
    for i in range(len(report)):
        if last - int(report[i]) >= 1 and last - int(report[i]) <= 3:
            last = int(report[i])
        else:
            return False

    return True

ss = 0

# Brute force 
# 1. For each list, go through each variation where you remove on element
# 2. Then just do the same thing as step one for that sub list
# 3. Tally results
for r in reports:
#     print(r)
    rsl = []
    for i in range(len(r)):
        ns = r.copy()
        ns.pop(i)
#         print(ns)
        
        inc = check_increasing(ns)
        dec = check_decreasing(ns)
        safe = inc or dec
        
        rsl.append(safe)
        
#         print(f"inc: {inc}, dec: {dec}, safe: {safe}")
        
    
    if True in rsl:
        print(f"{r} is safe")
        ss += 1
    else:
        print(f"{r} is unsafe")
    
print(f"{ss} safe levels")