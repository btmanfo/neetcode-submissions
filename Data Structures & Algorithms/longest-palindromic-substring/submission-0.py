class Solution:
    def longestPalindrome(self, s: str) -> str:
        #this is to keep track of the longest palindrome find so far
        resIdx = 0
        resLen = 0

        for i in range(len(s)):
            # this is to scan when the longest palindrome can be a odd number
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resIdx = l
                    resLen = r - l + 1
                l -= 1
                r += 1

            # this is to scan when the longest palindrom can be an event number
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resIdx = l
                    resLen = r - l + 1
                l -= 1
                r += 1

        return s[resIdx : resIdx + resLen]