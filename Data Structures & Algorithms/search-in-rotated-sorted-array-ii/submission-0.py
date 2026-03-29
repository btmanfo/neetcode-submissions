class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        value = set(nums)
        if target in value:
            return True
        else:
            return False