class Solution:
    def decodeString(self, s: str) -> str:
        #s = "2[a3[b]]c"
        self.i = 0

        def helper():
            ch = ''
            k = 0

            while self.i < len(s):
                c = s[self.i]

                if c.isdigit():
                    k = k*10 + int(c)
                elif c == '[':
                    self.i += 1
                    ch += k* helper()
                    k = 0
                elif c == ']':
                    return ch
                else:
                    ch += c
                self.i +=1
            return ch
        return helper()
