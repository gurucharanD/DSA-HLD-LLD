# We rotate an ascending order sorted array at some point unknown to user. So for instance, 3 4 5 6 7 might become 5 6 7 3 4. Modify binary search algorithm to find an element in the rotated array in O(log n) time and O(1) Space complexity

# nums = [4,5,6,7,0,1,2], target = 0
# nums = [4,5,6,7,0,1,2], target = 3
# nums = [1], target = 0

input = [4, 5, 6, 7, 0, 1, 2]
rotations = 0
keyToSearch = 2

for i in range(0, rotations):
    lastElement = input[len(input) - 1]
    for j in range(len(input) - 1, 0, -1):
        input[j] = input[j - 1]
    input[0] = lastElement

print(input)

low = 0
high = len(input) - 1
found = False

while low <= high:
    mid = (low + high) // 2

    if input[mid] == keyToSearch:
        print([mid, input[mid]])
        found = True
        break

    isRightSorted = input[mid] <= input[high]
    isLeftSorted = input[mid] >= input[low]

    isKeyInRight = input[mid] <= keyToSearch and keyToSearch <= input[high]
    isKeyInLeft = input[low] <= keyToSearch and keyToSearch <= input[mid]

    if isLeftSorted:
        if isKeyInLeft:
            high = mid - 1
        else:
            low = mid + 1

    if isRightSorted:
        if isKeyInRight:
            low = mid + 1
        else:
            high = mid - 1


print(-1) if found == False else print([mid, input[mid]])


class Solution(object):
    def search(self, input, keyToSearch):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(input) - 1
        found = False

        while low <= high:
            mid = (low + high) // 2

            if input[mid] == keyToSearch:
                print([mid, input[mid]])
                found = True
                break

            isRightSorted = input[mid] <= input[high]
            isLeftSorted = input[mid] >= input[low]

            isKeyInRight = input[mid] <= keyToSearch and keyToSearch <= input[high]
            isKeyInLeft = input[low] <= keyToSearch and keyToSearch <= input[mid]

            if isLeftSorted:
                if isKeyInLeft:
                    high = mid - 1
                else:
                    low = mid + 1

            if isRightSorted:
                if isKeyInRight:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1 if found == False else mid
