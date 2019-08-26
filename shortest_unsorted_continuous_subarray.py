class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        Find start and end indices starting from beginning and end of index that are not increasing or equal.

        Then need to include any values to left of start or right of end that should be included / won't be sorted after
        a swap.

        Do this by comparing values against min and max values in range of start and end and incrementing respective
        index until at end of array.
        
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2: return 0
        
        l, r = 0, len(nums) - 1
        
        while l < len(nums) - 1 and nums[l] <= nums[l + 1]:
            l += 1
        
        while r > 0 and nums[r] >= nums[r -1]:
            r -= 1
            
        if l > r:
            return 0
            
        temp = nums[l:r+1]
        tempMin = min(temp)
        tempMax = max(temp)
        
        while l > 0 and tempMin < nums[l-1]:
            l -= 1
        
        while r < len(nums) - 1 and tempMax > nums[r+1]:
            r += 1
            
        return r - l + 1