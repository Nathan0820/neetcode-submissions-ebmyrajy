class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        window = defaultdict(int)
        need = Counter(s1)
        l, r = 0, 0
        valid = 0

        while r < len(s2):
            c = s2[r]
            r += 1
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1

            while r - l >= len(s1):
                if valid == len(need):
                    return True
                d = s2[l]
                l += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        return False

                