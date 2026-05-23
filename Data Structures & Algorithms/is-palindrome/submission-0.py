class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.lower()
        s = ''.join(filter(lambda x: x.isalnum(), s))

        l = 0
        r = len(s) - 1

        while l < len(s):
            # print(f"{s[l]}:{s[r]}")
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True