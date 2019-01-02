# Move all zeros present in the array to the end,
# and return the same array
# Example : [ 1, 9, 0, 8, 4, 0, 2, 0]
# Solution: [ 1, 9, 8, 4, 2, 0, 0, 0]

# We should apply the queue concept in order to solve this problem.

def move_zeros(array):
    index = 0
    last = len(array) - 1

    while index < last:
        if array[index] == 0:
            element = array[index]
            array.pop(index)
            array.append(element)

        index += 1

    print(array)


array = [0, 1, 9, 0, 8, 4, 0, 2, 0]

move_zeros(array)
