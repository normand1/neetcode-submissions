from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        keys = defaultdict(list) 
        for s in strs:
            keys[str(sorted(s))].append(s) 
        return [x for x in keys.values()]