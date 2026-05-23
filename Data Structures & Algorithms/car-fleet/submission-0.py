class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        pair = [[p,s] for p, s in zip(position,speed) ]
        collisions = []
        last_time = None
        for p, s in sorted(pair)[::-1]:
            time = (target - p) / s
            print(time)
            collisions.append(time)
            if len(collisions) >= 2 and collisions[-1] <= collisions[-2]:
                collisions.pop()
        return len(collisions)

        
            


