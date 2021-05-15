# TODO: input types 

string = 'hello' #input() # python's default input() type is `str`
print(string, type(string))

i_number = 10 #int(input()) # `int`
print(i_number, type(i_number))

f_number = 10.0 # float(input()) # `float`
print(f_number, type(f_number))

print()

# list(map(int, input().split()))
i_list = list(map(int, '10 20 30 40 50 60'.split())) 
print(i_list, '\n')

# list(map(float, input().split()))
f_list = list(map(float, '10.0 20.5 30.12 40.5 50.6165 60.0'.split())) 
print(f_list, '\n')

# list(map(str, input().split())) or simply use input().split()
s_list = 'hello how are you'.split() 
print(s_list, '\n')

# how to define a linear array with size of n
n = 10 # int(input())
array = [None] * n
print('array:', *array)

# how to define a matrix with size of n * m

# int(input())
n = 3  # row
# int(input())
m = 2  # column
matrix = [([None] * m) for _ in range(n)]

print('matrix:')
for line in matrix:
    print(*line)
