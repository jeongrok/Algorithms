class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = {}
        result = i = j = 0
        while j < len(s):
            if s[j] not in d:
                d[s[j]] = 1
            else:
                d[s[j]] += 1
            l = j - i + 1
            if l - max(d.values()) > k:
                d[s[i]] -= 1
                if d[s[i]] == 0:
                    del d[s[i]]
                i += 1
            else:
                result = max(result, l)
            j+= 1
        return result