class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s = 0
        e = len(numbers) - 1

        while s < e:
            sum = numbers[s] + numbers[e]
            if sum == target:
                return [s + 1, e + 1] #1-indexed
            elif sum < target:
                s += 1
            else:
                e -= 1
        
        return []
        