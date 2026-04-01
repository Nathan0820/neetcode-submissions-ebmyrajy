class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window = defaultdict(int)
        need = Counter(t)
        l, r = 0, 0
        start = 0
        valid = 0
        length = float('inf')

        while r < len(s):
            c = s[r]
            r += 1
            
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1
            
            while valid == len(need):
                if r - l < length:
                    start = l
                    length = r - l
                d = s[l]
                l += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        return "" if length == float('inf') else s[start:start + length]
