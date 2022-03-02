with open(r"C:\Users\ADMIN\Desktop\lab\Python\Lab3\Lab5\test.txt") as f:
    l = f.readlines()
l = [x.strip() for x in l]
print(l)