"""
one solution:
create two lists for both inputs
for loop second list for first element of first list
if greater then second element of first list then end loop
print counter

another solution: 
use some kind of library and use less code iow: a short cut (standard library?)
"""


specs = input().split()
data = input().split()

specslist = list(map(int, specs))
datalist = list(map(int, data))

if datalist[0]==specslist[1]:
    print(1)
    sys.exit()

total = 0
reached = False

for i in range(len(datalist)):
    if i == len(datalist)-1 and total<specslist[1]:
        reached=True
    elif total <= specslist[1]:
        total+=datalist[i]
    else:
        counter = i-1
        print(counter)
        quit()

if reached:
    print(len(datalist))
else:
    print(i)
            
