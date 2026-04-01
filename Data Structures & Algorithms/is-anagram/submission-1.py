class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hs = {}
        for c in s:
            hs[c] = hs.get(c, 0) + 1
        for c in t:
            hs[c] = hs.get(c, 0) - 1
        for freq in hs.values():
            if freq != 0:
                return False
        return True
        