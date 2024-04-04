for i in range(1,101):
    if  i%15==0:
        print(str(i)+": Fizz Buzz")
    elif i%5!=0 and i%3==0:
        print(str(i)+": Fizz")
    elif i%5==0 and i%3!=0:
        print(str(i)+": Buzz")
    else:
    
      print(str(i)+": NA")