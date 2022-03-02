def sum(n):
  if n < 1:
    return 0
  else:
    return n + sum(n - 2)
n=input("Enter a number: ")
result=sum(int(n))
print(result)
