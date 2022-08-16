class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        h = {}
        i = 0
        for j in range(len(s)):
            if s[j] in h:
                i = max(i, h[s[j]])
            h[s[j]] = j + 1
            result = max(result, j - i + 1)
        return result