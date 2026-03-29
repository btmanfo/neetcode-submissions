class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tableauEnsemble ={}

        for i,n in enumerate(nums):
            reSearchValue = target -n
            if reSearchValue in tableauEnsemble:
                return [tableauEnsemble[reSearchValue], i]
            else:
                tableauEnsemble[n] =i
        return False




        