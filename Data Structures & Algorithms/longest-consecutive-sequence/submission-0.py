class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0
        for num in nums:
            if (num - 1) not in s:
                ans = 1
                while (num + ans) in s:
                    ans += 1
                longest = max(longest, ans)
        return longest