from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []

        if numRows == 1:
            return [[1]]

        result = [[1], [1, 1]]
        for i in range(2, numRows):
            row = [1]
            for j in range(len(result[i - 1]) - 1):
                row.append(result[i - 1][j] + result[i - 1][j + 1])

            row.append(1)
            result.append(row)

        return result


s = Solution()
a = s.generate(5)
print(a)
