class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        arr = []
        if a>0:
            arr.append([-a, 'a'])
        if b> 0:
            arr.append([-b, 'b'])
        if c>0:
            arr.append([-c, 'c'])
        heapq.heapify(arr)
        res = ""

        while arr:
            count, char = heapq.heappop(arr)
            if len(res)>1 and res[-1] == res[-2] == char:
                if not arr:
                    break
                count2, char2 = heapq.heappop(arr)
                res += char2
                count2 +=1
                if count2:
                    heapq.heappush(arr, [count2, char2])
                heapq.heappush(arr, [count, char])
            else:
                res += char
                count+=1
                if count:
                    heapq.heappush(arr, [count, char])
        return res