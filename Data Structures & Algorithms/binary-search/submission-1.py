class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if target == nums[0] else -1

        l = 0
        r = len(nums) - 1

        while l <= r:  # Note: <= instead of 
            mid = l + (r - l) // 2
            
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        
        return -1