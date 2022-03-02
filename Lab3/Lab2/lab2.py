def file_read_from_head(fname, nlines):
        from itertools import islice
        with open(fname) as f:
                for line in islice(f, nlines):
                        print(line)
n=input("Enter number of lines: ")
file_read_from_head(r"C:\Users\ADMIN\Desktop\lab\Python\Lab3\Lab2\test.txt",int(n))
