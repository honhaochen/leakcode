from typing import List


class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words_set = set(wordDict)
        dp = [[] for _ in range(len(s) + 1)]
        dp[0] = [""]
        for i in range(1, len(s) + 1):
            for j in range(i):
                if s[j:i] in words_set:
                    for w in dp[j]:
                        dp[i].append((w + " " + s[j:i]).strip())
        return dp[-1]


s = Solution()
a = s.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"])
print(a)
