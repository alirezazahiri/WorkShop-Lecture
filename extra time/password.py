# import random lib 

# use it to implement a simple random password generator

# our password can contain `a to z`, `A to Z` letters `0 to 9` digits and `@ # $ &` characters but no space allowed 

# get the length of password from user 8 <= length of password <= 32

# shuffle it as much as you can :)))

from random import shuffle, sample, choice

letters = list(range(ord('a'), ord('z')+1)) + list(range(ord('A'), ord('Z')+1))
letters = [chr(x) for x in letters]
characters = ['@', '#', '$', '&']
numbers = [str(x) for x in range(0, 10)]

master = letters + characters + numbers

length = int(input())

password = ''

for i in range(length):
    master = sample(master, len(master))
    password += choice(master)

print(password)
print(''.join(sample(list(password), length)))
