from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]

        if rowIndex == 1:
            return [1, 1]

        prev = [1, 1]
        i = 2
        while i <= rowIndex:
            res = [1]
            for j in range(len(prev) - 1):
                res.append(prev[j] + prev[j + 1])
            res.append(1)

            if i == rowIndex:
                return res

            prev = res
            i += 1


s = Solution()
a = s.getRow(3)
print(a)
