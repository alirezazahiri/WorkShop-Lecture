#TODO: 1. odd or even
#       """
#       get a number and check if it's odd or even
#       """

# TYPE 1:
number = 21
if number % 2 == 0:
    print('is even')
if number % 2 != 0:
    print('is odd')

# TYPE 2:
number = 22
if number % 2 == 0:
    print('is even')
elif number % 2 != 0:
    print('is odd')

# TYPE 3:
number = 23 % 2 == 0 
if number:
    print('is even')
else:
    print('is odd')

#TODO: 2. multiple if, elif and else 
#       """
#       get a number in range of 1 to 10 guess what number is it 
#       without using any algorithm and no loops because we don't know about anything but flow statements
#       """
number = 9
if number == 10:
    print("it's a 10")
elif number == 9:
    print("it's a 9")
elif number == 8:
    print("it's a 8")
elif number == 7:
    print("it's a 7")
elif number == 6:
    print("it's a 6")
elif number == 5:
    print("it's a 5")
elif number == 4:
    print("it's a 4")
elif number == 3:
    print("it's a 3")
elif number == 2:
    print("it's a 2")
else:
    print("it's a 1")

# Done !