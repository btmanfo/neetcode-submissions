class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        res = 1

        for i in range(n-1):
            if arr[i] == arr[i+1]:
                continue
            # on prend le premier signe
            sign = 1 if arr[i]> arr[i+1] else 0
            j = i+1

            while j < n-1:
                if arr[j] == arr[j+1]:
                    # on break pour passer a un autre nbre
                    break
                curr_sign = 1 if arr[j] > arr[j+1] else 0
                if curr_sign == sign:
                    break
                sign = curr_sign
                j+=1
            res = max(res, j-i+1)
        return res