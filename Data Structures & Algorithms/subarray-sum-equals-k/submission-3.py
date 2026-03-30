class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #1 on considere deja quil y a une comme prefix qui donne 0
        #Parce que count[x] = combien de fois on a déjà vu une somme préfixe égale à x
        #count[prefix - k] = 3
        #ça veut dire qu’il y a 3 positions différentes dans le passé où la somme préfixe valait prefix - k.
        count = defaultdict(int)
        count[0] = 1  # empty prefix has sum 0
        prefix = 0
        res = 0

        for num in nums:
            prefix += num
            res += count[prefix - k]
            count[prefix] += 1

        return res