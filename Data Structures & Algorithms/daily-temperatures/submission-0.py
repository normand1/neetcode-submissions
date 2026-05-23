class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        temps = [] # (index, temp)
        result = [0 for _ in range(len(temperatures))]

        for i, temp in enumerate(temperatures):
            while temps and temps[-1][1] < temp:
                upd_i, old_temp = temps.pop()
                result[upd_i] = i - upd_i # distance
            temps.append((i, temp))
        
        return result