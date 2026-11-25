class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap = [(-count , value) for value , count in freq.items()]
        heapify(heap)
        res = []
        for i in range(k):
            val = heappop(heap)[1]
            res.append(val)
        return res