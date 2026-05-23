from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = r = 0
        max_count = 0
        counter = Counter()

        while r < len(s):

            counter[s[r]] += 1

            while len(s[l:r+1]) - max(counter.values()) > k:
                counter[s[l]] -= 1
                l += 1
            
            max_count = max(max_count, len(s[l:r+1]))
            r += 1

        return max_count


