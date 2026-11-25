class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        heap = []
        for num, count in freq.items():
            heapq.heappush(heap, (count, -num))
        
        res = []
        while heap:
            count, neg_num = heapq.heappop(heap)
            res.extend([-neg_num] * count)
        
        return res