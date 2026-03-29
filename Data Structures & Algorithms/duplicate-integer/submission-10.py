class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        allValue = set()
        for i in nums:
            if i in allValue:
                return True
            else:
                allValue.add(i)

        return False