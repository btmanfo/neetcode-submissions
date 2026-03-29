class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        apperance = {}
        res = []
        for i in nums:
            apperance[i] = 1 + apperance.get(i, 0)
        for i,j in apperance.items():
            if j> math.floor(len(nums)/3):
                res.append(i)
        return res