# GET A LIST OF NUMBERS

#TODO: MAP THEM TO THEIR SQUARED
#TODO: SHOW THE EVEN NUMBERS ONLY
#TODO: SHOW THE PRIME NUMBERS ONLY

numbers = list(map(int, input().split()))

print('\nsquare: ')
print(list(map(lambda x: x**2, numbers)))
print([x**2 for x in numbers])

print('\neven: ')
print(list(filter(lambda x: x%2==0, numbers)))
print([x for x in numbers if x%2==0])

print('\nprime: ')
def isPrime(number):
    
    if 2 <= number <= 3:
        return True
    
    if number % 2 == 0:
        return False
    
    for i in range(3, number // 2):
        if number % i == 0:
            return False
    
    return True

print(list(filter(lambda x: isPrime(x), numbers)))
print([x for x in numbers if isPrime(x)])