from datetime import date
name = input("Enter name:")
age = input("Enter age:")
l=100-int(age)
year1=date.today().year+l
print("Hi " + name+"!You will turn 100 years old on "+str(year1)
)