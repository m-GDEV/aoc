# Part 1
f = open("/home/user/aoc-day1-input", "r")

ll = []
rl = []

for line in f:
    w = line.replace("   ", " ").split(" ")
    ll.append(int(w[0]))
    rl.append(int(w[1]))

lls = sorted(ll)
rls = sorted(rl)

# print(rls)

distances = []

for i in range(len(lls)):
    l = lls[i]
    r = rls[i]
    d = abs(r - l)
    distances.append(d)
#     print(f"lls: {l}, rls: {r}, distance: {d}")


sum = 0
for num in distances:
    sum += num
    
print(sum)
    
f.close()