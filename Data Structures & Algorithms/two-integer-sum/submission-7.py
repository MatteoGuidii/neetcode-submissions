class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            complem = target - num
            if complem in seen:
                return [seen[complem], i]
        
            seen[num] = i

# 0: 3
# compl = 7 - 4 = 3
# 3 in seen? Yes -> return 3, in position seen[complem] and i