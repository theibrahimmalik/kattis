"""
This solution passes on kattis but not flexibleSpaces1.py? Even though when tested on an ide they get the same output. Why is this? 
"""

width, n = [int(x) for x in input().split()]
partitions = [int(x) for x in input().split()] + [width]

spaces = set()
for data in partitions:
    spaces.add(data)
    for data2 in partitions:
        if data == data2:
            break
        spaces.add(abs(data-data2))
        
print(" ".join(str(x) for x in sorted(spaces)))
