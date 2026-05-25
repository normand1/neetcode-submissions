class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = "" 
        for s in strs:
            encoded = encoded + str(len(s)) + "#" + s                                   
        return encoded 

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            s_len = int(s[i:j])
            end = j + 1 + s_len
            res.append(s[j + 1 : end])
            i = end 
        return res