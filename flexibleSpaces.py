"""
Incomplete: does not pass 

include links/methodology


solution one: 
create two lists of ints: https://stackoverflow.com/questions/19334374/python-converting-a-string-of-numbers-into-a-list-of-int

use some kind of function perhaps from library to generate all 
distinct pairs from 0 --> l1[0]: https://stackoverflow.com/questions/29745593/finding-differences-between-all-values-in-an-list
ALTERNATIVELY:  use a for loop and a 
nested for loop cal different between elements in list and append to 
another list. then use distinct elements function: https://stackoverflow.com/questions/12897374/get-unique-values-from-a-list-in-python

solution two:

"""

specs = input()
data = input()

specsList = [int(s) for s in specs.split()]
dataList = [int(s) for s in data.split()]
newDataList = [0]+dataList+[specsList[0]]

#print(newDataList)
i = list(set([abs(i-j) for i in newDataList for j in newDataList if i != j]))
#print(i)

print(', '.join(str(x) for x in i))
