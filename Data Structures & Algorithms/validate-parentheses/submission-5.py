class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)<=1:
            return False
        stack = []
        closeToOpen = {"(":")","{":"}", "[":"]"}

        for c in s:
            if c in closeToOpen:
                stack.append(c)
            else:
                if len(stack)>0 and c == closeToOpen[stack[-1]]:
                    stack.pop()
                else:
                    return False
        if len(stack) != 0:
            return False
        else:
            return True
        #[]