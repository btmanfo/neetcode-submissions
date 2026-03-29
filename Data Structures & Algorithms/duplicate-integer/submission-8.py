class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        value = set()

        for i in nums:
            if i in value:
                return True
            else:
                value.add(i);
        return False