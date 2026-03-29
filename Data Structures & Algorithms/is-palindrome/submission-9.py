class Solution:
    def isPalindrome(self, s: str) -> bool:
        num =""

        for i in s:
            if i.isalnum():
                num+= i.lower()

        return num == num[::-1]