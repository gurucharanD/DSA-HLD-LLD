
# We rotate an ascending order sorted array at some point unknown to user. So for instance, 3 4 5 6 7 might become 5 6 7 3 4. Modify binary search algorithm to find an element in the rotated array in O(log n) time and O(1) Space complexity


input = [3,4,5,6,7]
rotations = 3

for i in range(0,rotations):
    lastElement = input[len(input)-1]
    for j in range( len(input)-1, 0, -1 ):
        input[j] = input[j-1]
    input[0] = lastElement
    print(input)


# print(input)
