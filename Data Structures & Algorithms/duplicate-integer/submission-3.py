class Solution:

    def hasDuplicate(self, nums: List[int]) -> bool:
        ensembleValeur = set()
        for num in nums:
            if num in ensembleValeur:
                return True
            ensembleValeur.add(num)
        return False


         