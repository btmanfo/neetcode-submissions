class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        stack = 0
        for i in bills:
            if stack < 0:
                return False
            stack += 5
            billsToPay = i -5
            print("billsToPay =", billsToPay,"Stack =", stack, "Sorted")
            stack -= billsToPay
        return True
            
