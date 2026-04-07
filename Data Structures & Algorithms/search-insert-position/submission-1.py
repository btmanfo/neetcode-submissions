class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # pourquoi on veut plus grande que notre target?
        # Parce que l’index d’insertion est précisément la position du premier élément plus grand que target.
        # Ex:
        # nums = [1, 3, 5, 6]
        # target = 2
        # 2 n’est pas dans le tableau.
        # Le premier élément plus grand que 2, c’est 3, à l’index 1
        # Donc si on insère 2, ça donne :
        # [1, 2, 3, 5, 6]
        # Donc on retourne 1
        rightPtr = len(nums)-1
        leftPtr = 0
        res = len(nums)
        while rightPtr >= leftPtr:
            middlePtr = leftPtr + math.floor((rightPtr -leftPtr)/2)
            if nums[middlePtr] > target:
                res = middlePtr
                rightPtr = middlePtr -1
            elif nums[middlePtr] < target:
                leftPtr = middlePtr +1
            else:
                return middlePtr
        return res