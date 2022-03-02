def isPalindrome(s):
    return s == s[::-1]
str=input("Enter string: ")
ans = isPalindrome(str)
if ans:
    print("Entered string is a Palindrome")
else:
    print("Entered string is not Palindrome")