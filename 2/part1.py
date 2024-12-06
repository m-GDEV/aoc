# Part 1
def check_increasing(report):
    last = int(report[0]) - 1
    for i in range(len(report)):
        if int(report[i]) - last >= 1 and int(report[i]) - last <= 3:
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

f = open("/home/user/aoc-day-2-input", "r")

reports = []
safe_sum = 0

for line in f:
    reports.append(line.replace("\n", "").split(" "))

    
    
for report in reports:
    inc = check_increasing(report)
    dec = check_decreasing(report)
    safe = inc or dec
    print(f"Report: {report} is increasing ({inc}), decreasing ({dec}), and safe ({safe})")
    if safe is True:
        safe_sum += 1
    
print(safe_sum)
    
f.close()