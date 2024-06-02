from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        area = 0
        while l < r:
            h = min(height[l], height[r])
            w = r - l
            area = max(area, h * w)

            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return area


s = Solution()
a = s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
print(a)
