class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0]*len(height)
        varMaxLeft = 0

        for i,v in enumerate(height):
            if i == 0:
                varMaxLeft = v
                continue
            else:
                maxLeft[i] = varMaxLeft
                varMaxLeft = max(varMaxLeft, v)

        maxRight = [0]*len(height)
        varRightMax = 0

        for i in range(len(height)-1, -1 ,-1):
            if i == len(height)-1:
                varRightMax = height[i]
                continue
            else:
                maxRight[i] = varRightMax
                varRightMax = max(varRightMax, height[i])
        sumTotal = 0

        for i, v in enumerate(height):
            if (v - min(maxRight[i], maxLeft[i]) < 0):
                sumTotal += min(maxRight[i], maxLeft[i]) -v
        return sumTotal