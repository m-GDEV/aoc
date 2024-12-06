# Part 2
f = open("/home/user/aoc-day1-input", "r")

ll = []
rl = {}

for line in f:
    w = line.replace("   ", " ").split(" ")
    ll.append(int(w[0]))
    
    r = int(w[1])
    res = rl.get(r)
    if res == None: 
        rl[r] = 1
    else: 
        rl[r] = res + 1
            


lls = sorted(ll)
# rls = sorted(rl)

# print(rls)

sim_score = 0

for i in range(len(lls)):
    l = lls[i]
    
    mul = rl.get(l, 0)
    sim_score += (mul * l)
    
print(sim_score)
    
f.close()