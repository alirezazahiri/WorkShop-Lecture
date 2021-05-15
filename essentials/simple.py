#TODO: guessing game

import random

number = random.randint(1, 1000)
print(number)
L = 1
R = 1000
attempts = 0

while L < R:
    
    attempts += 1
    mid = (L + R) // 2
    
    if number < mid:
        print('{} -> number is lower than {:>3}'.format(attempts, mid))
        R = mid
    
    elif number > mid:
        print('{} -> number is higher than {:>3}'.format(attempts, mid))
        L = mid
    
    else:
        print('{} -> so the number is {}'.format(attempts, mid))
        break

