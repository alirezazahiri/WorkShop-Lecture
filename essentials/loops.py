#TODO: 1. print numbers
#        """
#        write a loop to iterate through 1 to 10
#        print numbers
#        """
print('1 ->')
for i in range(1, 11):
    print(i, end=' ')
print()
for i in range(1, 11, 1):
    print(i, end=' ')
print()
i = 1
while i <= 10:
    print(i, end=' ')
    i += 1

#TODO: 2. Print the pattern
# """
#     1 
#     1 2 
#     1 2 3 
#     1 2 3 4 
#     1 2 3 4 5
# """

print('\n\n2 ->')
print('for : ')
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=' ')
    print()

print('\nwhile : ')
i = 1
while i < 6:
    j = 1
    while j < i+1:
        print(j, end=' ')
        j += 1
    i += 1
    print()

