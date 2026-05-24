class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement_dict = {}

        for i in range(len(nums)):   
            complement_dict[target - nums[i]] = i
        for i in range(len(nums)): 
            if nums[i] in complement_dict.keys() and complement_dict[nums[i]] != i:
                return [i, complement_dict[nums[i]]]       