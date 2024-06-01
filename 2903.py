from typing import List


class Solution:
    def findIndices(
        self, nums: List[int], indexDifference: int, valueDifference: int
    ) -> List[int]:
        min_index = 0
        max_index = 0
        for i in range(indexDifference, len(nums)):
            if nums[i - indexDifference] < nums[min_index]:
                min_index = i - indexDifference
            if nums[i - indexDifference] > nums[max_index]:
                max_index = i - indexDifference
            if abs(nums[i] - nums[min_index]) >= valueDifference:
                return [i, min_index]
            if abs(nums[max_index] - nums[i]) >= valueDifference:
                return [i, max_index]
        return [-1, -1]


s = Solution()
a = s.findIndices([5, 1, 4, 1], 2, 4)
print(a)
