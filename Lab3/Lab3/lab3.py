file1 = open(r"C:\Users\ADMIN\Desktop\lab\Python\Lab3\Lab3\test.txt", "a")  
file1.write("\n End of File \n")
file1.close()
file1 = open(r"C:\Users\ADMIN\Desktop\lab\Python\Lab3\Lab3\test.txt", "r")
print(file1.read())
print()
file1.close()