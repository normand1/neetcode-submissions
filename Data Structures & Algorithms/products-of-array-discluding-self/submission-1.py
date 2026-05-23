class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = []

        prefix = []
        product = 1
        for i in range(len(nums)):
            product *= nums[i]
            prefix.append(product)

        postfix = []
        product = 1
        for i in range(len(nums) -1, -1, -1):
            product *= nums[i]
            postfix.insert(0, product)
        
        print(prefix)
        print(postfix)

        for i in range(len(nums)):
            pre = prefix[i - 1] if i-1 >= 0 else 1
            post = postfix[i + 1] if i+1 < len(nums) else 1
            res.append(pre*post)

        return res
        