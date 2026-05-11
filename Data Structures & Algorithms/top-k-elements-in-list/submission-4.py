from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)

        for el in nums:
            dic[el] += 1

        max_el = heapq.nlargest(k, dic, key=dic.get)

        return max_el

# Time Complexity: O(n log k)
# Space Complexity: O(n + k)