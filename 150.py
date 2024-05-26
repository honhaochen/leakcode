from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[1])
        intervals.sort(key=lambda x: x[0])

        if len(intervals) <= 1:
            return intervals

        res = []
        l = intervals[0]
        for r in range(1, len(intervals)):
            if l[1] >= intervals[r][0] and l[0] <= intervals[r][1]:
                l = [l[0], max(intervals[r][1], l[1])]
            else:
                res.append(l)
                l = intervals[r]

            if r == len(intervals) - 1:
                res.append(l)

        return res


s = Solution()
a = s.merge(
    [[5, 5], [1, 2], [2, 4], [2, 3], [4, 4], [5, 5], [2, 3], [5, 6], [0, 0], [5, 6]]
)
print(a)
