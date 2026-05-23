from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dic = defaultdict(list)

        for s in strs:
            dic[tuple(sorted(list(s)))].append(s)

        return list(dic.values())
