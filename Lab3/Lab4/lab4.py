def read_lastnlines(fname,n):
	with open(r"C:\Users\ADMIN\Desktop\lab\Python\Lab3\Lab4\test.txt") as f:
		for line in (f.readlines() [-n:]):
			print(line)
n=input("Enter number of lines: ")
read_lastnlines(r"C:\Users\ADMIN\Desktop\lab\Python\Lab3\Lab4\test.txt",int(n))