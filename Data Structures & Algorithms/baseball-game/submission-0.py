class Solution:
    def calPoints(self, operations: List[str]) -> int:
        resArr = []
        for op in operations:
            if op == 'C':
                resArr = resArr[:(len(resArr)-1)]
                continue
            elif op == 'D':
                resArr.append(resArr[-1]*2)
                continue
            elif op == '+':
                resArr.append(resArr[-1]+ resArr[-2])
            else:
                resArr.append(int(op))
        res = 0
        for i in resArr:
            res += i
        return res
