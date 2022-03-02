import random
r=random.randrange(1, 10,)
gnumber=int(input("Guess the number!:"))
print("random number is:"+str(r))
if(gnumber<r):
    print("Your guess is too low")
elif(gnumber>r):
    print("Your guess is too high")
elif(gnumber==r):
    print("Your guess is right")