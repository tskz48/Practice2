
x=input("Please type in a word")
x1=x.lower()
x2=x.upper()
y=''
for i in range (0,len(x)):
    
    if x[i]==x1[i]:
        y=y+x2[i]
       
    else:
        y=y+x1[i]
print(y)



