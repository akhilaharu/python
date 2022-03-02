with open(r"C:\Users\ADMIN\Desktop\lab\Python\Lab3\Lab13\test.txt",'r') as firstfile, open(r"C:\Users\ADMIN\Desktop\lab\Python\Lab3\Lab13\test1                                                                                                           .txt",'a') as secondfile:
	for line in firstfile:
			secondfile.write(line)
