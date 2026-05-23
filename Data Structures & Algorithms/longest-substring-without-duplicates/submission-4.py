class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        l = 0
        seen = set()
        max_len = 0
        
        for r in range(len(s)):
            # Keep removing from left until s[r] is not in seen
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            
            # Add current character to seen
            seen.add(s[r])
            
            # Update max length using actual window size
            max_len = max(max_len, len(seen))
        
        return max_len