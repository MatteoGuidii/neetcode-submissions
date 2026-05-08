class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        seen = set()
        for el in nums:
            if el in seen:
                return True
            seen.add(el)

        return False

# Time Complexity: O(n)
# Space Complexity: O(n)