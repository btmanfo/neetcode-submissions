class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.dfs([],[False]*len(nums), nums)
        return self.res
    def dfs(self, allElement:list, visited: list, arr: list):
        if len(allElement) == len(arr):
            self.res.append(allElement[:])
        for i in range(len(arr)):
            if not visited[i]:
                allElement.append(arr[i])
                visited[i] = True
                self.dfs(allElement, visited, arr)
                visited[i] = False
                allElement.pop()
        