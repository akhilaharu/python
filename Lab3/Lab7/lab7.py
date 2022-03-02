with open(r"C:\Users\ADMIN\Desktop\lab\Python\Lab3\Lab7\test.txt") as f:
    l = f.readlines()
arr1=[]
for x in l:
    arr1.append(x.strip())
print(arr1)