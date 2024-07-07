from typing import List


class Solution:

    MAP = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"],
    }

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        result = []
        for d in list(digits):
            to_add = self.MAP[d]
            if len(result) == 0:
                result = to_add
                continue

            new_result = []
            for r in result:
                for t in to_add:
                    new_result.append(r + t)

            del result
            result = new_result

        return result


s = Solution()
a = s.letterCombinations("23")
print(a)
