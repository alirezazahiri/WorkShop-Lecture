#TODO: make title
    #   """
    #   given a string, you should make it title;
    #   1 < len(string) < 1000
    #   example :
    #   helLoWoRLd -> Helloworld
    #   """
print('non-pythonic way : ')
string = 'helLoWoRLd' # input()
string = list(string)
string[0] = string[0].upper()

for i in range(1, len(string)):
    string[i] = string[i].lower()

print(''.join(string))

# or do it more like a python programmer
print('pythonic way:')
string = 'helLoWoRLd' # input()
print(string[0].upper() + string[1:].lower())

#TODO: count items
    #   """
    #   given a string, you should count alphabets, numbers and non-alpha-num characters 
    #   example: 
    #   2(*8ffsidfu03 -> 7 4 2
    #   """
print()
string = '2(*8ffsidfu03' # input()
alphas, nums, other = 0, 0, 0

for i in range(len(string)):
    if string[i].isalpha():
        alphas += 1
    elif string[i].isnumeric():
        nums += 1
    else:
        other += 1

print(alphas, nums, other)
