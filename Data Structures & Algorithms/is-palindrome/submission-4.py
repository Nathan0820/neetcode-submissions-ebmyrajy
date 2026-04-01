class Solution:
    def isPalindrome(self, s: str) -> bool:

        def is_alpha(s):
            return (ord('A') <= ord(s) <= ord('Z') or
                    ord('a') <= ord(s) <= ord('z') or
                    ord('0') <= ord(s) <= ord('9'))

        left = 0
        right = len(s) - 1
        s = s.lower()

        while left < right:
            while not is_alpha(s[left]) and left < right:
                left += 1
            while not is_alpha(s[right]) and right > left:
                right -= 1
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True