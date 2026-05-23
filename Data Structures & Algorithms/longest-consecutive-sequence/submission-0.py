class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums.sort()
        
        max_length = 1
        current_length = 1
        
        for i in range(1, len(nums)):
            # Skip duplicates
            if nums[i] == nums[i-1]:
                continue
            
            # Check if current number continues the sequence
            if nums[i] == nums[i-1] + 1:
                current_length += 1
            else:
                # Gap found, reset current sequence length
                max_length = max(max_length, current_length)
                current_length = 1
        
        # Don't forget to check the final sequence
        return max(max_length, current_length)