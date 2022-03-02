with open(r"C:\Users\ADMIN\Desktop\lab\Python\Lab3\Lab14\test.txt") as fh1, open(r"C:\Users\ADMIN\Desktop\lab\Python\Lab3\Lab12\test1.txt") as fh2:
    for line1, line2 in zip(fh1, fh2):
        # line1 from abc.txt, line2 from test.txtg
        print(line1+line2)
		