class Solution:
    def longestNiceSubstring(self, s: str) -> str:

        if len(s) < 2:
            return ""

        for i in range(len(s)):
            ch = s[i]

            if ch.swapcase() not in s:
                left = self.longestNiceSubstring(s[:i])
                right = self.longestNiceSubstring(s[i + 1:])

                if len(left) >= len(right):
                    return left
                else:
                    return right

        return s