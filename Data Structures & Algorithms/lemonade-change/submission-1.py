class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        bills.sort()
        stack = 0
        for i in bills:
            if stack < 0:
                return False
            if i == 5:
                stack += 5
                continue
            if i != 5:
                toPay = i-5
                if stack < toPay:
                    return False
                else:
                    stack -= toPay
                    stack += 5
                    
        return True
            
