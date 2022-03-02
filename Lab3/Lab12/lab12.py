l=['HTML','CSS','JS','ANGULAR']
with open(r"C:\Users\ADMIN\Desktop\lab\Python\Lab3\Lab12\test1.txt", "w") as myfile:
        for c in l:
                myfile.write("%s\n" % c)

content = open(r"C:\Users\ADMIN\Desktop\lab\Python\Lab3\Lab12\test1.txt")
print(content.read())
