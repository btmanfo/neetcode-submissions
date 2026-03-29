class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        numberOf0 = 0
        numberOf1 = 0
        numberOf2 = 0

        for num in nums:
            if num == 0:
                numberOf0+=1
            if num == 1:
                numberOf1+=1
            if num == 2:
                numberOf2+=1
        res = []
        if numberOf0 != 0:
            for i in range(numberOf0):
                res.append(0)
        if numberOf1 != 0:
            for i in range(numberOf1):
                res.append(1)
        if numberOf2 != 0:
            for i in range(numberOf2):
                res.append(2)
        for i in range(len(res)):
            nums[i] = res[i]
