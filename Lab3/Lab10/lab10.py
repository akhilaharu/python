from collections import Counter
def word_count(fname):
        with open(fname) as f:
                return Counter(f.read().split())
print(word_count(r"C:\Users\ADMIN\Desktop\lab\Python\Lab3\Lab10\test.txt"))
