class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, el in enumerate(nums):
            comp = target - el
            if comp in seen:
                return [seen[comp], i]
            
            seen[el] = i