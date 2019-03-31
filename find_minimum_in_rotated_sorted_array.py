"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2]
Output: 1
Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0

"""


class Solution(object):
    def findMin(self, nums):
        """
        Strategy is to use binary search.
        For a given element, if the previous value is greater than it, the current element must be the minimum.
        If the current element is not the minimum value to find the next range to search check
        1. If current element is greater than or equal to left value and greater than right value
           then minimum value must be on right side. The GTE for left value is to handle case for two values
           where first value is > second value but minimum index calculation rounds down (to 0).
        2. Else minimum value is on left side
        :type nums: List[int]
        :rtype: int
        """
        if nums is None:
            return 0

        if len(nums) == 1:
            return nums[0]

        start_index = 0
        end_index = len(nums) - 1

        while start_index < end_index:
            middle_index = (start_index + end_index) // 2
            start_value = nums[start_index]
            end_value = nums[end_index]
            middle_value = nums[middle_index]

            if middle_index >= 1:
                previous_index = middle_index - 1
                previous_value = nums[previous_index]
                if previous_value > middle_value:
                    return middle_value

            if middle_value >= start_value and middle_value > end_value:
                start_index = middle_index + 1
            else:
                end_index = middle_index - 1

        return nums[start_index]
