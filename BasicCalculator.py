def add(x,y):

    return x+y

def subtract(x,y):
    return x-y
def multiply(x,y):
   return x*y
def divide (x,y):

    return x/y

print("1.Add")
print('2.Subtract')
print('3.Multiply')
print('4.Divide')

while True:
    n=''
    try:
        n=int(input("Please select 1/2/3/4 for one of the four options above."))
        x1=float(input("Type in your first number."))
        x2=float(input("Type in your second number."))
        type(x1)#this finds the data type of variable x1.
    except  ValueError:
        print("Not a valid input. Try again")
        continue
        
     
    if n==1 :
        print (add(x1,x2))
    if n==2 :
        print (subtract(x1,x2))
    if n==3 :
        print (multiply(x1,x2))
    if n==4 :
        print (divide(x1,x2))
    
    x= input("Do you want to calculate another value? Type in Y/N for yes or no.")
    if x.lower()=='n':
        break

