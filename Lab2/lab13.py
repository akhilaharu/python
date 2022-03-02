l=[1,2,3,4,5,6,7,8]
lists = [[]]
for i in range(len(l) + 1):
    for j in range(i):
        lists.append(l[j: i])
print(lists)