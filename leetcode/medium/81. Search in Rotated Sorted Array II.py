class Solution:
    def search(self, nums: List[int], keyToSearch: int) -> int:
        low = 0
        high = len(nums)-1
        found = False

        while low<=high:
                
            mid = (low+high)//2
                
            if nums[mid] == keyToSearch:
                found = True

            isKeyInRight = nums[mid] <= keyToSearch and keyToSearch <= nums[high]
            isKeyInLeft = nums[low] <= keyToSearch and keyToSearch <= nums[mid]

            if nums[mid] > nums[low]: 
                if isKeyInLeft:
                    high = mid-1
                else:
                    low = mid+1
            elif nums[low] > nums[mid]:
                if isKeyInRight:
                    low = mid+1
                else:
                    high = mid-1
            else:
                low+=1

        return found