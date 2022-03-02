import itertools
from itertools import permutations
x=['a','e','i','o','u']
y=list(permutations(x,len(x)))
str=""
for i in range(len(y)):
    for j in range(0,5):
        str=str+y[i][j]
    print(str)
    str=""
