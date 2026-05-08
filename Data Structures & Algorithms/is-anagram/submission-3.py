from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Store them in a dic
        # Compare the dic
        dic1 = defaultdict(int)
        dic2 = defaultdict(int)

        for el in s:
            dic1[el] += 1

        for el in t:
            dic2[el] += 1

        return dic1.items() == dic2.items()