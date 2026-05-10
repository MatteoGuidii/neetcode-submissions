from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)

        for words in strs:
            word = "".join(sorted(words)) #sorted is (nlogn)
            seen[word].append(words)

        return list(seen.values())

# Time Complexity: 
# - sorting one word: k log k
# - Doing that for all n words: O(n · k log k)

# Space Complexity: O(n · k) — you're storing all the words in seen 
# (the keys total ~n·k characters across all entries, 
# and the values hold all n original strings).