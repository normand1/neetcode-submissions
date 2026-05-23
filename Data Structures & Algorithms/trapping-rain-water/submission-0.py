class Solution:
    def trap(self, height: List[int]) -> int:
        
        max_h_l = []
        max_h_r = []
        res = 0

        curr_max = 0
        for i in range(len(height)):
            h = height[i - 1] if i > 0 else 0
            curr_max = max(curr_max, h)
            max_h_l.append(curr_max)
        
        curr_max = 0
        for i in range(len(height) - 1, -1, -1):
            h = height[i + 1] if i + 1 < len(height) else 0
            curr_max = max(curr_max, h)
            max_h_r.insert(0, curr_max)
        
        for i in range(len(height)):
            min_h = min(max_h_l[i], max_h_r[i]) 
            water = min_h - height[i]
            if water > 0:
                res += water

        return res
        
        