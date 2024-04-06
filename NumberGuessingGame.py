
import random 

a=input("Type number 1.")
a=int(a)
b=input("Type number 2.")
b=int(b)
n=random.randint(a,b)
x=n-1
i=0
while x!=n and i<5:
     i=i+1
     x=input("Guess a number")
     

if x==n:
     
     print("You won.")
else:
     print("You lost.")


