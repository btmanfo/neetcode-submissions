class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        k = len(matrix)
        e = 0
        while e < k:
            r = len(matrix[e]) - 1
            l = 0
            while l <= r:
                m = (r + l) // 2

                if matrix[e][m] > target:
                    r = m - 1  # Corrigé ici
                elif matrix[e][m] < target:
                    l = m + 1  # Corrigé ici
                else:
                    return True
            e = e + 1
        return False