# GET A LIST OF NUMBERS

# SORT THEM USING BUBBLESORT (use shorthand syntax for swapping elements)

# print it to the console

def bubbleSort(numbers: list) -> None:
    
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]

numbers = [int(x) for x in input().split()]
bubbleSort(numbers)
print(' '.join([str(x) for x in numbers]))

  