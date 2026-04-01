class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = set()
        l = 0
        length = 0

        for r in range(len(s)):
            while s[r] in freq:
                freq.remove(s[l])
                l += 1
            freq.add(s[r])
            length = max(length, r - l + 1)
        return length 