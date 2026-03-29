class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        num =[]
        num2 = []
        for i in range(len(position)):
            num2.append((position[i],speed[i]))

        num2.sort(key= lambda x:x[0], reverse=True)
        stack = []
        for p, s in num2:  # Reverse Sorted Order
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
                