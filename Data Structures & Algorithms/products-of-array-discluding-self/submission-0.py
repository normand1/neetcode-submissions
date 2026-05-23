class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        prefix = []
        for num_val in nums:
            product = product * num_val
            prefix.append(product)

        product = 1
        postfix = []
        for i in range(len(nums) - 1, -1, -1):
            product = product * nums[i]
            postfix.insert(0, product)

        res=[]
        for i in range(len(nums)):
            left = prefix[i-1] if i - 1 >= 0  else 1
            right = postfix[i+1] if i + 1 < len(nums) else 1
            res.append(left * right)

        return res