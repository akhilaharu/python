def longest_words(filename):
    with open(filename, 'r') as infile:
        words = infile.read().split()
    max_len = len(max(words, key=len))
    return [word for word in words if len(word) == max_len]
print(longest_words(r"C:\Users\ADMIN\Desktop\lab\Python\Lab3\Lab8\test.txt"))