from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set(list("qwertyuiop"))
        row2 = set(list("asdfghjkl"))
        row3 = set(list("zxcvbnm"))

        res = []
        for w in words:
            w_set = set(list(w.lower()))
            if (
                len(w_set & row1) == len(w_set)
                or len(w_set & row2) == len(w_set)
                or len(w_set & row3) == len(w_set)
            ):
                res.append(w)

        return res


s = Solution()
a = s.findWords(["Hello", "Alaska", "Dad", "Peace"])
print(a)
