file = open(r"C:\Users\ADMIN\Desktop\lab\Python\Lab3\Lab9\test.txt","r")
Counter = 0
Content = file.read()
CoList = Content.split("\n")
for i in CoList:
	if i:
		Counter += 1
print("Count of lines in the file:")
print(Counter)
