class Solution:
    def topKFrequent(self, nums, k):
        hs = defaultdict(int)
        result = []
        for num in nums:
            hs[num] += 1
        
        for i in range(k):
            maximum = max(hs, key = hs.get)
            result.append(maximum)
            del hs[maximum]

        return result
        