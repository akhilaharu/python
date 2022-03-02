def remove_newlines(fname):
    flist = open(fname).readlines()
    return [s.rstrip('\n') for s in flist]

print(remove_newlines(r"C:\Users\ADMIN\Desktop\lab\Python\Lab3\Lab16\test.txt"))
