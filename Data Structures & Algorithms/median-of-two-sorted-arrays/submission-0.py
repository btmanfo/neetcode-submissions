class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        newList = nums1 + nums2
        heapq.heapify(newList)
        new_list = [heapq.heappop(newList) for _ in range(len(newList))]
        totalLen = len(new_list)
        if len(new_list)%2 == 0:
            return (new_list[totalLen // 2 - 1] + new_list[totalLen // 2]) / 2.0
        else:
            return new_list[totalLen//2]