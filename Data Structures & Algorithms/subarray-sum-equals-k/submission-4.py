class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        arrayValue = defaultdict(int)
        arrayValue[0] =1
        presum = 0
        res = 0
        for num in nums:
            presum += num
            res += arrayValue[presum-k]
            arrayValue[presum] += 1
        return res
#veut dire avec defaultDict:
#si la clé existe, on prend sa valeur
#si elle nexiste pas encore, Python crée automatiquement cette clé avec la valeur 0