from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)

        for words in strs:
            word = "".join(sorted(words))
            seen[word].append(words)

        return list(seen.values())
            