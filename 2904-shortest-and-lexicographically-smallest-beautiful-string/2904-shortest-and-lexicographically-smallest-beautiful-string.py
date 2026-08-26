class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ans = ""
        for i in range(len(s)):
            ones = 0
            for j in range(i, len(s)):
                if s[j] == '1':
                    ones += 1
                if ones == k:
                    cur = s[i:j + 1]
                    if (ans == "" or
                        len(cur) < len(ans) or
                        (len(cur) == len(ans) and cur < ans)):
                        ans = cur
                    break
        return ans
        