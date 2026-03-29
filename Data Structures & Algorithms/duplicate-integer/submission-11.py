class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        singleValue = set()
        for i in nums:
            if i in singleValue:
                return True
            else:
                singleValue.add(i)
        return False