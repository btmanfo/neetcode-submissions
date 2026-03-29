class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res =[]
        num =1
        for i in range(len(nums)):
            for t in range(len(nums)):
                if (t!=i):
                    num*= nums[t]
            res.append(num)
            num =1
        return res