class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        pre = [1] * len(nums)
        post = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            pre[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            post[i] = postfix
            postfix *= nums[i]
        for i in range(len(nums)):
            ans[i] = pre[i] * post[i]
        return ans
        