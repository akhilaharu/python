with open(r"C:\Users\ADMIN\Desktop\lab\Python\Lab3\Lab6\test.txt") as f:
    l = f.readlines()
combined=""
for x in l:
    combined+= x.strip()
print(combined)