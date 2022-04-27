# do binary search over the smaller array

class Solution(object):
    def findMedianSortedArrays(self, num1, num2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        A,B = num1,num2
        total = len(num1) + len(num2)
        half = total // 2
        
        if len(B)<len(A):
            A,B = B,A
        
        l,r = 0,len(A)-1
        
        while True:
            i = (l+r)//2
            j = half - i - 2
            
            Aleft = A[i] if i>= 0 else float("-inf")
            Aright = A[i+1] if(i+1) < len(A) else float("inf")
            Bleft = B[j] if j>= 0 else float("-inf")
            Bright = B[j+1] if(j+1) < len(B) else float("inf")
            
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright,Bright)
                return (max(Aleft,Bleft)+min(Aright,Bright))/2.
            elif Aleft > Bright:
                r = i-1
            else:
                l = i+1
                
        
        