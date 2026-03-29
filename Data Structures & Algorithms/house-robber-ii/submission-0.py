class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        def findSize(arr):
            df = [0] * len(arr)
            df[0] = arr[0]
            df[1] = max(arr[1], arr[0])
            for i in range(2, len(arr)):
                df[i] = max(df[i-1], arr[i]+ df[i-2])
            return df[-1]
        return max(findSize(nums[1:]), findSize(nums[:-1]))
