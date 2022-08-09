# 229. Majority Element II

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums1 = None
        nums2 = None
        count1 = 0
        count2 = 0
        
        for num in nums:
            if num == nums1:
                count1+=1
            elif num == nums2:
                count2+=1
            elif count1==0:
                nums1 = num
                count1=1
            elif count2 == 0:
                nums2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        
        count1 = 0
        count2 = 0
        ans = []
        for num in nums:
            if num == nums1:
                count1+=1
            if num == nums2:
                count2+=1
        
        
        if count1 > len(nums)//3:
            ans.append(nums1)
        if count2 > len(nums)//3:
            ans.append(nums2)
        
        return ans
        
       