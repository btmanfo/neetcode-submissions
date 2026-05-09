class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backPagrating(i, subset):
            if i > n:
                if len(subset) == k:
                    res.append(subset.copy())
                return
            subset.append(i)
            backPagrating(i+1, subset)
            subset.pop()
            backPagrating(i+1, subset)
        backPagrating(1, [])
        return res