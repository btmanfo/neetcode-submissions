class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0
        r = len(arr)-1
        while (r-l) >= k:
            if abs(x-arr[r]) < abs(x- arr[l]):
                l+=1
            else:
                r-=1
        return arr[l:r+1]
        